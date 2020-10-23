#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.version.version)
"""1.19.2"""

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.random((2,3,5))


#4. Print a.

print(a)

"""[[[0.80222493 0.42029408 0.78039113 0.58721377 0.72518018]
  [0.60683695 0.36694919 0.37249113 0.01239638 0.23655994]
  [0.04821455 0.6971946  0.6888483  0.43058395 0.40011912]]

 [[0.8059214  0.61855801 0.96705493 0.35988266 0.70827823]
  [0.09980214 0.50450925 0.70015765 0.50128975 0.37647308]
  [0.95894273 0.33905761 0.66233813 0.00279417 0.21494568]]]"""



#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))


#6. Print b.

print(b)

"""[[[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]]"""


#7. Do a and b have the same size? How do you prove that in Python code?

print(a.shape)
print(b.shape)
print(a.size)
print(b.size)

"""(2, 3, 5)
(5, 2, 3)
30
30"""

#8. Are you able to add a and b? Why or why not?

""" no puedo porque están estrudcturado de manera diferente:

(2, 3, 5)
(5, 2, 3)"""



#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose()
print(c)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = (a+c)
print(d)
print(c.shape)
"""(3, 2, 5) sigue sin funcionar porque los elementos aun siguen siendo distintos entre a y c"""

""" c= [[[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]

 [[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]

 [[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]]"""

"""a=[[[0.80222493 0.42029408 0.78039113 0.58721377 0.72518018]
  [0.60683695 0.36694919 0.37249113 0.01239638 0.23655994]
  [0.04821455 0.6971946  0.6888483  0.43058395 0.40011912]]

 [[0.8059214  0.61855801 0.96705493 0.35988266 0.70827823]
  [0.09980214 0.50450925 0.70015765 0.50128975 0.37647308]
  [0.95894273 0.33905761 0.66233813 0.00279417 0.21494568]]]"""

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.




#12. Multiply a and c. Assign the result to e.



#13. Does e equal to a? Why or why not?




#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"




#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.




"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""




"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""


"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""