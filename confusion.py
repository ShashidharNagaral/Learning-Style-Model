import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from scipy import stats
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

pt_conf = preprocessing.PowerTransformer(method='yeo-johnson', standardize=True, copy=False)
minmax_conf = preprocessing.MinMaxScaler()

df = pd.read_csv("training3.csv")
df = df[['videostay', 'pptstay', 'pdfstay', 'forumstay', 'forumpost', 'testcount']]

df['contentstay'] = df['videostay'] + df['pdfstay'] + df['pptstay']
df.drop(['videostay', 'pdfstay', 'pptstay'], axis=1, inplace=True)

stats.mstats.winsorize(df.testcount, limits=[0, 0.04], inplace=True)
stats.mstats.winsorize(df.contentstay, limits=[0.01, 0], inplace=True)
stats.mstats.winsorize(df.forumpost, limits=[0, 0.01], inplace=True)
stats.mstats.winsorize(df.forumstay, limits=[0, 0.01], inplace=True)
features = ['forumstay', 'forumpost', 'testcount', 'contentstay']
df = df[features]

temp = df.copy()
pt_conf.fit(temp)
temp = pt_conf.transform(temp)

minmax_conf.fit(temp)
temp = minmax_conf.transform(temp)

df = pd.DataFrame(data=temp, index=df.index, columns=df.columns)

kmeans = KMeans(n_clusters=2, random_state=0).fit(df)
df.insert(4, "style", kmeans.labels_, True)

Y = df[['style']]
X = df[features]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, shuffle=True, random_state=7)
model = DecisionTreeClassifier(criterion='entropy', max_depth=4, min_samples_leaf=4, min_samples_split=6,
                               random_state=13, max_features=2)
model.fit(X_train, y_train)
test_predict = model.predict(X_test)
train_predict = model.predict(X_train)
print("Confusion Model")
print("Accuracy testing: ", accuracy_score(y_test, test_predict))
print("Accuracy training: ", accuracy_score(y_train, train_predict))


cv_score = cross_val_score(model, X, Y, cv=5, scoring='accuracy')
print(cv_score)
print("Mean 5-fold: {}".format(np.mean(cv_score)))

fpr, tpr, t = metrics.roc_curve(y_test, test_predict)
print(metrics.roc_auc_score(y_test, test_predict))


def predict(data):
    data = pt_conf.transform(data)
    data = minmax_conf.transform(data)
    return model.predict(data)
