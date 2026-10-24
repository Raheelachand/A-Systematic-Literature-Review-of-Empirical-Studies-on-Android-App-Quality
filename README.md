# Replication Package

## What Gets Measured Gets Studied: A Cross-Attribute Systematic Literature Review of Android Application Quality Revealing Measurability Bias and Its Implications

**Version:** v2.0 (screening protocol revision)  
**Review period:** January 2017 – October 2026  
**Status:** Revised screening and quality assessment in progress  
**Quality framework:** ISO/IEC 25010:2011

---

## Overview

This repository contains the replication package for the systematic literature review:

**"What Gets Measured Gets Studied: A Cross-Attribute Systematic Literature Review of Android Application Quality Revealing Measurability Bias and Its Implications."**

The review investigates Android application quality research across the eight software product quality characteristics defined in ISO/IEC 25010:2011:

1. Functional suitability
2. Performance efficiency
3. Compatibility
4. Usability
5. Reliability
6. Security
7. Maintainability
8. Portability

The study examines how research attention is distributed across these characteristics, identifies recurring quality challenges, analyses proposed assessment and improvement approaches, and synthesises research gaps and future directions.

A central objective is to investigate **measurability bias**: whether research attention tends to concentrate on quality problems for which measurement techniques, datasets, tools, and evaluation procedures are readily available.

The review follows established systematic literature review practices in software engineering, informed by Kitchenham's guidelines, and uses PRISMA to report the study selection process.

**Note:** The revised screening is in progress. Final study counts, quality assessment results, and inter-rater reliability statistics will be reported after screening and validation are complete.

---

## Research Questions

The review addresses four research questions:

| ID | Research Question |
|---|---|
| RQ1 | What is the research landscape of Android application quality across the ISO/IEC 25010 quality characteristics? |
| RQ2 | What are the main quality challenges reported in Android application research? |
| RQ3 | What methods and approaches have been proposed in the literature to assess or improve Android application quality? |
| RQ4 | What research gaps and future directions emerge from the existing literature on Android application quality? |

---

## Search Strategy

The literature search covers publications from **January 2017 to October 2026**.

The review considers records retrieved from the following scholarly databases and digital libraries:

- Scopus
- IEEE Xplore
- ACM Digital Library
- SpringerLink
- ScienceDirect
- Wiley Online Library

Database-specific search strings, filters, execution dates, and retrieval counts should be documented in `docs/search_strings.md`.

Search results are deduplicated before title and abstract screening. Eligible candidates proceed to full-text assessment and quality assessment.

The repository should preserve the original search exports and screening decisions to enable independent verification of the review process.

---

## Inclusion Criteria (IC)

| ID | Inclusion Criterion |
|---|---|
| IC1 | Peer-reviewed, full-length journal articles or conference research papers published in English between January 2017 and October 2026. |
| IC2 | Primary studies specifically investigating Android applications or Android application components, with identifiable Android-specific findings. |
| IC3 | Studies presenting an original empirical investigation, method, technique, tool, framework, dataset, or theoretical contribution that directly addresses at least one Android application quality characteristic defined in ISO/IEC 25010:2011. |

## Exclusion Criteria (EC)

| ID | Exclusion Criterion |
|---|---|
| EC1 | Secondary studies, short papers, posters, demos, extended abstracts, editorials, non-peer-reviewed publications, retracted papers, corrections, duplicates, or superseded versions. |
| EC2 | Studies focused on application development, domain-specific functionality, Android OS, hardware, or general mobile computing without a direct contribution to Android application quality. |
| EC3 | Studies primarily focused on malware detection, malware classification, or malicious application identification rather than assessing or improving Android application security quality. |
| EC4 | Studies whose full text cannot be obtained through institutional access or open-access sources after reasonable retrieval attempts. |

### Eligibility Clarifications

- Android games are assessed under the same eligibility criteria as other Android applications.
- Studies do not need to explicitly mention ISO/IEC 25010 to be eligible.
- Studies addressing multiple quality characteristics may receive multiple attribute mappings.
- Research on Android application vulnerabilities, permission misuse, privacy leakage, or insecure application behavior may be eligible.
- Studies primarily concerned with identifying or classifying malicious applications are excluded under EC3.
- Cross-platform studies are eligible when identifiable Android-specific findings are available.
- Unclear titles or abstracts are marked as **Unsure (U)** rather than automatically excluded.
- EC4 is applied during full-text assessment.

---

## Quality Assessment Criteria (QAC)

After full-text eligibility assessment, included studies are evaluated using five study-specific quality assessment criteria.

| ID | Quality Assessment Criterion |
|---|---|
| QA1 | Does the study identify the Android application quality problem or characteristic being investigated? |
| QA2 | Does the study describe the method, technique, tool, framework, dataset, or research approach used to investigate Android application quality? |
| QA3 | Does the study explain how its approach addresses the identified Android application quality problem? |
| QA4 | Does the study provide evidence, analysis, or reasoning supporting its findings or contribution concerning Android application quality? |
| QA5 | Does the study report limitations or assumptions relevant to its Android application quality findings or proposed approach? |

### Quality Assessment Scoring

Each criterion is scored using the following scale:

- **1 — Yes:** The criterion is fully satisfied.
- **0.5 — Partial:** The criterion is partially satisfied.
- **0 — No:** The criterion is not satisfied.

