import pandas as pd


file_path_list = [r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\interim\energy\2015_2019\generation_per_type_20150101_20160101.csv",
            r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\interim\energy\2015_2019\generation_per_type_20160101_20170101.csv",
            r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\interim\energy\2015_2019\generation_per_type_20170101_20180101.csv",
            r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\interim\energy\2015_2019\generation_per_type_20180101_20190101.csv",
            r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\interim\energy\2015_2019\generation_per_type_20190101_20200101.csv"]


def transform_energy_time_frequ(file_path):
    # load the csv file to a DataFrame
    df = pd.read_csv(file_path, index_col=0)
    # convert the index to datetime
    df.index = pd.to_datetime(df.index)
    # Convert columns to numeric
    df['Wind Onshore (MW)'] = pd.to_numeric(df['Wind Onshore (MW)'], errors='coerce')
    df['Wind Offshore (MW)'] = pd.to_numeric(df['Wind Offshore (MW)'], errors='coerce')
    df['Solar (MW)'] = pd.to_numeric(df['Solar (MW)'], errors='coerce')

    # Resample data to 1-hour frequency. You can choose the method of aggregation.
    # Here, I'm using the mean, but you could use sum, max, etc., depending on your needs.
    df_resampled = df.resample('1H').mean()
    # round the values to 0 decimal places and convert to int
    df_resampled = df_resampled.round(0)
    df_resampled = df_resampled.astype(int)
    
    return df_resampled


for file_path in file_path_list:
    df_resampled = transform_energy_time_frequ(file_path)
    # print the info, first 50 rows, null values and average of each row of the resampled DataFrame
    print(df_resampled.info())
    print(df_resampled.head(50))
    print(df_resampled.isnull().sum())
    for column in df_resampled.columns:
        print(f"Average {column}: {df_resampled[column].mean()}")
    # save the resampled DataFrame to a csv file
    df_resampled.to_csv(file_path[:-4] + "_hourly.csv") # must be manually adjusted for the different time periods





