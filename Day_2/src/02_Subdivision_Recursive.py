__author__ = "Zuardin Akbar"
__version__ = "2020.04.18"

"""
Component Input 1 -- srf, 
Item Access, 
Type Hint: Surface

Component Input 2 -- tol, 
Item Access, 
Type Hint: float
"""

import Rhino as rh

def Subdivide(_srf, _tol):
    
    #Get the the U & V domain of the _srf as intervals
    u = rh.Geometry.Surface.Domain(_srf, 0)
    v = rh.Geometry.Surface.Domain(_srf, 1)
    
    #Get the domain edge values
    uMin = u.Min
    uMax = u.Max
    vMin = v.Min
    vMax = v.Max
    
    #Get the middle value of the domains
    uMid = (uMax+uMin)/2
    vMid = (vMax+vMin)/2
    
    #Create Division Intervals
    u0 = rh.Geometry.Interval(uMin, uMid)
    u1 = rh.Geometry.Interval(uMid, uMax)
    v0 = rh.Geometry.Interval(vMin, vMid)
    v1 = rh.Geometry.Interval(vMid, vMax)
    
    #Recursive Part
    #Evaluate Planarity Tolerance
    if rh.Geometry.Surface.IsPlanar(_srf, _tol):
        sub_Srfs.append(_srf)
    else:
        #Trim the _srf using the intervals (Surface division)
        s0 = rh.Geometry.Surface.Trim(_srf, u0, v0)
        s1 = rh.Geometry.Surface.Trim(_srf, u1, v0)
        s2 = rh.Geometry.Surface.Trim(_srf, u0, v1)
        s3 = rh.Geometry.Surface.Trim(_srf, u1, v1)
        
        #Subdivide again
        Subdivide(s0, _tol)
        Subdivide(s1, _tol)
        Subdivide(s2, _tol)
        Subdivide(s3, _tol)

#OUTPUT
sub_Srfs = [] 

#MAIN PROGRAM
Subdivide(srf, tol)



