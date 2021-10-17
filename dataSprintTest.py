import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import datetime.datetime
import json
from functions import *

#tripsFile = 'dataFiles/data-sample_data-nyctaxi-trips-2009-json_corrigido.json'

tripsFile = 'dataFiles/teste.json'
dfDataTrips = pd.read_json(tripsFile)

vendorsFile = 'dataFiles/data-vendor_lookup-csv.csv'
dfDataVendors = pd.read_csv(vendorsFile)

#meanDistance(dfDataTrips)

#bigVendors(dfDataVendors, dfDataTrips)

histogramCash(dfDataTrips)

#tripsFile2012 = 'dataFiles/teste_2012.json'
#tripsFile2012 = 'dataFiles/data-sample_data-nyctaxi-trips-2010-json_corrigido.json'

#dfDataTrips12 = pd.read_json(tripsFile2012)
#timeSeries(dfDataTrips12)
