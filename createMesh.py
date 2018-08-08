import maya.OpenMaya as om


curveFn = om.MFnNurbsCurve() 
arr = om.MPointArray() 


for pos in coords: 
     arr.append(*pos) 

curveFn.createWithEditPoints( arr, 3, om.MFnNurbsCurve.kOpen, False, False, True )


cmds.EPCurveTool