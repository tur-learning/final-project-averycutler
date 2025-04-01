import requests
import os

# # Example images – replace these URLs with your actual image files or local paths
# # (must be at least 2 images for matching to work meaningfully)
# image_urls = [
#     "./img/pisa.jpg"  # repeat for testing
# ]

# # Convert remote image URLs into files that the client can upload
# filelist = [handle_file(url) for url in image_urls]

# Google Drive file IDs
file_ids = [
    "17QxZpfjLsL5BElf0OYNwBU0hq4wr1MG_",
    "19vAoGLwLDXrr620WHmpkNXiNwZXCVcnt",
    "1LANtLNxl5UzKY1j7gofH-kdugJeEtkLX",
    "1DEQyClx4Be_hQtq1f3xtc2X9Smz8R686",
    "1nIhExOE8asL0-7SSHx87BUij5TPxXfwj"
]

def download_google_drive_file(file_id, dest_folder="./downloads"):
    os.makedirs(dest_folder, exist_ok=True)
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    file_path = os.path.join(dest_folder, f"{file_id}.jpg")
    r = requests.get(url)
    with open(file_path, "wb") as f:
        f.write(r.content)
    return file_path

# Download files
local_paths = [download_google_drive_file(fid) for fid in file_ids]