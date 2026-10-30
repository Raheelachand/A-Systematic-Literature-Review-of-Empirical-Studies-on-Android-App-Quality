"""Reproduce the inter-rater reliability results (Table 10).

Usage:  python compute_irr.py
Requires only the Python standard library (3.8+). Reads the CSV files in ./data
and prints the results; also writes results.csv next to this script.

Measures
  observed agreement  p_o = share of items on which both raters agree
  Cohen's kappa       (p_o - p_e) / (1 - p_e), p_e from each rater's own marginals
  Gwet's AC1          (p_o - p_e) / (1 - p_e), p_e = sum_k pi_k (1 - pi_k) / (q - 1),
                      pi_k = mean share of category k over both raters, q = number of categories
Interpretation follows Landis and Koch (1977). Gwet's AC1 is reported where
near-uniform scores make Cohen's kappa uninformative (kappa paradox).
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
CHARS = ["Functional suitability", "Performance efficiency", "Compatibility", "Usability",
         "Reliability", "Security", "Maintainability", "Portability"]
QACS = ["QAC1", "QAC2", "QAC3", "QAC4", "QAC5", "QAC6"]


def read(name):
    with open(os.path.join(DATA, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def agreement(a, b):
    return sum(x == y for x, y in zip(a, b)) / len(a)


def cohen_kappa(a, b):
    n = len(a)
    po = agreement(a, b)
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in set(a) | set(b))
    return float("nan") if pe == 1 else (po - pe) / (1 - pe)


def gwet_ac1(a, b):
    n = len(a)
    cats = set(a) | set(b)
    po = agreement(a, b)
    if len(cats) < 2:
        return 1.0
    pi = {c: (a.count(c) + b.count(c)) / (2 * n) for c in cats}
    pe = sum(p * (1 - p) for p in pi.values()) / (len(cats) - 1)
    return (po - pe) / (1 - pe)


def num(x):
    return float(x) if x not in ("", None) else None


def chars(s):
    return {c.strip() for c in (s or "").split(";") if c.strip()}


results = []


def report(stage, measure, a, b, stat="kappa"):
    k = cohen_kappa(a, b) if stat == "kappa" else gwet_ac1(a, b)
    results.append([stage, measure, len(a), round(100 * agreement(a, b), 1),
                    "Cohen's kappa" if stat == "kappa" else "Gwet's AC1", round(k, 2)])


# Stage 1: title/abstract screening, stratified sample of 400 records
s1 = read("stage1_screening_400.csv")
report("Screening (sample)", "Include/exclude decision",
       [r["r1_decision"] for r in s1], [r["r2_decision"] for r in s1])

# Stage 2: full-text eligibility and quality, sample of 50 full texts
s2 = [r for r in read("stage2_fulltext_qa_50.csv") if r["r1_decision"] and r["r2_decision"]]
report("Full text and quality (sample)", "Final decision",
       [r["r1_decision"] for r in s2], [r["r2_decision"] for r in s2])

# Stage 3: ISO/IEC 25010 classification within pairs, initial sample of 102 studies
s3 = read("stage3_classification_102.csv")
report("Classification within pairs (initial sample)", "Primary ISO/IEC 25010 characteristic",
       [r["r1_primary_characteristic"] for r in s3], [r["r2_primary_characteristic"] for r in s3])

# Stage 4: cross-pair re-check of the 159 studies under the final criteria
s4 = read("stage4_crosspair_recheck_159.csv")
report("Cross-pair re-check", "Include decision",
       [r["r1_include"] for r in s4], [r["r2_include"] for r in s4], stat="ac1")
for q in QACS:
    pairs = [(num(r["r1_" + q]), num(r["r2_" + q])) for r in s4]
    pairs = [p for p in pairs if None not in p]
    report("Cross-pair re-check", q, [p[0] for p in pairs], [p[1] for p in pairs], stat="ac1")
all1, all2 = [], []
for c in CHARS:
    a = [c in chars(r["r1_characteristics"]) for r in s4]
    b = [c in chars(r["r2_characteristics"]) for r in s4]
    all1 += a
    all2 += b
    report("Cross-pair re-check (ISO/IEC 25010)", c, a, b)
report("Cross-pair re-check (ISO/IEC 25010)", "Overall (all characteristics)", all1, all2)

head = ["Stage", "Measure", "n", "Observed agreement (%)", "Statistic", "Value"]
with open(os.path.join(HERE, "results.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(head)
    w.writerows(results)
width = [40, 38, 5, 10, 14, 6]
print("  ".join(h[:w_].ljust(w_) for h, w_ in zip(head, width)))
for r in results:
    print("  ".join(str(x)[:w_].ljust(w_) for x, w_ in zip(r, width)))
