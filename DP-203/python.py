import pandas as pd

uri = "https://sawedemo01.blob.core.windows.net/data/ActivityLog-01.csv"

response = pd.read_csv(uri)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print(response)