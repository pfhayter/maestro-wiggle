import requests
import base64

# Set the cnMaestro API endpoint
token_url = "https://cnmaestro.arc.vincent.solutions/api/v1/access/token"
devices_url = "https://cnmaestro.arc.vincent.solutions/api/v1/data/devices"

# Set the Client ID and Client Password
client_id = "paulhayter"
client_password = "39nyn5WyDPU2Rv"

# Encode the Client ID and Client Password
credentials = base64.b64encode(f"{client_id}:{client_password}".encode("utf-8")).decode("utf-8")

# Set the headers for the access token request
token_headers = {
    "Authorization": f"Basic {credentials}",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}

# Set the body for the access token request
token_body = {"grant_type": "client_credentials"}

# Send the access token request and get the response
token_response = requests.post(token_url, headers=token_headers, data=token_body)

# Check if the access token request was successful
if token_response.status_code == 200:
    # Extract the access token from the response
    access_token = token_response.json()["access_token"]
    
    # Set the headers for the devices request
    devices_headers = {"Authorization": f"Bearer {access_token}"}
    
    # Send the devices request and get the response
    devices_response = requests.get(devices_url, headers=devices_headers)
    
    # Check if the devices request was successful
    if devices_response.status_code == 200:
        # Extract the devices from the response
        devices = devices_response.json()

        # Print the list of devices
        for device in devices:
            print(device["name"])
    else:
        print(f"Devices request failed with error code {devices_response.status_code}")
else:
    print(f"Access token request failed with error code {token_response.status_code}")
