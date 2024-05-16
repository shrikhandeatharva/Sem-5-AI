import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset from CSV
titanic = pd.read_csv('titanic.csv')

# Display the first few rows of the dataset to understand its structure
print(titanic.head())

# Visualize data distributions with a box plot
sns.boxplot(data=titanic[['Age', 'SibSp', 'Parch', 'Fare']])
plt.title('Box Plot of Titanic Dataset')
plt.show()
plt.pause(1)

# Scatter Plot
sns.scatterplot(x='Age', y='Fare', data=titanic, hue='Pclass', palette='Set2')
plt.title('Scatter Plot of Age vs Fare in Titanic Dataset')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()
plt.pause(1)

# Identify outliers using a box plot
sns.boxplot(data=titanic[['Age', 'SibSp', 'Parch', 'Fare']])
plt.title('Box Plot to Identify Outliers')
plt.show()
plt.pause(1)
# Histogram
titanic['Age'].plot(kind='hist', bins=20, edgecolor='black')
plt.title('Histogram of Age in Titanic Dataset')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
plt.pause(1)

# Bar Chart
titanic['Pclass'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Bar Chart of Passenger Class in Titanic Dataset')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.show()
plt.pause(1)

# Pie Chart
titanic['Embarked'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart of Embarked Locations in Titanic Dataset')
plt.axis('equal')
plt.show()
plt.pause(1)


# Box plot: Box plots summarize the distribution of data, highlighting median, quartiles, and outliers.

# Scatter plot: Scatter plots reveal relationships between two variables by displaying individual data points.

# Histogram: Histograms depict the frequency distribution of a single variable, offering insights into its distribution and identifying patterns or outliers.

# Bar chart: Bar charts visually compare categorical data using rectangular bars to represent each category's frequency or value.

# Pie chart: Pie charts illustrate categorical data proportions as slices of a circle, showing the relative contribution of each category to the whole.

# Outliers: Outliers are data points deviating significantly from the rest, often indicating anomalies or interesting patterns.

# Data visualization: Data visualization is the graphical representation of data to convey insights efficiently, aiding exploration, analysis, and communication.
