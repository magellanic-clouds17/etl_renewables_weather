import pandas as pd
import numpy as np

# load df_meta data interim file
path = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather/data/interim/df_meta.csv"
df_meta = pd.read_csv(path, index_col=0)


# use df_meta to find a representative subsample of weather stations in germany

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

# Remove rows from df_meta_laenge and df_meta_breite in a way that the remaining values of the 'geolaenge' and 'geobreite' columns are evenly distributed

df = df_meta

# Define the number of bins you want to divide your data into
num_bins = 70

# Create bins for 'geolaenge' and 'geobreite'
df['geolaenge_bin'] = pd.cut(df['geolaenge'], bins=num_bins, labels=False)
df['geobreite_bin'] = pd.cut(df['geobreite'], bins=num_bins, labels=False)

# Initialize a column to mark rows for retention
df['retain'] = False

# Define a function to safely compute the closest index to the median within a bin
def mark_closest_to_median(group, column):
    if not group.empty:
        median_value = group[column].median()
        diff = (group[column] - median_value).abs()
        # Safely get the index with the minimum difference
        idx_min_diff = diff.idxmin()
        df.at[idx_min_diff, 'retain'] = True

# Iterate over bins and mark the closest row to the median for retention
for bin_label in range(num_bins):
    # geolaenge
    bin_group_laenge = df[df['geolaenge_bin'] == bin_label]
    mark_closest_to_median(bin_group_laenge, 'geolaenge')
    
    # geobreite
    bin_group_breite = df[df['geobreite_bin'] == bin_label]
    mark_closest_to_median(bin_group_breite, 'geobreite')

# Filter the DataFrame to keep only marked rows, preserving the original index
filtered_df = df[df['retain']].drop(['geolaenge_bin', 'geobreite_bin', 'retain'], axis=1)

# filtered_df now contains the filtered rows with the original indices preserved

# plot filtered_df['geobreite'] as y and filtered_df['geolaenge'] as x
len(filtered_df)
filtered_df.plot.scatter(x='geolaenge', y='geobreite', c='DarkBlue')

df_station_sample_evenly_distributed = filtered_df

## save and use df_evenly_distributed as subsample of weather stations in germany
df_station_sample_evenly_distributed.to_csv(r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\interim\df_sample_stations.csv")
