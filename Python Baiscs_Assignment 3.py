#!/usr/bin/env python
# coding: utf-8

# ## 1. Why are functions advantageous to have in your programs?

#  Functions reduce the need for duplicate code. This makes programs shorter, easier toread, and easier to update

# ## 2. When does the code in a function run: when it's specified or when it's called?

# The code in a function executes when the function is called, not when the function is specified or defined.
# 

# ## 3. What statement creates a function?

# A function is defined by using the def keyword, followed by a name of your choosing, followed by a set of parentheses which hold any parameters the function will take (they can be empty), and ending with a colon.
# 

# ## 4. What is the difference between a function and a function call?

# A function is procedure to achieve a particular result while function call is using this function to achive that task. 

# ## 5. How many global scopes are there in a Python program? How many local scopes?

# In python there are two primary variable scopes.
# 
# The variables created outside the function are called global variables.
# The variables defined inside the function are called the local variables.

# ## 6. What happens to variables in a local scope when the function call returns?

# When the execution of the function terminates (returns), the local variables are destroyed.

# ## 7. What is the concept of a return value? Is it possible to have a return value in an expression?

# A return value is the value that a function call evaluates to. Like any value, a return value can be used as part of an expression.

# ## 8. If a function does not have a return statement, what is the return value of a call to that function?

# If there is no return statement for a function, its return value is None.

# ## 9. How do you make a function variable refer to the global variable?

# In[7]:


# This function uses global variable 'x'

def f():
    print("Local Func:", x)
  
# Global scope

x = "I love iNeuron"
f()
print("Global Func:", x)


# ## 10. What is the data type of None?

# The data type of None is NoneType.

# ## 11. What does the sentence import areallyourpetsnamederic do?

# That import statement imports a module named areallyourpetsnamederic

# ## 12. If you had a bacon() feature in a spam module, what would you call it after importing spam?

# This function can be called with spam.bacon().

# ## 13. What can you do to save a programme from crashing if it encounters an error?

# In Python, we use the try and except statements to handle exceptions. Whenever the code breaks down, an exception is thrown without crashing the program.

# ## 14. What is the purpose of the try clause? What is the purpose of the except clause?

# The code that could potentially cause an error goes in the try clause.
# 
# The code that executes if an error happens goes in the except clause.

# In[ ]:




