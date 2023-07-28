from matplotlib import pyplot as plt

import pandas as pd

 

def Qsort (value):

    if len(value)<= 1:

        return value

 

    pivot = value[len(value) // 2]

    left = [x for x in value if x < pivot]

    middle = [x for x in value if x == pivot]

    right = [x for x in value if x > pivot]

 

    return Qsort(left) + middle + Qsort(right)

 

column = 'Price'

filepath = 'DiamondValues.csv'

df = pd.read_csv(filepath)

 

unsorted_data = df[column].tolist()

sorted_data = Qsort(unsorted_data)

 

# Step 3: Plot the graph

plt.figure(figsize=(10, 6))

 

# Unsorted data

plt.plot(range(len(unsorted_data)), unsorted_data, marker='o', label='Unsorted Data')

 

# Sorted data

plt.plot(range(len(sorted_data)), sorted_data, marker='x', label='Sorted Data')

 

plt.xlabel('Index')

plt.ylabel(column)

plt.title(f'Comparison of Sorted and Unsorted Data for {column}')

plt.legend()

plt.grid(True)

plt.show()