#!/usr/bin/env python
# coding: utf-8

# # Assignment_11

# # 1. Create an assert statement that throws an AssertionError if the variable spam is a negative integer.
# 

# assert spam >0
# 

# # 2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
# 

# Either assert eggs.lower() != bacon.lower() 'The eggs and bacon variables are the same!' 
# or assert eggs.upper() != bacon.upper(), 'The eggs and bacon variables are the same!'
# 

# # 3. Create an assert statement that throws an AssertionError every time.
# 

# assert False, 'This assertion always triggers.'

# # 4. What are the two lines that must be present in your software in order to call logging.debug()?
# 

#  To be able to call logging.debug(), you must have these two lines at the start of your program:
# 
# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -
# %(levelname)s -  %(message)s')

# # 5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?
# 

# To be able to send logging messages to a file named programLog.txt with logging.debug(), you must have these two lines at the start of your program:
# 
# import logging
# >>> logging.basicConfig(filename='programLog.txt', level=logging.DEBUG,
# format=' %(asctime)s -  %(levelname)s -  %(message)s')

# # 6. What are the five levels of logging?
# 

# DEBUG, INFO, WARNING, ERROR, and CRITICAL

# # 7. What line of code would you add to your software to disable all logging messages?
# 

# logging.disable(logging.CRITICAL)

# # 8.Why is using logging messages better than using print() to display the same message?
# 

# Using logging messages is better than using print() because:
# Logging messages can be easily disabled or configured to only show certain levels of messages
# Logging messages can be directed to different outputs (e.g. console, file, email) without changing the code
# Logging messages can include additional information such as timestamps, severity levels, and source code location

# # 9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

# The Step Over button allows the debugger to execute the current line of code and move to the next line, without stepping into any function calls. The Step In button allows the debugger to step into the currently selected function or method. The Step Out button allows the debugger to finish executing the current function or method and return to the calling code.

# # 10.After you click Continue, when will the debugger stop ?

# After clicking Continue, the debugger will stop at the next breakpoint encountered or when the program terminates.

# # 11. What is the concept of a breakpoint?

# A breakpoint is a setting on a line of code that causes the debugger to pause when the program execution reaches the line.

# In[ ]:




