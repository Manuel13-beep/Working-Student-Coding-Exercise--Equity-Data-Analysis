# Working-Student-Coding-Exercise--Equity-Data-Analysis
Equity Data Analysis Exercise
Objective

The objective of this exercise was to identify the five best-performing securities between 1 June 2021 and 13 October 2021, calculate their percentage return, determine each company's 30-day average trading volume as of the end date, and present the findings using tables and visualisations.

# Summarised Approach

The analysis was implemented in Python using Pandas for data manipulation, Matplotlib for visualisation, and ReportLab for generating the final PDF report.

The workflow consisted of the following steps:

1. Load the CSV dataset into a Pandas DataFrame.
2. Inspect the dataset structure and identify missing values.
3. Convert the date column from string format to a datetime object.
4. Remove rows containing missing numerical values.
5. Filter the dataset to the required analysis period (2021-06-01 to 2021-10-13).
6. Calculate each company's percentage performance using the first and last closing prices within the selected period.
7. Rank companies according to their percentage return.
8. Calculate the 30-trading-day average trading volume ending on 13 October 2021 for the five best-performing companies.
9. Generate visualisations showing both the raw closing price history and the normalized price history.
10.  Produce a PDF report summarising the analysis.

# Performance calculation

Performance was calculated using the closing prices at the beginning and end of the analysis period:
<img width="427" height="77" alt="image" src="https://github.com/user-attachments/assets/fad8a437-729b-4170-b070-7acbe27b8abb" />


Only closing prices were considered, as these represent the standard reference for measuring historical equity returns.

# 30-day average trading volume

The exercise requested the 30-day average trading volume on 13 October 2021.

# Data observations

Several characteristics of the dataset influenced my analysis.

The dataset contains historical market information for 100 companies over approximately one trading year.
Most companies contained the expected number of observations for the selected period, although a few companies had fewer records due to missing observations.

One particularly notable finding was the approximately 940% increase observed for General Electric during the analysis period. Such a large increase is unusual for publicly traded equities over a four-month period.
I interpreted this as the average trading volume over the previous 30 trading sessions, rather than the previous 30 calendar days(that is excluding holidays and weekends)following a common practice in financial market.

# Additional analysis

In addition to the requested closing price history, I generated a normalized price chart (base = 100).
<img width="508" height="82" alt="image" src="https://github.com/user-attachments/assets/572233e3-a119-457b-b896-8a27b0b26f9c" />

Although not explicitly required, it provides a more meaningful comparison of relative performance because all securities begin from the same reference value regardless of their initial share price.

This makes percentage growth easier to compare across companies with substantially different starting prices.



