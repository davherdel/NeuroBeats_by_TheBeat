# NeuroBeats – Applied Machine Learning for YouTube Niche Engagement

## Project Overview

NeuroBeats is an end-to-end applied Machine Learning project focused on modeling engagement dynamics within highly specific YouTube niches:

- Lofi
- Chillhop
- Study-oriented content

The objective was not only to build a predictive model, but to:

- Engineer domain-specific features
- Detect and correct data leakage
- Design robust validation strategies
- Prioritize generalization over inflated metrics
- Interpret model behavior using feature importance tools

This project emphasizes ML rigor over surface-level analytics.

---

## Business Framing

Can we predict expected audience engagement using structured metadata, niche-specific triggers, temporal patterns, and channel authority signals?

Rather than modeling views, the project targets:

**Engagement = Likes + Comments**

Engagement was chosen because it reflects active audience commitment — especially relevant in niche communities.

Target transformation:
`log1p(likes + comments)`  
to normalize skewed distributions and reduce viral outlier distortion.

---

## Feature Engineering (Core Contribution)

Significant effort was invested in domain-driven feature creation.

### Content & Niche Strategy (Engineered)
- `is_pomodoro`
- `is_live`
- `is_long_form` (>20 minutes)
- `has_visuals`
- `video_duration_seconds`
- `title_length`

These features capture behavioral triggers specific to the Lofi/Study ecosystem.

### Temporal Modeling
- `year`
- `year_label`

Captures post-2020 niche acceleration and structural shifts.

### Channel Authority Metrics
- `log_subscribers`
- `log_channel_views`
- `channel_video_count`

Log transformations were applied to stabilize variance and reduce heteroscedasticity.

---

## Model Development & Validation

### Baseline Phase
- Linear Regression
- Random Forest

Initial Random Split produced R² ≈ 0.49  
→ Identified as leakage-prone and overly optimistic.

### Leakage Detection & Correction

Evaluation transitioned to:

- GroupShuffleSplit (by channel)
- GroupKFold (by keyword)

This forced cross-niche generalization and removed hidden signal leakage.

### Final Model Comparison

| Model | Validation Strategy | R² | Notes |
|-------|--------------------|-----|------|
| RF | Random Split | 0.49 | Leakage likely |
| RF | GroupKFold | 0.18 | Realistic baseline |
| XGBoost | GroupKFold | 0.20–0.37 | Strongest generalizable model |

Peak fold performance reached R² = 0.83 in niche-specific segments.

---

## Feature Importance & Model Interpretation

Interpretability was prioritized over raw performance.

- SHAP Global Explainer used for impact analysis
- Feature importance showed:

  - Long-form duration strongly influences engagement
  - Channel authority stabilizes predictions
  - Keyword stacking has limited predictive impact
  - Format-driven triggers add measurable signal

The project demonstrates how domain-aligned feature engineering can outperform superficial metadata optimization.

---

## Technical Stack

- Python
- Pandas
- Scikit-learn
- XGBoost
- SHAP
- YouTube Data API
- Cross-validation (GroupKFold)
- REAPER (applied production layer)

---

## Engineering Highlights

- End-to-end ML pipeline ownership
- Advanced feature engineering
- Leakage detection & mitigation
- Group-aware cross-validation
- Model stability analysis
- SHAP-based interpretability
- Translation of ML insights into real production decisions

---

## What This Project Demonstrates

- Applied ML thinking
- Model robustness prioritization
- Evaluation discipline
- Feature design in low-signal environments
- Practical ML implementation beyond notebook-level experimentation

---

## Author
David Hernandez
💻📊Applied ML & Data Analyst  
📍 Based in Portugal  
💼 Open to ML Engineer & Data-focused roles  
📫 LinkedIn: https://www.linkedin.com/in/david-hernandez-cr-pt/