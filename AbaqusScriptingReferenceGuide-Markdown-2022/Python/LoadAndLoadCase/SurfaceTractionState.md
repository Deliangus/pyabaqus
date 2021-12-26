# SurfaceTractionState object

The SurfaceTractionState object stores the propagating data for a [SurfaceTraction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetractionpyc.htm?ContextScope=all) object in a step. One instance of this object is created internally by the [SurfaceTraction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetractionpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [SurfaceTraction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetractionpyc.htm?ContextScope=all) object.

The SurfaceTractionState object has no constructor or methods.

The SurfaceTractionState object is derived from the [LoadState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].loadStates[name]
```

## Members

The SurfaceTractionState object has the following members:

- *magnitude*

  A Float or a Complex specifying the load magnitude.

- *magnitudeState*

  A SymbolicConstant specifying the propagation state of the load magnitude. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

- *amplitudeState*

  A SymbolicConstant specifying the propagation state of the *amplitude* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *status*

  A SymbolicConstant specifying the propagation state of the [LoadState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?ContextScope=all) object. Possible values are:

  - NOT_YET_ACTIVE
  - CREATED
  - PROPAGATED
  - MODIFIED
  - DEACTIVATED
  - NO_LONGER_ACTIVE
  - TYPE_NOT_APPLICABLE
  - INSTANCE_NOT_APPLICABLE
  - BUILT_INTO_BASE_STATE

- *amplitude*

  A String specifying the name of the amplitude reference. The String is empty if the load has no amplitude reference.



## Corresponding analysis keywords

- [DSLOAD](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-dsload.htm?ContextScope=all#simakey-r-dsload)
- [DLOAD](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-dload.htm?ContextScope=all#simakey-r-dload)