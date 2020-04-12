import Rhino

def Subdivide(_surface):
    #Create emptylist
    listOfSurfaces = []
    
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
    
    #Trim the _surface using the intervals (Surface division)
    s0 = Rhino.Geometry.Surface.Trim(_surface, u0, v0)
    s1 = Rhino.Geometry.Surface.Trim(_surface, u1, v0)
    s2 = Rhino.Geometry.Surface.Trim(_surface, u0, v1)
    s3 = Rhino.Geometry.Surface.Trim(_surface, u1, v1)
    
    #Add the splited _surfaces into the list
    listOfSurfaces.append(s0)
    listOfSurfaces.append(s1)
    listOfSurfaces.append(s2)
    listOfSurfaces.append(s3)
    
    return listOfSurfaces

#OUTPUT
subSurfaces = Subdivide(surface)


