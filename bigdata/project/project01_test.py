
import pandas as pd
import numpy as np
import os

path = os.getcwd()

CCTV_Seoul = pd.read_csv(path+'/bigdata/data/01.CCTV_in_Seoul.csv')
CCTV_Seoul.head()
CCTV_Seoul.describe()
