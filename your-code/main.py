#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.version.version)

"""
1.20.2
"""

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.random((2,3,5))

#4. Print a.

print(a)

"""
[[[0.77460267 0.48993377 0.58977043 0.32788483 0.15786997]
  [0.63766803 0.07693789 0.55638094 0.12157146 0.95912392]
  [0.41944935 0.47198286 0.83796252 0.69134065 0.05546568]]

 [[0.62966786 0.25756726 0.3643475  0.11949642 0.436977  ]
  [0.19524472 0.04309596 0.94310784 0.45683855 0.61560849]
  [0.16763798 0.75537097 0.46433708 0.36814314 0.13263072]]]
"""

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,3,2))

#6. Print b.

print(b)

"""
[[[1. 1.]
  [1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]
  [1. 1.]]]
"""

#7. Do a and b have the same size? How do you prove that in Python code?

a.size == b.size

"""
True
"""


#8. Are you able to add a and b? Why or why not?

"""
no, because they don't have the same amount of columns and rows. If you want to do it, you need to flatten them or transpose them.
"""


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose()
print(c)

"""
[[[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]

 [[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]]
"""

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = (a + c)
print(d)
"""
Because both arrays have the same structure (3 matrices of 3x5)

[[[1.07962885 1.88349223 1.13382177 1.27856537 1.66823682]
  [1.17087907 1.5774335  1.69203923 1.36592676 1.21176575]
  [1.06587072 1.35768526 1.20961881 1.56231849 1.01307871]]

 [[1.31841801 1.49005234 1.50329835 1.23843537 1.84945624]
  [1.8380541  1.42009439 1.04606641 1.61738208 1.85107404]
  [1.39154992 1.80355943 1.13962886 1.44907977 1.84662827]]]
"""


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
print(d)

"""
array a = (array d)-1
[[[0.07962885 0.88349223 0.13382177 0.27856537 0.66823682]
  [0.17087907 0.5774335  0.69203923 0.36592676 0.21176575]
  [0.06587072 0.35768526 0.20961881 0.56231849 0.01307871]]

 [[0.31841801 0.49005234 0.50329835 0.23843537 0.84945624]
  [0.8380541  0.42009439 0.04606641 0.61738208 0.85107404]
  [0.39154992 0.80355943 0.13962886 0.44907977 0.84662827]]]
[[[1.07962885 1.88349223 1.13382177 1.27856537 1.66823682]
  [1.17087907 1.5774335  1.69203923 1.36592676 1.21176575]
  [1.06587072 1.35768526 1.20961881 1.56231849 1.01307871]]

 [[1.31841801 1.49005234 1.50329835 1.23843537 1.84945624]
  [1.8380541  1.42009439 1.04606641 1.61738208 1.85107404]
  [1.39154992 1.80355943 1.13962886 1.44907977 1.84662827]]]
"""


#12. Multiply a and c. Assign the result to e.

e = a * c
print(e)

"""
[[[0.07962885 0.88349223 0.13382177 0.27856537 0.66823682]
  [0.17087907 0.5774335  0.69203923 0.36592676 0.21176575]
  [0.06587072 0.35768526 0.20961881 0.56231849 0.01307871]]

 [[0.31841801 0.49005234 0.50329835 0.23843537 0.84945624]
  [0.8380541  0.42009439 0.04606641 0.61738208 0.85107404]
  [0.39154992 0.80355943 0.13962886 0.44907977 0.84662827]]]
"""

#13. Does e equal to a? Why or why not?

e == a

"""
Yes, because the values of c are ones.
array([[[ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True]],

       [[ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True]]])
"""

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2,3,5))


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