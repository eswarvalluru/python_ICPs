import pandas as pd

train_df = pd.read_csv('./train_preprocessed.csv')
test_df = pd.read_csv('./test_preprocessed.csv')
relation = train_df[["Survived","Sex"]].groupby(['Sex'],as_index = False).mean()
print (relation)