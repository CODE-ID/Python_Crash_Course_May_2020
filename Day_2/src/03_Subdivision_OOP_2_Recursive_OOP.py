__author__ = "Zuardin Akbar"
__version__ = "2020.04.18"

"""
Component Input 1 -- srf, 
Item Access, 
Type Hint: Surface

Component Input 2 -- tol, 
Item Access, 
Type Hint: float

Component Input 3 -- mainGen, 
Item Access, 
Type Hint: int
"""

import Rhino as rh
from copy import deepcopy

class PanelObject():
    #Class Constructor
    def __init__(self, _srf):
        #Object Attributes
        self.surface = _srf
        self.generation = None
        self.ID = None
        self.mainPanelID = None
        
    #Class Functions
    def GetSubSurfaces(self):
        
        self.SubSurfaces = []
        
        #Get the the U & V domain of the _srf as intervals
        u = rh.Geometry.Surface.Domain(self.surface, 0)
        v = rh.Geometry.Surface.Domain(self.surface, 1)
        
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
        
        s0 = rh.Geometry.Surface.Trim(self.surface, u0, v0)
        s1 = rh.Geometry.Surface.Trim(self.surface, u1, v0)
        s2 = rh.Geometry.Surface.Trim(self.surface, u0, v1)
        s3 = rh.Geometry.Surface.Trim(self.surface, u1, v1)
        
        self.SubSurfaces.append(s0)
        self.SubSurfaces.append(s1)
        self.SubSurfaces.append(s2)
        self.SubSurfaces.append(s3)
        
        return self.SubSurfaces

def Subdivide(_panel, _tol):
    if _panel.generation == mainGen: 
        _panel.ID = len(ListOfMainPanels)
        _panel.mainPanelID = _panel.ID
        ListOfMainPanels.append(_panel)
        
    #Evaluate Planarity Tolerance
    if rh.Geometry.Surface.IsPlanar(_panel.surface, _tol):
        ListOfPanels.append(_panel)
    else:
        #Trim the _srf using the intervals (Surface division)
        for s in _panel.GetSubSurfaces():
            p = deepcopy(_panel)
            p.surface = s
            p.generation += 1
            
            
            Subdivide(p, _tol)
            
        ListOfPanels.Remove(_panel)

#LIST FOR OBJECTS
ListOfPanels = [] 
ListOfMainPanels = []

#MAIN PROGRAM
panel = PanelObject(srf)
panel.generation = 0
Subdivide(panel, tol)

#OUTPUT
sub_Srfs = []
main_Srfs = []
main_Panel_ID = []

for p in ListOfPanels:
    
    p.surface.SetUserString("Main Panel No.", p.mainPanelID.ToString())
    sub_Srfs.append(p.surface)
    main_Panel_ID.append(p.mainPanelID)
    
    

for p in ListOfMainPanels:
    main_Srfs.append(p.surface)



