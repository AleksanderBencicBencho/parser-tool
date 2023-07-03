import os

import requests


def download(url: str, folder_path: str) -> None:
    """Download file from url and save it locally in file_name"""
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, url.split("/")[-1])
    with open(folder_path, "wb") as file:
        response = requests.get(url)
        file.write(response.content)
        print(f"Downloader {url} to {file_path}.")


def main():
    url = "https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/blood_pressure.csv"
    file_path = "data/blood_pressure2.csv"
    download(url, file_path)


main()
