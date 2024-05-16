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