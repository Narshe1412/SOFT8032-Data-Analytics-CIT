# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 20:24:49 2017

@author: Manuel Colorado R00156054
"""
import pandas as pd
import numpy as np
from time import time
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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)


##fold validation
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
t0 = time()
dt = DecisionTreeClassifier()
dt_fit = dt.fit(X_train, y_train)

print("###### Decision Tree Classifier CV ######")
dt_scores = cross_val_score(dt_fit, X_train, y_train, cv = 5)
print("mean cross validation score: {}".format(np.mean(dt_scores)))
print("score without cv: {}".format(dt_fit.score(X_train, y_train)))
print("score on test set", dt_fit.score(X_test, y_test))
t = time()
print("Results obtained in %.2f" %(t-t0), "s.")

##fold validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
t0 = time()
rf = RandomForestClassifier()
rf_fit = rf.fit(X_train, y_train)

print("###### Random Forest Classifier CV ######")
rf_scores = cross_val_score(rf_fit, X_train, y_train, cv = 5)
print("mean cross validation score: {}".format(np.mean(rf_scores)))
print("score without cv: {}".format(rf_fit.score(X_train, y_train)))
print("score on test set", rf_fit.score(X_test, y_test))
t = time()
print("Results obtained in %.2f" %(t-t0), "s.")

import numpy as np
import matplotlib.pyplot as plt

# Build a forest and compute the feature importances
forest = RandomForestClassifier()

forest.fit(X, y)
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in range(X.shape[1]):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

# Plot the feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(range(X.shape[1]), importances[indices],
       color="r", yerr=std[indices], align="center")
plt.xticks(range(X.shape[1]), indices)
plt.xlim([-1, X.shape[1]])
plt.show()