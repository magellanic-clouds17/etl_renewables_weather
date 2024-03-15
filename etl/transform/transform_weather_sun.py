
import pandas as pd
import os

def csvs_to_df(file_path):
    df = pd.read_csv(file_path, delimiter=";")
    df = df.drop(['QN_7', 'eor'], axis=1)
    df['MESS_DATUM'] = pd.to_datetime(df['MESS_DATUM'], format='%Y%m%d%H')
    df = df.set_index('MESS_DATUM')
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
    
    # Optional: Sort the DataFrame by index if necessary
    combined_df.sort_index(inplace=True)
    
    return combined_df

# Example usage
root_folder = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\raw\weather\sun\historical"

combined_df = loop_folders(root_folder)

# Save the combined DataFrame to a CSV file
combined_df.to_csv(r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\interim\weather\combined_sun_data.csv")


# reshape df using the station_id as columns, the datetime index as rows and the temperature as values
df = combined_df.pivot(columns='STATIONS_ID', values='SD_SO').round(1)

# count nan values per column
df.isnull().sum().head(32)
df.isnull().sum().tail(32)

# transform datetime index from hourly to 3-hourly frequency
df3 = df.resample('3H').sum()
# fill NaN values using linear interpolation
df = df.interpolate(method='linear')

df3.head(20)

''' NEED TO FIND SOLUTION FOR NAN VALUES'''