import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 2D Data Structure assosiated with Python
df = pd.read_excel('Test.xlsx')

data_array = df.to_numpy().transpose()
print(data_array)

x = np.array(data_array[0])
y = np.array(data_array[1])

plt.plot(x, y)
plt.show()