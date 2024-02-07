# tranform from txt to csv

# Define the path to the unzipped .txt file
txt_file_path = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\raw\yourfile.txt"

# Define the path for the new .csv file
csv_file_path = txt_file_path.replace('.txt', '.csv')

# Read the .txt file
df = pd.read_csv(txt_file_path, sep=';', skipinitialspace=True)

# Write to a .csv file
df.to_csv(csv_file_path, index=False)

print(f"Converted {txt_file_path} to {csv_file_path}")