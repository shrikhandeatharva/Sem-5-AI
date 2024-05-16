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


# Regression model: Regression models predict a continuous outcome variable based on one or more predictor variables, 
# aiming to capture the relationship between them and make accurate predictions.

# Logistic regression: Logistic regression is a type of regression used for binary classification problems, predicting 
# the probability of a binary outcome (0 or 1) based on one or more predictor variables, and is widely used in fields such as medicine, finance, and marketing.

# Implementation in Python: Logistic regression can be implemented in Python using libraries like scikit-learn or statsmodels. 
# With scikit-learn, you can create and fit logistic regression models using the LogisticRegression class, specifying the desired 
# parameters and input data, making it accessible for both beginners and experienced users.





