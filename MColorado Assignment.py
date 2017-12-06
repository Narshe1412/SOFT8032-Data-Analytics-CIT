# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:09:11 2017

@author: Manuel Colorado

Open book exam
"""

import pandas as pd

df = pd.read_csv("netflow_sorted.txt")

#Create a copy of the data frame to work without destroying the original
cleandf = df.copy()

#Verify if there are null data. and clean it
#to verify-> print(pd.isnull(cleandf).any())
cleandf = cleandf.dropna()

#Extract the desired columns from the data set
cleandf = cleandf[["Proto", "Flows", "Bytes", "src_ips", "dst_ips"]]

#We clean leading spaces in Proto property
cleandf["Proto"] = cleandf["Proto"].str.strip()

#1. Save the elements into a new file
cleandf.to_csv('NetflowCleaned.txt')
print("CSV created -> NetflowCleaned.txt")
