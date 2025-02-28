"""
This script demonstrates the creation of a pandas DataFrame
and prints its type and content.
"""

import pandas as pd

# Initialize data of lists
data = {
    'Name': ['tom', 'nick', 'krish', 'jack'],
    'Age': [20, 21, 19, 18]
}

# Create DataFrame
df = pd.DataFrame(data)
print(type(df))

# Print the output
print(df.head())
