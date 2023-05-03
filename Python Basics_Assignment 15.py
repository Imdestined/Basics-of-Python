#!/usr/bin/env python
# coding: utf-8

# # Assignment_15

# 
# 
# 
# 
# 
# 

# # 1.How many seconds are in an hour? Use the interactive interpreter as a calculator and multiply the number of seconds in a minute (60) by the number of minutes in an hour (also 60).
# 

# In[1]:


60 * 60


# # 2. Assign the result from the previous task (seconds in an hour) to a variable called seconds_per_hour.

# In[2]:


seconds_per_hour = 60 * 60


# In[3]:


seconds_per_hour


# # 3. How many seconds do you think there are in a day? Make use of the variables seconds per hour and minutes per hour.

# In[6]:


seconds_per_hour * 24


# # 4. Calculate seconds per day again, but this time save the result in a variable called seconds_per_day

# In[7]:


seconds_per_day = seconds_per_hour * 24


# In[8]:


seconds_per_day


# # 5. Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.

# In[9]:


seconds_per_day / seconds_per_hour


# # 6. Divide seconds_per_day by seconds_per_hour, using integer (//) division. Did this number agree with the floating-point value from the previous question, aside from the final .0?

# In[10]:


seconds_per_day // seconds_per_hour


# Yes

# # 7. Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
# 

# In[11]:


def genPrimes():
    primes = []
    n = 2
    last = n

    while True:
        for i in primes:
            if n % i == 0:
                n += 1
                break

        else:
            primes.append(n)
            last = n
            n += 1
            yield last


# In[12]:


genPrimes()


# In[14]:


None
def genPrimes():
    primes = [2]
    yield primes[0]
    guess = 3
    while True:
        if all(guess%x != 0 for x in primes):
            primes.append(guess)        
        if guess == primes[-1]:
            yield primes[-1]
        guess += 2


# In[15]:


genPrimes()

