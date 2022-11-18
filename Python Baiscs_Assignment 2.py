#!/usr/bin/env python
# coding: utf-8

# ## 1. What are the two values of the Boolean data type? How do you write them?

# * True and False, using capital T and F, with the rest of the word in lowercase

# ## 2. What are the three different types of Boolean operators?

# * The AND operator (&& or "and")
# * The OR operator (|| or "or")
# * The NOT operator (not)

# ## 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

# #### Truth Table:
#  * True and True -| True
#  * True and False | False
#  * False and True | False
#  * False and False | False

# ## 4. What are the values of the following expressions?
# * (5 > 4) and (3 == 5)
# * not (5 > 4)
# * (5 > 4) or (3 == 5)
# * not ((5 > 4) or (3 == 5))
# * (True and True) and (True == False)
# * (not False) or (not True)
# 

# In[2]:


(5 > 4) and (3 == 5)


# In[3]:


not (5 > 4)


# In[4]:


(5 > 4) or (3 == 5)


# In[5]:


not ((5 > 4) or (3 == 5))


# In[6]:


(True and True) and (True == False)


# In[7]:


(not False) or (not True)


# ## 5. What are the six comparison operators?

# ##### == Equal
# ##### != Not Equal
# ##### > Greater than
# ###### < Less than
# ###### >= greater than equal to 
# ##### <= less than equal to

# ### 6. How do you tell the difference between the equal to and assignment operators? Describe a condition and when you would use one.

# == is the equal to operator that compares two values and evaluates to a Boolean, while = is the assignment operator that stores a value in a variable.
# 
# For example:-
# 
# x=25 y=27 z=27
# 
# (x==y) is False because we assigned different values to x and y.
# 
# (y==z) is True because we assign equal values to y and z.
# 
# A condition is an expression used in a flow control statement that evaluates to a Boolean value

# ## 7. Identify the three blocks in this code:
# 
# spam = 0
# if spam == 10:
# print('eggs')
# if spam > 5:
# print('bacon')
# else:
# print('ham')
# print('spam')
# print('spam')
# 

# In[16]:


spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')       ## The three blocks are everything inside the if statement and the lines print('bacon') and print('ham').


# ## 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

# In[19]:


if spam ==1:
    print ("hello")
    if spam  == 2:
        print ("Howdy")
else:
    print ("Greetings")


# 10. How can you tell the difference between break and continue?
# 

# ## 9.If your programme is stuck in an endless loop, what keys you’ll press?

# Press CTRL+C to stop a program stuck in an infinite loop.

# ## 10. How can you tell the difference between break and continue?

# a)The break statement will move the execution outside and just after a loop. The continue statement will move the execution to the start of the loop.
# 
# b)whenever break statement executed then else block will not be executed whereas In continue ,all the time else block is executed.

# ## 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

# They all do the same thing. The range(10) call ranges from 0 up to (but not including) 10, range(0, 10) explicitly tells the loop to start at 0, and range(0, 10, 1) explicitly tells the loop to increase the variable by 1 on each iteration.

# ## 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[25]:


for i in range(1,11):
    print (i)


# In[28]:


i = 1
while i <= 10:
    print(i)
    i = i + 1


# ## 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

# This function can be called with spam.bacon().
