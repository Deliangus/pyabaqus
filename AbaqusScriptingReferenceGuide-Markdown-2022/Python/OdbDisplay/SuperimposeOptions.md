# SuperimposeOptions object

The SuperimposeOptions object stores values and attributes associated with the undeformed shape when the display contains both the deformed shape and the undeformed shape. The SuperimposeOptions object has no constructor command. Abaqus creates a *defaultOdbDisplay.superimposeOptions* member when you import the Visualization module. Abaqus creates a *superimposeOptions* member when it creates the [OdbDisplay](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdisplaypyc.htm?ContextScope=all) object, using the values from *defaultOdbDisplay.superimposeOptions*. Abaqus creates the *odbDisplay* member when a viewport is created, using the values from *defaultOdbDisplay*.

SuperimposeOptions objects are accessed in one of two ways:

- The default superimpose options. These settings are used as defaults when other *superimposeOptions* members are created. These settings can be set to customize user preferences.
- The superimpose options associated with a particular viewport.

The SuperimposeOptions object is derived from the [DGSuperimposeOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dgsuperimposeoptionspyc.htm?ContextScope=all) object.

## Access

```
import visualization
session.defaultOdbDisplay.superimposeOptions
session.viewports[name].assemblyDisplay.displayGroupInstances[name]\
.odbDisplayOptions.superimposeOptions
session.viewports[name].layers[name].assemblyDisplay\
.displayGroupInstances[name].odbDisplayOptions.superimposeOptions
session.viewports[name].layers[name].odbDisplay\
.displayGroupInstances[name].odbDisplayOptions.superimposeOptions
session.viewports[name].layers[name].odbDisplay.superimposeOptions
session.viewports[name].layers[name].partDisplay\
.displayGroupInstances[name].odbDisplayOptions.superimposeOptions
session.viewports[name].odbDisplay.displayGroupInstances[name]\
.odbDisplayOptions.superimposeOptions
session.viewports[name].odbDisplay.superimposeOptions
session.viewports[name].partDisplay.displayGroupInstances[name]\
.odbDisplayOptions.superimposeOptions
```

## setValues(...)



This method modifies the SuperimposeOptions object.



### Required arguments

None.

### Optional arguments

- *options*

  A SuperimposeOptions object from which values are to be copied. If other arguments are also supplied to setValues, they will override the values in *options*. The default value is None.

- *renderStyle*

  A SymbolicConstant specifying the render style of the plot. Possible values are WIREFRAME, FILLED, HIDDEN, and SHADED. The default value is WIREFRAME.

- *visibleEdges*

  A SymbolicConstant specifying which edges to plot. Possible values are ALL, EXTERIOR, FEATURE, FREE, and NONE. The default value is FEATURE.NONE can be used only when *renderStyle*=SHADED.

- *edgeColorWireHide*

  A String specifying the color to be used to plot the edges of the model when *renderStyle*=WIREFRAME or HIDDEN. The default value is "Green".

- *edgeColorFillShade*

  A String specifying the color to be used to plot the edges of the model when *renderStyle*=FILLED or SHADED. The default value is "Black".

- *edgeLineStyle*

  A SymbolicConstant specifying the edge line style. Possible values are SOLID, DASHED, DOTTED, and DOT_DASH. The default value is SOLID.

- *edgeLineThickness*

  A SymbolicConstant specifying the edge line thickness. Possible values are VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.

- *colorCodeOverride*

  A Boolean specifying whether to allow color coded items in the output database to override the edge and fill color settings. The default value is ON.

- *fillColor*

  A String specifying the color to be used to fill elements when *renderStyle*=FILLED or SHADED. The default value is "Green".

- *labelFont*

  A String specifying the label font to be used for all model labels. The default value is "-*-courier-medium-r-normal-*-*-120-*-*-m-*-*-*".

- *elemLabels*

  A Boolean specifying whether to plot the element labels. The default value is OFF.

- *elemLabelColor*

  A String specifying the color to be used to plot the element labels. The default value is "Cyan".

- *faceLabels*

  A Boolean specifying whether to plot the face labels. The default value is OFF.

- *faceLabelColor*

  A String specifying the color to be used to plot the face labels. The default value is "Red".

- *nodeLabels*

  A Boolean specifying whether to plot the node labels. The default value is OFF.

- *nodeLabelColor*

  A String specifying the color to be used to plot the node labels. The default value is "Yellow".

- *nodeSymbols*

  A Boolean specifying whether to plot the node symbols. The default value is OFF.

