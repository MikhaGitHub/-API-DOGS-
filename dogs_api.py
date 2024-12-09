import requests
import os
import shutil




def download_pictures(name_folder, url_dog):

    if os.path.exists(name_folder):
        shutil.rmtree(name_folder)
    os.makedirs(name_folder)

    for img in range(50):

        params = {"filter": "mp4,webm"}
        response = requests.get(url_dog, params=params)
        response.raise_for_status()
        picture_link = response.json()['url']
        link, picture_extension = os.path.splitext(picture_link)

        filename = f'dog_{img+1}{picture_extension}'
        full_path = os.path.join(name_folder,filename)

        
        response = requests.get(picture_link)
        response.raise_for_status()

        with open(full_path, 'wb') as f:
            f.write(response.content)


def main():
    url_dog = 'https://random.dog/woof.json'
    name_folder = "dogs"
    download_pictures(name_folder, url_dog)


if __name__ == "__main__":
    main()