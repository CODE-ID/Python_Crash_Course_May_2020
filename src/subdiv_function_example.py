__author__ = "Zuardin Akbar"
__version__ = "2020.04.18"

import Rhino as rh

def Subdivide(_srf):
    
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
    
    #Evaluate Tolerance
    p0 = rh.Geometry.Surface.PointAt(_srf, uMin, vMin)
    p1 = rh.Geometry.Surface.PointAt(_srf, uMin, vMax)
    p2 = rh.Geometry.Surface.PointAt(_srf, uMax, vMin)
    p3 = rh.Geometry.Surface.PointAt(_srf, uMax, vMax)
    
    if rh.Geometry.Surface.IsPlanar(_srf, tol):
        listOfSubSurfaces.append(_srf)
    else:
        #Trim the _srf using the intervals (Surface division)
        s0 = rh.Geometry.Surface.Trim(_srf, u0, v0)
        s1 = rh.Geometry.Surface.Trim(_srf, u1, v0)
        s2 = rh.Geometry.Surface.Trim(_srf, u0, v1)
        s3 = rh.Geometry.Surface.Trim(_srf, u1, v1)
        
        #Subdivide again
        Subdivide(s0)
        Subdivide(s1)
        Subdivide(s2)
        Subdivide(s3)

#MAIN PROGRAM
listOfSubSurfaces = []
Subdivide(srf)

#OUTPUT
sub_Srfs = listOfSubSurfaces


