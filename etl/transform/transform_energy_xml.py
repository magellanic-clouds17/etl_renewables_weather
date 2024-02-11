import pprint
import pandas as pd
import xmltodict

# Isolate the wind and solar generation data from the XML file
## Function to parse XML and convert to Python dictionary
def parse_xml_to_dict(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        xml_content = file.read()
        dict_data = xmltodict.parse(xml_content)
        return dict_data
    
## Parse the XML file to a dictionary
file_path = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\raw\energy\solar_wind_generation_20230101_20230131.xml"
data_dict = parse_xml_to_dict(file_path)

## how is the dictionary structured?
data_dict.keys()
data_dict['GL_MarketDocument'].keys()
data_dict['GL_MarketDocument']['TimeSeries'][0].keys()

### pretty print to better understand the structure
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data_dict['GL_MarketDocument']['TimeSeries'][17])

## Extract the wind and solar generation data quantities to lists
wind_on_list_dict= data_dict['GL_MarketDocument']['TimeSeries'][17]['Period']['Point']
wind_on_list = []
for dict in wind_on_list_dict:
    wind_on_list.append(dict['quantity'])

wind_off_list_dict= data_dict['GL_MarketDocument']['TimeSeries'][16]['Period']['Point']
wind_off_list = []
for dict in wind_off_list_dict:
    wind_off_list.append(dict['quantity'])
    
solar_list_dict = data_dict['GL_MarketDocument']['TimeSeries'][13]['Period']['Point']
solar_list = []
for dict in solar_list_dict:
    solar_list.append(dict['quantity'])

pp.pprint(solar_list)


# Create a DataFrame with datetime 15 min index from the lists (start: 2023-01-01 00:00:00, end: 2023-01-31 23:45:00)
## convert the lists to series
wind_on_series = pd.Series(wind_on_list)
wind_off_series = pd.Series(wind_off_list)
solar_series = pd.Series(solar_list)

## create a DataFrame from the series
df = pd.DataFrame({'Wind Onshore (MW)': wind_on_series, 'Wind Offshore (MW)': wind_off_series, 'Solar (MW)': solar_series})

## create a datetime index
start = '2023-01-01 00:00:00'
end = '2023-01-30 23:45:00'
index = pd.date_range(start, end, freq='15min')
len(index)
df.index = index
index.dtype

# look at the first 60 rows
df.head(60)

# save the DataFrame to a csv file
df.to_csv(r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\interim\energy\wind_solar_generation_20230101_20230130.csv")