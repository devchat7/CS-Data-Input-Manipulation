import numpy as np
import matplotlib.pyplot as plt
import statistics as s
data = np.genfromtxt('rain.txt')

#plt.hist(data)
#plt.show()

print(s.mean(data))
print(s.stdev(data))

