# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 20:24:49 2017

@author: Manuel Colorado R00156054
"""
import pandas as pd
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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)


#Gaussian NaiveBayes
from sklearn.naive_bayes import GaussianNB
t0 = time()
nb_model = GaussianNB()
nb_model.fit(X_train, y_train.ravel())

nb_predict_train = nb_model.predict(X_train)
nb_predict_test = nb_model.predict(X_test)
print("###### Naive Bayes classification report ######")
t = time()
print("Results obtained in %.2f" %(t-t0), "s.")
print("Accuracy in training set: ", metrics.accuracy_score(y_train, nb_predict_train))
print("Accuracy in test set: ", metrics.accuracy_score(y_test, nb_predict_test))

## KNeighbours Classifier
from sklearn.neighbors import KNeighborsClassifier
t0 = time()
knn_model = KNeighborsClassifier()
knn_model.fit(X_train, y_train.ravel())

knn_predict_train = knn_model.predict(X_train)
knn_predict_test = knn_model.predict(X_test)
print("###### kNearest Neighbors Classifier ######")
t = time()
print("Results obtained in %.2f" %(t-t0), "s.")
print("Accuracy in training set: ", metrics.accuracy_score(y_train, knn_predict_train))
print("Accuracy in test set: ", metrics.accuracy_score(y_test, knn_predict_test))

## decission tree
from sklearn.tree import DecisionTreeClassifier
t0 = time()
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train.ravel())

dt_predict_train = dt_model.predict(X_train)
dt_predict_test = dt_model.predict(X_test)
print("###### Decision Tree Classifier ######")
t = time()
print("Results obtained in %.2f" %(t-t0), "s.")
print("Accuracy in training set: ", metrics.accuracy_score(y_train, dt_predict_train))
print("Accuracy in test set: ", metrics.accuracy_score(y_test, dt_predict_test))

## random forest
from sklearn.ensemble import RandomForestClassifier
t0 = time()
rf_model = RandomForestClassifier(random_state = 42)
rf_model.fit(X_train, y_train.ravel())

rf_predict_train = rf_model.predict(X_train)
rf_predict_test = rf_model.predict(X_test)
print("###### Random Forest Classifier ######")
t = time()
print("Results obtained in %.2f" %(t-t0), "s.")
print("Accuracy in training set: ", metrics.accuracy_score(y_train, rf_predict_train))
print("Accuracy in test set: ", metrics.accuracy_score(y_test, rf_predict_test))

'''
## Linear SVC
from sklearn.svm import SVC
t0 = time()
svc_model = SVC(kernel="linear")
svc_model.fit(X, y)

svc_predict = svc_model.predict(X)
svc_predict_test = svc_model.predict(X_test)
print("###### SVC Vector Machines Classifier ######")
t = time()
print("Results obtained in %.2f" %(t-t0), "s.")
print("Accuracy in whole set: ", metrics.accuracy_score(y, svc_predict))
print("Accuracy in test set: ", metrics.accuracy_score(y_test, svc_predict_test))
'''
## Polynomial SVC
from sklearn.svm import SVC
t0 = time()
svp_model = SVC(kernel="poly")
svp_model.fit(X, y)

svp_predict = svp_model.predict(X)
svp_predict_test = svp_model.predict(X_test)
print("###### SVC Poly Vector Machines Classifier ######")
t = time()
print("Results obtained in %.2f" %(t-t0), "s.")
print("Accuracy in whole set: ", metrics.accuracy_score(y, svp_predict))
print("Accuracy in test set: ", metrics.accuracy_score(y_test, svp_predict_test))