#!/usr/bin/env python
# coding: utf-8

# In[29]:


#1. Import the NUMPY package under the name np.

import numpy as np


# In[30]:


#2. Print the NUMPY version and the configuration.
print(np.__version__)
print(np.show_config())


# In[31]:


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays.
#How many ways can you find?
#4. Print a.

a= np.random.rand(2,3,5)
print(a)

#falta investigar las otras dos formas de generar random arrays


# In[47]:


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
#6. Print b.

b = np.ones((5,3,2))
print(b)


# In[48]:


#7. Do a and b have the same size? How do you prove that in Python code?
#print(a.shape)
#print(b.shape)

if a.size == b.size:
    print("Son iguales") 
elif a.size > b.size:
    print("A es mayor") 
elif a.size < b.size:
    print("B es mayor") 


# In[49]:


#8. Are you able to add a and b? Why or why not? No porque no se pueden unir dos arreglos de distinta forma
#ValueError: all the input array dimensions for the concatenation axis must match exactly, 
#but along dimension 2, the array at index 0 has size 5 and the array at index 1 has size 2

c = np.concatenate((a, b))


# In[50]:


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). 
#Assign the transposed array to varialbe "c".

c = np.transpose(b)


# In[51]:


print(c)


# In[52]:


d = np.concatenate((c, b))
d


# In[53]:


#11. Print a and d. 
#Notice the difference and relation of the two array in terms of the values? Explain.
print ("A:", a)
print ("D:", d)


# In[54]:


#12. Multiply a and c. Assign the result to e.
e = np.multiply (a,c)
e


# In[56]:


#13. Does e equal to a? Why or why not?
#sí porque multiplicamos por uno
if a.all() == e.all():
    print("Sí")


# In[62]:


#14. Identify the max, min, and mean values in d.
#Assign those values to variables "d_max", "d_min", and "d_mean"

d_max= d.max()
print("MAX:",d_max)

d_min= d.min()
print("MIN:",d_min)

d_mean= d.mean()
print("MEAN:",d_mean)


# In[ ]:


#15. Now we want to label the values in d. 
#First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.


# In[64]:


f = np.empty ((2,3,5))


# In[ ]:


"""
#16. Populate the values in f. For each value in d, if 
it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""


# In[1]:


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


# In[ ]:


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

