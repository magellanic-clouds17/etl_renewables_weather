import requests
import zipfile
import os
import pandas as pd
from bs4 import BeautifulSoup

def download_and_extract_weather_data(filtered_urls, save_path_root, extract_to_root):
    for file_url in filtered_urls:
        # Extract file name from URL
        file_name = file_url.split("/")[-1]
        
        # Generate save path and extract path
        save_path = os.path.join(save_path_root, file_name)
        extract_to = os.path.join(extract_to_root, file_name.replace(".zip", ""))
        
        # Check if save path already exists
        if os.path.exists(save_path):
            print(f"{file_name} already exists. Skipping...")
            continue
        
        # Ensure the directories exist
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        os.makedirs(extract_to, exist_ok=True)
        
        # Attempt to download the file
        print(f"Downloading {file_url}...")
        response = requests.get(file_url)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"Successfully downloaded {file_name}. Extracting...")
            
            # Extract the ZIP file
            with zipfile.ZipFile(save_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
            print(f"Successfully extracted {file_name}.")
        else:
            print(f"Failed to download {file_name}. Status code: {response.status_code}")

def list_files(directory_url):
    # Send a request to the url

    response = requests.get(directory_url)
    response.raise_for_status()  # Ensure we got a successful response

    # Parse the response content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all <a> tags, assuming files are linked using <a href="..."> tags
    links = soup.find_all('a')
    
    # Extract the href attribute from each link
    file_urls = [link.get('href') for link in links if link.get('href')]

    return file_urls

def filter_files_for_multiple_ids(file_urls, formatted_ids):
    # Initialize an empty list to hold the filtered URLs for all IDs
    filtered_urls = []
    
    # Iterate through each station ID in the list
    for station_id in formatted_ids:
        # Define the start pattern for the current station ID
        start_pattern = f"stundenwerte_FF_{station_id}_" # must still be manually adjusted for the different weather parameters (Air Temperature (TU), Sun (SD), Wind (FF))
        end_pattern = "_hist.zip"

        # Filter URLs for the current station ID and add them to the list
        filtered_urls.extend(
            [url for url in file_urls if url.startswith(start_pattern) and url.endswith(end_pattern)]
        )

    return filtered_urls

def retrieve_sample_station_ids(df_sample_path):
    ## Load the sample stations DataFrame
    df_sample = pd.read_csv(df_sample_path, index_col=0)
        
    ## Extract station IDs from the DataFrame
    station_ids = df_sample.index.astype(str).tolist()
        
    ## Format station IDs to match the filename pattern
    formatted_ids = [id.zfill(5) for id in station_ids]

    return formatted_ids

# Example usage
save_path_root = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\raw\weather\wind\historical" # must be manually adjusted for the different weather parameters)
extract_to_root = save_path_root
directory_url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/wind/historical/" # must be manually adjusted for the different weather parameters)
df_sample_path = r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\interim\weather\df_sample_stations.csv"
formatted_ids = retrieve_sample_station_ids(df_sample_path)
all_files = list_files(directory_url)
filtered_files = filter_files_for_multiple_ids(all_files, formatted_ids)
filtered_urls =[f"{directory_url}{file}" for file in filtered_files]


download_and_extract_weather_data(filtered_urls, save_path_root, extract_to_root)

print(filtered_files)
len(filtered_files)
