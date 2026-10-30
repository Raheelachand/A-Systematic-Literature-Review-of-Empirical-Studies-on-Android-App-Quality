# Inter-rater reliability

Data and script that reproduce the inter-rater reliability results reported in the paper (Table 10).

```text
data/stage1_screening_400.csv          Title/abstract screening, stratified sample of 400 records
data/stage2_fulltext_qa_50.csv         Full-text eligibility and quality assessment, sample of 50 full texts
data/stage3_classification_102.csv     Primary ISO/IEC 25010 characteristic, initial sample of 102 studies
data/stage4_crosspair_recheck_159.csv  Cross-pair re-check of the 159 studies under the final criteria:
                                       include decision, QAC1–QAC6 and ISO/IEC 25010 characteristics
compute_irr.py                         Computes observed agreement, Cohen's kappa and Gwet's AC1
results.csv                            Output of compute_irr.py
```

Run with Python 3.8 or later (standard library only):

```bash
python compute_irr.py
```

Columns prefixed `r1_` and `r2_` hold the two independent codings of each item. In stage 2, two records without a decision from one rater are excluded from the computation (n = 48). In stage 4, ISO/IEC 25010 agreement is computed per characteristic on presence/absence, since a study can address more than one characteristic. Interpretation follows Landis and Koch (1977); Gwet's AC1 is reported where near-uniform scores make Cohen's kappa uninformative.
