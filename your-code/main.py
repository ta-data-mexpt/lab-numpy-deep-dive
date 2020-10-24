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

""" no puedo porque están estrudcturados de manera diferente:

(2, 3, 5)
(5, 2, 3)"""



#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = np.transpose(b,(1,2,0))  
print(c)
print(c.shape)

"""[[[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]

 [[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]]
(2, 3, 5)
"""

""" por medio del indice de cada lista donde 5(0),2(1) y 3(2), entonces el transpose lo debo de ejecutar pero por medio de los índices indicando cómo quiero mover las listas, es por eso que se queda 1,2,0"""

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = np.add(a,c)
print(d)

"""[[1.58024593 1.89460273 1.45577385 1.45602597 1.66577597]
  [1.65434783 1.44134631 1.78840384 1.07586526 1.55396914]
  [1.84985215 1.82634681 1.39905465 1.81604979 1.85549905]]

 [[1.8867132  1.02400526 1.3894615  1.48186056 1.50985459]
  [1.8011103  1.93707528 1.21243258 1.23512388 1.81793219]
  [1.89545311 1.5141946  1.26130986 1.22149293 1.04347969]]]

Ahora funciona porque la estructura de la matriz es igual que la de a


"""

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
print(d)

"""a = [[[0.7655685  0.67607778 0.87540081 0.86840538 0.99499375]
  [0.04403751 0.1018542  0.5834431  0.47974999 0.58242216]
  [0.31389618 0.84218418 0.36995668 0.976939   0.27804133]]

 [[0.97694687 0.78324639 0.69803825 0.60669947 0.17116921]
  [0.02917731 0.30686496 0.39377623 0.58532203 0.88511954]
  [0.55584535 0.42803711 0.52546765 0.14541563 0.84205185]]]
  
  
   d = [[[1.7655685  1.67607778 1.87540081 1.86840538 1.99499375]
  [1.04403751 1.1018542  1.5834431  1.47974999 1.58242216]
  [1.31389618 1.84218418 1.36995668 1.976939   1.27804133]]

 [[1.97694687 1.78324639 1.69803825 1.60669947 1.17116921]
  [1.02917731 1.30686496 1.39377623 1.58532203 1.88511954]
  [1.55584535 1.42803711 1.52546765 1.14541563 1.84205185]]]
  
  A eran números decimales sin cumplir un entero, d, eran numeros enteros con !, entonces solo se le suma el entero a los demcimales"""

#12. Multiply a and c. Assign the result to e.

e = print(a*c)
print(e)


#13. Does e equal to a? Why or why not?


"""si, porque los valores de C todos son 1""""

"""[[[0.7655685  0.67607778 0.87540081 0.86840538 0.99499375]
  [0.04403751 0.1018542  0.5834431  0.47974999 0.58242216]
  [0.31389618 0.84218418 0.36995668 0.976939   0.27804133]]

 [[0.97694687 0.78324639 0.69803825 0.60669947 0.17116921]
  [0.02917731 0.30686496 0.39377623 0.58532203 0.88511954]
  [0.55584535 0.42803711 0.52546765 0.14541563 0.84205185]]]"""

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

print(d_max)
print(d_min)
print(d_mean)

"""1.9949937450602855
1.0291773147496226
1.5562049465731307"""


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