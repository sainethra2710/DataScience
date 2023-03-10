#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 14:39:19 2023

@author: nethrachekuri
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 14:57:00 2022

@author: nethrachekuri
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv(r"C:\Users\neth\Desktop\LR.csv")

x = dataset.iloc[:,[2,3]].values
y = dataset.iloc[:-1].values
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=3,weights='uniform',algorithm='auto',p=2 )
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)

bias=classifier.score(x_train,y_train)
bias
variance= classifier.score(x_test,y_test)
variance

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

cm = confusion_matrix(y_test,y_pred)
cr = classification_report(y_test, y_pred)

from sklearn.metrics import accuracy_score
c = accuracy_score(y_test, y_pred)