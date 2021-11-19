import joblib
import pandas as pd
from sklearn.datasets import make_gaussian_quantiles
# load the model
loaded_rf = joblib.load("/Users/sravanisigadam/PycharmProjects/Airflow/my_random_forest.joblib")
# generate a dataset to score
X1, y1 = make_gaussian_quantiles(cov=3.,
                                 n_samples=1000, n_features=2,
                                 n_classes=2, random_state=1)

testdf = pd.DataFrame(X1,columns=['x','y'])

# predict the values for scoring data
pred = loaded_rf.predict(testdf)
print(len(pred))
