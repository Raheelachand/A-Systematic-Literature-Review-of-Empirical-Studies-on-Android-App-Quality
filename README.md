# Replication Package  
## Android App Quality Systematic Literature Review

This repository contains the full replication package for the study:

**"A Systematic Literature Review on Android App Quality: Taxonomy, Challenges and Future Directions"**

---

## Repository Structure

data/SLR_PS1_78.xlsx → Extracted dataset (78 primary studies)
scripts/inter_rater_reliability.py → Cohen's kappa + observed agreement script
output/agreement_results.csv → Generated agreement statistics
docs/search_strings.md → Executed search queries and filters
docs/query_screenshots/ → Database query execution logs

---

## What This Package Contains

- Executed search queries for all databases
- PRISMA initial retrieval (443 records)
- Extracted ISO/IEC 25010 attribute mappings (FS–P)
- Methodological quality assessment (Q1–Q6)
- Inter-rater reliability calculations (Cohen’s κ)
- Observed agreement percentages

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

### Transparency

All database search strings, filters, and execution screenshots are provided in the /docs directory.