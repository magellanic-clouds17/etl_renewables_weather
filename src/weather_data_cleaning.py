import pandas as pd

# load df_meta data interim file
path = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather/data/interim/df_meta.csv"
df_meta = pd.read_csv(path, index_col=0)