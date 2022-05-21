# pip install matplotlib
import matplotlib.pyplot as plt
# pip install numpy
import numpy as np
# pip install pandas
import pandas as pd

df = pd.read_excel('Test.xlsx')

data_array = df.to_numpy()
transposed_array = data_array.transpose()
sorted_array = transposed_array[:, np.argsort( transposed_array[1] ) ]

x = np.array(sorted_array[1])
y = np.array(sorted_array[0])

plt.plot(x, y, color='green', marker='o')
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.show()