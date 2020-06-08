import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from scipy import stats
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

pt_vv = preprocessing.PowerTransformer(method='yeo-johnson', standardize=True, copy=False)
minmax_vv = preprocessing.MinMaxScaler()

df = pd.read_csv('training3.csv')

df = df[['videostay', 'videocount', 'pdfstay',
         'pdfcount', 'pptstay', 'pptcount', 'forumpost']]

# merging pdf and ppt into text
df['textstay'] = df['pdfstay'] + df['pptstay']
df['textcount'] = df['pdfcount'] + df['pptcount']

# replacing outliers
stats.mstats.winsorize(df.pdfstay, limits=[0, 0.01], inplace=True)
stats.mstats.winsorize(df.pdfcount, limits=[0, 0.02], inplace=True)
stats.mstats.winsorize(df.forumpost, limits=[0, 0.01], inplace=True)

features = ['videostay', 'pdfstay', 'pptstay']
df = df[features]
temp_df = df

# fit and transform PowerTranformer
pt_vv.fit(temp_df)
temp_df = pt_vv.transform(temp_df)

# fit and transform MinMaxScalar
minmax_vv.fit(temp_df)
temp_df = minmax_vv.transform(temp_df)
df = pd.DataFrame(data=temp_df, index=df.index, columns=df.columns)

# K-Means clustering
kmeans = KMeans(n_clusters=2, random_state=0).fit(df)
df.insert(1, "style", kmeans.labels_, True)

# input features
X = df[features]

# target feature
Y = df[['style']]

# split data into train and test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=3, shuffle=True)

# decisiontreeclassfier model
model = DecisionTreeClassifier(max_depth=3, min_samples_leaf=4, min_samples_split=2,
                               criterion='entropy', random_state=0)
model.fit(X_train, Y_train)
train_predict = model.predict(X_train)
print("Visual Verbal Model")
print("training accuracy: {}".format(metrics.accuracy_score(Y_train, train_predict)))
test_predict = model.predict(X_test)
print("testing accuracy: {}".format(metrics.accuracy_score(Y_test, test_predict)))

# cv-score of model
cv_score = cross_val_score(model, X, Y, cv=5, scoring='accuracy')
print(cv_score)
print("Mean 5-fold: {}".format(np.mean(cv_score)))

# roc_curve and roc_auc_score
fpr, tpr, t = metrics.roc_curve(Y_test, test_predict)
print("roc_auc score {}".format(metrics.roc_auc_score(Y_test, test_predict)))


def predict(data):
    data = pt_vv.transform(data)
    data = minmax_vv.transform(data)
    return model.predict(data)
