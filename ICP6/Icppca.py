from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.decomposition import PCA

# You can add the parameter data_home to wherever to where you want to download your data
dataset = pd.read_csv('CC.csv')
dataset.drop(["MINIMUM_PAYMENTS"],axis=1,inplace=True)
# print(dataset)
x = dataset.iloc[:,1:16]
y = dataset.iloc[:,-1]
x["CREDIT_LIMIT"].fillna(x["CREDIT_LIMIT"].mean(),inplace=True)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit on training set only.
scaler.fit(x)

# Apply transform to both the training set and the test set.
x_scaler = scaler.transform(x)
pca = PCA(4)
x_pca = pca.fit_transform(x_scaler)
df2 = pd.DataFrame(data=x_pca)
finaldf = pd.concat([df2,dataset[['TENURE']]],axis=1)
print(finaldf)


from sklearn.cluster import KMeans
nclusters = 3 # this is the k in kmeans
km = KMeans(n_clusters=nclusters)
km.fit(finaldf)
# #
# # predict the cluster for each data point
y_cluster_kmeans = km.predict(finaldf)
from sklearn import metrics
score = metrics.silhouette_score(finaldf, y_cluster_kmeans)
print(score)



# fig = plt.figure(figsize = (8,8))
# ax = fig.add_subplot(1,1,1)
# ax.set_xlabel('Principal Component 1', fontsize = 15)
# ax.set_ylabel('Principal Component 2', fontsize = 15)
# ax.set_title('2 component PCA', fontsize = 20)
# targets = ['A', 'B']
# colors = ['r', 'g']
# for target, color in zip(targets,colors):
#     indicesToKeep = finalDf['target'] == target
#     ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
#                , finalDf.loc[indicesToKeep, 'principal component 2']
#                , c = color
#                , s = 50)
# ax.legend(targets)
# ax.grid()