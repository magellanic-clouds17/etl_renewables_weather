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

## Define the number of bins 
num_bins = 110

## Create bins for 'geolaenge' and 'geobreite'
df['geolaenge_bin'] = pd.cut(df['geolaenge'], bins=num_bins, labels=range(num_bins))
df['geobreite_bin'] = pd.cut(df['geobreite'], bins=num_bins, labels=range(num_bins))

## Define a function to select a row with the median value in each bin
def select_median_row(group):
    if group.empty:
        return None 
    # Proceed with the logic for non-empty groups
    median_geolaenge = group['geolaenge'].median()
    median_geobreite = group['geobreite'].median()
    diff_laenge = (group['geolaenge'] - median_geolaenge).abs()
    diff_breite = (group['geobreite'] - median_geobreite).abs()
    idx_min_diff_laenge = diff_laenge.idxmin() if not diff_laenge.empty else None
    idx_min_diff_breite = diff_breite.idxmin() if not diff_breite.empty else None
    # Handling cases where idx_min_diff_* could be None
    valid_idxs = [idx for idx in [idx_min_diff_laenge, idx_min_diff_breite] if idx is not None]
    return group.loc[valid_idxs] if valid_idxs else None

# Apply the function safely to each bin group
# Using 'group_keys=False' to avoid adding an extra index layer
median_sampled = df.groupby('geolaenge_bin', group_keys=False).apply(select_median_row).dropna(how='all')

# Since the selection is based on median, there's no need to separate by 'geolaenge' and 'geobreite' unless you want to prioritize one

# Cleanup: Remove the bin columns if they are no longer needed
median_sampled.drop(['geolaenge_bin', 'geobreite_bin'], axis=1, inplace=True, errors='ignore')

# median_sampled now contains your consistently distributed samples

# Apply the function to each bin group for both 'geolaenge' and 'geobreite'
median_sampled_laenge = df.groupby('geolaenge_bin').apply(select_median_row).reset_index(drop=True)
median_sampled_breite = df.groupby('geobreite_bin').apply(select_median_row).reset_index(drop=True)

# Combine the results by taking the unique entries to ensure no duplication
combined_median_sampled = pd.concat([median_sampled_laenge, median_sampled_breite]).drop_duplicates()

# Cleanup: Remove the bin columns
combined_median_sampled.drop(['geolaenge_bin', 'geobreite_bin'], axis=1, inplace=True)

# The combined_median_sampled DataFrame now contains rows that are more evenly distributed

len(combined_median_sampled)
combined_median_sampled.plot.scatter(x='geolaenge', y='geobreite', c='DarkBlue')

df_station_sample_evenly_distributed = combined_median_sampled

## save and use df_evenly_distributed as subsample of weather stations in germany
df_station_sample_evenly_distributed.to_csv(r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\interim\df_sample_stations.csv")



# Assuming df is your DataFrame
'
# Define the number of bins you want to divide your data into
num_bins = 170

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
