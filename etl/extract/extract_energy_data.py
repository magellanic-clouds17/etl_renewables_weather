import requests
from urllib.parse import urlencode

def fetch_energy_data(api_key, start_period, end_period, domain="10Y1001A1001A83F"):
    base_url = "https://web-api.tp.entsoe.eu/api?"
    
    # Parameters for the API request
    params = {
        "securityToken": api_key,
        "documentType": "A65",  # Example: Actual Generation per Generation Unit
        "processType": "A16",  # Realised data
        "in_Domain": domain,  # EIC Code for Germany (example value, replace with actual)
        "out_Domain": domain,  # EIC Code for Germany (example value, replace with actual)
        "periodStart": start_period,
        "periodEnd": end_period,
    }
    
    # Constructing the full URL with encoded parameters
    full_url = base_url + urlencode(params)
    
    # Make the HTTP GET request
    response = requests.get(full_url)
    
    if response.status_code == 200:
        # Handle the response content (XML) depending on your needs
        print(response.text)
    else:
        print(f"Failed to fetch data: {response.status_code}")

# Example usage
api_key = "YOUR_API_TOKEN"
start_period = "201001010000"  # Start of 2010
end_period = "202012312359"  # End of 2020

fetch_energy_data(api_key, start_period, end_period)
