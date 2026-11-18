# Credit Risk Analysis

## 1. Project Overview

This project investigates the factors that may influence loan defaults using a Credit Risk Dataset containing approximately 32,000 loan records.

The aim is to explore borrower characteristics and loan information to better understand what factors may be associated with the likelihood of default.

## 2. Project Objectives

- Explore and understand the credit risk dataset.
- Identify and investigate data quality issues.
- Clean and prepare the dataset for analysis.
- Analyse factors associated with loan defaults.
- Develop visualisations to communicate findings.
- Explore predictive modelling for credit risk assessment.

## 3. Dataset

The project uses the Credit Risk Dataset from Kaggle.

Initial dataset dimensions:
- Rows: 32,581
- Columns: 12

The dataset includes information about:
- Borrower age and income.
- Employment length.
- Home ownership.
- Loan amount and interest rate.
- Loan purpose and grade.
- Previous credit history.
- Loan default status.

## 4. Initial Data Quality Observations

The initial inspection identified three potential data quality issues:

1. **Missing employment length:** `person_emp_length` contains 895 missing values.
2. **Missing interest rates:** `loan_int_rate` contains 3,116 missing values.
3. **Potentially unrealistic age:** `person_age` has a maximum value of 144, which requires further investigation.

These observations will be investigated further during the data-cleaning stage.

## 5. Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- PyCharm
- Git and GitHub

## 6. Project Status

**Current stage:** Initial data loading and inspection.

Further cleaning, exploratory data analysis, visualisation and modelling will be added as the project progresses.
