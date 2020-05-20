#!/usr/bin/env python
# coding: utf-8

# ## Python Data Containers / Functions

# In[ ]:


# Data Types
a=False
b=10  
c="Python"  
d = 10.5 
e = 3+4j
print(type(a))   
print(type(b))   
print(type(c))
print(type(d))
print(type(e))


# In[ ]:


# Data Type Conversion
num_int = 123
num_flo = 1.23
num_new = num_int + num_flo
print(type(num_new))


# In[ ]:


# Data Type Conversion
num_int = 123
num_str_c = str(num_int)
print(type(num_str_c))

num_str = "456"
num_int_c = int(num_str)
print(type(num_int_c))


# In[ ]:


print(2+2)
print('a'+'bc')
print(2*3)
print('a'*5)


# In[ ]:


# if statements
a=10
print("even") if a%2==0 else print("odd")

a=9
print("even") if a%2==0 else print("odd")


# In[ ]:


# if else
a = 9
if a%2==0:
    print(a, "is a even number")
else:
    print(a, "is a odd number")


# In[ ]:


# elif
if a >1000:
    print(" >1000" )
elif a > 0:
    print(" >0 & LT 1000")
elif a == 0:
    print(" =0 ")
else:
    print(" < 0 ")


# In[ ]:


a = float(input("Enter any alphanumeric "))
if a%2==0:
    if a==0:
        print("Zero")
    else:
        print("Even")
else:
    print("odd")


# In[ ]:


# Data Containers - List / Tuple / Dictionary
a=[1,2,3,4,5,6]
print(type(a))

# Lists are mutable
a[0]=100
print(a)


# In[ ]:


#Index from 0 to n-1
print(a[0])

#Slicing [start:stop:step]
print(a[0:5:2])
print(a[::2])
print(a[::-1])


# In[ ]:


#List Key operations
a=[1,2,3,4,5,6]
a.append([1,2,3,4])
print(a)

a=[1,2,3,4,5,6]
a.extend([1,2,3,4])
print(a)


# In[ ]:


a=[10,20,30,40,50,60]
a.remove(40)
print(a)

a=[10,20,30,40,50,60]
a.pop(2)
print(a)

a=[10,20,30,40,50,60]
b=[20,30]
c=list(set(a)-set(b))
print(c)


# In[ ]:


a=[100,20,30,40,50,60]
a.sort()
print(a)

a=[10,20,30,40,50,60]
a.reverse()
print(a)


# In[ ]:


# List Comprehensions
a=[1,2,3,4,5,6]
b=[i*i for i in a]
print(b)


# In[ ]:


'''
Exercise - write the code for list comprehension to create another list which is concatenation of all
possible values of lists
'''
a=[1,2,3,4,5,6]
b=["a","b","c","d","e","f"]
c=[#write the code]
print(c)


# In[ ]:


# tuples - immutable
a=(1,2,3,4,5,6)
print(type(a))
print(a[0])


# In[ ]:


a[0]=100


# In[ ]:


#Dictionary - key value pairs
a={'a':100,'b':300,'c':400,1:200}
print(type(a))


# In[ ]:


print(a.keys())
print(a.values())
print(a.items())


# In[ ]:


a['100']


# In[ ]:


print(a.get('100'))
print(a.get('a'))


# In[ ]:


a={'a':100,'b':300,'c':400,1:200}
print(a.pop('b'))  
print(a)


# In[ ]:


a={'a':100,'b':300,'c':400,1:200}
print(a.popitem())
print(a)


# In[ ]:


# Views, Copy , deepcopy
a=[1,2,3,4,[5,6]]
b=a
a[4]=100
print(a)
print(b)


# In[ ]:


a=[1,2,3,4,[5,6]]
b=a.copy()
a[1]=100
print(a)
print(b)


# In[ ]:


import copy
a=[1,2,3,4,[5,6]]
b=copy.deepcopy(a)
a[4].append(100)
print(a)
print(b)


# In[ ]:


#zip enumerate
a=[1,2,3,4,5]
b=['a1','a2','a3','a4','a5']
c=zip(a,b)
d=list(c)


# In[ ]:


for i,j in d:
    print(i)
    print(j)


# In[ ]:


a=[100,200,300,400]
b=enumerate(a)
for i in b:
    print(i)


# In[ ]:


# functions
def add(x,y):
    return x*y
add(2,3)


# In[ ]:


def gt(x,y):
    x if x>y else y
gt(2,3)


# In[ ]:


def gt(x,y):
    return x if x>y else y
gt(2,3)


# In[ ]:


'''
Excercise - write a function - input a number
output number and band - < 0, =0, 0 - 100, 100 - 200, 200+
'''