- *nodeSymbolType*

  A SymbolicConstant specifying the node symbol types. Possible values are:FILLED_CIRCLEFILLED_SQUAREFILLED_DIAMONDFILLED_TRIHOLLOW_CIRCLEHOLLOW_SQUAREHOLLOW_DIAMONDHOLLOW_TRICROSSXMARKERThe default value is HOLLOW_CIRCLE.

- *nodeSymbolColor*

  A String specifying the color to be used to plot the node symbols. The default value is "Yellow".

- *nodeSymbolSize*

  A SymbolicConstant specifying the node symbol size. Possible values are SMALL, MEDIUM, and LARGE. The default value is SMALL.

- *elementShrink*

  A Boolean specifying whether elements are displayed in a shrunk format. The default value is OFF.

- *elementShrinkFactor*

  An Int specifying the percentage to shrink the elements when *elementShrink*=ON. Possible values are 0≤ *elementShrinkPercentage* ≤ 90. The default value is 5.

- *coordinateScale*

  A Boolean specifying whether to scale coordinates. The default value is OFF.

- *coordinateScaleFactors*

  A sequence of three Floats specifying the coordinate scaling in each of the three coordinate directions when *coordinateScale*=ON. The default value is (1, 1, 1).

- *normals*

  A Boolean specifying whether to draw arrows that indicate the directions of element and surface normals. The default value is OFF.

- *normalDisplay*

  A SymbolicConstant specifying whether to draw element normals and surface normals. Possible values are ELEMENT and SURFACE. The default value is ELEMENT.

- *faceNormalColor*

  A String specifying the color to be used to plot the normal to a nonbeam element or to a surface. The default value is "Red".

- *beamN1Color*

  A String specifying the color to be used to plot an arrow along the beam n1n1-direction. The default value is "Blue".

- *beamN2Color*

  A String specifying the color to be used to plot an arrow along the beam n2n2-direction. The default value is "Red".

- *beamTangentColor*

  A String specifying the color to be used to plot an arrow along the tangent to a beam. The default value is "White".

- *normalArrowLength*

  A SymbolicConstant specifying the length of the normal arrows. Possible values are SHORT, MEDIUM, and LONG. The default value is MEDIUM.

- *normalLineThickness*

  A SymbolicConstant specifying the thickness of the normal arrows. Possible values are VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.

- *normalArrowheadStyle*

  A SymbolicConstant specifying the arrowhead style of the normal arrows. Possible values are NONE, FILLED, and WIRE. The default value is WIRE.

- *translucency*

  A Boolean specifying whether to set translucency. The default value is OFF.

- *translucencyFactor*

  A Float specifying the translucency factor when *translucency*=ON. Possible values are 0.0≤ *translucencyFactor* ≤ 1.0. The default value is 0.3.

- *deformedOffsetMode*

  A SymbolicConstant specifying the offset of the deformed shape from the undeformed shape. Possible values are NONE, UNIFORM, and NONUNIFORM. The default value is NONE.NONE specifies that there should be no offset of the deformed shape from the undeformed shape.

- *uniformOffset*

  A Float specifying the uniform offset value when *deformedOffsetMode*=UNIFORM. The default value is 0.0.

- *nonuniformOffset*

  A sequence of three Floats specifying the offset value in each of the three coordinate directions when *deformedOffsetMode*=NONUNIFORM. The default value is (0, 0, 0).

### Return value

None.

### Exceptions

RangeError.



## Members

The SuperimposeOptions object can have the following members:

- *deformedOffsetMode*

  A SymbolicConstant specifying the offset of the deformed shape from the undeformed shape. Possible values are NONE, UNIFORM, and NONUNIFORM. The default value is NONE.NONE specifies that there should be no offset of the deformed shape from the undeformed shape.

- *uniformOffset*

  A Float specifying the uniform offset value when *deformedOffsetMode*=UNIFORM. The default value is 0.0.

- *nonuniformOffset*

  A tuple of three Floats specifying the offset value in each of the three coordinate directions when *deformedOffsetMode*=NONUNIFORM. The default value is (0, 0, 0).

- *renderStyle*

  A SymbolicConstant specifying the render style of the plot. Possible values are WIREFRAME, FILLED, HIDDEN, and SHADED. The default value is WIREFRAME.

- *visibleEdges*

  A SymbolicConstant specifying which edges to plot. Possible values are ALL, EXTERIOR, FEATURE, FREE, and NONE. The default value is FEATURE.NONE can be used only when *renderStyle*=SHADED.

