# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:51:47 2017

@author: Manuel Colorado

Open book exam
"""

import pandas as pd

df = pd.read_csv("NetflowCleaned.txt")

def Src_ips_analysis(df):
    #We count the amount of observations in 'src_ips' and extract the top 10
    top10 = df['src_ips'].value_counts().head(10)
    #2.1 Print the results in the console
    print("The top 10 IPs with more activities:", top10)

    #2.2 And plot them using the Series.plot() function
    top10.plot()
    

def Prot_analysis(df):
    #Create different data frame of booleans to filter out protocols
    udp = df['Proto'] == 'UDP'
    tcp = df['Proto'] == 'TCP'
    icmp = df['Proto'] == 'ICMP6'
    #We use them here to filter them out
    filtereddf = df[udp | tcp | icmp]
    #Then group to count them together
    groupedProto = filtereddf.groupby('Proto')
    totalPackets = groupedProto['Flows'].count()
    #3.1 And print the results on the console
    print(totalPackets)
    #3.2 Use the Series.plot() function to plot them in a graph
    totalPackets.plot()
    

def Bytes_analysis(df, iprange):
    #Filter those IPs that contains the specified iprange
    boolfilter = df['dst_ips'].str.contains(iprange)
    #Create new dataframe with just those IPs
    filtereddf = df[boolfilter]
    #Group all entries with the same IP together for aggregation
    groupeddf = filtereddf.groupby('dst_ips')
    #4.1 Calculate the sum of bytes on this aggregation, and print the new table
    totalbytes = groupeddf['Bytes'].sum()
    print("Total amount of bytes transferred from IPs that contains the range " , iprange)
    print(totalbytes)
    
    #4.2 SORT or ORDER methods cannot be used on Series or Dataframes for some reason
    #may be related to older versions of pandas?
    #I used the nlargest method from the Dataframe object, after converting my
    #totalbytes Series into a new Dataframe
    tobesorted = pd.DataFrame(totalbytes)
    print("Top 10 of destination IP addresses by total of bytes")
    print(tobesorted.nlargest(10, 'Bytes'))

    
Src_ips_analysis(df)
Prot_analysis(df)
Bytes_analysis(df, "157.190")

#Note: for some reason while testing each function separatedly the graphs
#were working correctly. Now that I've put them all together the graphs
#stopped working