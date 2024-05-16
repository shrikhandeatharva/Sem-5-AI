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


# Basic descriptive statistics, including measures like mean, median, mode, standard deviation, and range, 
# provide fundamental insights into the distribution and characteristics of data. Pandas' describe() function 
# offers a concise summary of these statistics for each numerical column in a DataFrame, while the str attribute 
# provides essential information about the data types of each column. Quartiles and the quantile() function allow 
# for the exploration of data variability by dividing datasets into four equal parts and calculating specific quantiles. 
# Subsetting involves selecting relevant portions of a dataset based on specific criteria, facilitated by pandas' intuitive 
# methods such as boolean indexing, slicing, and querying. Aggregate functions like groupby() and sum(), mean(), or count() 
# enable the calculation of summary statistics for subsets of data based on grouping variables, supporting in-depth analysis 
# and insights derivation from grouped data structures. These tools collectively form the foundation of exploratory data analysis, 
# aiding in understanding data distribution, variability, and underlying patterns.
