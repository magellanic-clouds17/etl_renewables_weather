import pandas as pd

"""
Goal of this script: Transform all txt weather files to csv files and combine them into one csv file based on date time index
"""


# Load the txt files to a DataFrame
file_path = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\raw\weather\air_temperature\historical\stundenwerte_TU_00102_20020101_20221231_hist\produkt_tu_stunde_20020101_20221231_00102.txt"
df = pd.read_csv(file_path, delimiter=";")

# drop columns ['QN_9', 'RF_TU' and 'eor']
df = df.drop(['QN_9', 'RF_TU', 'eor'], axis=1)

# convert MESS_DATUM column to datetime and set as index. MESS_Datum format is YYYYMMDDHH
df['MESS_DATUM'] = pd.to_datetime(df['MESS_DATUM'], format='%Y%m%d%H')
df = df.set_index('MESS_DATUM')

# drop rows outside the time period 2015-2019
df = df['2015-01-01':'2019-12-31']