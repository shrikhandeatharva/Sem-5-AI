import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris_data = pd.read_csv('D:\\GCOEN SEM 6\\PS-2 LAB\\ps-2 vs folder\\IRIS.csv')

X = iris_data.iloc[:, :-1]
y = iris_data.iloc[:, -1] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

k = 3

knn_model = KNeighborsClassifier(n_neighbors=k)

knn_model.fit(X_train, y_train)

y_pred = knn_model.predict(X_test) 

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

correct_predictions = results[results['Actual'] == results['Predicted']] 
incorrect_predictions = results[results['Actual'] != results['Predicted']] 

print("\nCorrect Predictions:")
print(correct_predictions)

print("\nIncorrect Predictions:")
print(incorrect_predictions)



# K Nearest Neighbors (KNN) is a simple yet powerful supervised learning algorithm used for classification and regression tasks. 
# It classifies new data points based on the majority class of their nearest neighbors in the feature space, making it 
# non-parametric and robust to complex decision boundaries. In KNN, the algorithm assigns a class label to a new data 
# point by selecting the most common class among its k nearest neighbors.

# Algorithm:

# Choose the number of neighbors (k) and a distance metric.
# For each new data point, calculate the distance to all existing data points.
# Select the k nearest neighbors based on the calculated distances.
# Assign the class label by majority vote among the k neighbors (for classification) or calculate the average (for regression).
