---
layout: default
title: Curated Data for Efficient Learning
buttons:
  Overview: './index.html'
  Invited Speakers: './index.html#invited-speakers'
  Schedule: './index.html#schedule'
  Call for Papers: './index.html#call-for-papers'
#  Important Dates: './index.html#important-workshop-dates'
  Deadlines: './index.html#deadlines'
  Related Workshops: './index.html#related-workshops'
  Organizers: './index.html#organizers'
#  Program Committee: './index.html#program-committee'
# we use the iccv logo here
description: []
---

<style> 
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 100%;
  width: 75%;
}
</style>

<style>
table {
  width: 100%;
  border-collapse: collapse;
  overflow-x: auto;
  display: block;
}
td {
  padding: 6px 8px;
  vertical-align: top;
}
</style>

<style>
@media (max-width: 600px) {
  h1, h2, h3 {
    font-size: 1.2em;
  }

  div {
    padding: 0 10px;
  }

  .center {
    width: 100%;
  }
}
</style>

<meta name="viewport" content="width=device-width, initial-scale=1">

# Overview
<div style="text-align: left; max-width: 800px; margin: auto;">
The ICCV 2025 Workshop on Curated Data for Efficient Learning (CDEL) seeks to advance the understanding and development of data-centric techniques that improve the efficiency of training large-scale machine learning models. As model sizes continue to grow and data requirements scale accordingly, this workshop brings attention to the increasingly critical role of data quality, selection, and synthesis in achieving high model performance with reduced computational cost. Rather than focusing on ever-larger datasets and models, CDEL emphasizes the curation and distillation of high-value data—leveraging techniques such as dataset distillation, data pruning, synthetic data generation, and sampling optimization. These approaches aim to reduce redundancy, improve generalization, and enable learning in data-scarce regimes. The workshop will bring together researchers and practitioners from vision, language, and multimodal learning to share insights and foster collaborations around efficient, scalable, and sustainable data-driven machine learning.
</div>

# Invited Speakers
<div style="display: flex; flex-wrap: wrap; justify-content: center;">
  <div style="flex: 1 1 300px; max-width: 300px; margin: 10px;">
    <a href="https://web.mit.edu/torralba/www/">
      <img alt="Antonio Torralba" src="pics/speakers/antonio_torralba.jpg"  height="200" width="200" style="border-radius: 50%; object-fit: cover;">
    </a><br>
    <a href="https://web.mit.edu/torralba/www/">Antonio Torralba</a><br>
    Massachusetts Institute of Technology
  </div>

  <div style="flex: 1 1 300px; max-width: 300px; margin: 10px;">
    <a href="https://people.eecs.berkeley.edu/~efros/">
      <img alt="Alexei Efros" src="pics/speakers/alexei_efros.jpg"  height="200" width="200" style="border-radius: 50%; object-fit: cover;">
    </a><br>
    <a href="https://people.eecs.berkeley.edu/~efros/">Alexei Efros</a><br>
    University of California, Berkeley
  </div>

  <div style="flex: 1 1 300px; max-width: 300px; margin: 10px;">
    <a href="https://www.cs.princeton.edu/~olgarus/">
      <img alt="Olga Russakovsky" src="pics/speakers/olga_russakovsky.jpeg"  height="200" width="200" style="border-radius: 50%; object-fit: cover;">
    </a><br>
    <a href="https://www.cs.princeton.edu/~olgarus/">Olga Russakovsky</a><br>
    Princeton University
  </div>

  <div style="flex: 1 1 300px; max-width: 300px; margin: 10px;">
    <a href="https://beerys.github.io/">
      <img alt="Sara Beery" src="pics/speakers/sara_beery.jpg" height="200" width="200" style="border-radius: 50%; object-fit: cover;">
    </a><br>
    <a href="https://beerys.github.io/">Sara Beery</a><br>
    Massachusetts Institute of Technology
  </div>

  <div style="flex: 1 1 300px; max-width: 300px; margin: 10px;">
    <a href="https://liuzhuang13.github.io/">
      <img alt="Zhuang Liu" src="pics/speakers/zhuang_liu.png" height="200" width="200" style="border-radius: 50%; object-fit: cover;">
    </a><br>
    <a href="https://liuzhuang13.github.io/">Zhuang Liu</a><br>
    Princeton University
  </div>
