import numpy as np
'''
a1 = np.array([1,2,3,4,5])
a2 = np.array([[1,2,3],[4,5,6]])
a3 = np.array([[1,2,3],[4,5,6]],dtype=float)

a11 = np.arange(1,6,1)
a22 = np.arange(2,3,.1)
a33 = np.arange(1,6,1,dtype=float)

a12 = np.linspace(1,5,num=10,endpoint=True)
a23 = np.linspace(1,6,num=10,endpoint=False)
a34 = np.linspace(1,2,num=10)

a0 = np.random.random((1,1))
#a4 = np.random.random((2,4))
#a5 = np.random.random((2,4,5)) # depth 2

a4 = np.array([[1,2,3],[4,5,6]])
a5 = a4[1,2] # identical to a6[1][2]
a6 = [[1,2,3],[4,5,6]]
'''
a1 = np.array([[1,2,3],[4,5,6]])
a2 = a1[0:2,1:3]

print(a2)


