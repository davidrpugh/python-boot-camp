import copy

from swampy.World import World
from Point import *

class Rectangle(object):
    """Represents a rectangle.
    
    Attributes: width, height, corner, color.
    
    """
    
def find_center(rect):
    """Pure function that returns a Point object representing the center of a 
    rectangle. 
    
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p
    
def grow_rectangle(rect, dwidth, dheight):
    """Modifies the dimensions of the Rectangle object rect."""
    rect.width += dwidth
    rect.height += dheight
    
# solution to exercise 2
def move_rectangle(rect, dx, dy):
    """Modifes the coordinates of the Point object representing the corner of
    the Rectangle object rect.
    
    """
    rect.corner.x += dx
    rect.corner.y += dy
   
# solution to exercise 3
def move_rectangle2(rect, dx, dy):
    """A version of move_rectangle that creates and returns a new Rectangle 
    instead of modifying the old one.
    
    """
    # copy both rect and the Point object representing its corner
    new_rect = copy.deep_copy(rect)
    
    # modify the Point coords
    new_rect.corner.x += dx
    new_rect.corner.y += dy
    
    return new_rect
    
# Draw something resembling the flag of Bangladesh
world = World()
canvas = world.ca(width=500, height=500, background='white')
bbox = [[-150,-100], [150, 100]]
canvas.rectangle(bbox, outline='black', width=2, fill='green4')
canvas.circle([-25,0], 70, outline=None, fill='red')
world.mainloop()

# solution to exercise 4.1 and 4.2
def draw_rectangle(canvas, rect):
    """Takes a Canvas and a Rectangle as arguments and draws a representation
    of the Rectangle on the Canvas.
    
    """
    # specify bounds of the rectangle
    lower_left = [rect.corner.x, rect.corner.y]
    upper_right = [rect.corner.x + rect.width, rect.corner.y + rect.height]
    bbox = [lower_left, upper_right] 
    
    # draws the rectangle on the canvas
    canvas.rectangle(bbox, outline=None, fill=rect.color)
                  
# create a blank canvas
world = World()
canvas = world.ca(width=500, height=500, background='white')

# create the Rectangle
box = Rectangle()
box.width = 150
box.height = 50
box.corner = Point()
box.corner.x = -32
box.corner.y = -50
box.color = 'DarkCyan'

# draw the rectangle
draw_rectangle(canvas, box)
world.mainloop()
       
# solution to exercise 4.3
def draw_point(canvas, point):
    """Takes a Canvas and a Point as arguments and draws a representation of 
    the Point on the Canvas.
    
    """
    pass
    
# solution to exercise 4.4
class Circle(object):
    """Represents a circle.
    
    Attributes: center, radius, color.
    
    """
    
def draw_circle(canvas, circle):
    """Takes a Canvas and a Circle as arguments and draws a representation of 
    the Circle on the Canvas.
    
    """
    canvas.circle([circle.center.x, circle.center.y], circle.radius, 
                  outline=None, fill=circle.color)

# solution to exercise 4.5
world = World()
canvas = world.ca(width=500, height=250, background='white')
rect = Rectangle()
rect.width = canvas.get_width()
rect.height = canvas.get_height() / 2.0
rect.corner = Point()
rect.corner.x = -canvas.get_width() / 2.0
rect.corner.y = -canvas.get_height() / 2.0
rect.color = 'red'
draw_rectangle(canvas, rect)
points = [[-250,-125], [-250, 125], [0, 0]]
canvas.polygon(points, fill='DarkBlue')
world.mainloop()