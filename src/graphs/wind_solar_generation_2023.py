import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# load solar wind 2023 data interim file
path = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\interim\energy\wind_solar_generation_20230101_20231231.csv"
df = pd.read_csv(path, index_col=0)

# plot lineplot of timeseries of wind and solar generation with the datetime index as x-axis and the generation in MW as y-axis
## add month column to df to use as x axis
df['month'] = df.index.month

## plot lineplot of timeseries of wind and solar generation with month as x-axis and the generation in MW as y-axis
df.plot(y=['Wind Onshore (MW)'], figsize=(15, 8), title='Wind Onshore Generation 2023', color='green')
df.plot(y=['Wind Offshore (MW)'], figsize=(15, 8), color='blue', title='Wind Offshore Generation 2023')
df.plot(y=['Solar (MW)'], figsize=(15, 8), color='orange', title='Solar Generation 2023')
