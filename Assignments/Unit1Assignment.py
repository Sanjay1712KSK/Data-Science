''' Create a NumPy array representing reflectivity values measured at 3 temperatures over 4-time intervals.
Task:
1.	Create the array using NumPy.
2.	Reshape it into a 3 × 4 matrix.
3.	Extract the second column using slicing.
Reverse the order of columns.
'''
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=a.reshape(3,4)
print(b,"\n")
print("Second column: \n",b[:,1])
print("Reversed order of columns: \n",b[:,::-1])