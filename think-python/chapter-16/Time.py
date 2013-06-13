import datetime
import copy

# TODO: Solution for exercise 7.

class Time(object):
    """Represents the time of day.
    
    Attributes: hour, minute, second.
    
    """
# solution to exercise 1
def print_time(time):
    """Takes a Time object and prints it in the form hour:minute:second."""
    print '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)
    
# solution to exercise 2
def is_after(t1, t2):
    """Takes two Time objects, t1 and t2, and returns True if t1 follows t2 
    chronologically and False otherwise.
    
    """
    # convert time objects to integer
    integer_t1 = 3600 * t1.hour + 60 * t1.minute + t1.second 
    integer_t2 = 3600 * t2.hour + 60 * t2.minute + t2.second
    
    return integer_t1 > integer_t2

def add_time(t1, t2):
    """Pure function that adds two time objects."""
    sum = Time()
    sum.hour   = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    # carry over extra seconds
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    # carry over extra minutes
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
        
    return sum 

def add_time2(t1, t2):
    """More succinct implementation of add_time."""
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
 
def add_time3(t1, t2):
    """Version of add_time that checks for invariants."""
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError, 'invalid Time object in add_time'
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
       
def add_time4(t1, t2):
    """Slightly different way of checking invariants using assert."""
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
    
def increment(time, seconds):
    """Adds a given number of seconds to a Time object."""
    # modify the time object
    time.second += seconds
    
    # deal with carry over (inefficently!)
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
        
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1

# solution to exercise 3
def increment2(time, seconds):
    """Adds a given number of seconds to a Time object."""
    # modify the time object
    time.second += seconds

    # deal with carry over    
    time.second = time.second % 60
    time.minute += time.second / 60 # integer division
        
    time.minute = time.minute % 60
    time.hour += time.minute / 60 # integer division

# solution to exercise 4
def increment3(time, seconds):
    """A 'Pure' version of increment that creates and returns a new Time object
    rather than modifying the parameter.
   
    """
    # create a new Time object by copying time
    new_time = copy.copy(time)
    
    # deal with carry over    
    new_time.second = new_time.second % 60
    new_time.minute += new_time.second / 60 # integer division
        
    new_time.minute = new_time.minute % 60
    new_time.hour += new_time.minute / 60 # integer division 
    
    return new_time
    
# solution to exercise 5
def increment4(time, seconds):
    """More succinct version of increment3."""
    total_time = time_to_int(time) + seconds
    return int_to_time(total_time)
    
def time_to_int(time):
    """Converts Time object to an integer."""
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds
    
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

# solution to exercise 6    
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
