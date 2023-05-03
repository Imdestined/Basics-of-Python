#!/usr/bin/env python
# coding: utf-8

# # Python Basics_Assignment 14

# # 1. What does RGBA stand for?
#  An RGBA value is a tuple of 4 integers, each ranging from 0 to 255. The four integers correspond to the amount of red, green, blue, and alpha (transparency) in the color.

# # 2. From the Pillow module, how do you get the RGBA value of any images?
# A function call to ImageColor.getcolor('CornflowerBlue', 'RGBA') will return (100, 149, 237, 255), the RGBA value for that color.

# # 3. What is a box tuple, and how does it work?
# A box tuple is a tuple value of four integers: the left-edge x-coordinate, the top-edge y-coordinate, the width, and the height, respectively.

# # 4. Use your image and load in notebook then, How can you find out the width and height of an Image object?
# imageObj.size is a tuple of two integers, the width and the height.

# # 5. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?
# imageObj.crop((0, 50, 50, 50)). Notice that you are passing a box tuple to crop(), not four separate integer arguments.

# # 6. After making changes to an Image object, how could you save it as an image file?
# Call the imageObj.save('new_filename.png') method of the Image object.

# # 7. What module contains Pillow’s shape-drawing code?
# The ImageDraw module contains code to draw on images.

# # 8. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?
# ImageDraw objects have shape-drawing methods such as point(), line(), or rectangle(). They are returned by passing the Image object to the ImageDraw.Draw() function.
