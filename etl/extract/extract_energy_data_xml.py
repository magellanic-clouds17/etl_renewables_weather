import requests
from urllib.parse import urlencode
import xmltodict
from pymongo import MongoClient
import bson


def fetch_energy_data(api_key, start_period, end_period, domain="10Y1001A1001A83F"):
    base_url = "https://web-api.tp.entsoe.eu/api?"
    
    # Parameters for the API request (https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html#_complete_parameter_list)
    params = {
        "securityToken": api_key,
        "documentType": "A74",  # wind and solar generation A74, generation per type A75, Aggregated energy data report A11 (not working for realised data)
        "processType": "A16",  # Realised data
        "in_Domain": domain,  # EIC Code for Germany 
        "out_Domain": domain,  # EIC Code for Germany 
        "periodStart": start_period,
        "periodEnd": end_period,
    }
    
    # Constructing the full URL with encoded parameters
    full_url = base_url + urlencode(params)
    
    # Make the HTTP GET request
    response = requests.get(full_url)
    
    if response.status_code == 200:
        # Specify the file path to save the XML data
        file_path = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\raw\energy\solar_wind_generation_20230101_20230131.xml"
        
        # Open the file in write-binary mode and write the response content
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print("File saved successfully.")
    else:
        print(f"Failed to fetch data: {response.status_code}")


# Example usage
api_key = "api-key" # real API key not published on GitHub
start_period = "202201010000"  # Start of January 2023
end_period = "202301010000"  # End of January 2023

fetch_energy_data(api_key, start_period, end_period)
