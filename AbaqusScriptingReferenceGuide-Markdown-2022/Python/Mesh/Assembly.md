# Assembly object

The following commands operate on Assembly objects. For more information about the Assembly object, see [Assembly object](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?ContextScope=all).

## Access

```
import mesh
```

## assignStackDirection(...)



This method assigns a stack direction to geometric cells. The stack direction will be used to orient the elements during mesh generation.



### Required arguments

- *cells*

  A sequence of [Cell](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cellpyc.htm?ContextScope=all) objects specifying regions where to assign the stack direction.

- *referenceRegion*

  A [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object specifying the top side of the stack direction.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## associateMeshWithGeometry(...)



This method associates a geometric entity with mesh entities that are either orphan elements, bounds orphan elements, or were created using the bottom-up meshing technique.



### Required arguments

- *geometricEntity*

  A [Cell](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cellpyc.htm?ContextScope=all) , a [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all), an [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all), or a [Vertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object specifying geometric entity to be associated with one or more mesh entities.If the geometric entity is a [Cell](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cellpyc.htm?ContextScope=all) object then the argument *elements* must be specified.If the geometric entity is a [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object then the argument *elemFaces* must be specified.If the geometric entity is an [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) object then the argument *elemEdges* must be specified.If the geometric entity is a [Vertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object then the argument *node* must be specified.

### Optional arguments

- *elements*

  A sequence of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects specifying the elements to be associated with the geometric cell.

- *elemFaces*

  A sequence of [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) objects specifying the element faces to be associated with the geometric face.

- *elemEdges*

  A sequence of [MeshEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all) objects specifying the element edges to be associated with the geometric edge.

- *node*

  A [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) object specifying the mesh node to be associated with the geometric vertex.

### Return value

None.

### Exceptions

None.



## createVirtualTopology(...)



This method creates a virtual topology feature by automatically merging faces and edges based on a set of geometric parameters. The edges and vertices that are being merged will be ignored during mesh generation.



### Required arguments

- *regions*

  A sequence of [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) objects or [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) objects specifying the domain to search for geometric entities that need to be merged. Entities identified as candidates to be merged may be merged with entities from outside the specified region.

### Optional arguments

- *mergeShortEdges*

  A Boolean specifying whether to merge short edges. The default value is False.

- *shortEdgeThreshold*

  A Float specifying a threshold that determines which edges are considered to be short. These edges are the candidate entities to be merged. This argument is a required argument if the argument *mergeShortEdges* equals True and it is ignored if the argument *mergeShortEdges* equals False.

- *mergeSmallFaces*

  A Boolean specifying whether to merge faces with small area. The default value is False.

- *smallFaceAreaThreshold*

  A Float specifying a threshold that determines which faces are considered to have a small area. These faces are the candidate entities to be merged. This argument is a required argument if the argument *mergeSmallFaces* equals True and it is ignored if the argument *mergeSmallFaces* equals False.

- *mergeSliverFaces*

  A Boolean specifying whether to merge faces with high aspect ratio. The default value is False.

- *faceAspectRatioThreshold*

  A Float specifying a threshold that determines which faces are considered to have high aspect ratio. These faces are candidate entities to be merged. This argument is a required argument if the argument *mergeSliverFaces* equals True and it is ignored if the argument *mergeSliverFaces* equals False.

- *mergeSmallAngleFaces*

  A Boolean specifying whether to merge faces that have a sharp corner angle. The default value is False.

- *smallFaceCornerAngleThreshold*

  A Float specifying a threshold that determines which face corner angles are considered to be small. These faces will be candidate entities to be merged. This argument is a required argument if the argument *mergeSmallAngleFaces* equals True and it is ignored if the argument *mergeSmallAngleFaces* equals False.

- *mergeThinStairFaces*

  A Boolean specifying whether to merge faces that represent a thin stair-like feature. The default value is False.

- *thinStairFaceThreshold*

  A Float specifying a threshold that determines which faces representing small stair-like features are considered thin. These faces will be candidate entities to be merged. This argument is required if the argument *mergeThinStairFaces* is True and it is ignored if *mergeThinStairFaces* is False.

- *ignoreRedundantEntities*

  A Boolean specifying whether to abstract away redundant edges and vertices. The default value is False.

- *cornerAngleTolerance*

  A Float specifying the angle deviation from 180 degrees at a vertex or at an edge such that the two edges radiating from the vertex or the two faces bounded by the edge can be merged. The default value is 30.0 degrees.

- *applyBlendControls*

  A Boolean specifying whether to verify that blend faces can be merged with neighboring faces. If *applyBlendControls* is True then all faces that have angle larger than *blendSubtendedAngleTolerance* and a radius smaller than *blendRadiusTolerance* will not be merged with neighboring faces unless the neighboring faces are also blend faces with similar geometric characteristics. The default value is False.

- *blendSubtendedAngleTolerance*

  A Float specifying the largest subtended angle of blend faces that can be merged with neighboring faces. This argument is a required argument if the argument *applyBlendControls* equals True and it is ignored if the argument *applyBlendControls* equals False.

- *blendRadiusTolerance*

  A Float specifying the smallest radius of curvature of blend faces that can be merged with neighboring faces. This argument is a required argument if the argument *applyBlendControls* equals True and it is ignored if the argument *applyBlendControls* equals False.

### Return value

A Feature object.

### Exceptions

None.



## deleteBoundaryLayerControls(...)



This method deletes the control parameters for boundary layer mesh for all the specified regions.



### Required arguments

- *regions*

  A sequence of [Cell](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cellpyc.htm?ContextScope=all) objects specifying the regions for which to set the boundary layer mesh control parameters.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## deleteMesh(...)



This method deletes a subset of the mesh that contains the native elements from the given part instances or regions.



### Required arguments

- *regions*

  A sequence of [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) objects or [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) objects specifying the part instances or regions from where the native mesh is to be deleted.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## deleteMeshAssociationWithGeometry(...)



This method deletes the association of geometric entities with mesh entities.



### Required arguments

- *geometricEntities*

  A sequence of [Cell](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cellpyc.htm?ContextScope=all) objects, [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) objects, [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects, or [Vertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) objects specifying the geometric entities that will be disassociated from the mesh.

### Optional arguments

- *addBoundingEntities*

  A Boolean specifying whether the mesh will also be disassociated from the geometric entities that bounds the given *geometricEntities*. For example, if the argument *geometricEntities* contains a face, this boolean indicates whether the edges and vertices that bound the face will also be disassociated from the mesh. The default value is False.

### Return value

None.

### Exceptions

None.



## deletePreviewMesh()



This method deletes all boundary meshes in the assembly. See the *boundaryPreview* argument of generateMesh for information about generating boundary meshes.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## deleteSeeds(...)



This method deletes the global edge seeds from the given part instances or deletes the local edge seeds from the given edges.



### Required arguments

- *regions*

  A sequence of [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) objects or Edge objects specifying the part instances or edges from which the seeds are to be deleted.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## generateBottomUpExtrudedMesh(...)



This method generates solid elements by extruding a 2D mesh along a vector, either on an orphan mesh or within a cell region using a bottom-up technique.



### Required arguments

- *cell*

  A [Cell](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cellpyc.htm?ContextScope=all) object specifying the geometric region where the mesh is to be generated. This argument is valid only for native part instances.

- *numberOfLayers*

  An Int specifying the number of layers to be generated along the extrusion vector.

- *extrudeVector*

  A sequence of sequences of Floats specifying the start point and end point of a vector. Each point is defined by a tuple of three coordinates indicating its position. The direction of the mesh extrusion operation is from the first point to the second point.

### Optional arguments

At least one of the three optional "SourceSide" arguments must be specified.

- *geometrySourceSide*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) of [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) objects specifying the geometric domain to be used as the source for the extrude meshing operation.

- *elemFacesSourceSide*

  A sequence of [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) objects specifying the faces of 3D elements to be used as the source for the extrude meshing operation.

- *elemSourceSide*

  A sequence of 2D [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects specifying the elements to be used as the source for the extrude meshing operation.

- *depth*

  A Float specifying the distance of the mesh extrusion. If unspecified, the vector length of the *extrudeVector* argument is assumed.

- *targetSide*

  A datum plane, a sequence of [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) objects, a sequence of [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) objects, or a sequence of 2D [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects specifying the target of the extrude meshing operation. If specified, this argument overrides the *depth* argument, and all points on the source will be extruded in the direction of the extrusion vector until meeting the target.

- *biasRatio*

  A Float specifying a ratio of the element size in the extrusion direction between the source and the target sides of the extrusion. The default is 1.0, meaning no bias.

- *extendElementSets*

  A Boolean specifying whether existing element sets that include source elements will be extended to also include extruded elements. This argument is ignored for native part instances. The default value is False.

### Return value

None.

### Exceptions

None.

## generateBottomUpSweptMesh(...)



This method generates solid elements by sweeping a 2D mesh, either on an orphan mesh or within a cell region using a bottom-up technique.



### Required arguments

- *cell*

  A [Cell](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cellpyc.htm?ContextScope=all) object specifying the geometric region where the mesh is to be generated. This argument is valid only for native part instances.

### Optional arguments

At least one of the following three arguments must be specified: *geometrySourceSide*, *elemFacesSourceSide*, or *elemSourceSide*.

In addition one of the following two sets of arguments must also be specified:

- One of the following three arguments: *geometryConnectingSides*, *elemFacesConnectingSides*, or *elemConnectingSides*. In this case the targetSide is an optional argument.
- *targetSide* and *numberOfLayers*.

- *geometrySourceSide*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) of [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) objects specifying the geometric domain to be used as the source for the sweep meshing operation.

- *elemFacesSourceSide*

  A sequence of [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) objects specifying the faces of 3D elements to be used as the source for the sweep meshing operation.

- *elemSourceSide*

  A sequence of 2D [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects specifying the elements to be used as the source for the sweep meshing operation.

- *geometryConnectingSides*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) of [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) objects specifying the connecting sides of the sweep meshing operation.

- *elemFacesConnectingSides*

  A sequence of [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) objects specifying connecting sides of the sweep meshing operation.

- *elemConnectingSides*

  A sequence of 2D [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects specifying connecting sides of the sweep meshing operation.

- *targetSide*

  A [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object specifying the target side of the sweep meshing operation.

- *numberOfLayers*

  An Int specifying the number of layers to be generated along the sweep direction.

- *extendElementSets*

  A Boolean specifying whether existing element sets that include source elements will be extended to also include swept elements. This argument is ignored for native part instances. The default value is False.

### Return value

None.

### Exceptions

None.

## generateBottomUpRevolvedMesh(...)



This method generates solid elements by revolving a 2D mesh around an axis, either on an orphan mesh or within a cell region using a bottom-up technique.



### Required arguments

- *cell*

  A [Cell](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cellpyc.htm?ContextScope=all) object specifying the geometric region where the mesh is to be generated. This argument is valid only for native part instances.

- *numberOfLayers*

  An Int specifying the number of layers of elements to be generated around the axis of revolution.

- *axisOfRevolution*

  A sequence of sequences of Floats specifying the two points of the vector that describes the axis of revolution. Each point is defined by a tuple of three coordinates indicating its position. The direction of the axis of revolution is from the first point to the second point. The orientation of the revolution operation follows the right-hand-rule about the axis of revolution.

- *angleOfRevolution*

  A Float specifying the angle of revolution.

### Optional arguments

At least one of the three optional "SourceSide" arguments must be specified.

- *geometrySourceSide*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) of [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) objects specifying the geometric domain to be used as the source for the revolve meshing operation.

- *elemFacesSourceSide*

  A sequence of [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) objects specifying the faces of 3D elements to be used as the source for the revolve meshing operation.

- *elemSourceSide*

  A sequence of 2D [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects specifying the elements to be used as the source for the revolve meshing operation.

- *extendElementSets*

  A Boolean specifying whether existing element sets that include source elements will be extended to also include extruded elements. This argument is ignored for native part instances. The default value is False.

### Return value

None.

### Exceptions

None.

## generateMesh(...)



This method generates a mesh in the given part instances or regions.



### Required arguments

None.

### Optional arguments

- *regions*

  A sequence of [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) objects or [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) objects specifying the part instances or regions where the mesh is to be generated.

- *seedConstraintOverride*

  A Boolean specifying whether mesh generation is allowed to modify seed constraints. The default value is OFF.

- *meshTechniqueOverride*

  A Boolean specifying whether mesh generation is allowed to modify the existing mesh techniques so that a compatible mesh can be generated. The default value is OFF.

- *boundaryPreview*

  A Boolean specifying whether the generated mesh should be a boundary mesh. This option will only have an effect if any of the specified regions are to be meshed with tetrahedral elements or using the bottom-up technique with hexahedral or wedge elements. The default value is OFF.

- *boundaryMeshOverride*

  A Boolean specifying whether mesh generation is allowed to modify an existing boundary preview mesh. This option will only have an effect if any of the specified regions are to be meshed with tetrahedral elements and a boundary preview mesh already exists. The default value is OFF.

### Return value

None.

### Exceptions

None.

## getEdgeSeeds(...)



This method returns an edge seed parameter for a specified edge of an assembly.



### Required arguments

- *edge*

  An [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) object specifying the edge to be queried.

- *attribute*

  A SymbolicConstant specifying the type of edge seed attribute to return. Possible values are:

  - EDGE_SEEDING_METHOD
  - BIAS_METHOD
  - NUMBER
  - AVERAGE_SIZE
  - DEVIATION_FACTOR
  - MIN_SIZE_FACTOR
  - BIAS_RATIO
  - BIAS_MIN_SIZE
  - BIAS_MAX_SIZE
  - VERTEX_ADJ_TO_SMALLEST_ELEM
  - SMALLEST_ELEM_LOCATION
  - CONSTRAINT

  The return value is dependent on the *attribute* argument.

  - If *attribute*=EDGE_SEEDING_METHOD, the return value is a SymbolicConstant specifying the edge seeding method used to create the seeds along the edge. Possible values are:

    - UNIFORM_BY_NUMBER
    - UNIFORM_BY_SIZE
    - CURVATURE_BASED_BY_SIZE
    - BIASED
    - NONE

  - If *attribute*=BIAS_METHOD, the return value is a SymbolicConstant specifying the bias type used to create the seeds along the edge. Possible values are:

    - SINGLE
    - DOUBLE
    - NONE

  - If *attribute*=NUMBER, the return value is an Int specifying the number of element seeds along the edge.

  - If *attribute*=AVERAGE_SIZE, the return value is a Float specifying the average element size along the edge.

  - If *attribute*=DEVIATION_FACTOR, the return value is a Float specifying the deviation factor h/Lh/L, where hh is the chordal deviation and LL is the element length. If edge seeds are not defined, the return value is zero.

  - If *attribute*=MIN_SIZE_FACTOR, the return value is a Float specifying the size of the smallest allowable element as a fraction of the specified global element size. If edge seeds are not defined, the return value is zero.

  - If *attribute*=BIAS_RATIO, the return value is a Float specifying the length ratio of the largest element to the smallest element.

  - If *attribute*=BIAS_MIN_SIZE, the return value is a Float specifying the length of the largest element; only applicable if the EDGE_SEEDING_METHOD is BIASED and seeds were specified by minimum and maximum sizes.

  - If *attribute*=BIAS_MAX_SIZE, the return value is a Float specifying the length of the largest element; only applicable if the EDGE_SEEDING_METHOD is BIASED and seeds were specified by minimum and maximum sizes.

  - If *attribute*=VERTEX_ADJ_TO_SMALLEST_ELEM, the return value is an Int specifying the ID of the vertex next to the smallest element; only applicable if the EDGE_SEEDING_METHOD is BIASED.

  - If *attribute*=SMALLEST_ELEM_LOCATION, the return value is a SymbolicConstant specifying the location of smallest elements for double bias seeds; only applicable if the EDGE_SEEDING_METHOD is BIASED and BIAS_METHOD is DOUBLE. Possible values are:

    - SMALLEST_ELEM_AT_CENTER
    - SMALLEST_ELEM_AT_ENDS
    - NONE

  - If *attribute*=CONSTRAINT, the return value is a SymbolicConstant specifying how close the seeds must be matched by the mesh. Possible values are:

    - FREE
    - FINER
    - FIXED
    - NONE

    A value of NONE indicates that the edge is not seeded.

### Optional arguments

None.

### Return value

The return value is a Float, an Int, or a SymbolicConstant depending on the value of the *attribute* argument.

### Exceptions

None.

## getElementType(...)



This method returns the [ElemType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-elemtypepyc.htm?ContextScope=all) object of a given element shape assigned to a region of the assembly.



### Required arguments

- *region*

  A [Cell](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cellpyc.htm?ContextScope=all), a [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all), or an [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) object specifying the region to be queried.

- *elemShape*

  A SymbolicConstant specifying the shape of the element for which to return the element type. Possible values are:LINEQUADTRIHEXWEDGETET

### Optional arguments

None.

### Return value

[ElemType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-elemtypepyc.htm?ContextScope=all) object.

### Exceptions

- TypeError

  If the region cannot be associated with element types or if the *elemShape* is not consistent with the dimension of the *region*.

## getIncompatibleMeshInterfaces(...)



This method returns a sequence of face objects that are meshed with incompatible elements.



### Required arguments

None.

### Optional arguments

- *cells*

  A sequence of Cell objects which will be used to search the incompatible faces.

### Return value

A sequence of [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) objects.

### Exceptions

None.



## getMeshControl(...)



This method returns a mesh control parameter for the specified region of the assembly.



### Required arguments

- *region*

  A [Cell](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cellpyc.htm?ContextScope=all), a [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all), or an [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) object specifying the region to be queried.

- *attribute*

  A SymbolicConstant specifying the mesh control attribute to return. Possible values are:

  - ELEM_SHAPE
  - TECHNIQUE
  - ALGORITHM
  - MIN_TRANSITION

  The return value is dependent on the *attribute* argument.

  - If *attribute*=ELEM_SHAPE, the return value is a SymbolicConstant specifying the element shape used during meshing. Possible values are:

    - LINE
    - QUAD
    - TRI
    - QUAD_DOMINATED
    - HEX
    - TET
    - WEDGE
    - HEX_DOMINATED

  - If *attribute*=TECHNIQUE, the return value is a SymbolicConstant specifying the meshing technique to be used during meshing. Possible values are:

    - FREE
    - STRUCTURED
    - SWEEP
    - UNMESHABLE

    Where UNMESHABLE indicates that no meshing technique is applicable with the currently assigned element shape.

  - If *attribute*=ALGORITHM, the return value is a SymbolicConstant specifying the meshing algorithm to be used during meshing. Possible values are:

    - MEDIAL_AXIS
    - ADVANCING_FRONT
    - DEFAULT
    - NON_DEFAULT
    - NONE

    Where NONE indicates that no algorithm is applicable.

  - If *attribute*=MIN_TRANSITION, the return value is a Boolean indicating whether minimum transition will be used during meshing. This option is applicable only to the following:

    - Free quadrilateral meshing or sweep hexahedral meshing with *algorithm*=MEDIAL_AXIS.
    - Structured quadrilateral meshing.

### Optional arguments

None.

### Return value

The return value is a SymbolicConstant or a Boolean depending on the value of the *attribute* argument.

### Exceptions

- TypeError

  The region cannot carry mesh controls.

## getMeshStats(...)



This method returns the mesh statistics for the given part instances or regions.



### Required arguments

- *regions*

  A sequence or tuple of [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) objects or Geometry regions for which mesh statistics should be returned.

### Optional arguments

None.

### Return value

A MeshStats object.

### Exceptions

None.



## getPartSeeds(...)



This method returns a part seed parameter for the specified instance.



### Required arguments

- *region*

  A [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) object specifying the part instance to be queried.

- *attribute*

  A SymbolicConstant specifying the type of part seed attribute to return. Possible values are:

  - SIZE
  - DEFAULT_SIZE
  - DEVIATION_FACTOR
  - MIN_SIZE_FACTOR

  The return value is dependent on the value of the *attribute* argument.

  - If *attribute*=SIZE, the return value is a Float specifying the assigned global element size. If part seeds are not defined, the return value is zero.
  - If *attribute*=DEFAULT_SIZE, the return value is a Float specifying a suggested default global element size based upon the part geometry.
  - If *attribute*=DEVIATION_FACTOR, the return value is a Float specifying the deviation factor h/Lh/L, where hh is the chordal deviation and LL is the element length. If part seeds are not defined, the return value is zero.
  - If *attribute*=MIN_SIZE_FACTOR, the return value is a Float specifying the size of the smallest allowable element as a fraction of the specified global element size. If part seeds are not defined, the return value is zero.

### Optional arguments

None.

### Return value

The return value is a Float, and its value is dependent on the *attribute* argument.

### Exceptions

- An exception occurs if the part instance does not contain native geometry.

  Error: Part instance does not contain native geometry

## getUnmeshedRegions()



This method returns all geometric regions in the assembly that require a mesh for submitting an analysis but are either unmeshed or are meshed incompletely.



### Arguments

None.

### Return value

A Region object, or None.

### Exceptions

None.



## ignoreEntity(...)



This method creates a virtual topology feature. Virtual topology allows unimportant entities to be ignored during mesh generation. You can combine two adjacent faces by specifying a common edge to ignore. Similarly, you can combine two adjacent edges by specifying a common vertex to ignore.



### Required arguments

- *entities*

  A sequence of vertices and edges specifying the entities to be ignored during meshing.

### Optional arguments

None.

### Return value

A Feature object.

### Exceptions

None.



## restoreIgnoredEntity(...)



This method restores vertices and edges that have been merged using a virtual topology feature.



### Required arguments

- *entities*

  A sequence of [IgnoredVertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignoredvertexpyc.htm?ContextScope=all) objects and [IgnoredEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignorededgepyc.htm?ContextScope=all) objects specifying the entities to be restored.

### Optional arguments

None.

### Return value

A Feature object.

### Exceptions

None.

## seedEdgeByBias(...)



This method seeds the given edges nonuniformly using the specified number of elements and bias ratio or the specified minimum and maximum element sizes.



### Required arguments

- *biasMethod*

  A SymbolicConstant specifying whether single- or double-biased seed distribution will be applied. If unspecified, single-biased seed distribution will be applied. Possible values are:

  - SINGLE: Single-biased seed distribution will be applied.
  - DOUBLE: Double-biased seed distribution will be applied.

- *end1Edges*

  A sequence of [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects specifying the edges to seed. The smallest elements will be positioned near the end where the normalized curve parameter=0.0. You must provide either the *end1Edges* or the *end2Edges* argument or both when *biasMethod*=SINGLE and omit both of them when *biasMethod*=DOUBLE.Note:You can determine which end is which by the order of the vertex indices returned by [getVertices()](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all#simaker-edgegetverticespyc).

- *end2Edges*

  A sequence of [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects specifying the edges to seed. The smallest elements will be positioned near the end where the normalized curve parameter=1.0.

- *centerEdges*

  A sequence of [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects specifying the edges to seed. The smallest elements will be positioned near edge center. You must provide either the *centerEdges* or the *endEdges* argument or both when *biasMethod*=DOUBLE and omit both of them when *biasMethod*=SINGLE.

- *endEdges*

  A sequence of [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects specifying the edges to seed. The smallest elements will be positioned near edge ends.

- *ratio*

  A Float specifying the ratio of the largest element to the smallest element. Possible values are 1.0 ≤≤ *ratio* ≤≤ 106.

- *number*

  An Int specifying the number of elements along each edge. Possible values are 1 ≤≤ *number* ≤≤ 104.

- *minSize*

  A Float specifying the desired smallest element size.

- *maxSize*

  A Float specifying the desired largest element size.Note:You must specify either the *ratio* and *number* or *minSize* and *maxSize* pair of arguments.

### Optional arguments

- *constraint*

  A SymbolicConstant specifying how closely the seeds must be matched by the mesh. The default value is FREE. If unspecified, the existing constraint will remain unchanged. Possible values are:

  - FREE: The resulting mesh can be finer or coarser than the specified seeds.
  - FINER: The resulting mesh can be finer than the specified seeds.
  - FIXED: The seeds must be exactly matched by the mesh (only with respect to the number of elements, not to the nodal positioning).

### Return value

None.

### Exceptions

None.

## seedEdgeByNumber(...)



This method seeds the given edges uniformly based on the number of elements along the edges.



### Required arguments

- *edges*

  A sequence of [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects specifying the edges to seed.

- *number*

  An Int specifying the number of elements along each edge. Possible values are 1 ≤≤ *number* ≤≤ 104.

### Optional arguments

- *constraint*

  A SymbolicConstant specifying how closely the seeds must be matched by the mesh. The default value is FREE. If unspecified, the existing constraint will remain unchanged. Possible values are:FREE: The resulting mesh can be finer or coarser than the specified seeds.FINER: The resulting mesh can be finer than the specified seeds.FIXED: The seeds must be exactly matched by the mesh (only with respect to the number of elements, not to the nodal positioning).

### Return value

None.

### Exceptions

None.



## seedEdgeBySize(...)



This method seeds the given edges either uniformly or following edge curvature distribution, based on the desired element size.



### Required arguments

- *edges*

  A sequence of [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects specifying the edges to seed.

- *size*

  A Float specifying the desired element size.

### Optional arguments

- *deviationFactor*

  A Float specifying the deviation factor h/Lh/L, where hh is the chordal deviation and LL is the element length.

- *minSizeFactor*

  A Float specifying the size of the smallest allowable element as a fraction of the specified global element size.

- *constraint*

  A SymbolicConstant specifying how closely the seeds must be matched by the mesh. The default value is FREE. If unspecified, the existing constraint will remain unchanged. Possible values are:FREE: The resulting mesh can be finer or coarser than the specified seeds.FINER: The resulting mesh can be finer than the specified seeds.FIXED: The seeds must be exactly matched by the mesh (only with respect to the number of elements, not to the nodal positioning).

### Return value

None.

### Exceptions

None.



## seedPartInstance(...)



This method assigns global edge seeds to the given part instances.



### Required arguments

- *regions*

  A sequence of [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) objects specifying the part instances to seed.

- *size*

  A Float specifying the desired global element size for the edges.

### Optional arguments

- *deviationFactor*

  A Float specifying the deviation factor h/Lh/L, where hh is the chordal deviation and LL is the element length.

- *minSizeFactor*

  A Float specifying the size of the smallest allowable element as a fraction of the specified global element size.

- *constraint*

  A SymbolicConstant specifying how closely the seeds must be matched by the mesh. The default value is FREE. If unspecified, the existing constraint will remain unchanged. Possible values are:FREE: The resulting mesh can be finer or coarser than the specified seeds.FINER: The resulting mesh can be finer than the specified seeds.

### Return value

None.

### Exceptions

None.



## setBoundaryLayerControls(...)



This method sets the control parameters for boundary layer mesh for the specified regions.



### Required arguments

- *regions*

  A sequence of [Cell](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cellpyc.htm?ContextScope=all) objects specifying the regions for which to set the boundary layer mesh control parameters.

- *firstElemSize*

  A Float specifying the height of the first element layer off boundary. Possible values are 0.0 << *firstElemSize* ≤≤ 106.

- *growthFactor*

  A Float specifying the ratio of heights of any two consecutive element layers. Possible values are 1.0 ≤≤ *growthFactor* ≤≤ 10.0.

- *numLayers*

  An Int specifying the number of element layers to be generated. Possible values are 1 ≤≤ *numLayers* ≤≤ 104.

### Optional arguments

- *inactiveFaces*

  A sequence of [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) objects specifying the faces where boundary layer should not be generated. By default, boundary layer mesh will be generated on all faces of the selected regions.

- *setName*

  A String specifying a unique name for a set that will contain boundary layer elements.

### Return value

None.

### Exceptions

None.



## setElementType(...)



This method assigns element types to the specified regions.



### Required arguments

- *regions*

  A sequence of Geometry regions or [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects, or a Set object containing either geometry regions or elements, specifying the regions to which element types are to be assigned.

- *elemTypes*

  A sequence of ElemType objects, one for each element shape applicable to the regions.Note:If an ElemType object has an UNKNOWN_*xxx* value for *elemCode*, its order will be deduced from the order of other valid ElemType objects within the same setElementType command. If no valid ElemType objects can be found, the order will remain unchanged.

### Optional arguments

None.

### Return value

None.

### Exceptions

As a result of the element assignment, a region must have the same library, family, and order for all its assigned element types. Otherwise, an exception will be thrown.

For example, suppose the Hex, Wedge, and Tet elements previously assigned to a cell are all linear. The user now constructs an ElemType object with a quadratic Hex element and includes only this object in the setElementType command. An exception will be thrown because the Wedge and Tet elements will remain linear (i.e., As Is) and become incompatible with the newly assigned quadratic Hex element.



## setLogicalCorners(...)



This method sets the logical corners for a mappable face region.



### Required arguments

- *region*

  A Face region.

- *corners*

  Three, four, or five Vertex objects defining the logical corners for a given mappable face region.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

## setMeshControls(...)



This method sets the mesh control parameters for the specified regions.



### Required arguments

- *regions*

  A sequence of Face or Cell regions specifying the regions for which to set the mesh control parameters.

### Optional arguments

- *elemShape*

  A SymbolicConstant specifying the element shape to be used for meshing. The default value is QUAD for Face regions and HEX for Cell regions. If unspecified, the existing element shape will remain unchanged. Possible values are:

  - QUAD: Quadrilateral mesh.
  - QUAD_DOMINATED: Quadrilateral-dominated mesh.
  - TRI: Triangular mesh.
  - HEX: Hexahedral mesh.
  - HEX_DOMINATED: Hex-dominated mesh.
  - TET: Tetrahedral mesh.
  - WEDGE: Wedge mesh.

- *technique*

  A SymbolicConstant specifying the mesh technique to be used. The default value is FREE for Face regions. For Cell regions the initial value depends on the geometry of the regions and can be STRUCTURED, SWEEP, or unmeshable. If unspecified, the existing mesh technique(s) will remain unchanged. Possible values are:

  - FREE: Free mesh technique.
  - STRUCTURED: Structured mesh technique.
  - SWEEP: Sweep mesh technique.
  - BOTTOM_UP: Bottom-up mesh technique. Only applicable for cell regions.
  - SYSTEM_ASSIGN: Allow the system to assign a suitable technique. The actual technique assigned can be STRUCTURED, SWEEP, or “unmeshable”.

- *algorithm*

  A SymbolicConstant specifying the algorithm used to generate the mesh for the specified regions. Possible values are MEDIAL_AXIS, ADVANCING_FRONT, and NON_DEFAULT. If unspecified, the existing value will remain unchanged. This option is applicable only to the following:

  - Free quadrilateral or quadrilateral-dominated meshing. In this case the possible values are MEDIAL_AXIS and ADVANCING_FRONT.
  - Sweep hexahedral or hexahedral-dominated meshing. In this case the possible values are MEDIAL_AXIS and ADVANCING_FRONT.
  - Free tetrahedral meshing. In this case the only possible value is NON_DEFAULT, and it indicates that the free tetrahedral-meshing technique available in Abaqus 6.4 or earlier will be used. If algorithm is not specified, the default tetrahedral-meshing technique will be used.

- *minTransition*

  A Boolean specifying whether minimum transition is to be applied. The default value is ON. If unspecified, the existing value will remain unchanged. This option is applicable only in the following cases:

  - Free quadrilateral meshing or hexahedral sweep meshing with *algorithm*=MEDIAL_AXIS.
  - Structured quadrilateral meshing.

- *sizeGrowth*

  A SymbolicConstant specifying element size growth to be applied when generating the interior of a tetrahedral mesh. Possible values are MODERATE and MAXIMUM. If unspecified, the existing value will remain unchanged. This option only applies to the default tetrahedral mesher.

- *allowMapped*

  A Boolean specifying whether mapped meshing can be used to replace the selected mesh technique. The *allowMapped* argument is applicable only in the following cases:

  - Free triangular meshing.
  - Free quadrilateral or quadrilateral-dominated meshing with *algorithm*=ADVANCING_FRONT.
  - Hexahedral or hexahedral-dominated sweep meshing with *algorithm*=ADVANCING_FRONT.
  - Free tetrahedral meshing. *allowMapped*=True implies that mapped triangular meshing can be used on faces that bound three-dimensional *regions*.

### Return value

None.

### Exceptions

None.

## setSweepPath(...)



This method sets the sweep path for a sweepable region or the revolve path for a revolvable region.



### Required arguments

- *region*

  A sweepable region.

- *edge*

  An [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) object specifying the sweep or revolve path.

- *sense*

  A SymbolicConstant specifying the sweep sense. The sense will affect only how gasket elements will be created; it will have no effect if gasket elements are not used. Possible values are FORWARD or REVERSE.If *sense*=FORWARD, the sense of the given edge's underlying curve will be used.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## verifyMeshQuality(...)



This method tests the quality of part instance meshes and returns poor-quality elements.



### Required arguments

- *criterion*

  A SymbolicConstant specifying the criterion used for the quality check. Possible values are:

  - ANALYSIS_CHECKS

    When this criterion is specified Abaqus/CAE will invoke the element quality checks included with the input file processor for Abaqus/Standard and Abaqus/Explicit.

  - ANGULAR_DEVIATION

    The maximum amount (in degrees) that an element's face corner angles deviate from the ideal angle. The ideal angle is 90° for quadrilateral element faces and 60° for triangular element faces. Elements with an angular deviation larger than the specified threshold will fail this test.

  - ASPECT_RATIO

    The ratio between the lengths of the longest and shortest edges of an element. Elements with an aspect ratio larger than the specified threshold will fail this test.

  - GEOM_DEVIATION_FACTOR

    The largest geometric deviation factor evaluated along any of the element edges associated with geometric edges or faces. The geometric deviation factor along an element edge is calculated by dividing the maximum gap between the element edge and its associated geometry by the length of the element edge. Elements with a geometric deviation factor larger than the specified threshold will fail this test.

  - LARGE_ANGLE

    The largest corner angle on any of an element's faces. Elements with face angles larger than the specified threshold (in degrees) will fail this test.

  - LONGEST_EDGE

    The length of an element's longest edge. Elements with an edge longer than the specified threshold will fail this test.

  - MAX_FREQUENCY

    An estimate of an element's contribution to the initial maximum allowable frequency for Abaqus/Standard analyses. This calculation requires appropriate section assignments and material definitions. Elements whose maximum allowable frequency is smaller than the given value will fail this test.

  - SHAPE_FACTOR

    The shape factor for triangular and tetrahedral elements. This is the ratio between the element area or volume and the optimal element area or volume. Elements with a shape factor smaller than the specified threshold will fail this test.

  - SHORTEST_EDGE

    The length of an element's shortest edge. Elements with an edge shorter than the specified threshold will fail this test.

  - SMALL_ANGLE

    The smallest corner angle on any of an element's faces. Elements with face angles smaller than the given value (in degrees) will fail this test.

  - STABLE_TIME_INCREMENT

    An estimate of an element's contribution to the initial maximum stable time increment for Abaqus/Explicit analyses. This calculation requires appropriate section assignments and material definitions. Elements that require a time increment smaller than the given value will fail this test.

### Optional arguments

- *threshold*

  A Float value used to determine low quality elements according to the specified criterion. This argument is ignored when the ANALYSIS_CHECKS criterion is used. For other criterion, if this argument is unspecified then no list of failed elements will be returned.

- *elemShape*

  A SymbolicConstant specifying an element shape for limiting the query. Possible values are LINE, QUAD, TRI, HEX, WEDGE, and TET.

- *regions*

  A sequence of [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) or [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects. If you do not specify the *regions* argument, all meshes in the assembly are considered.

### Return value

A Dictionary object containing values for some number of the following keys: failedElements, warningElements, naElements (sequences of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects); numElements (Int); average, worst (Float); worstElement ([MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) object)

### Exceptions

None.