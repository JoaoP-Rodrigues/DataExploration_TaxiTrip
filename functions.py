import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose


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

    plt.barh(x, y, width=0.5)
    plt.show()


def bigVendors(dfVendors, dfTrips):
    total_vendors = len(dfVendors)
    i = 0
    df_big_vendors = pd.DataFrame()
    df_big_vendors['Alias'] = dfVendors['vendor_id']
    df_big_vendors['Name'] = dfVendors['name']
    list_ammount = []
    while i < total_vendors:
        vendor = dfVendors["vendor_id"][i]
        dfVendor = dfTrips.query(f'vendor_id == "{vendor}"')
        dfSumVendor = np.sum(dfVendor['total_amount']).round(2)
        list_ammount.append(dfSumVendor)
        i += 1

    df_big_vendors['Ammount'] = list_ammount
    df_big_vendors = df_big_vendors.nlargest(3, 'Ammount')
    x = np.array(df_big_vendors['Name'])
    y = np.array(df_big_vendors['Ammount'])

    plt.ylabel("Valores recebidos")
    plt.xlabel("Empresas de Taxi")

    plt.bar(x, y, width=0.5)
    plt.show()


def histogramCash(dfDataTrips):

    #months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul',
    #          8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

    dfCashTrips = dfDataTrips.query('payment_type == "CASH" | payment_type == "Cash"')

    df_count_cash_trips = pd.DataFrame()
    #df_count_cash_trips['Months'] = months.values()
    list_count_trips = []
    date_m = 1
    while date_m <= 12:
        if date_m < 10:
            date_search = '2009-0'+str(date_m)
        else:
            date_search = '2009-'+str(date_m)

        count_trips = dfCashTrips.query(f'pickup_datetime.str.contains("{date_search}")')
        count_trips = np.count_nonzero(count_trips['payment_type'])
        list_count_trips.append(count_trips)
        date_m += 1

    df_count_cash_trips['Total_trips'] = list_count_trips

    y = np.array(df_count_cash_trips['Total_trips'])

    plt.ylabel("Quantidade de Meses")
    plt.xlabel("Total Recebido em Dinheiro")
    plt.title('Histograma de Faturamento Mensal')
    plt.hist(y, 20, facecolor='g', alpha=0.75)
    plt.xticks(rotation=45)
    plt.show()


def timeSeries(dfDataTrips2012):
    dfDataTrips2012['pickup_datetime'] = pd.to_datetime(dfDataTrips2012['pickup_datetime'])

    df_tips = dfDataTrips2012.query("pickup_datetime.dt.month > 6 & pickup_datetime.dt.month < 10 & tip_amount > 0")

    month = 7
    dict_diary_tips = {}
    list_days = []
    list_tips = []
    while month <= 9:
        day = 1

        while day <= 31:
            list_days.append((str(month)+"-"+str(day)))
            if month == 9 and day == 31:
                list_tips.append(0)
            else:
                diary_tips = df_tips.query(f"pickup_datetime.dt.month == {month} & pickup_datetime.dt.day == {day}")

                #print(len(diary_tips.index))
                #print(day)
                list_tips.append(len(diary_tips.index))

            day += 1
        dict_diary_tips["Dias"] = list_days
        dict_diary_tips["Gorgetas"] = list_tips
        month += 1

    df_diary_tips = pd.DataFrame(dict_diary_tips)

    df_diary_tips = df_diary_tips.set_index('Dias')
    df_diary_tips.plot()
    plt.tight_layout()

    #resultado = seasonal_decompose(df_diary_tips["Gorgetas"], period=30, extrapolate_trend='freq')

    #tendencia = resultado.trend
    plt.xlabel('Dias')
    plt.xticks(rotation=45)
    plt.ylabel('Quantidade de Gorgetas')
    #plt.plot(tendencia)
    plt.show()

