import pandas as pd

def read_csv(filepath, columns):
    dataframe = pd.read_csv(filepath, usecols=columns)
    return dataframe

# Column names you want to read from the CSV file
columns = [0,4]

# Escaping the backslashes
filepath = 'C:\\Users\\Mkbv2\\OneDrive\\Desktop\\excel read\\DiamondValues.csv'

dataframe = read_csv(filepath, columns)

print(dataframe)
print("")

sorted_data = dataframe.sort_values(by='Price')
print("Sorted Data: ")
print(sorted_data)
