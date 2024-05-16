import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Specify the file path using raw string literal
# file_path = r'D:\GCOEN SEM 6\PS-2 LAB\ps-2 vs folder\US  E-commerce records 2020.csv'

# Load the dataset with 'latin1' encoding
# data = pd.read_csv(file_path, encoding='latin1')
data = pd.read_csv('US  E-commerce records 2020.csv', encoding='latin1')
# Selecting relevant columns for the analysis
selected_columns = ['Quantity', 'Discount', 'Profit']  # Independent variables
X = data[selected_columns]
y = data['Sales']  # Dependent variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the multiple regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r_squared = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", r_squared)

# Interpret the coefficients
coefficients = pd.DataFrame({'Variable': selected_columns, 'Coefficient': model.coef_})
print(coefficients)


# Multiple regression models extend simple linear regression to predict an outcome variable based on two or 
# more predictor variables. Key concepts include the coefficient estimates, which represent the strength and 
# direction of the relationship between each predictor variable and the outcome, and the intercept, which is 
# the predicted value of the outcome when all predictor variables are zero. Assumptions of multiple regression 
# include linearity, independence of errors, homoscedasticity (constant variance of errors), and normality of errors. 
# Evaluation metrics for multiple regression models typically include mean squared error (MSE), which measures the average 
# squared difference between predicted and actual values, and R-squared, which quantifies the proportion of variance in 
# the outcome variable explained by the predictor variables, providing insights into the model's goodness of fit and predictive performance.
