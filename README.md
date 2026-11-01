# Mental Health in Tech — Project G7

**Authors:** Chamini Dissanayake, Bohdan Fochuk
**Course:** Introduction to Data Science (LTAT.02.002), University of Tartu, autumn 2026

## Motivation and goal

Mental health problems are common in the technology sector, but whether someone
seeks treatment depends on more than symptoms alone — workplace culture, employer
benefits and fear of career consequences all play a part. Using seven waves of survey responses 
collected between 2014 and 2021 from Open Sourcing Mental Health (OSMI), we ask which workplace
and demographic factors predict whether a tech worker seeks treatment, and how
attitudes to disclosure have changed over time.

## Data

| Wave | Size | Source |
|---|---|---|
| 2014 | 304 KB | https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey |
| 2016 | 1.1 MB | https://www.kaggle.com/datasets/osmi/mental-health-in-tech-2016 |
| 2017–2021 | 1.91 MB | https://data.mendeley.com/datasets/mmnzx4w8cg/1 (DOI 10.17632/mmnzx4w8cg.1) |

Licences: CC BY-SA 3.0 (2014), CC BY-SA 4.0 (2016), CC BY 4.0 (2017–2021).
The 2017–2021 file is a third-party compilation, pre-filtered to tech roles with
free-text questions removed.

## Goals

1. Clean the 2014 and 2016 waves, harmonise their schemas against the 2017–2021
   compilation, and merge all seven surveys into a single unified dataset.
2. Build and compare classification models predicting whether a respondent has
   sought treatment for a mental health condition.
3. Analyse how attitudes shifted across 2014-2021 - willingness to discuss mental health with an employer, and perceived career consequences of disclosure.
4. (If time allows) Compare employer-level factors against help-seeking.

## Repository contents

- `data/raw/` — the three source survey files, unmodified. See `data/raw/README.md` for provenance.
- `data/processed/` — merged and cleaned datasets produced by our notebooks (not tracked in git).
- `notebooks/` — analysis notebooks.
- `src/` — reusable code.

## How to reproduce

_To be filled in as the project develops._

## Licensing

Code in this repository is released under the MIT Licence (see `LICENSE`).

The survey data is **not** ours. It is published by Open Sourcing Mental Health
(OSMI) under CC BY-SA 3.0 (2014 wave) and CC BY-SA 4.0 (2016 wave), and the
2017–2021 compilation by Faran Rasheed Memon under CC BY 4.0
(DOI 10.17632/mmnzx4w8cg.1).

Any merged or derived dataset in `data/processed/` is distributed under
**CC BY-SA 4.0**, as required by the ShareAlike terms of the source data.
