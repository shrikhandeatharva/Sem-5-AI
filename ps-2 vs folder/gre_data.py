import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(123)

# Generate sample data
n = 100  # Number of observations
admit = np.random.choice([0, 1], size=n)  # Simulate admission status (0 = not admitted, 1 = admitted)
gre = np.random.randint(200, 801, size=n)  # Simulate GRE scores
gpa = np.random.uniform(2, 4, size=n).round(2)  # Simulate GPAs
rank = np.random.choice([1, 2, 3, 4], size=n)  # Simulate rank (assuming 1=high, 2=medium, 3=low, 4=very low)

# Create a DataFrame
data = pd.DataFrame({'admit': admit, 'gre': gre, 'gpa': gpa, 'rank': rank})

# Save the DataFrame as a CSV file
data.to_csv('admission_data.csv', index=False)

# Confirm the file is saved
import os
os.path.exists('admission_data.csv')
