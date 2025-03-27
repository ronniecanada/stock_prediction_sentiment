from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime, timedelta
import pandas as pd
import os

# === Settings ===
ticker = "AAPL"
today = datetime.today().date()
output_dir = "StockPrediction"  # <- Match your forecast file folder here

# Create directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# === Generate Mock News Data ===
data = []
for i in range(365):
    date = today - timedelta(days=i)
    data.append({
        "source": "Yahoo Finance",
        "title": f"{ticker} stock report – {date}",
        "text": f"{ticker} stock shows strong investor sentiment.",
        "date": date
    })

df = pd.DataFrame(data)

# === Sentiment Analysis ===
analyzer = SentimentIntensityAnalyzer()
df["sentiment"] = df["text"].apply(lambda t: analyzer.polarity_scores(t)["compound"])

# === Save to CSV ===
csv_name = f"{ticker}_news_sentiment.csv"
csv_path = os.path.join(output_dir, csv_name)
df.to_csv(csv_path, index=False)

print(f"✅ Sentiment file saved to: {csv_path}")
import matplotlib.pyplot as plt

# === Plot Sentiment Over Time ===
plt.figure(figsize=(10, 5))
plt.plot(df["date"], df["sentiment"], marker='o', linestyle='-', color='teal')
plt.title(f"{ticker} - News Sentiment Over Time")
plt.xlabel("Date")
plt.ylabel("Sentiment Score")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot in same folder
plot_path = os.path.join(output_dir, f"{ticker}_sentiment_plot.png")
plt.savefig(plot_path)
plt.show()

print(f"📊 Sentiment plot saved to: {plot_path}")
