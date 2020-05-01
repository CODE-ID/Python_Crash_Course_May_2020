##################  LIST 1  ###################
###############################################

__author__ = "gilang.arenza"
__version__ = "2020.04.30"

#you can create an empty list
numbers = []
#put your data inside square brackets[]
numbers = [1,2,3]
friends = ['Ahmad', 'Hartono', 'Ratna', 'Dewi']
#get first name from the list (index 0)
print (friends[0])
#get last name from the list (index 3)
print (friends[3])

##################  LIST 2  ###################
###############################################

__author__ = "gilang.arenza"
__version__ = "2020.04.30"

#list can have multiple data types
my_list = ['apel',150,'pisang',77,'jeruk',23]
#you can add more data to list
my_list.append(7)
#use extend method to add more elements
my_list.extend([1000, 'anggur'])
print (my_list)


###################  LOOP  ####################
###############################################

__author__ = "gilang.arenza"
__version__ = "2020.04.30"

#import RhinoCommon library
import Rhino as rh

#the number of points
x_size = 10
#define a new list
my_points = []

for i in range(x_size): #loop to repeat until max number.
    print(i)
    #use i as 'x' coordinate and store every process to a list
    my_points.append(rh.Geometry.Point3d(i, 0,0))
    

###################  LOOP  ####################
###############################################

__author__ = "gilang.arenza"
__version__ = "2020.04.30"

import math #mathemathic library
import Rhino as rh #rhinocommon library

#define a new list
math_pts = []

for i in range(500):
    x = math.cos(i*0.1) * i*0.1 #coordinate of x
    y = math.sin(i*0.1) * i*0.08 #coordinate of y
    #conditiona logic of z coordinate
    if(i < 200):
        z = i*0.05
    else:
        z = 20-i*0.05
    #create point w/ x,y,z values
    p = rh.Geometry.Point3d(x,y,z) 
    #store the point result into list
    math_pts.append(p)