</div>

# Schedule
- **Date:** October 18, 2025
- **Time:** 8:30 AM – 5:30 PM
- **Location:** ICCV Workshop Venue (TBA)

<table>
<tr><td>08:30 – 08:55</td><td>Welcome & Coffee</td></tr>
<tr><td>09:00 – 09:35</td><td>Invited Talk: Antonio Torralba</td></tr>
<tr><td>09:35 – 10:10</td><td>Invited Talk: Alexei Efros</td></tr>
<tr><td>10:10 – 10:45</td><td>Oral Presentations I</td></tr>
<tr><td>10:50 – 12:00</td><td>Poster Session</td></tr>
<tr><td>12:00 – 13:25</td><td>Lunch Break</td></tr>
<tr><td>13:30 – 14:25</td><td>Invited Talk: Olga Russakovsky</td></tr>
<tr><td>14:30 – 15:05</td><td>Invited Talk: Sara Beery</td></tr>
<tr><td>15:05 – 15:40</td><td>Invited Talk: Zhuang Liu</td></tr>
<tr><td>15:40 – 16:25</td><td>Oral Presentations II</td></tr>
<tr><td>16:30 – 17:00</td><td>Panel Discussion & Closing</td></tr>
</table>

# Call for Papers
We welcome submissions on all topics related to the curation of training data.<br>
Some potential topics include:
- **Data Pruning:** How can we eliminate redundant or low-quality samples from large datasets?
- **Synthetic Data:** How can we use generative models to create or augment datasets?
- **Dataset Distillation:** How can we learn tiny datasets of highly-efficient synthetic samples?
- **Obscure Domains:** How can we train models in areas where existing data is extremely scarce?
<!-- - **Scaling Laws:** How does the quality of training samples affect performance scaling?-->
- **Future directions:** What problems in data-centric AI can we expect in the near future?

