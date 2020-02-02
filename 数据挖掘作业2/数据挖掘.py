#转成csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

txt = np.loadtxt('data_study.txt')
txtDF = pd.DataFrame(txt)
txtDF.to_csv('data_study.csv',index=False)
txt2 = np.loadtxt('data_check.txt')
txtDF2 = pd.DataFrame(txt2)
txtDF2.to_csv('data_check.csv',index=False)

#取出属性和标签
dataset = pd.read_csv('data_study.csv')
X_stard = dataset.iloc[:,0:9].values
Y_stard = dataset.iloc[:, 9].values

dataset2 = pd.read_csv('data_check.csv')
X_pred = dataset2.iloc[:,0:9].values
Y_pred = dataset2.iloc[:, 9].values

#主成分分析
pca1 = PCA(n_components=9)
pca1.fit(X_stard)
#返回所保留的n个成分各自的方差百分比
print(pca1.explained_variance_ratio_)
print(pca1.explained_variance_)

#PCA降维
from sklearn.decomposition import PCA
#print(X_stard.shape)
pca = PCA(n_components=2)
X_stard=pca.fit_transform(X_stard)
X_pred=pca.fit_transform(X_pred)

#标准化
from sklearn import preprocessing
X_stard = preprocessing.scale(X_stard)
X_pred = preprocessing.scale(X_pred)

### GridSearchCV寻找超参数
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

clf = KNeighborsClassifier()
n_neighbors = list(range(1,10))
weights = ['uniform','distance']
algorithm_options = ['auto','ball_tree','kd_tree','brute']
leaf_range = list(range(1,10))
p = list(range(1,10))
param_grid = [{'n_neighbors': n_neighbors, 'weights': weights, 'algorithm': algorithm_options, 'leaf_size': leaf_range, 'p':p}]
grid_search = GridSearchCV(clf, param_grid=param_grid, cv=10)
grid_search.fit(X_pred, Y_pred)
#grid_search.grid_scores_
grid_search.best_score_, grid_search.best_estimator_, grid_search.best_params_

#Using KNeighborsClassifier Method of neighbors class to use Nearest Neighbor algorithm
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
classifier = KNeighborsClassifier(algorithm='auto',n_neighbors = 3, metric = 'minkowski', p = 1, weights='uniform')  #0.839
classifier.fit(X_stard, Y_stard)
YY_pred = classifier.predict(X_pred)
result_NMI=metrics.normalized_mutual_info_score(YY_pred, Y_pred)
print("result_NMI:",result_NMI)  #3,1,minkowski   3,1,manhattan