#############  RhinoScripSyntax  ##############
###############################################

import rhinoscriptsyntax as rs
a = rs.AddLine(x,y)

########  RhinoCommon with Coercion  ##########
###############################################

import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
a = rg.Line(rs.coerce3dpoint(x),rs.coerce3dpoint(y))

########  RhinoCommon with Type Hint  #########
###############################################
"""
Input -- x -- ItemAccess -- TypeHint: Point3d
Input -- y -- ItemAccess -- TypeHint: Point3d
"""
import Rhino.Geometry as rg
a = rg.Line(x,y)
