"""
Created on Wed Oct 25 20:35:12 2017

@author: akai_
"""

import numpy as np
import pandas as pd

df = pd.read_csv("attacks.csv", encoding = "ISO-8859-1")

"""1"""
print(df['Location'].value_counts().head(1))


"""2"""
print(df['Country'].value_counts().head(6))


"""3"""
dffatal = df['Country'][df['Fatal'] == 'Y']
print(dffatal.value_counts().head(6))

"""4"""
scuba = df['Activity']=='Scuba diving'
surfing = df['Activity'] == 'Surfing'
print("Accidents while scuba diving ", len(df[scuba]))
print("Accidents while surfing", len(df[surfing]))

"""5"""

totalFatal = len(df[df['Fatal']=='Y'])
totalNonFatal = len(df[df['Fatal'] =='N'])
print("Percentage of fatal attacks", totalFatal / (totalFatal + totalNonFatal) * 100)

"""6"""
def calculateFatal(country):
    boolCountry = df["Country"]==country
    isFatal = df['Fatal']=='Y'
    nonFatal = df['Fatal']== 'N'
    countryFatal = df[boolCountry & isFatal]
    countryNonFatal = df[boolCountry & nonFatal]
    if (len(countryFatal) != 0 and len(countryNonFatal) != 0):
        print("Attacks on " +  country + ":", len(countryFatal) / (len(countryFatal) + len(countryNonFatal)) * 100)
    
countryList = pd.unique(df['Country'])
for country in countryList:
    calculateFatal(country)
    
"""7"""
def calculateYearlyAttacks(country, df):
    yearlist = pd.unique(df['Year'])
    for year in yearlist:
        yearattacks = df['Year'] == year
        countryattacks= df['Country']==country
        print("Total attacks for year ", year, " : " , len(df[yearattacks & countryattacks]) )
    
calculateYearlyAttacks("AUSTRALIA", df)