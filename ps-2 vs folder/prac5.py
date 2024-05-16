import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy import stats
import urllib.request
# url = ".csv"
data = pd.read_csv('admission_data.csv')
# urllib.request.urlretrieve(url, "dataset.csv")
# dataset = pd.read_csv("dataset.csv")
data.columns = ['admit', 'gre_score', 'gpa', 'rank']
X = data[['gre_score', 'gpa', 'rank']]
y = data['admit']
X = sm.add_constant(X)
model = sm.Logit(y, X).fit()
print(model.summary())
null_model = sm.Logit(y, np.ones((X.shape[0], 1))).fit()
resid_deviance = -2 * (null_model.llf - model.llf)
p_value = stats.chi2.sf(resid_deviance, model.df_resid)
print('\np-value:', p_value)
if p_value > 0.05:
 print("Model is fit.")
else:
 print("Model is unfit.") 