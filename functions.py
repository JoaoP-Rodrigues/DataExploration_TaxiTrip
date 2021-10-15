import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import datetime.datetime


def meanDistance(dfDataTrips):
    dfPassengers = dfDataTrips.query('passenger_count <= 2')

    dfMeanTotal = np.mean(dfDataTrips['trip_distance']).round(2)
    dfMeanPass = np.mean(dfPassengers['trip_distance']).round(2)

    print(dfMeanTotal)
    print(dfMeanPass)

    x = np.array(["Any Passengers", "2 or less Passengers"])
    y = np.array([dfMeanTotal, dfMeanPass])

    plt.xlabel("Number of Passengers")
    plt.ylabel("Mean of Distance")

    plt.bar(x, y, width=0.5)
    plt.show()


def bigVendors(dfVendors, dfTrips):
    total_vendors = len(dfVendors)
    i = 0
    dict_vendors_amount = {}
    while i < total_vendors:
        vendor = dfVendors["vendor_id"][i]
        dfVendor = dfTrips.query(f'vendor_id == "{vendor}"')
        dfSumVendor = np.sum(dfVendor['total_amount'])

        dict_vendors_amount[vendor] = dfSumVendor
        i += 1

    print(dict_vendors_amount)
    #print(dfTrips.info())
