import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from scipy import stats
from sklearn import preprocessing
from sklearn_extra.cluster import KMedoids
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

pt_ar = preprocessing.PowerTransformer(method='yeo-johnson', standardize=True, copy=False)
minmax_ar = preprocessing.MinMaxScaler()

df = pd.read_csv('training3.csv')

df = df[['videostay', 'videocount', 'pdfstay',
         'pdfcount', 'pptstay', 'pptcount', 'teststay', 'testcount', 'total_attempt']]

# merging video, pdf and ppt into content
df['contentstay'] = df['videostay'] + df['pdfstay'] + df['pptstay']
df['contentcount'] = df['videocount'] + df['pdfcount'] + df['pptcount']
df.drop(['videostay', 'pdfstay', 'pptstay', 'videocount', 'pdfcount', 'pptcount'], axis=1, inplace=True)

# replacing outliers
stats.mstats.winsorize(df.contentstay, limits=[0.01, 0], inplace=True)
stats.mstats.winsorize(df.contentcount, limits=[0.01, 0], inplace=True)
stats.mstats.winsorize(df.teststay, limits=[0, 0.02], inplace=True)
stats.mstats.winsorize(df.testcount, limits=[0, 0.04], inplace=True)
stats.mstats.winsorize(df.total_attempt, limits=[0, 0.04], inplace=True)

features = ['teststay', 'contentstay', 'contentcount', 'total_attempt']
df = df[features]
temp_df = df
# fit and transform PowerTranformer
pt_ar.fit(temp_df)
temp_df = pt_ar.transform(temp_df)

# fit and transform MinMaxScalar
minmax_ar.fit(temp_df)
temp_df = minmax_ar.transform(temp_df)
df = pd.DataFrame(data=temp_df, index=df.index, columns=df.columns)

# K-Means clustering
kmedoids = KMedoids(n_clusters=2, random_state=0).fit(df)
df.insert(1, "style", kmedoids.labels_, True)

# input features
X = df[features]

# target feature
Y = df[['style']]

# split data into train and test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.35, random_state=0, shuffle=True)

# decisiontreeclassfier model
model = DecisionTreeClassifier(max_depth=3, min_samples_leaf=4, min_samples_split=2,
                               criterion='entropy', random_state=0)
model.fit(X_train, Y_train)
train_predict = model.predict(X_train)
print("Active Reflective Model")
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
    data = pt_ar.transform(data)
    data = minmax_ar.transform(data)
    return model.predict(data)
