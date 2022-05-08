# -*- coding: utf-8 -*-
"""
Created on Fri May  6 22:40:34 2022

@author: chinn
"""

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from firebase import firebase

dataset = pd.read_csv('\HackDefine\Crop_recommendation.csv')
data = dataset.values
X = data[:, :-1].astype(str)
y = data[:, -1].astype(str)
ordinal_encoder = preprocessing.OrdinalEncoder()
X = ordinal_encoder.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=10)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
from sklearn.ensemble import ExtraTreesClassifier
clf = ExtraTreesClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(accuracy*100)

l=[]

firebase =firebase.FirebaseApplication('https://farmai-b8827-default-rtdb.firebaseio.com/')
l.append(firebase.get('N',None))
l.append(firebase.get('P',None))
l.append(firebase.get('K',None))
l.append(firebase.get('temperature',None))
l.append(firebase.get('humidity',None))
l.append(firebase.get('pH',None))
l.append(firebase.get('rain',None))

predictcrop=[l]
crop = clf.predict(predictcrop)
firebase.put('https://farmai-b8827-default-rtdb.firebaseio.com/','result',crop[0])
print(crop)
print(l)