import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

train_df = pd.read_csv('./glass.csv')
X_train = train_df.drop("Type",axis=1)
Y_train = train_df["Type"]


X_train, X_test, Y_train, y_test= train_test_split(X_train, Y_train, test_size=0.4, random_state=0)
gnb = GaussianNB()

y_pred = gnb.fit(X_train, Y_train).predict(X_test)
gnb.fit(X_train, Y_train)
Y_pred = gnb.predict(X_test)
acc_gnb = round(gnb.score(X_train, Y_train) * 100, 2)
print("GNB accuracy is:",acc_gnb)
print(classification_report(y_test,Y_pred))