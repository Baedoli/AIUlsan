import pandas as pd
import numpy as np
import os
import googlemaps


path = os.getcwd()
path = path+'/bigdata/data/'

crime_analysis_police = pd.read_csv(path+'02. crime_in_Seoul2.csv')
crime_analysis_police.head()

gmaps_key = 'AIzaSyAH4lBEZbvwvC5d7ecKroaJLisu7Ub4yxA'
gmaps = googlemaps.Client(key=gmaps_key)

gmaps.geocode('서울중부경찰서',language='ko')