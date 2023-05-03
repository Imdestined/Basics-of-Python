#!/usr/bin/env python
# coding: utf-8

# # Python Basics_Assignment 13

# # 1. What advantages do Excel spreadsheets have over CSV spreadsheets?
# In Excel, spreadsheets can have values of data types other than strings; cells can have different fonts, sizes, or color settings; cells can have varying widths and heights; adjacent cells can be merged; and you can embed images and charts.

# # 2.What do you pass to csv.reader() and csv.writer() to create reader and writer objects?
# You pass a File object, obtained from a call to open().

# # 3. What modes do File objects for reader and writer objects need to be opened in?
#  File objects need to be opened in read-binary ('rb') for reader objects and write-binary ('wb') for writer objects.

# # 4. What method takes a list argument and writes it to a CSV file?
# The writerow() method

# # 5. What do the keyword arguments delimiter and line terminator do?
# The delimiter argument changes the string used to separate cells in a row. The lineterminator argument changes the string used to separate rows.

# # 6. What function takes a string of JSON data and returns a Python data structure?
# json.loads()

# # 7. What function takes a Python data structure and returns a string of JSON data?
# json.dumps()
