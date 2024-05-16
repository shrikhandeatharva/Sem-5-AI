# import pandas as pd
# import seaborn as sns

# import matplotlib.pyplot as plt
# df = pd.read_csv('IRIS.csv')

# print(df.cov())
# print(df.corr())
# sns.heatmap(data=df.corr(),annot=True)
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# IRIS_data = pd.read_csv(r'D:\Professional skills 2\Practicals\Prac 1\IRIS.csv')
IRIS_data = pd.read_csv('IRIS.csv')
first_four_columns = IRIS_data.iloc[:, :4]
correlation_matrix = first_four_columns.corr()
covariance_matrix = first_four_columns.cov()
print(correlation_matrix)
print("\n\n",covariance_matrix)

axis_corr = sns.heatmap(
correlation_matrix,
vmin=-1, vmax=1, center=0,
cmap=sns.diverging_palette(50, 500, n=500),
square=True,annot=True
)

plt.show()


# Correlation: Correlation measures the strength and direction of the linear relationship between two variables, 
# with values ranging from -1 to 1, where 1 indicates a perfect positive correlation, -1 a perfect negative correlation, and 0 no correlation.

# Covariance: Covariance measures the degree to which two variables change together, with positive values 
# indicating a positive relationship and negative values indicating an inverse relationship, but its scale is not standardized.

# Correlation matrix: A correlation matrix displays the pairwise correlation coefficients between variables 
# in a dataset, providing a comprehensive view of their relationships and aiding in feature selection or dimensionality reduction.

# ANOVA (Analysis of Variance): ANOVA tests the equality of means across two or more groups by comparing the 
# variance between groups to the variance within groups. It helps determine whether there are significant differences in means among the groups.
