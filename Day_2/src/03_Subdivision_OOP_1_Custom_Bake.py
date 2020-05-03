"""
Component Input 1 -- x, 
Item Access, 
Type Hint: Surface

Component Input 2 -- bake, 
Item Access, 
Type Hint: bool
"""

import Rhino as rh

if bake:
    att = rh.RhinoDoc.ActiveDoc.CreateDefaultAttributes();
    data = x.GetUserString("Main Panel No.")
    
    print data 
    
    att.SetUserString("Main Panel No.", data)
    rh.RhinoDoc.ActiveDoc.Objects.Add(x, att)
