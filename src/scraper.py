"""
Seismic Data Scraper Module.

This module is responsible for fetching raw earthquake data from the
Kandilli Observatory, parsing the unstructured text, and cleaning it
into a structured format for analysis.
"""

import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Constants
URL = "http://www.koeri.boun.edu.tr/scripts/lst0.asp"
DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "quakes.csv")
TIMEOUT_SECONDS = 10


def fetch_quake_data():
    """
    Fetches raw text data from the Kandilli Observatory.

    Returns:
        list: A list of raw text lines from the website.
              Returns an empty list if the connection fails.
    """
    try:
        response = requests.get(URL, timeout=TIMEOUT_SECONDS)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        pre_tag = soup.find('pre')

        if not pre_tag:
            return []

        raw_text = pre_tag.text
        # Split by new line and skip the header rows (approx first 7 lines)
        lines = raw_text.split('\n')[7:]
        return lines

    except requests.RequestException as error:
        print(f"Network error occurred: {error}")
        return []


def parse_line(line):
    """
    Parses a single line of raw text into a structured dictionary.

    Args:
        line (str): A raw string containing earthquake data.

    Returns:
        dict: A dictionary containing timestamp, lat, long, depth, magnitude, and location.
              Returns None if the line is malformed.
    """
    if len(line) < 50:
        return None

    parts = line.split()
    if len(parts) < 8:
        return None

    try:
        # Extract columns based on standard Kandilli format
        date_str = parts[0]
        time_str = parts[1]
        latitude = float(parts[2])
        longitude = float(parts[3])
        depth = float(parts[4])
        
        # Magnitude is usually in the 6th index (ML), replacing empty placeholders
        magnitude_str = parts[6].replace('-.-', '0.0')
        magnitude = float(magnitude_str)

        location = " ".join(parts[8:])
        timestamp = f"{date_str} {time_str}"

        return {
            "timestamp": timestamp,
            "latitude": latitude,
            "longitude": longitude,
            "depth": depth,
            "magnitude": magnitude,
            "location": location
        }
    except ValueError:
        return None


def update_dataset():
    """
    Main execution function.
    Fetches data, parses it, and saves it to a CSV file.
    """
    print("Fetching data from Kandilli Observatory...")
    raw_lines = fetch_quake_data()
    
    clean_data = []
    for line in raw_lines:
        parsed_item = parse_line(line)
        if parsed_item:
            clean_data.append(parsed_item)

    if clean_data:
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        df_quakes = pd.DataFrame(clean_data)
        df_quakes.to_csv(DATA_FILE, index=False)
        print(f"Success: Saved {len(df_quakes)} earthquake records to {DATA_FILE}")
    else:
        print("No valid data found.")

if __name__ == "__main__":
    update_dataset()
