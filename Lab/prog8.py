import pandas as pd
import numpy as np
dataset = pd.read_csv('winequality-red.csv')
X=dataset.drop(['quality'],axis=1)
Y=dataset[['quality']]


from sklearn import linear_model
MR = linear_model.LinearRegression()
MR.fit(X, Y)


#Before EDA
from sklearn.metrics import mean_squared_error, r2_score
y_pred=MR.predict(X)
print("R^2(VARIANCE): %.2f" % r2_score(Y,y_pred))      # variance
print("RMSE(MEAN_SQUARED_ERROR): %.2f" % mean_squared_error(Y,y_pred))  #squaring errors for removing negative values



from sklearn.model_selection import train_test_split
#removing null values
#Reading File
train_df = pd.read_csv('winequality-red.csv')

#filling the null values with mean
train_df=train_df.apply(lambda x: x.fillna(x.mean()),axis=0)
print(train_df.isnull().sum())

#dropping the predicting value from training data
X_train = train_df.drop("quality",axis=1)
Y_train = train_df["quality"]

#using the inbuild function for splitting train data and test data
X_train, X_test, Y_train, y_test= train_test_split(X_train, Y_train, test_size=0.4, random_state=0)

#training the Model
from sklearn import linear_model
MR = linear_model.LinearRegression()
MR.fit(X_train, Y_train)

#After EDA
from sklearn.metrics import mean_squared_error, r2_score
y_pred=MR.predict(X_train)
print("R^2(VARIANCE): %.2f" % r2_score(Y_train,y_pred))      # variance
print("RMSE(MEAN_SQUARED_ERROR): %.2f" % mean_squared_error(Y_train,y_pred))  #squaring errors for removing negative values

