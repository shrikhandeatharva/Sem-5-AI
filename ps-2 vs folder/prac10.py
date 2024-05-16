import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

iris_data = pd.read_csv('D:\\GCOEN SEM 6\\PS-2 LAB\\ps-2 vs folder\\IRIS.csv') 

X = iris_data.iloc[:, :-1]
y = iris_data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)  

kmeans = KMeans(n_clusters=3, random_state=42) 
kmeans.fit(X_train)

y_pred = kmeans.predict(X_test)  

label_map = {0: 'Iris-setosa', 1: 'Iris-virginica', 2: 'Iris-versicolor'}

y_pred_mapped = [label_map[label] for label in y_pred]

accuracy = accuracy_score(y_test, y_pred_mapped)

print(f"Accuracy: {accuracy:.2f}")

results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred_mapped})

correct_predictions = results[results['Actual'] == results['Predicted']] 
incorrect_predictions = results[results['Actual'] != results['Predicted']]  

print("\nCorrect Predictions:")
print(correct_predictions)

print("\nIncorrect Predictions:")
print(incorrect_predictions)
