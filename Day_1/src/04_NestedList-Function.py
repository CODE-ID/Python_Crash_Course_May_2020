###############  Nested List  #################
###############################################

__author__ = "gilang.arenza"
__version__ = "2020.04.30"


import Rhino as rh
import math
import ghpythonlib as ghp

pts = []

for i in range(x):
    for j in range(y):
        #coordinate of z
        pt_z = math.sin(i*u) * math.sin(j*u) * z
        #create point geometry
        pt = rh.Geometry.Point3d(i,j, pt_z)
        #store the point to a list
        pts.append(pt)
        
#define more new list
nested_pts, my_polylines = [], []

i = 0
#this is will loop until reach the length of pts
while i < len(pts):
    nested_pts.append(pts[i:i+y]) #list slicing
    i += y 

for i in nested_pts:
    #create a polyline from list of nested points
    my_polyline = rh.Geometry.Polyline(i)
    #convert polyline to a curve, check RhinoCommon doc for detail
    my_polylines.append(my_polyline.ToPolylineCurve())

#convert python nested list into Grasshopper tree structure
nested_pts = ghp.treehelpers.list_to_tree(nested_pts)

#################  Function  ##################
###############################################

__author__ = "gilang.arenza"
__version__ = "2020.04.30"

import Rhino as rh
import math

def spiral(n):
    """Create spiral points based on mathematical equations
    
    Args:
        n (int): number of points in spiral
    Return:
        math_pts (list): list of spiral points"""
    
    #define a new list
    math_pts = []
    for i in range(n):
        x = math.cos(i*0.1) * i*0.1 #x coordinate
        y = math.sin(i*0.1) * i*0.08 #y coordinate
        z = i*0.05 if i<200 else 20-i*0.05   #list comprehension for z coord.
        p = rh.Geometry.Point3d(x,y,z) #create point geometry
        math_pts.append(p) #add point to list
    return math_pts #function results

#this is where Grasshopper execute your function
a = spiral(500)


