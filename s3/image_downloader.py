import urllib.request
import os

def image_downloader(url):
    name="1.jpg"
    urllib.request.urlretrieve(str(url),os.path.join("image/",name))


