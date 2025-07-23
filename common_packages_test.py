# common_packages_test.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json
from io import StringIO
from datetime import datetime, timezone, timedelta

def test_versions():
    print("✅ Package Versions:")
    print(f"numpy: {np.__version__}")
    print(f"pandas: {pd.__version__}")
    print(f"matplotlib: {plt.matplotlib.__version__}")
    print(f"seaborn: {sns.__version__}")
    print(f"requests: {requests.__version__}")

def test_dataframe():
    print("\n✅ Testing DataFrame creation...")
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Score': [85.6, 92.1, 78.9]
    }
    df = pd.DataFrame(data)
    print(df.describe())

def test_plot():
    print("\n✅ Testing simple plot...")
    sns.set(style="whitegrid")
    tips = sns.load_dataset("tips")
    plt.figure(figsize=(6, 4))
    sns.boxplot(x="day", y="total_bill", data=tips)
    plt.title("Total Bill Distribution by Day")
    plt.tight_layout()
    plt.savefig("test_plot.png")
    print("Plot saved as 'test_plot.png'")

def test_requests():
    print("\n✅ Testing HTTP request...")
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
    response = requests.get(url)
    if response.status_code == 200:
        print("HTTP request success!")
        df = pd.read_csv(StringIO(response.text))
        print("First 3 rows of downloaded CSV:")
        print(df.head(3))
    else:
        print(f"Request failed with status code: {response.status_code}")

if __name__ == "__main__":
    print("⏰ Current UTC Time:", datetime.utcnow())
    print("⏰ Current Beijing Time:", datetime.utcnow() + timedelta(hours=8))
    test_versions()
    test_dataframe()
    test_plot()
    test_requests()
