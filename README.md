# Replication Package

## A Systematic Literature Review of Empirical Studies on Android App Quality: Taxonomy, Challenges, Solutions and Future Directions

Version: v1.0  
Release Date: February 2026  

This repository contains the complete replication package for the study:

**"A Systematic Literature Review of Empirical Studies on Android App Quality: Taxonomy, Challenges, Solutions and Future Directions."**

The review synthesises 78 primary empirical studies published between 2017–2025 and systematically maps them onto the ISO/IEC 25010 software quality model. The study provides a structured taxonomy of research themes, identifies recurring Android-specific quality challenges, evaluates methodological patterns, and outlines evidence-based future research directions.

---

## Repository Structure


data/SLR_PS1_78.xlsx
→ Final extracted dataset (78 primary studies)

scripts/inter_rater_reliability.py
→ Python script for computing Cohen’s κ and observed agreement

output/agreement_results.csv
→ Generated inter-rater reliability statistics

docs/search_strings.md
→ Executed database search queries and applied filters

docs/query_screenshots/
→ Database query execution screenshots

requirements.txt
→ Python dependencies

---


## What This Package Contains

- Executed search queries for all databases
- Initial retrieval dataset (N = 443 records)
- PRISMA-based screening workflow
- Extracted ISO/IEC 25010 attribute mappings (FS–P)
- Methodological quality assessment (Q1–Q6)
- Inter-rater reliability calculations (Cohen’s κ)
- Observed agreement percentages
- Final dataset of included primary studies (N = 78)

The review methodology follows Kitchenham’s guidelines for systematic literature reviews in software engineering.

---

## Reproducing Reliability Results

### Requirements
Python 3.9+

### Install dependencies

bash
pip install -r requirements.txt


### Run
python scripts/inter_rater_reliability.py

The script will compute:
- Cohen’s κ per ISO attribute
- Overall ISO κ
- κ for Q1–Q6
- Observed agreement (%)
- Save results to output/agreement_results.csv

### Transparency and Reproducibility

This repository provides full transparency of the review process, including:
- Exact executed search queries
- Database-specific filters
- Execution logs and screenshots
- Extraction dataset
- Coding scheme
- Inter-rater reliability computation scripts
- The archival version of this replication package is available via Zenodo:

DOI: [To be added after Zenodo archiving]


### Citation

If you use this replication package, please cite the associated journal article:

Chand, R., et al. (2026).
A Systematic Literature Review of Empirical Studies on Android App Quality: Taxonomy, Challenges, Solutions and Future Directions.
[Journal Name – under review].

Zenodo archive DOI: https://doi.org/10.5281/zenodo.18621632


### License


This repository is distributed under the MIT License.

