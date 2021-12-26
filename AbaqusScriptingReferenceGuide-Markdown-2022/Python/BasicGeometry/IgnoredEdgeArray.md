# IgnoredEdgeArray object

The IgnoredEdgeArray is a sequence of [IgnoredEdge](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignorededgepyc.htm?ContextScope=all) objects. If the part is modified, then IgnoredEdgeArray must be updated for that part.

## Access

```
import part
mdb.models[name].parts[name].ignoredEdges
import assembly
mdb.models[name].rootAssembly.allInstances[name].ignoredEdges
mdb.models[name].rootAssembly.instances[name].ignoredEdges
```

## findAt(...)



This method returns the object or objects in the IgnoredEdgeArray located at the given coordinates.

findAt initially uses the ACIS tolerance of 1E-6. As a result, findAt returns any [IgnoredEdge](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignorededgepyc.htm?ContextScope=all) that is at the arbitrary point specified or at a distance of less than 1E-6 from the arbitrary point. If nothing is found, findAt uses the tolerance for imprecise geometry (applicable only for imprecise geometric entities). The arbitrary point must not be shared by a second [IgnoredEdge](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignorededgepyc.htm?ContextScope=all). If two [IgnoredEdge](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignorededgepyc.htm?ContextScope=all) objects intersect or coincide at the arbitrary point, findAt chooses the first [IgnoredEdge](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignorededgepyc.htm?ContextScope=all) that it encounters, and you should not rely on the return value being consistent.

findAt will always try to find objects among all the ignored edges in the part or assembly instance and will not restrict itself to a subset even if the IgnoredEdgeArray represents such subset.



### Required arguments

- *coordinates*

  A sequence of Floats specifying the *X*-, *Y*-, and *Z*-coordinates of the object to find.findAt returns either an [IgnoredEdge](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignorededgepyc.htm?ContextScope=all) object or a sequence of [IgnoredEdge](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignorededgepyc.htm?ContextScope=all) objects based on the type of input.If *coordinates* is a sequence of Floats, findAt returns the [IgnoredEdge](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignorededgepyc.htm?ContextScope=all) object at that point.If you omit the *coordinates* keyword argument, findAt accepts as arguments a sequence of sequence of floats in the following format:`ignoredEdges = e.findAt(((20.19686, -169.513997, 27.798593), ),                        ((19.657627, -167.295749, 27.056402), ),                        ((18.274129, -157.144741, 25.15218), ))`

### Optional arguments

- *printWarning*

  A Boolean specifying whether a message is to be printed to the CLI if no entity is found at the specified location. The default value is True.

### Return value

An [IgnoredEdge](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignorededgepyc.htm?ContextScope=all) object or a sequence of [IgnoredEdge](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignorededgepyc.htm?ContextScope=all) objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getSequenceFromMask(...)



This method returns the object or objects in the IgnoredEdgeArray identified using the specified *mask*. This command is generated when the [JournalOptions](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-journaloptionspyc.htm?ContextScope=all) are set to COMPRESSEDINDEX. When large number of objects are involved, this method is highly efficient.



### Required arguments

- *mask*

  A String specifying the object or objects.

### Optional arguments

None.

### Return value

An [IgnoredEdge](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignorededgepyc.htm?ContextScope=all) object or a sequence of [IgnoredEdge](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignorededgepyc.htm?ContextScope=all) objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getMask()



This method returns a string specifying the object or objects.



### Arguments

None.

### Return value

A String specifying the object or objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getClosest(...)



This method returns a object or objects in the IgnoredEdgeArray closest to the given set of points, where the given points need not lie on the edges in the IgnoredEdgeArray.



### Required arguments

- *coordinates*

  A sequence of a sequence of floats, where each sequence of floats describes the *X*-, *Y*-, and *Z*-coordinates of a point.`r=e.getClosest(coordinates=((20.0,20.0,10.0),(-1.0, -15.0, 15),))``r.keys()``[0, 1]``r[0]``(mdb.models['Model-1'].parts['Part-1'].ignoredEdges[3],                                 (15.7090625762939, 20.0, 10.0))`

### Optional arguments

- *searchTolerance*

  A double specifying the distance within which the closest object must lie. The default value is half of the parent part/instance size.

### Return value

This method returns a dictionary object. The key to the dictionary object is the position of the input point in the tuple specified in the *coordinates* starting at index 0. If a closest [IgnoredEdge](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignorededgepyc.htm?ContextScope=all) could be found then the value is a sequence consisting of two objects. The first object in the sequence is an [IgnoredEdge](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignorededgepyc.htm?ContextScope=all) that is close to the input point referred to by the key. The second object in the sequence, is a sequence of floats which specify the *X*-, *Y*-, and *Z*-location of the closest point on the [IgnoredEdge](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignorededgepyc.htm?ContextScope=all) to the given point. See program listing above.

### Exceptions

- An exception occurs if the resulting sequence is empty.

  Error: The mask results in an empty sequence

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The IgnoredEdgeArray object has no members.