- *edgeLineStyle*

  A SymbolicConstant specifying the edge line style. Possible values are SOLID, DASHED, DOTTED, and DOT_DASH. The default value is SOLID.

- *edgeLineThickness*

  A SymbolicConstant specifying the edge line thickness. Possible values are VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.

- *colorCodeOverride*

  A Boolean specifying whether to allow color coded items in the output database to override the edge and fill color settings. The default value is ON.

- *elemLabels*

  A Boolean specifying whether to plot the element labels. The default value is OFF.

- *faceLabels*

  A Boolean specifying whether to plot the face labels. The default value is OFF.

- *nodeLabels*

  A Boolean specifying whether to plot the node labels. The default value is OFF.

- *nodeSymbols*

  A Boolean specifying whether to plot the node symbols. The default value is OFF.

- *nodeSymbolType*

  A SymbolicConstant specifying the node symbol types. Possible values are:FILLED_CIRCLEFILLED_SQUAREFILLED_DIAMONDFILLED_TRIHOLLOW_CIRCLEHOLLOW_SQUAREHOLLOW_DIAMONDHOLLOW_TRICROSSXMARKERThe default value is HOLLOW_CIRCLE.

- *nodeSymbolSize*

  A SymbolicConstant specifying the node symbol size. Possible values are SMALL, MEDIUM, and LARGE. The default value is SMALL.

- *elementShrink*

  A Boolean specifying whether elements are displayed in a shrunk format. The default value is OFF.

- *elementShrinkFactor*

  An Int specifying the percentage to shrink the elements when *elementShrink*=ON. Possible values are 0≤ *elementShrinkPercentage* ≤ 90. The default value is 5.

- *coordinateScale*

  A Boolean specifying whether to scale coordinates. The default value is OFF.

- *normals*

  A Boolean specifying whether to draw arrows that indicate the directions of element and surface normals. The default value is OFF.

- *normalDisplay*

  A SymbolicConstant specifying whether to draw element normals and surface normals. Possible values are ELEMENT and SURFACE. The default value is ELEMENT.

- *normalArrowLength*

  A SymbolicConstant specifying the length of the normal arrows. Possible values are SHORT, MEDIUM, and LONG. The default value is MEDIUM.

- *normalLineThickness*

  A SymbolicConstant specifying the thickness of the normal arrows. Possible values are VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.

- *normalArrowheadStyle*

  A SymbolicConstant specifying the arrowhead style of the normal arrows. Possible values are NONE, FILLED, and WIRE. The default value is WIRE.

- *translucency*

  A Boolean specifying whether to set translucency. The default value is OFF.

- *translucencyFactor*

  A Float specifying the translucency factor when *translucency*=ON. Possible values are 0.0≤ *translucencyFactor* ≤ 1.0. The default value is 0.3.

- *edgeColorWireHide*

  A String specifying the color to be used to plot the edges of the model when *renderStyle*=WIREFRAME or HIDDEN. The default value is "Green".

- *edgeColorFillShade*

  A String specifying the color to be used to plot the edges of the model when *renderStyle*=FILLED or SHADED. The default value is "Black".

- *fillColor*

  A String specifying the color to be used to fill elements when *renderStyle*=FILLED or SHADED. The default value is "Green".

- *labelFont*

  A String specifying the label font to be used for all model labels. The default value is "-*-courier-medium-r-normal-*-*-120-*-*-m-*-*-*".

- *elemLabelColor*

  A String specifying the color to be used to plot the element labels. The default value is "Cyan".

- *faceLabelColor*

  A String specifying the color to be used to plot the face labels. The default value is "Red".

- *nodeLabelColor*

  A String specifying the color to be used to plot the node labels. The default value is "Yellow".

- *nodeSymbolColor*

  A String specifying the color to be used to plot the node symbols. The default value is "Yellow".

- *faceNormalColor*

  A String specifying the color to be used to plot the normal to a nonbeam element or to a surface. The default value is "Red".

- *beamN1Color*

  A String specifying the color to be used to plot an arrow along the beam n1n1-direction. The default value is "Blue".

- *beamN2Color*

  A String specifying the color to be used to plot an arrow along the beam n2n2-direction. The default value is "Red".

- *beamTangentColor*

  A String specifying the color to be used to plot an arrow along the tangent to a beam. The default value is "White".

- *coordinateScaleFactors*

  A tuple of three Floats specifying the coordinate scaling in each of the three coordinate directions when *coordinateScale*=ON. The default value is (1, 1, 1).