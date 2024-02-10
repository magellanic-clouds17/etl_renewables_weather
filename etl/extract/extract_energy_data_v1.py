import requests
from urllib.parse import urlencode
import xml.etree.ElementTree as ET


def fetch_energy_data(api_key, start_period, end_period, domain="10Y1001A1001A83F"):
    base_url = "https://web-api.tp.entsoe.eu/api?"
    
    # Parameters for the API request (https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html#_complete_parameter_list)
    params = {
        "securityToken": api_key,
        "documentType": "A75",  # wind and solar generation A74, generation per type A75
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
        file_path = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\raw\energy\generation_per_type_20230101_20230131.xml"
        
        # Open the file in write-binary mode and write the response content
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print("File saved successfully.")
    else:
        print(f"Failed to fetch data: {response.status_code}")


# Example usage
api_key = "API_KEY" # real API key not published on GitHub
start_period = "202301010000"  # Start of January 2023
end_period = "202301310000"  # End of January 2023

fetch_energy_data(api_key, start_period, end_period)

# convert the xml file to csv

def xml_to_csv(xml_file_path, csv_file_path):
    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Define a list to hold your extracted data
    data = []

    # Specify the XML namespace
    namespace = {'ns': 'urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0'}

    # Iterate through each TimeSeries element in the XML
    for timeseries in root.findall('.//ns:TimeSeries', namespace):
        # For each TimeSeries, iterate through each Point
        for point in timeseries.findall('.//ns:Point', namespace):
            # Extract the data you're interested in
            position = point.find('ns:position', namespace).text
            quantity = point.find('ns:quantity', namespace).text
            
            # Append the data to list as a dictionary
            data.append({'position': position, 'quantity': quantity})

    # Convert the list of dictionaries into a pandas DataFrame
    df = pd.DataFrame(data)

    # Write the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)

    print(f"CSV file has been created at {csv_file_path}")

# Define file paths
xml_file_path = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\raw\energy\solar_wind_generation_20230101_20230131.xml"
csv_file_path = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\raw\energy\solar_wind_generation_20230101_20230131.csv"

# Apply the function to convert the XML to CSV
xml_to_csv(xml_file_path, csv_file_path)
