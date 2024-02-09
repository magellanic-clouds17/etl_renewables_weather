import pandas as pd

# tranform from txt to csv

# Define the path to the unzipped .txt file
txt_file_path = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\raw\air_temperature\stundenwerte_TU_00096_akt\produkt_tu_stunde_20220807_20240207_00096.txt"

# Define the path for the new .csv file
csv_file_path = txt_file_path.replace('.txt', '.csv')

# Read the .txt file
df = pd.read_csv(txt_file_path, sep=';', skipinitialspace=True)

# Write to a .csv file
df.to_csv(csv_file_path, index=False)

print(f"Converted {txt_file_path} to {csv_file_path}")

"""
next step: automate the process of converting all .txt files in the air_temperature folder to .csv files
then: combine all .csv files into one time series file with datetime as index and station id as first column
"""


