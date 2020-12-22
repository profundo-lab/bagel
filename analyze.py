import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport
import sys


def main() -> None:
    if len(sys.argv) != 4:
        print("Usage: python3 analyze.py title input.csv output.html")
        return
    data_source = sys.argv[2]
    df = pd.read_csv(data_source)
    profile = ProfileReport(df, title=sys.argv[1])
    profile.to_file(sys.argv[3])

if __name__ == '__main__':
    main()


