import csv
import re
import os
import requests
from urllib.parse import urlparse, parse_qs


def extract_google_drive_id(url):
    """Extract file ID from various Google Drive URL formats."""
    if not url or not url.strip():
        return None

    # Pattern 1: /open?id=FILE_ID
    match = re.search(r'id=([a-zA-Z0-9_-]+)', url)
    if match:
        return match.group(1)

    # Pattern 2: /d/FILE_ID/
    match = re.search(r'/d/([a-zA-Z0-9_-]+)', url)
    if match:
        return match.group(1)

    # Pattern 3: /file/d/FILE_ID/
    match = re.search(r'/file/d/([a-zA-Z0-9_-]+)', url)
    if match:
        return match.group(1)

    return None


def download_google_drive_file(file_id, output_path):
    """
    Download a file from Google Drive given its file ID.

    Args:
        file_id: Google Drive file ID
        output_path: Local path to save the file

    Returns:
        bool: True if successful, False otherwise
    """

    # Google Drive direct download URL
    url = f"https://drive.google.com/uc?id={file_id}&export=download"

    session = requests.Session()

    try:
        # First request
        response = session.get(url, stream=True)

        # Check for virus scan warning (large files)
        token = None
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                token = value
                break

        # If there's a confirmation token, make a second request
        if token:
            url = f"https://drive.google.com/uc?export=download&id={file_id}&confirm={token}"
            response = session.get(url, stream=True)

        # Check content type to verify it's actually a PDF
        content_type = response.headers.get('Content-Type', '')
        if 'text/html' in content_type:
            # This means we got an HTML page (error or login page), not a PDF
            print(f"  ✗ Got HTML instead of PDF - file may not be publicly accessible")
            return False

        # Check if download was successful
        if response.status_code == 200:
            # Save file
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=32768):
                    if chunk:
                        f.write(chunk)

            # Verify file size is reasonable (at least 1KB)
            file_size = os.path.getsize(output_path)
            if file_size < 1024:
                print(f"  ✗ Downloaded file too small ({file_size} bytes) - likely not a valid PDF")
                return False

            return True
        else:
            print(f"  ✗ HTTP {response.status_code}")
            return False

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def download_pdfs_from_csv(csv_file, output_dir='downloaded_pdfs'):
    """
    Download all PDFs from the CSV file.

    Args:
        csv_file: Path to the input CSV file
        output_dir: Directory to save downloaded PDFs
    """

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # First pass: collect all papers, keeping only the most recent for each title
    papers_by_title = {}

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            title = row['Paper Title']
            pdf_url = row['If not providing an arXiv link, please upload a PDF of your paper here.']

            # Skip if no PDF URL
            if not pdf_url or not pdf_url.strip():
                continue

            # Store/overwrite with most recent entry (later rows overwrite earlier ones)
            papers_by_title[title] = {
                'title': title,
                'pdf_url': pdf_url
            }

    # Track statistics
    total = len(papers_by_title)
    downloaded = 0
    skipped = 0
    failed = 0

    # Second pass: download the PDFs
    for i, paper in enumerate(papers_by_title.values(), 1):
        title = paper['title']
        pdf_url = paper['pdf_url']
        # Extract Google Drive file ID
        file_id = extract_google_drive_id(pdf_url)

        if not file_id:
            print(f"{i}. ✗ Could not extract file ID from: {title}")
            failed += 1
            continue

        # Create safe filename from paper title
        safe_title = re.sub(r'[^\w\s-]', '', title)
        safe_title = re.sub(r'[-\s]+', '_', safe_title)
        safe_title = safe_title[:100]  # Limit length
        filename = f"{safe_title}.pdf"
        output_path = os.path.join(output_dir, filename)

        # Skip if already downloaded
        if os.path.exists(output_path):
            print(f"{i}. ○ Already exists: {filename}")
            skipped += 1
            continue

        # Download the file
        print(f"{i}. Downloading: {title}")
        print(f"   → {filename}")

        if download_google_drive_file(file_id, output_path):
            print(f"   ✓ Success ({os.path.getsize(output_path) / 1024:.1f} KB)")
            downloaded += 1
        else:
            failed += 1
            # Remove partial file if download failed
            if os.path.exists(output_path):
                os.remove(output_path)


    # Print summary
    print("\n" + "=" * 50)
    print("Download Summary:")
    print(f"  Total PDFs found: {total}")
    print(f"  Successfully downloaded: {downloaded}")
    print(f"  Already existed: {skipped}")
    print(f"  Failed: {failed}")
    print(f"  Output directory: {output_dir}")
    print("=" * 50)

if __name__ == "__main__":
    # Configuration
    csv_file = "CDEL 2025 Paper Collection (Responses) - Form Responses 1.csv"
    output_dir = "cdel_2025_pdfs"

    print("CDEL 2025 PDF Downloader")
    print("=" * 50)
    print(f"Reading from: {csv_file}")
    print(f"Saving to: {output_dir}/")
    print("=" * 50 + "\n")

    download_pdfs_from_csv(csv_file, output_dir)