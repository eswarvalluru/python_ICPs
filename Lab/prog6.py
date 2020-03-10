import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")
from sklearn import metrics

#Reading the Data
data = pd.read_csv('CC.csv')

#Removing the unrequired columns
x = data.iloc[:,1:18]

#Filling all the null values with mean
x=x.apply(lambda x: x.fillna(x.mean()),axis=0)
print(x.isnull().sum())

# Standardize features by removing the mean and scaling to unit variance
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()# Fit on training set only.
scaler.fit(x)

# Apply transform to both the training set and the test set.
x= scaler.transform(x)
X_scaled_array=scaler.transform(x)
X_scaled=pd.DataFrame(X_scaled_array)
x=X_scaled

#Plotting the Elbow Graph for best K value
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
wcss=[]
for i in range(1,11):
    kmeans= KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
    # # Silhouette Score
    # y_cluster_kmeans = kmeans.predict(x)
    # score = metrics.silhouette_score(x, y_cluster_kmeans)
    # print(score)
plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

#WE GOT K=3
#Building the model
from sklearn.cluster import KMeans
# for i in range(1,12):
k_means =3             # this is the k in kmeans
km = KMeans(n_clusters=k_means)
km.fit(x)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(x)

#Silhouette Score
# from sklearn import metrics
score = metrics.silhouette_score(x, y_cluster_kmeans)
print(score)