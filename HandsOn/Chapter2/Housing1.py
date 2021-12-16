import os
import tarfile
from six.moves import urllib
import pandas as pd
import matplotlib.pyplot as plt

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"

#DOWNLOAD_ROOT = "https://github.com/ageron/handson-ml/blob/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path,"housing.tgz")
    #tgz_path = os.path.join(os.getcwd(),housing_path)
    print(housing_url)
    urllib.request.urlretrieve(housing_url, tgz_path)
    print(tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path,"housing.csv")
    return pd.read_csv(csv_path)

fetch_housing_data()
housing = load_housing_data()
print(housing["ocean_proximity"].value_counts())
housing.hist(bins=50,figsize=(20,15))
plt.show()
