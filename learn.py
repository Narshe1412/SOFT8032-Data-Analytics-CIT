# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 20:24:49 2017

@author: Manuel Colorado R00156054
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics

df = pd.read_csv('terrordataset_cleaned.csv', encoding = "ISO-8859-1")

target = df['gname']
data = df.drop(['Unnamed: 0', 'gname'], axis=1)
datanostrings = data.drop(['weapdetail', 'provstate', 'city', 'summary', 'corp1', 'target1'], axis=1)

from sklearn.preprocessing import Imputer
fillnan = Imputer(missing_values = "NaN",strategy = "mean", axis=0)

#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
X = datanostrings.values
y = target.values
test_size = 0.3

X= fillnan.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

'''
#Gaussian NaiveBayes
from sklearn.naive_bayes import GaussianNB
nb_model = GaussianNB()
nb_model.fit(X_train, y_train.ravel())

nb_predict_train = nb_model.predict(X_train)
print(metrics.accuracy_score(y_train, nb_predict_train))
'''

## random forest
from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier(random_state = 42)
rf_model.fit(X_train, y_train.ravel())

rf_predict_train = rf_model.predict(X_train)
print(metrics.accuracy_score(y_train, rf_predict_train))
