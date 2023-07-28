import pandas as pd
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j]['Price'] > arr[j + 1]['Price']:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def read_csv(filepath, columns):
    dataframe = pd.read_csv(filepath, usecols=columns)
    return dataframe

# Column names you want to read from the CSV file
columns = ['Carat', 'Price']

# Escaping the backslashes using a raw string
filepath = r'C:\Users\GGPC\Documents\excel-read\DiamondValues.csv'

dataframe = read_csv(filepath, columns)

print("Original Data:")
print(dataframe)
print("")

# Convert DataFrame to a list of dictionaries to perform bubble sort
data_list = dataframe.to_dict('records')

# Sort the data using bubble sort based on the 'Price' column
bubble_sort(data_list)

# Convert the sorted list of dictionaries back to a DataFrame
sorted_dataframe = pd.DataFrame(data_list)

print("Sorted Data:")
print(sorted_dataframe)

plt.subplot(1, 2, 1)
plt.plot(dataframe['Price'])
plt.ylabel('price')
plt.title('Original Data')

plt.subplot(1, 2, 2)
plt.plot(sorted_dataframe['Price'])
plt.ylabel('price')
plt.title('Sorted Data')

plt.tight_layout()
plt.show()
