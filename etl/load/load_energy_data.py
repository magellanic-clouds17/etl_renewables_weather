import xmltodict
from pymongo import MongoClient
import pandas as pd

# convert xml to dict to load into mongodb

file_path = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\raw\energy\solar_wind_generation_20230101_20230131.xml"

## Function to parse XML and convert to Python dictionary
def parse_xml_to_dict(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        xml_content = file.read()
        dict_data = xmltodict.parse(xml_content)
        return dict_data
    
## Parse the XML file to a dictionary
data_dict = parse_xml_to_dict(file_path)

## Connect to MongoDB 
client = MongoClient('mongodb://localhost:27017/')
db = client['etl_renewables_weather']
collection = db['wind_solar_data']

## Insert the parsed data into MongoDB
insert_to_mongodb(collection, data_dict)
collection.insert_one(data_dict)

