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
