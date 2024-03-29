import pandas as pd
import os

def csvs_to_df(file_path):
    df = pd.read_csv(file_path, delimiter=";")
    df = df.drop(['QN_9', 'RF_TU', 'eor'], axis=1)
    df['MESS_DATUM'] = pd.to_datetime(df['MESS_DATUM'], format='%Y%m%d%H')
    df = df.set_index('MESS_DATUM')
    # transform datetime index from hourly to 3-hourly frequency using mean
    df = df.resample('3H').mean().round(1)
    # fill NaN values using linear interpolation
    df = df.interpolate(method='linear')
    df = df['2015-01-01':'2019-12-31']
    return df

def loop_folders(root_folder):
    dfs = []  # List to store individual DataFrames
    for subdir, dirs, files in os.walk(root_folder):
        for file in files:
            if file.startswith("produkt"):
                file_path = os.path.join(subdir, file)
                df = csvs_to_df(file_path)
                dfs.append(df)
    
    # Concatenate all DataFrames
    combined_df = pd.concat(dfs)
    
    # Sort the DataFrame by index
    combined_df.sort_index(inplace=True)
    
    return combined_df

# Example usage
root_folder = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\raw\weather\air_temperature\historical"
combined_df = loop_folders(root_folder)

# Save the combined DataFrame to a CSV file
combined_df.to_csv(r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\interim\weather\combined_air_temp_data.csv")

# count rows with with same index
print(combined_df.index.value_counts().head(10))

# check for missing values through 3-hourly frequency
combined_df.tail(60)

# reshape df using the station_id as columns, the datetime index as rows and the temperature as values
df = combined_df.pivot(columns='STATIONS_ID', values='TT_TU').round(1)

# drop columns with nan values
df = df.dropna(axis=1)

# save df in processed folder
df.to_csv(r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\processed\weather\air_temp\air_temp_2015_2019.csv")