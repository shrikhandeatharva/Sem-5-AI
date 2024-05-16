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
