#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:52:26 2019

@author: antoineohleyer
"""

from sklearn.decomposition import PCA
import numpy as np

X = np.array([[-1, -1], [0, 0], [1, 1]])
mean_X = np.mean(X)

pca = PCA(n_components=2)
pca.fit(X)

print(pca.get_params)


