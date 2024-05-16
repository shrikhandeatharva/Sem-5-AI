# a) 1)part
import pandas as pd

# Load mtcars dataset
mtcars = pd.read_csv('mtcars.csv')

# Display summary statistics
print("Summary Statistics for mtcars dataset:")
print(mtcars.describe())

# Display structure of the dataset
print("\nStructure of mtcars dataset:")
print(mtcars.info())

# Display quartile information
print("\nQuartiles for mtcars dataset:")
print(mtcars['mpg'].quantile([0.25, 0.5, 0.75]))

# a) 2)part
import pandas as pd

# Load mtcars dataset
cars = pd.read_csv('cars.csv')

# Display summary statistics
print("Summary Statistics for cars dataset:")
print(cars.describe())

# Display structure of the dataset
print("\nStructure of cars dataset:")
print(cars.info())

# Display quartile information
print("\nQuartiles for cars dataset:")
print(cars['mpg'].quantile([0.25, 0.5, 0.75]))
# b) part

import pandas as pd

# Load iris dataset
iris = pd.read_csv('iris.csv')

# Display subset of the dataset using subset() function
subset_data = iris[iris['sepal_width'] >= 3.8]
print("\nSubset of iris dataset (rows with sepal_width>=3.8):")
print(subset_data)

# Display aggregated information using aggregate() function
aggregated_data = iris.groupby('species').mean()
print("\nAggregated information for iris dataset:")
print(aggregated_data)

