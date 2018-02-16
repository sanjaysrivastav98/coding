# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 18:55:33 2016

@author: Sanjay
"""

###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    a=[]
    cows1=cows.copy()
    cows2={}
    store=0
    
    values=sorted(cows1.values(),reverse=True)
    keys=sorted(cows1,key=lambda x:cows1[x],reverse=True)
    while(bool(cows1)):
        c=0
        b=[]
        store=0
        for i in range(len(keys)):
            if values[i]+store<=limit and keys[i] in cows1.keys():
                b+=[keys[i]]
                store+=values[i]
                del cows1[keys[i]]
        a+=[b]
    return a
    
# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows1 = cows.copy()
    a=[]
    to=[]
    t=[]
    values=sorted(cows1.values(),reverse=True)
    keys=sorted(cows1,key=lambda x:cows1[x],reverse=True)
    for i in cows1.keys():
        to+=[i]
    def allpossi(to):
        
        
        if len(to)==0:
            return [[]]
        t=allpossi(to[:-1])
        b=[]
        
        c=to[-1:]
        for j in t :
            
            b.append(c+t)
            
        return b+t
            
    s=0
    a = allpossi(to)
    for i in a :
        s=0
        for j in i:
           s+=values[keys.index(j)]
        t+=[s]
    for i in range(len(t)):
        if t[i]<=limit:
            return a[i]
    
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))
print(greedy_cow_transport({'Lotus': 10, 'Horns': 50, 'Patches': 60, 'Polaris': 20, 'Miss Bella': 15, 'MooMoo': 85, 'Louis': 45, 'Milkshake': 75, 'Muscles': 65, 'Clover': 5}, 100))
print(greedy_cow_transport({'Starlight': 54, 'Rose': 42, 'Buttercup': 11, 'Willow': 59, 'Coco': 59, 'Betsy': 39, 'Abby': 28, 'Luna': 41}, 120))
