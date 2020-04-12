import Rhino

def Subdivide(_surface):
    #Create emptylist
    #Get the the U & V domain of the _surface as intervals
    u = Rhino.Geometry.Surface.Domain(_surface, 0)
    v = Rhino.Geometry.Surface.Domain(_surface, 1)
    
    #Get the domain edge values
    uMin = u.Min
    uMax = u.Max
    vMin = v.Min
    vMax = v.Max
    
    #Get the middle value of the domains
    uMid = (uMax+uMin)/2
    vMid = (vMax+vMin)/2
    
    #Create Division Intervals
    u0 = Rhino.Geometry.Interval(uMin, uMid)
    u1 = Rhino.Geometry.Interval(uMid, uMax)
    v0 = Rhino.Geometry.Interval(vMin, vMid)
    v1 = Rhino.Geometry.Interval(vMid, vMax)
    
    #Evaluate Tolerance
    p0 = Rhino.Geometry.Surface.PointAt(_surface, uMin, vMin)
    p1 = Rhino.Geometry.Surface.PointAt(_surface, uMax, vMax)
    
    pM0 = Rhino.Geometry.Surface.PointAt(_surface, uMid, vMid)
    pM1 = (p0 + p1) / 2
    
    dist = Rhino.Geometry.Point3d.DistanceTo(pM0, pM1)
    
    print dist
    
    if dist < threshold:
        listOfSurfaces.append(_surface)
    else:
        #Trim the _surface using the intervals (Surface division)
        s0 = Rhino.Geometry.Surface.Trim(_surface, u0, v0)
        s1 = Rhino.Geometry.Surface.Trim(_surface, u1, v0)
        s2 = Rhino.Geometry.Surface.Trim(_surface, u0, v1)
        s3 = Rhino.Geometry.Surface.Trim(_surface, u1, v1)
        
        
        #Subdivide again
        Subdivide(s0)
        Subdivide(s1)
        Subdivide(s2)
        Subdivide(s3)

#MAIN PROGRAM
listOfSurfaces = []
Subdivide(surface)

#OUTPUT
subSurfaces = listOfSurfaces


