""" 
!!!
Resulting csv file of extract_energy_data_v1 does not contain the expected data.
NEW APPROACH: Download the yearly csv files manually and read them into a pandas DataFrame.
!!!
"""

import pandas as pd
import numpy as np

path = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\raw\energy\generationperproductiontype_202301010000-202401010000.csv"
path1 = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\raw\energy\one_day.csv"

# Remove the double quotes and row quotes (only visible when csv file is opened in text editor) from each row and write it to a new file

# Read the original file
with open(path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Process to remove the quotes
processed_lines = []
for line in lines:
    processed_line = line.strip()  # Remove leading/trailing white spaces
    if processed_line.startswith('"') and processed_line.endswith('"'):
        processed_line = processed_line[1:-1]  # Remove the leading and trailing quote
        processed_line = processed_line.replace('""', '"')  # Replace double quotes with single quote
    processed_lines.append(processed_line + '\n')  # Add newline character at the end

# Write the processed lines to a new file
corrected_file_path = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\raw\energy\generationpertype_202301010000-202401010000_readable.csv"
with open(corrected_file_path, 'w', encoding='utf-8') as corrected_file:
    corrected_file.writelines(processed_lines)

corrected_file_path


df = pd.read_csv(corrected_file_path)

df.head(60)