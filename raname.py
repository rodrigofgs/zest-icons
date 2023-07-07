# raname.py


import requests

# Set the necessary authentication details
username = "rodrigofgs"
token = "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"

# Set the repository and folder information
repository = "zest-icons"
folder_path = ".icona"
new_folder_name = "icons"

# Construct the API endpoint URL
url = f"https://api.github.com/repos/{username}/{repository}/contents/{folder_path}"

# Prepare the request headers with authentication
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json"
}

# Get the current folder information
response = requests.get(url, headers=headers)
response_data = response.json()

if "message" in response_data:
    print("An error occurred:", response_data["message"])
    exit()

# Extract the necessary data
sha = response_data["sha"]
current_folder_name = response_data["name"]

# Construct the new folder path
new_folder_path = folder_path.rsplit(current_folder_name, 1)[0] + new_folder_name

# Prepare the request payload with the updated folder path
payload = {
    "path": folder_path,
    "message": f"Renamed '{current_folder_name}' to '{new_folder_name}'",
    "content": sha,
    "branch": "master",
    "new_path": new_folder_path
}

# Send the request to update the folder name
response = requests.put(url, headers=headers, json=payload)

if response.status_code == 200:
    print("Folder name changed successfully.")
else:
    print("An error occurred:", response.json()["message"])
