import pandas as pd

file_path = "kc_house_data.csv"
data = pd.read_csv(file_path)
print(data.head())

