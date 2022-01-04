import os

import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": 'test/' + os.path.basename(file_path), "overwrite": "true"}
        response = requests.get(url, headers=self.get_headers(), params=params)
        href = response.json().get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    file_path = "/Users/dmitro/Documents/netology/text.txt"
    token = "AQAAAABbyXwMAADLW-f6Hy5R802fuHez8MR67NM"
    uploader = YaUploader(token)
    uploader.upload(file_path)