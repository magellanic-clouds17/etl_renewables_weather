import pandas as pd
import numpy as np

# load df_meta data interim file
path = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather/data/interim/df_meta.csv"
df_meta = pd.read_csv(path, index_col=0)


# use df_meta to find a representative subsample of weather stations in germany

len(stations_id_list) # total number of weather stations = 663

## plot df['geobreite'] as y and df['geolaenge'] as x
df_meta.plot.scatter(x='geolaenge', y='geobreite', c='DarkBlue')

## order df_meta by geolaenge and geobreite
### laenge 
df_meta_laenge = df_meta.sort_values(by=['geolaenge'])

### breite
df_meta_breite = df_meta.sort_values(by=['geobreite'])

## remove every second row from df_meta_laenge_sorted and df_meta_breite_sorted
df_meta_laenge_half = df_meta_laenge.iloc[::2, :]
df_meta_breite_half = df_meta_breite.iloc[::2, :]

### left join df_meta_laenge_half and df_meta_breite_half base on the 'id' column
df_meta_half = pd.merge(df_meta_laenge_half, df_meta_breite_half, on='id', how='left')

#### drop all y columns and rename x columns
#####drop columns
df_meta_half = df_meta_half.drop(['bundesland_x',	'hoehe_y','geobreite_y', 'geolaenge_y', 'stationsname_y',	'bundesland_y'], axis=1)
###### rename columns
df_meta_half = df_meta_half.rename(columns={'stationsname_x': 'stationsname', 'geolaenge_x': 'geolaenge', 'geobreite_x': 'geobreite', 'hoehe_x': 'hoehe'})

## plot df_meta_half['geobreite'] as y and df_meta_half['geolaenge'] as x
df_meta_half.plot.scatter(x='geolaenge', y='geobreite', c='DarkBlue')


"""
Not content with the uneven distribution of weather stations. 
New approach below.
"""

# remove rows from df_meta_laenge and df_meta_breite in a way that the remaining values of the 'geolaenge' and 'geobreite' columns are evenly distributed

df = df_meta

## Define the number of bins to divide data into
num_bins = 200

## Create bins for 'geolaenge' and 'geobreite'
df['geolaenge_bin'] = pd.cut(df['geolaenge'], bins=num_bins, labels=range(num_bins))
df['geobreite_bin'] = pd.cut(df['geobreite'], bins=num_bins, labels=range(num_bins))

## Sample one entry from each bin for 'geolaenge' and 'geobreite'

### For 'geolaenge'
sampled_laenge = df.groupby('geolaenge_bin', group_keys=False).apply(lambda x: x.sample(min(len(x), 1)))

### For 'geobreite'
sampled_breite = df.groupby('geobreite_bin', group_keys=False).apply(lambda x: x.sample(min(len(x), 1)))

## Combining the results
combined_sampled = pd.concat([sampled_laenge, sampled_breite]).drop_duplicates()

## Cleanup: Remove the bin columns
combined_sampled.drop(['geolaenge_bin', 'geobreite_bin'], axis=1, inplace=True)

## The combined_sampled DataFrame now contains rows that are more evenly distributed across 'geolaenge' and 'geobreite'.
combined_sampled.hist(column='geolaenge', bins=50)
combined_sampled.hist(column='geobreite', bins=50)

df_evenly_distributed = combined_sampled 

## plot combined_sampled['geobreite'] as y and combined_sampled['geolaenge'] as x 
df_evenly_distributed.plot.scatter(x='geolaenge', y='geobreite', c='DarkBlue')
len(df_evenly_distributed) # 325
len(df_meta_half) # 332

## save and use df_evenly_distributed as subsample of weather stations in germany
df_evenly_distributed.to_csv(r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\interim\df_sample_stations.csv")
