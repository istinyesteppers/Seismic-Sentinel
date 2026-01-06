# 🌍 Seismic-Sentinel: Turkey Earthquake Anomaly Detector

**Seismic-Sentinel** is a robust Python data analysis tool designed to monitor, clean, and analyze real-time seismic activity in Turkey.

This project scrapes raw, unstructured data from the **Kandilli Observatory** (Boğaziçi University), cleans the "messy" text formats into structured datasets, and applies statistical analysis to detect anomalies—specifically **high-magnitude events** (Z-Score Analysis).

### 🚀 Key Features (Bonus Points Implemented)

* **Messy Data Scraping (+10):**
    * Connects to the Kandilli Observatory live feed.
    * Parses raw `<pre>` text blocks (unstructured strings) into clean, usable Python dictionaries.
    * Handles inconsistent formatting and missing magnitude values.

* **Statistical Analysis & Anomaly Detection (+15):**
    * **Z-Score Calculation:** Automatically flags earthquakes with magnitudes significantly higher than the local average (Statistical Outliers > 2 Standard Deviations).

* **React.js Dashboard (+15):**
    * Includes a modern frontend (`frontend/index.html`) using **React** and **Recharts** to visualize the data interactively.

* **Robustness (+5):**
    * Includes unit tests (`tests/test_project.py`) to verify math logic and data handling.
    * Code is linted and modular.

### 🛠️ Installation & Usage

1.  **Install Dependencies:**
    * Use this command to ensure all libraries install correctly:
    ```bash
    python -m pip install -r requirements.txt
    ```

2.  **Run the Pipeline (Scrape & Analyze):**
    ```bash
    python src/main.py
    ```
    * This scrapes the latest data, saves `data/quakes.csv`, calculates anomalies, and generates `data/quakes.json` for the frontend.

3.  **Launch the React Dashboard:**
    ```bash
    python -m http.server 8000
    ```
    * Open your browser to: `http://localhost:8000/frontend/index.html`

### 📊 Data Source
* **Source:** Kandilli Observatory and Earthquake Research Institute (KOERI).
* **Format:** Raw HTTP Text Stream (Parsed & Cleaned via `src/scraper.py`).
