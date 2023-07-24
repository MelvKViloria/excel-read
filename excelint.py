import pandas as pd

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key['Price'] < arr[j]['Price']:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def read_csv(filepath, columns):
    dataframe = pd.read_csv(filepath, usecols=columns)
    return dataframe

# Column names you want to read from the CSV file
columns = [0,4]

# Escaping the backslashes
filepath = 'C:\\Users\\Mkbv2\\OneDrive\\Desktop\\excel read\\DiamondValues.csv'

dataframe = read_csv(filepath, columns)

print("Original Data:")
print(dataframe)
print("")

# Convert DataFrame to list of dictionaries to perform insertion sort
data_list = dataframe.to_dict('records')

# Sort the data using insertion sort based on the 'Price' column
insertion_sort(data_list)

# Convert the sorted list of dictionaries back to a DataFrame
sorted_dataframe = pd.DataFrame(data_list)

print("Sorted Data:")
print(sorted_dataframe)
