import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import statistics as std

data = np.genfromtxt("Deflection.txt", dtype = np.int64)
index = data[:,0]
deflection = data[:,1]
pipe1 = deflection[index == 1]
pipe2 = deflection[index == 2]

#plt.hist(deflection, bins='auto')
#plt.show()

#plt.hist(pipe1, bins='auto')
#plt.show()

#plt.hist(pipe2, bins='auto')
#plt.show()

print(np.mean(pipe1))
print(np.mean(pipe2))

#print(np.sqrt(np.var(pipe1,ddof=1)))
#print(np.sqrt(np.var(pipe2,ddof=1)))

pipe1Interval = st.t.interval(alpha = 0.95, df = len(pipe1), loc=np.mean(pipe1),scale=st.sem(pipe1))
print(pipe1Interval)

pipe2Interval = st.t.interval(alpha = 0.95, df = len(pipe2), loc=np.mean(pipe2),scale=st.sem(pipe2))
print(pipe2Interval)