**Submission Details:**<br>
We accept submissions of both long conference-style papers (8 pages) and short extended abstracts (4 pages). 
Authors of accepted long papers have the _option_ of having their work published in the ICCV workshop proceedings if they do not violate dual-submission guidelines. 
<br>
<br>
We also welcome submissions of work currently in submission or recently accepted to other venues, but these will not be published in the workshop proceedings (but may still be presented at our workshop). 
<br>
<br>
Please sign up [here](https://docs.google.com/forms/d/e/1FAIpQLScLDrqtEKdd4TqS3sfQ2MLbtBU_IRZOysw-r_LHQ7-TVaABBg/viewform?usp=dialog) if you'd like to volunteer as a reviewer. 

[//]: # (- Full papers: 8 pages &#40;excluding references&#41;)

[//]: # (- Short papers: 4 pages &#40;excluding references&#41;)

[//]: # (- Submission site: [OpenReview link coming soon])

# Deadlines
**To be published in the proceedings:**
- Submission deadline: July 7, 2025
- Notification: July 11, 2025
- Camera-ready: August 15, 2025

**All other submissions:**
- Submission deadline: August 29, 2025
- Notification: September 5, 2025
- Camera-ready: September 12, 2025

Please contact George ([gcaz@mit.edu](mailto:gcaz@mit.edu)) with any questions.

# Related Workshops
- [Dataset Distillation Challenge @ ECCV 2024](https://eccv2024.org/)
- [Data-centric AI @ NeurIPS 2023](https://neurips.cc/Conferences/2023/)


# Organizers

<div style="display: flex; flex-wrap: wrap; justify-content: center;">
  <div style="flex: 1 1 300px; max-width: 300px; margin: 10px;">
    <a href="https://georgecazenavette.github.io/">
      <img alt="George Cazenavette" src="pics/organizers/george_cazenavette.jpg" height="200" width="200" style="border-radius: 50%; object-fit: cover;">
    </a><br>
    <a href="https://georgecazenavette.github.io/">George Cazenavette</a><br>
    Massachusetts Institute of Technology
  </div>

  <div style="flex: 1 1 300px; max-width: 300px; margin: 10px;">
    <a href="https://kaiwang960112.github.io/">
      <img alt="Kai Wang" src="pics/organizers/kai_wang.jpg" height="200" width="200" style="border-radius: 50%; object-fit: cover;">
    </a><br>
    <a href="https://kaiwang960112.github.io/">Kai Wang</a><br>
    National University of Singapore
  </div>

  <div style="flex: 1 1 300px; max-width: 300px; margin: 10px;">
    <a href="https://lizekai-richard.github.io/">
      <img alt="Zekai Li" src="pics/organizers/zekai_li.png" height="200" width="200" style="border-radius: 50%; object-fit: cover;">
    </a><br>
    <a href="https://lizekai-richard.github.io/">Zekai Li</a><br>
    National University of Singapore
  </div>

  <div style="flex: 1 1 300px; max-width: 300px; margin: 10px;">
    <a href="https://xindiwu.github.io/">
      <img alt="Xindi Wu" src="pics/organizers/xindi_wu.jpg" height="200" width="200" style="border-radius: 50%; object-fit: cover;">
    </a><br>
    <a href="https://xindiwu.github.io/">Xindi Wu</a><br>
    Princeton University
  </div>

  <div style="flex: 1 1 300px; max-width: 300px; margin: 10px;">
    <a href="https://tongzhouwang.info/">
      <img alt="Tongzhou Wang" src="pics/organizers/tongzhou_wang.jpg" height="200" width="200" style="border-radius: 50%; object-fit: cover;">
    </a><br>
    <a href="https://tongzhouwang.info/">Tongzhou Wang</a><br>
    Massachusetts Institute of Technology
  </div>

  <div style="flex: 1 1 300px; max-width: 300px; margin: 10px;">
    <a href="https://peihaowang.github.io/">
      <img alt="Peihao Wang" src="pics/organizers/peihao_wang.jpg" height="200" width="200" style="border-radius: 50%; object-fit: cover;">
    </a><br>
    <a href="https://peihaowang.github.io/">Peihao Wang</a><br>
    University of Texas at Austin
  </div>

  <div style="flex: 1 1 300px; max-width: 300px; margin: 10px;">
    <a href="https://ruihangao.github.io/">
      <img alt="Ruihan Gao" src="pics/organizers/ruihan_gao.jpg" height="200" width="200" style="border-radius: 50%; object-fit: cover;">
    </a><br>
    <a href="https://ruihangao.github.io/">Ruihan Gao</a><br>
    Carnegie Mellon University
  </div>

  <div style="flex: 1 1 300px; max-width: 300px; margin: 10px;">
    <a href="https://scholar.google.com.hk/citations?user=R3_AR5EAAAAJ">
      <img alt="Bo Zhao" src="pics/organizers/bo_zhao.jpg" height="200" width="200" style="border-radius: 50%; object-fit: cover;">
    </a><br>
    <a href="https://scholar.google.com.hk/citations?user=R3_AR5EAAAAJ">Bo Zhao</a><br>
    Shanghai Jiao Tong University
  </div>

  <div style="flex: 1 1 300px; max-width: 300px; margin: 10px;">
    <a href="https://vita-group.github.io/research.html">
      <img alt="Zhangyang Wang" src="pics/organizers/zhangyang_wang.jpg" height="200" width="200" style="border-radius: 50%; object-fit: cover;">
    </a><br>
    <a href="https://vita-group.github.io/research.html">Zhangyang Wang</a><br>
    University of Texas at Austin
  </div>

  <div style="flex: 1 1 300px; max-width: 300px; margin: 10px;">
    <a href="https://www.cs.cmu.edu/~junyanz/">
      <img alt="Jun-Yan Zhu" src="pics/organizers/junyan_zhu.jpg" height="200" width="200" style="border-radius: 50%; object-fit: cover;">
    </a><br>
    <a href="https://www.cs.cmu.edu/~junyanz/">Jun-Yan Zhu</a><br>
    Carnegie Mellon University
  </div>
</div>

[//]: # (# Program Committee)

[//]: # (<ul>)

[//]: # (  <li>Manel Baradad &#40;MIT&#41;</li>)

[//]: # (  <li>George Cazenavette &#40;MIT&#41;</li>)

[//]: # (  <li>David Charatan &#40;MIT&#41;</li>)

[//]: # (  <li>Xuxi Chen &#40;UT Austin&#41;</li>)

[//]: # (  <li>Justil Cui &#40;UCLA&#41;</li>)

[//]: # (  <li>Ziyao Guo &#40;NUS&#41;</li>)

[//]: # (  <li>Yidi Jiang &#40;NUS&#41;</li>)

[//]: # (  <li>Jang-Hyun Kim &#40;SNU&#41;</li>)

[//]: # (  <li>Jinuk Kim &#40;SNU&#41;</li>)

[//]: # (  <li>Qi Li &#40;MS Student, NUS&#41;</li>)

[//]: # (  <li>Shiye Li &#40;U of Sydney&#41;</li>)

[//]: # (  <li>Guang Li &#40;Hokkaido U&#41;</li>)

[//]: # (  <li>Shikun Li &#40;CAS&#41;</li>)

[//]: # (  <li>Yanqing Liu &#40;UCSC&#41;</li>)

[//]: # (  <li>Jiawei Liu &#40;NUS&#41;</li>)

[//]: # (  <li>Songhua Liu &#40;NUS&#41;</li>)

[//]: # (  <li>Wei-Chiu Ma &#40;Cornell&#41;</li>)

[//]: # (  <li>Brian Moser &#40;University of Kaiserslautern&#41;</li>)

[//]: # (  <li>Adrian Munoz &#40;MIT&#41;</li>)

[//]: # (  <li>Federico Raue &#40;University of Kaiserslautern&#41;</li>)

[//]: # (  <li>Yuzhang Shang &#40;Illinois Tech&#41;</li>)

[//]: # (  <li>Qin Shi &#40;Purdue University&#41;</li>)

[//]: # (  <li>Seungjae Shin &#40;KAIST&#41;</li>)

[//]: # (  <li>Jake Touchet &#40;Louisiana Tech University&#41;</li>)

[//]: # (  <li>Haonan Wang &#40;NUS&#41;</li>)

[//]: # (  <li>Kai Wang &#40;NUS&#41;</li>)

[//]: # (  <li>Tongzhou Wang &#40;MIT&#41;</li>)

[//]: # (  <li>Xindi Wu &#40;Princeton&#41;</li>)

[//]: # (  <li>William Yang &#40;Princeton&#41;</li>)

[//]: # (  <li>Yue Xu &#40;SJTU&#41;</li>)

[//]: # (  <li>Yuchen Zhang &#40;UESTC&#41;</li>)

[//]: # (  <li>Tianle Zhang &#40;UESTC&#41;</li>)

[//]: # (  <li>Junhao Zhang &#40;NUS&#41;</li>)

[//]: # (  <li>Jie Zhang &#40;ETH Zurich&#41;</li>)

[//]: # (  <li>Bo Zhao &#40;BAAI&#41;</li>)

[//]: # (  <li>Wangbo Zhao &#40;NUS&#41;</li>)

[//]: # (  <li>Zekai Li &#40;NUS&#41;</li>)

[//]: # (  <li>Peihao Wang &#40;UT Austin&#41;</li>)

[//]: # (</ul>)
