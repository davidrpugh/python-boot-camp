import datetime
import copy

class Time(object):
    """Represents the time of day."""
    
    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a Time object with the following attributes:
        
            hour:   (int)
            minute: (int)
            second: (int)
            
        """
        self.hour   = hour
        self.minute = minute
        self.second = second
        
    def __str__(self):
        """Takes a Time object and prints it in the form hour:minute:second."""
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    
    def __add__(self, other):
        """Over-loads addition operator for Time objects."""
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    
    def __radd__(self, other):
        """Makes addition commutative."""
        return self.__add__(other)
    
    def add_time(self, other):
        """Adds two time objects."""
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
        
    # solution to exercise 1
    def time_to_int(self):
        """Converts Time object to an integer."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
        
    def increment(self, seconds):
        """Takes a time object and increments it by some number of seconds."""
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        """Returns True if self follows other chronologically and False 
        otherwise.
    
        """
        return self.time_to_int() > other.time_to_int()

def int_to_time(seconds):
    """Converts an integer to a Time object."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
    
def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def mul_time(time, number):
    """Takes a Time object and a number and returns a new Time object that 
    contains the product of the original Time and the number.
    
    """
    total_time = number * time_to_int(time)
    return int_to_time(total_time)
    
def race_pace(time, number):
    """takes a Time object that represents the finishing time in a race, and a 
    number that represents the distance, and returns a Time object that 
    represents the average pace (time per mile).
    
    """
    return mul_time(time, 1 / float(number))
    
def print_attributes(obj):
    """traverses the items in the object's dictionary and prints each attribute
    name and its corresponding value.
    
    """
    for attr in obj.__dict__:
        print attr, getattr(obj, attr)