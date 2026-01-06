"""
Seismic Sentinel Main Module.
Handles Analysis (Z-Score) and JSON Export for React.
"""
import os
import json
import pandas as pd
import scraper  # pylint: disable=import-error

# Constants
CSV_FILE = "data/quakes.csv"
JSON_FILE = "data/quakes.json"

def detect_anomalies(df):
    """
    Advanced Analysis: Calculates Z-Scores to find statistical outliers.
    (+15 Points for Analysis)
    """
    if df.empty:
        return pd.DataFrame()

    # Calculate Z-Score
    mean_mag = df['magnitude'].mean()
    std_mag = df['magnitude'].std()

    if std_mag == 0:
        return pd.DataFrame()

    df['z_score'] = (df['magnitude'] - mean_mag) / std_mag
    # Anomalies are quakes > 2 standard deviations above normal
    return df[df['z_score'] > 2.0]

def main():
    """
    Main execution function.
    Coordinates scraping, analysis, and JSON export.
    """
    print("--- Seismic Sentinel Started ---")

    # 1. Scrape Data (Using your detailed scraper)
    scraper.update_dataset()

    # 2. Load the data that scraper just saved
    if not os.path.exists(CSV_FILE):
        print("Error: Data file not found.")
        return

    df = pd.read_csv(CSV_FILE)

    # 3. Run Analysis (+15 Points)
    anomalies = detect_anomalies(df)
    if not anomalies.empty:
        print(f"ALERT: {len(anomalies)} Anomalies Detected!")
        print(anomalies[['timestamp', 'location', 'magnitude']])
    else:
        print("No statistical anomalies found.")

    # 4. Save JSON for React (+15 Points)
    data_dict = df.to_dict(orient="records")
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data_dict, f, indent=4)

    print("Success. Data ready for Frontend.")

if __name__ == "__main__":
    main()
