import pandas as pd
import matplotlib.pyplot as plt
import os

# === Load Data ===
forecast_path = "StockPrediction/AAPL_2024-01-01_to_2025-02-28_forecast.csv"
sentiment_path = "StockPrediction/AAPL_news_sentiment.csv"
output_plot = "StockPrediction/AAPL_forecast_vs_sentiment.png"

forecast_df = pd.read_csv(forecast_path)
sentiment_df = pd.read_csv(sentiment_path)

# Ensure datetime format for merge
forecast_df["Date"] = pd.to_datetime(forecast_df["Date"])
sentiment_df["date"] = pd.to_datetime(sentiment_df["date"])

# Rename sentiment date column for merge
sentiment_df.rename(columns={"date": "Date"}, inplace=True)

# Merge on date
merged_df = pd.merge(forecast_df, sentiment_df[["Date", "sentiment"]], on="Date", how="inner")

# === Plot ===
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot forecast (stock prices)
ax1.set_xlabel("Date")
ax1.set_ylabel("Stock Price (Close)", color="blue")
ax1.plot(merged_df["Date"], merged_df["Close"], label="Forecasted Price", color="blue")
ax1.tick_params(axis='y', labelcolor="blue")

# Plot sentiment on secondary y-axis
ax2 = ax1.twinx()
ax2.set_ylabel("Sentiment Score", color="green")
ax2.plot(merged_df["Date"], merged_df["sentiment"], label="Sentiment", color="green", linestyle="--")
ax2.tick_params(axis='y', labelcolor="green")

# Finalize plot
plt.title("AAPL: Forecasted Stock Price vs News Sentiment")
fig.tight_layout()
plt.grid(True)
plt.savefig(output_plot)
plt.show()

print(f"📊 Plot saved to: {output_plot}")
