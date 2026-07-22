import pandas as pd
import matplotlib.pyplot as plt
import os




# Loading of equity dataset
data_frame = pd.read_csv(r"C:\Users\manue\Documents\Quant_project\data\equity_data.csv")

##########  Data exploration and Inspection #################################

# Display first rows
print(data_frame.head())

print("\nDataset information:")
print(data_frame.info())

print("\nStatistical summary:")
print(data_frame.describe())

# Convert date column
data_frame["date"] = pd.to_datetime(data_frame["date"])

# Remove missing values
data_frame.dropna(inplace=True)

# Sort by company and date
data_frame = data_frame.sort_values(["ticker", "date"])

print(data_frame.info())

print(data_frame.head())

########  Understanding the companies inside the dataset   #########################################

# Number of unique companies
print("Number of companies:")
print(data_frame["ticker"].nunique())


# List companies
print("\nCompanies:")
print(data_frame["ticker"].unique())


# Number of records per company
print("\nRecords per company:")
print(data_frame["ticker"].value_counts())

##### Filtering the dataset in the Specific Timeframe #####

# Define analysis period
start_date = "2021-06-01"
end_date = "2021-10-13"

period_df = data_frame[
    (data_frame["date"] >= start_date) &
    (data_frame["date"] <= end_date)
]
print(period_df.head())
print(period_df.tail())

##### QUESTION 1. Calculating Performance Metrics for Each Company ######################

performance = (
    period_df
    .groupby(["ticker", "name", "isin"])
    .agg(
        start_price=("close", "first"),
        end_price=("close", "last")
    )
    .reset_index()
)

performance["performance_%"] = (
    (performance["end_price"] - performance["start_price"])
    /
    performance["start_price"]
    * 100
)

performance = performance.sort_values(
    "performance_%",
    ascending=False
)

top5 = performance.head(5)
print(top5)


##gene = period_df[period_df["ticker"]=="GENE"]
##print(gene[["date","close"]].head())
##print(gene[["date","close"]].tail())

#####  QUESTION 2. Calculating the 30-Day Average Trading Volume for Each Company on DAY 2021-10-13 #####

end_date = pd.to_datetime("2021-10-13")

volume_results = []

for ticker in top5["ticker"]:

    # Selecting stock history up to day Y
    stock_data = data_frame[
        (data_frame["ticker"] == ticker) &
        (data_frame["date"] <= end_date)
    ].sort_values("date")

    # Take the last 30 trading days
    last_30_days = stock_data.tail(30)

    avg_volume = last_30_days["volume"].mean()

    volume_results.append(
        {
            "ticker": ticker,
            "avg_volume_30d": avg_volume
        }
    )
volume_df = pd.DataFrame(volume_results)
print(volume_df)

##### Printing out Table with Performance and Average Volume for Top 5 Companies #####

# Merge top 5 performance with 30-day average volume
final_table = top5.merge(volume_df, on="ticker")


final_table["performance_%"] = final_table["performance_%"].round(2)

# Format average volume as millions (e.g., 8.17M)
final_table["avg_volume_30d"] = final_table["avg_volume_30d"].apply(
    lambda x: f"{x / 1_000_000:.2f}M"
)
print(final_table)


####### Question 3. Plotting Price of the Top 5 Companies Over Time #####
os.makedirs("../reports", exist_ok=True)

plt.figure(figsize=(12, 6))

for ticker in top5["ticker"]:

    stock = period_df[period_df["ticker"] == ticker]

    plt.plot(
        stock["date"],
        stock["close"],
        linewidth=2,
        label=ticker
    )

plt.title("Top 5 Performing Stocks- Closing Price History (2021-06-01 to 2021-10-13)")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.legend(title="Ticker")
plt.grid(True)

plt.tight_layout()

plt.savefig("../reports/top5_closing_price_history.png", dpi=300)
plt.show()

######### Plotting a more normalized version of the prices for better comparison #########

plt.figure(figsize=(12, 6))

for ticker in top5["ticker"]:

    stock = period_df[period_df["ticker"] == ticker].copy()

    # Normalize prices to start at 100
    stock["normalized_price"] = (
        stock["close"] / stock["close"].iloc[0]
    ) * 100

    plt.plot(
        stock["date"],
        stock["normalized_price"],
        linewidth=2,
        label=ticker
    )

plt.title("Top 5 Performing Stocks - Normalized Price History (Base = 100)")
plt.xlabel("Date")
plt.ylabel("Normalized Price")
plt.legend(title="Ticker")
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "../reports/top5_normalized_price_history.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
