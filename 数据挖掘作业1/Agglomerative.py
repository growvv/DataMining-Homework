import numpy as np
from sklearn.decomposition import IncrementalPCA
from sklearn.cluster import AgglomerativeClustering
from sklearn import metrics
import warnings
warnings.filterwarnings('ignore')

# 读取数据
f = open(r"breast.txt")
line = f.readline()
data_list = []
while line:
    num = list(map(float, line.split()))
    data_list.append(num)
    line = f.readline()
f.close()
data_array = np.array(data_list)
X = data_array[:, :-1]
y = data_array[:, -1]

# 降维处理
pca = IncrementalPCA(n_components=1)
X = pca.fit_transform(X)

# 聚类
clst = AgglomerativeClustering(n_clusters=2)
clst.fit(X)

# 计算 NMI
result_NMI = metrics.normalized_mutual_info_score(y, clst.labels_)
print("result_NMI:", result_NMI)
