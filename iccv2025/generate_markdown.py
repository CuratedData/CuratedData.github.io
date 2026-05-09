import csv
import re
from collections import defaultdict


def parse_csv_to_markdown(csv_file, output_file):
    """
    Convert CDEL 2025 papers CSV to Jekyll markdown format.

    Args:
        csv_file: Path to the input CSV file
        output_file: Path to the output markdown file
    """

    # Dictionary to store papers by title (keeps most recent)
    papers_by_title = {}

    # Read CSV file
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            track = row['To which track was your paper accepted?']
            title = row['Paper Title']
            authors = row[
                'Please enter the list of authors and affiliations following the given example :\n\nGeorge Cazenavette (MIT); Kai Wang (NUS); Xindi Wu (Princeton)']
            arxiv = row['If providing an arXiv link, please enter it here.']
            pdf_url = row['If not providing an arXiv link, please upload a PDF of your paper here.']
            project_url = row['You may provide a URL to a project page here.']

            # Store/overwrite with most recent entry (later rows overwrite earlier ones)
            paper = {
                'title': title,
                'authors': authors,
                'arxiv': arxiv.strip() if arxiv else '',
                'pdf_url': pdf_url.strip() if pdf_url else '',
                'project_url': project_url.strip() if project_url else '',
                'track': track
            }

            papers_by_title[title] = paper

    # Organize papers by track
    papers_by_track = defaultdict(list)
    for paper in papers_by_title.values():
        track = paper['track']
        papers_by_track[track].append(paper)

    # Generate markdown
    markdown = generate_markdown(papers_by_track)

    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown)

    print(f"✓ Generated {output_file}")
    print(f"  Archival papers: {len(papers_by_track['Archival'])}")
    print(f"  Non-Archival papers: {len(papers_by_track['Non-Archival'])}")


def generate_markdown(papers_by_track):
    """Generate Jekyll markdown from papers dictionary."""

    md = """---
layout: page
title: "CDEL 2025 Accepted Papers"
permalink: /accepted-papers/
---

# Accepted Papers

We are pleased to announce the accepted papers for CDEL 2025. Papers are organized by track.

"""

    # Archival track
    if 'Archival' in papers_by_track:
        md += "## Archival Track\n\n"
        for paper in papers_by_track['Archival']:
            md += format_paper(paper)
        md += "---\n\n"

    # Non-Archival track
    if 'Non-Archival' in papers_by_track:
        md += "## Non-Archival Track\n\n"
        for paper in papers_by_track['Non-Archival']:
            md += format_paper(paper)
        md += "---\n\n"

    # Add totals
    archival_count = len(papers_by_track.get('Archival', []))
    non_archival_count = len(papers_by_track.get('Non-Archival', []))
    md += f"*Total: {archival_count} Archival papers, {non_archival_count} Non-Archival papers*"

    return md


def format_paper(paper):
    """Format a single paper entry."""
    md = f"### {paper['title']}\n"
    md += f"**Authors:** {paper['authors']}  \n"

    # Add links if available
    links = []
    if paper['arxiv']:
        links.append(f"[arXiv]({paper['arxiv']})")
    if paper['pdf_url']:
        # Extract first author's last name
        authors_str = paper['authors'].strip()

        # Split by semicolon or comma
        if ';' in authors_str:
            first_author = authors_str.split(';')[0].strip()
        elif ',' in authors_str:
            first_author = authors_str.split(',')[0].strip()
        else:
            first_author = authors_str

        # Remove affiliation in parentheses if present
        if '(' in first_author:
            first_author = first_author.split('(')[0].strip()

        # Get the last word as the last name
        name_parts = first_author.split()
        if name_parts:
            last_name = name_parts[-1].lower()
            pdf_filename = f"{last_name}.pdf"
            links.append(f"[PDF](/pdfs/{pdf_filename})")
    if paper['project_url']:
        links.append(f"[Project Page]({paper['project_url']})")

    if links:
        md += " | ".join(links) + "\n"

    md += "\n"
    return md


if __name__ == "__main__":
    # Example usage
    input_csv = "CDEL 2025 Paper Collection (Responses) - Form Responses 1.csv"
    output_md = "accepted-papers.md"

    parse_csv_to_markdown(input_csv, output_md)