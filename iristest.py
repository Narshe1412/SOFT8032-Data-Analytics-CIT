# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:30:43 2017

@author: akai_
"""

from sklearn import cross_validation
from sklearn import datasets
from sklearn import tree
iris = datasets.load_iris()
print (iris.data.shape, iris.target.shape)
clf = tree.DecisionTreeClassifier()
scores = cross_validation.cross_val_score(clf, iris.data, iris.target, cv=10)
print (scores)
print (scores.mean(), scores.std())