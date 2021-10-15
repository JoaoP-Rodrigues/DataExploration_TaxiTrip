import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import datetime.datetime
import json
from functions import *

#file = 'dataFiles/data-sample_data-nyctaxi-trips-2010-json_corrigido.json'

tripsFile = 'dataFiles/teste.json'
dfDataTrips = pd.read_json(tripsFile)

vendorsFile = 'dataFiles/data-vendor_lookup-csv.csv'
dfDataVendors = pd.read_csv(vendorsFile)

#meanDistance(dfDataTrips)

bigVendors(dfDataVendors, dfDataTrips)
