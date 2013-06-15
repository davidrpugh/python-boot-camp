import math

class Point(object):
    """Represents a point in 2D space."""
    
    # solution to exercise 2
    def __init__(self, x=0.0, y=0.0):
        """Initializes a Point object with the following attributes:
        
            x: (float) x-coordinate of the point.
            y: (float) y-coordinate of the point.
        
        """
        self.x = x
        self.y = y
    
    # solution to exercise 3
    def __str__(self):
        """Takes a Point object and prints it in the form (x,y)."""
        return '(%g,%g)' % (self.x, self.y)
        
    # solution to exercise 4 and 5
    def __add__(self, other):
        """Over-loads the addition operator so that is works with Points."""
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):
            return Point(self.x + other[0], self.y + other[1])
        else:
            raise Exception, "other must be one of 'Point' or 'tuple'!"
    
def distance_between_points(p1, p2):
    """Computes the Euclidean distance between two Point objects."""
    dist = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    return dist