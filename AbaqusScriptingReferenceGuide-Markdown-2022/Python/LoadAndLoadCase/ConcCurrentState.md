# ConcCurrentState object

The ConcCurrentState object stores the propagating data of a concentrated current in a step. One instance of this object is created internally by the [ConcCurrent](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-conccurrentpyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [ConcCurrent](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-conccurrentpyc.htm?ContextScope=all) object.

The ConcCurrentState object has no constructor or methods.

The ConcCurrentState object is derived from the [LoadState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].steps[name].loadStates[name]
```

## Members

The ConcCurrentState object has the following members:

- *magnitude*

  A Float specifying the load magnitude.

- *magnitudeState*

  A SymbolicConstant specifying the propagation state of the load magnitude. Possible values are UNSET, SET, UNCHANGED, and FREED.

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

- [CECURRENT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-cecurrent.htm?ContextScope=all#simakey-r-cecurrent)