| ID | Yes (1) | Partial (0.5) | No (0) |
|---|---|---|---|
| QA1 | Both the Android quality problem and the investigated characteristic can be identified. | A quality concern is identifiable, but the problem is not specified. | Neither can be identified. |
| QA2 | The approach and its main steps or components are described. | The approach is identified, but one or more main steps or components are omitted. | No identifiable approach. |
| QA3 | The study explicitly explains how its approach addresses the quality problem. | The connection is identifiable but is not explicitly explained. | No identifiable connection. |
| QA4 | The main findings are supported by reported data, analysis, examples, or reasoned arguments. | Some main findings are supported, but others remain unsupported. | No support for the main findings. |
| QA5 | At least one relevant limitation or assumption is identified and discussed. | A limitation or assumption is mentioned without explaining its implications. | Neither is reported. |

The total quality score is calculated as:

**QA Total = QA1 + QA2 + QA3 + QA4 + QA5**

The possible score ranges from **0 to 5**.

Quality scores are used to characterise reporting quality and the strength of the available evidence. No automatic exclusion threshold is imposed solely on the basis of the total QA score.

Reviewers should record supporting passages or section references for their assigned scores.

---

## Study Selection Procedure

The review follows a multi-stage screening process.

**Stage 1 — Identification and Deduplication**

Search records are exported from the selected databases. Duplicate records are identified and removed, with the original retrieval counts and deduplication decisions documented.

**Stage 2 — Title and Abstract Screening**

Records are screened using IC1–IC3 and applicable exclusion criteria.

Screening decisions are recorded as:

- **Y — Include candidate:** The available information supports eligibility.
- **N — Exclude:** The record clearly fails an inclusion criterion or meets an exclusion criterion.
- **U — Unsure:** Eligibility cannot be determined from the available information.

**Stage 3 — Full-Text Eligibility Assessment**

Potentially eligible studies are assessed using their full texts. Exclusion reasons are recorded, including full-text unavailability under EC4.

**Stage 4 — Quality Assessment**

Eligible primary studies are assessed using QA1–QA5. Individual scores, total scores, and supporting justifications are recorded.

**Stage 5 — Data Extraction and Synthesis**

Included studies are mapped to ISO/IEC 25010:2011 and analysed in relation to RQ1–RQ4.

The final PRISMA flow diagram and screening counts will be updated when the revised selection process is complete.

---

## Data Extraction and Classification

The extraction protocol is designed to capture:

- Bibliographic information and publication year
- Android application context
- Investigated software quality problems
- ISO/IEC 25010:2011 quality characteristic mappings
- Proposed methods, techniques, tools, frameworks, or datasets
- Research design and evaluation approach
- Reported findings and supporting evidence
- Study limitations and assumptions
- Quality assessment scores
- Research gaps and future directions

The classification scheme supports mapping a single study to more than one quality characteristic when justified by its content.

Information about empirical validation, datasets, benchmarks, metrics, and evaluation environments is extracted separately to support the investigation of measurability bias.

---

## Repository Structure

The following structure represents the **target organisation for the revised replication package**. Files should be added or replaced as the updated screening and extraction are completed.

```text
data/
  raw/
    README.md
  screening/
    title_abstract_screening.csv
    full_text_screening.csv
  extraction/
    primary_studies.xlsx
  quality_assessment/
    quality_assessment.xlsx

docs/
  search_strings.md
  query_screenshots/
  screening_protocol.md
  quality_assessment_rubric.md
  data_extraction_codebook.md

scripts/
  inter_rater_reliability.py

output/
  agreement_results.csv
  prisma_counts.csv

requirements.txt
README.md
LICENSE
```

The revised package replaces the previous fixed study-count dataset and six-question quality assessment scheme with updated screening records and the five-question QA framework.

---

## Inter-Rater Reliability

Where independent reviewer assessments are available, inter-rater reliability is evaluated using Cohen's kappa (κ) and observed agreement.

Reliability analysis may cover:

- Title and abstract screening decisions
- Full-text eligibility decisions
- ISO/IEC 25010 quality characteristic classifications
- QA1–QA5 scores

The analysis should use an agreement statistic appropriate to the coding scale. For example, Cohen's κ may be used for nominal decisions, while weighted κ may be appropriate for the ordered QA scores of 0, 0.5, and 1.

Only results calculated from the revised reviewer data should be reported.

### Requirements

Python 3.9 or later, together with the dependencies listed in `requirements.txt`.

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Reliability Script

```bash
python scripts/inter_rater_reliability.py
```

The script and its expected input files must be verified or updated to reflect the revised QA1–QA5 scoring framework before publishing new reliability results.

---

## Transparency and Reproducibility

The revised replication package is intended to provide:

- Executed database search queries and filters
- Search execution dates and retrieval counts
- Original bibliographic exports, where redistribution is permitted
- Deduplication records
- Title and abstract screening decisions
- Full-text eligibility decisions and exclusion reasons
- PRISMA study selection counts
- Quality assessment criteria, scores, and justifications
- ISO/IEC 25010:2011 classification data
- Data extraction codebook
- Inter-rater reliability scripts and results
- Final included-study dataset

The package will be updated as the revised review progresses.

---

## Archival Record

An earlier replication package is associated with the following Zenodo DOI:

**https://doi.org/10.5281/zenodo.18621632**

This DOI should not be presented as the archived version of the revised package until the updated materials have been deposited and the corresponding Zenodo record has been verified.

---

## Citation

The revised manuscript is titled:

*What Gets Measured Gets Studied: A Cross-Attribute Systematic Literature Review of Android Application Quality Revealing Measurability Bias and Its Implications.*

The final bibliographic citation, journal information, and archival DOI will be added when confirmed.

---

## License

This repository is distributed under the MIT License, subject to the terms of the repository's `LICENSE` file.

Third-party publications, database exports, and other externally sourced materials remain subject to their respective copyright and licensing conditions.
