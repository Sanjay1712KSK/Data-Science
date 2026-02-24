''' Create a NumPy array representing reflectivity values measured at 3 temperatures over 4-time intervals.
Task:
1.	Create the array using NumPy.
2.	Reshape it into a 3 × 4 matrix.
3.	Extract the second column using slicing.
Reverse the order of columns.
'''
import numpy as np
'''a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=a.reshape(3,4)
print(b,"\n")
print("Second column: \n",b[:,1])
print("Reversed order of columns: \n",b[:,::-1])'''

'''
Generate a NumPy identity array (4x4) and an eye array. Reshape a flat array of 12 elements into 3x4 and 4x3; perform transposition and flattening. Illustrate iterating over the reshaped array with code for environmental sensor data simulation.'''
# Identity array
ida=np.identity(4)
print("Identity Array (4x4) using array:\n",ida,"\n")
# Eye array
eyea=np.eye(4)
print("Eye Array (4x4):\n",eyea,"\n")
# Reshape a flat array of 12 elements into 3x4
flat_array=np.arange(12)
reshaped_3x4=flat_array.reshape(3,4)
print("Reshaped Array (3x4):\n",reshaped_3x4,"\n")