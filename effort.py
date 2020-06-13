import pandas as pd
import numpy as np
from scipy import stats
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

pt_eff = preprocessing.PowerTransformer(method='yeo-johnson', standardize=True, copy=False)
minmax_eff = preprocessing.MinMaxScaler()

df = pd.read_csv('training3.csv')
features=['forumpost', 'forumcount', 'teststay', 'testcount']
df = df[features]

stats.mstats.winsorize(df.testcount, limits=[0, 0.04], inplace=True)
stats.mstats.winsorize(df.teststay, limits=[0, 0.02], inplace=True)
stats.mstats.winsorize(df.forumpost, limits=[0, 0.01], inplace=True)

temp_df = df[features]
# fit and transform PowerTranformer
pt_eff.fit(temp_df)
temp_df = pt_eff.transform(temp_df)

# fit and transform MinMaxScalar
minmax_eff.fit(temp_df)
temp_df = minmax_eff.transform(temp_df)
df = pd.DataFrame(data=temp_df, index=df.index, columns=df.columns)

kMeans = KMeans(n_clusters=2, random_state=0).fit(df)
df.insert(1, "style", kMeans.labels_, True)

# input features
X = df[features]

# target feature
Y = df[['style']]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.45, random_state=3, shuffle=True)

# decisiontreeclassfier model
model = DecisionTreeClassifier(max_depth=4,min_samples_leaf=2, min_samples_split=2,max_features=3,
                               criterion='entropy', random_state=0, min_weight_fraction_leaf=0)
model.fit(X_train, Y_train)
train_predict = model.predict(X_train)
print("Effort model")
print("training accuracy: {}".format(metrics.accuracy_score(Y_train, train_predict)))
test_predict = model.predict(X_test)
print("testing accuracy: {}".format(metrics.accuracy_score(Y_test, test_predict)))

cv_score = cross_val_score(model, X, Y, cv=5, scoring='accuracy')
print(cv_score)
print("Mean 5-fold: {}".format(np.mean(cv_score)))

fpr, tpr, t = metrics.roc_curve(Y_test, test_predict)
print(metrics.roc_auc_score(Y_test, test_predict))


def predict(data):
    data = pt_eff.transform(data)
    data = minmax_eff.transform(data)
    return model.predict(data)
