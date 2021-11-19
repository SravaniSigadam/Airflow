from sklearn.datasets import make_gaussian_quantiles
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import pandas as pd
import joblib
# Construct dataset
X1, y1 = make_gaussian_quantiles(cov=3.,
                                 n_samples=10000, n_features=2,
                                 n_classes=2, random_state=1)
X1 = pd.DataFrame(X1,columns=['x','y'])
y1 = pd.Series(y1)

# print(X1)
# print(X1.head())

X_train, X_test, y_train, y_test = train_test_split(X1, y1, test_size=0.3)

clf=RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)

#print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# save the model
joblib.dump(clf, "my_random_forest.joblib")