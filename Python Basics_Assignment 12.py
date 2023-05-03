#!/usr/bin/env python
# coding: utf-8

# # Assignment_12

# 
# 
# 
# 12. What integers represent the levels of headings available in Word documents?
# 
# 

# # 1. In what modes should the PdfFileReader() and PdfFileWriter() File objects will be opened?

# Read-binary ('rb') for PdfFileReader() and write-binary ('wb') for PdfFileWriter()

# # 2. From a PdfFileReader object, how do you get a Page object for page 5?

# Calling getPage(4) will return a Page object for page 5, since page 0 is the first page.

# # 3. What PdfFileReader variable stores the number of pages in the PDF document?

#  The numPages variable stores an integer of the number of pages in the PdfFileReader object.

# # 4. If a PdfFileReader object’s PDF is encrypted with the password swordfish, what must you do before you can obtain Page objects from it?

# Call decrypt('swordfish').

# # 5. What methods do you use to rotate a page?

# The rotateClockwise() and rotateCounterClockwise() methods. The degrees to rotate is passed as an integer argument.

# # 6. What is the difference between a Run object and a Paragraph object?

# A document contains multiple paragraphs. A paragraph begins on a new line and contains multiple runs. Runs are contiguous groups of characters within a paragraph.

# # 7. How do you obtain a list of Paragraph objects for a Document object that’s stored in a variable named doc?

# Use doc.paragraphs.

# # 8. What type of object has bold, underline, italic, strike, and outline variables?

# A Run object has these variables (not a Paragraph).

# # 9. What is the difference between False, True, and None for the bold variable?

# True always makes the Run object bolded and False makes it always not bolded, no matter what the style’s bold setting is. None will make the Run object just use the style’s bold setting.

# # 10. How do you create a Document object for a new Word document?

# Call the docx.Document() function.

# # 11. How do you add a paragraph with the text 'Hello, there!' to a Document object stored in a variable named doc?

# doc.add_paragraph('Hello there!')

# # 12. What integers represent the levels of headings available in Word documents?
# 
# 

# The integers 0, 1, 2, 3, and 4

# In[ ]:




