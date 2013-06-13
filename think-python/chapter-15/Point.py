import math

class Point(object):
    """Represents a point in 2D space."""
    
def print_point(p):
    print '(%g, %g)' % (p.x, p.y)
    
# Exercise 1 solution
def distance_between_points(p1, p2):
    """Computes the Euclidean distance between two Point objects."""
    dist = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    return dist