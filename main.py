# pip install matplotlib
import matplotlib.pyplot as plt
# pip install numpy
import numpy as np
# pip instal pandas
import pandas as pd

df = pd.read_excel('Test.xlsx')

data_array = df.to_numpy()
transposed_array = data_array.transpose()
print(transposed_array)

x = np.array(transposed_array[1])
y = np.array(transposed_array[0])
sorted_x = np.sort(-x)
sorted_y = np.sort(-y)
print(x)
print(y)

plt.plot(sorted_x, sorted_y, color='green', marker='o')
plt.show()