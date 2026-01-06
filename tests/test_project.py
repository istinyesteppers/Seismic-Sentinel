"""
Unit Tests for Seismic Sentinel.
Run with: pytest
"""
import sys
import os
import pandas as pd

# Fix import path to find src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# pylint: disable=wrong-import-position, import-error
import main
# pylint: enable=wrong-import-position, import-error


def test_anomaly_math():
    """Test if Z-Score logic correctly identifies an outlier."""
    data = {
        'magnitude': [2.0, 2.0, 2.0, 2.0, 9.0],  # 9.0 is the anomaly
        'location': ['Test'] * 5
    }
    df = pd.DataFrame(data)
    anomalies = main.detect_anomalies(df)

    # Should find exactly 1 anomaly
    assert len(anomalies) == 1
    assert anomalies.iloc[0]['magnitude'] == 9.0


def test_empty_data():
    """Test robustness against empty datasets."""
    df = pd.DataFrame()
    anomalies = main.detect_anomalies(df)
    assert anomalies.empty
