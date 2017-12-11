# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 20:24:20 2017

@author: Manuel Colorado R00156054
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('globalterrorismdb_0617dist.csv', encoding = "ISO-8859-1")
totalrows = len(df)
df = df.dropna(how = 'all')

'''
stats = []
for i in range(0, 105, 5):
    dropped = df.dropna(axis=1, thresh = (totalrows * (i/100)) )
    print ("Threshold: " + str(i/100) + " columns: " + str(len(dropped.columns)))

    stats.append({'Threshold': i, 'columns remaining': len(dropped.columns)})
dfstats = pd.DataFrame(stats)
dfstats.set_index(dfstats['Threshold']).plot()
plt.title("Amount of columns remaining")
plt.show()


Threshold: 0.0 columns: 135
Threshold: 0.05 columns: 90
Threshold: 0.1 columns: 71
Threshold: 0.15 columns: 69
Threshold: 0.2 columns: 67
Threshold: 0.25 columns: 65
Threshold: 0.3 columns: 63
Threshold: 0.35 columns: 62
Threshold: 0.4 columns: 60
Threshold: 0.45 columns: 58
Threshold: 0.5 columns: 58
Threshold: 0.55 columns: 58
Threshold: 0.6 columns: 55
Threshold: 0.65 columns: 49
Threshold: 0.7 columns: 48
Threshold: 0.75 columns: 48
Threshold: 0.8 columns: 47
Threshold: 0.85 columns: 47
Threshold: 0.9 columns: 45
Threshold: 0.95 columns: 40
Threshold: 1.0 columns: 31 '''

dropped = df.dropna(axis=1, thresh = (totalrows * 0.58))
cormatrix = dropped.corr()
sns.heatmap(cormatrix)
plt.show()

print ("Preliminary analysis")
print ("########################")
print ("1# Top ten types of attacks worldwide and count of those attacks")
print ("")
top10attacks = dropped['attacktype1_txt'].value_counts().head(10)
print (top10attacks)
print ("")
print ("########################")
print ("#2 Top ten regions where attacks occurred and number of people injured or killed")
print ("")
dropped['woundpluskill'] = dropped['nkill'] + dropped['nwound']
groupeddf = dropped.groupby('region_txt')
top10regions = groupeddf['woundpluskill'].sum().sort_values(ascending = False)
print(top10regions)
print ("")
print ("########################")
print ("#3 Interesting report on the target of attacks")
europe = dropped['region_txt'] == 'Western Europe'
terrorists = dropped[europe].groupby('gname').count().sort_values(ascending = False, by='woundpluskill')
terroristsTop10 = terrorists[1:11]
print(terroristsTop10)
       
cleared = dropped.drop(['eventid', 'imonth', 'iday',
                        'latitude', 'longitude',
                        'country_txt', 'region_txt', 'attacktype1_txt', 'targtype1_txt', 'targsubtype1_txt', 'natlty1_txt', 'weaptype1_txt', 'weapsubtype1_txt',
                        'targsubtype1',
                        #'weapsubtype1', may be relevant
                        'nwound', 'nwoundus',
                        'INT_LOG', 'INT_IDEO', 'INT_MISC', 'INT_ANY',
                        'scite1', 'dbsource'], axis=1)

cormatrix = cleared.corr()
sns.heatmap(cormatrix)
plt.show()
print(cleared.columns)

cleared.to_csv('terrordataset_cleaned.csv')
print("CSV created -> terrordataset_cleaned.csv")