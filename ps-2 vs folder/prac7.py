import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
iris = load_iris()
X = iris.data
y = iris.target
# Describe function to get a statistical summary of the dataset
print("Dataset Summary:\n")
print(pd.DataFrame(X).describe())
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Choose a classifier. In this example, we will use the Support Vector Machine (SVM) classifier
svm = SVC()
# Fit the model on the training data
svm.fit(X_train, y_train)
# Predict the target variable on the testing data
y_pred = svm.predict(X_test)
# Evaluate the performance of the classifier using accuracy score
accuracy = accuracy_score(y_test, y_pred)
print(f"\nclassification Accuracy: {accuracy:.2f}") 

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# from sklearn.svm import SVC
# from sklearn.metrics import accuracy_score

# # iris_data = pd.read_csv('D:\Professional skills 2\Practicals\Prac 1\IRIS.csv')
# iris_data = pd.read_csv('IRIS.csv')
# data_description = iris_data.describe()
# X = iris_data.drop('species', axis=1)
# y = iris_data['species']
# le = LabelEncoder()
# y = le.fit_transform(y)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# svm = SVC(kernel='linear')
# svm.fit(X_train, y_train)
# y_pred = svm.predict(X_test)

# print("Dataset Description:\n")
# print(data_description)
# accuracy = accuracy_score(y_test, y_pred)
# print("\nClassification Accuracy:", accuracy)