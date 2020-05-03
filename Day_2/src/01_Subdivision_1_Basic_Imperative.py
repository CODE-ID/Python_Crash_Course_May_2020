__author__ = "Zuardin Akbar"
__version__ = "2020.04.18"

"""
Component Input -- srf, 
Item Access, 
Type Hint: Surface
"""

import Rhino as rh

#Create emptylist
listOfSubSurfaces = []

#Get the the U & V domain of the surface as intervals
u = rh.Geometry.Surface.Domain(srf, 0)
v = rh.Geometry.Surface.Domain(srf, 1)

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

#Trim the surface using the intervals (Surface division)
s0 = rh.Geometry.Surface.Trim(srf, u0, v0)
s1 = rh.Geometry.Surface.Trim(srf, u1, v0)
s2 = rh.Geometry.Surface.Trim(srf, u0, v1)
s3 = rh.Geometry.Surface.Trim(srf, u1, v1)

#Add the splited surfaces into the list
listOfSubSurfaces.append(s0)
listOfSubSurfaces.append(s1)
listOfSubSurfaces.append(s2)
listOfSubSurfaces.append(s3)

#OUTPUT
sub_Srfs = listOfSubSurfaces


