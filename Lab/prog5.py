import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

#Reading File using read_csv function
train_df = pd.read_csv('CC.csv')

#checking for non-numeric data
print(train_df["CUST_ID"])

#using LaberlEncoder for transforming non numeric data to numeric one
Label_Encoder = LabelEncoder()

#Here we are transforming non-numeric type value to numeric value
train_df["CUST_ID"] = Label_Encoder.fit_transform(train_df["CUST_ID"])

#Here we are filling the null values with mean value by adding noise data
train_df=train_df.apply(lambda x: x.fillna(x.mean()),axis=0)

print(train_df["CUST_ID"])
print(train_df.isnull().sum())

#dropping the prediction value from training data
X_train = train_df.drop("TENURE",axis=1)
Y_train = train_df["TENURE"]

#using the build in function for splitting train data and test data
X_train, X_test, Y_train, y_test= train_test_split(X_train, Y_train, test_size=0.4, random_state=0)



# Gaussian Navie Bayes Classifier
from sklearn.naive_bayes import GaussianNB
Naive_Bayes = GaussianNB()
y_pred = Naive_Bayes.fit(X_train, Y_train).predict(X_test)
Naive_Bayes.fit(X_train, Y_train)
Y_pred = Naive_Bayes.predict(X_test)
accuracy = round(Naive_Bayes.score(X_train, Y_train) * 100, 2)
print("Using Naive Bayes accuracy is :",accuracy)


#KNN (K-NeighborsClassifier)
from sklearn.neighbors import KNeighborsClassifier
KNN = KNeighborsClassifier(n_neighbors = 3)
KNN.fit(X_train, Y_train)
Y_pred = KNN.predict(X_test)
accuracy = round(KNN.score(X_train, Y_train) * 100, 2)
print("Using KNN accuracy is :",accuracy)


#SVM
from sklearn.svm import SVC
svm = SVC()
svm.fit(X_train, Y_train)
Y_pred = svm.predict(X_test)
accuracy = round(svm.score(X_train, Y_train) * 100, 2)
print("Using SVM accuracy is :", accuracy)
