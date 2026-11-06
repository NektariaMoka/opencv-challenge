import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import Image

def download_and_unzip(url, save_path):
    print("Downloading and extracting assets...", end="")

    urlretrieve(url, save_path)

    try:
        with ZipFile(save_path) as archive:
            archive.extractall(os.path.dirname(save_path))
        print("Done")
    except Exception as error:
        print(f"\nInvalid file: {error}")


URL = "https://www.dropbox.com/s/qhhlqcica1nvtaw/opencv_bootcamp_assets_NB1.zip?dl=1"
asset_zip_path = os.path.join(os.getcwd(), "opencv_bootcamp_assets_NB1.zip")

if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)