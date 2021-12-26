# PredefinedFieldState object

The PredefinedFieldState object is the base object for the objects in the predefinedFieldState repository of the [Step](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-steppyc.htm?ContextScope=all) object. The members of the PredefinedFieldState object are common to all objects derived from PredefinedFieldState.

The PredefinedFieldState object has no constructor or methods.

## Access

```
import load
mdb.models[name].steps[name].predefinedFieldStates[name]
```

## Members

The PredefinedFieldState object has the following member:

- *status*

  A SymbolicConstant specifying the propagation state of the PredefinedFieldState object. Possible values are:

  - NOT_YET_ACTIVE
  - CREATED
  - PROPAGATED
  - MODIFIED
  - DEACTIVATED
  - DEACTIVATED_TO_INITIAL
  - NO_LONGER_ACTIVE
  - RESET_TO_INITIAL
  - TO_BE_COMPUTED
  - PROPAGATED_FROM_COMPUTED
  - BUILT_INTO_BASE_STATE
  - TYPE_NOT_APPLICABLE
  - INSTANCE_NOT_APPLICABLE

  This member exists in all PredefinedFieldState objects, but different predefined fields use different subsets of the entire list of possible values depending on propagation rules.