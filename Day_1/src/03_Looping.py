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













