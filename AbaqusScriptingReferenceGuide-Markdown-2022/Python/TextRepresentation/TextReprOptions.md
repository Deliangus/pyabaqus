# TextReprOptions object

The TextReprOptions object is used to configure the output of the Python `str()` command within Abaqus/CAE. (The `str()` command is used by the Python print function.) The TextReprOptions object stores the various settings that determine how objects are printed on the Python command line.

The TextReprOptions object has no constructor. Abaqus creates the *textReprOptions* member when a session is started.

## Access

```
import textRepr
textReprOptions
session.textReprOptions
```

## setValues(...)



This method modifies the TextReprOptions object.



### Required arguments

None.

### Optional arguments

- *style*

  A SymbolicConstant specifying the style of the text representation. Possible values are:RECURSIVE: return a recursive representation of the object.SIMPLE: return a String representing the object as either 'interface object', 'dictionary object', or 'sequence object'.The initial value is RECURSIVE.

- *maxRecursionDepth*

  An Int, SymbolicConstant, or None specifying the maximum depth to which the object will be printed. Possible values for the depth are Ints ≥≥ 0, the SymbolicConstant UNLIMITED, or None. A value of None implies that the current setting in the TextReprOptions object will be used. If *object* is not an Abaqus object, *maxRecursionDepth* has no effect. The default value is None.

- *maxRecursionString*

  A String specifying the string to be returned when the maximum depth of recursion is reached. The string can include a format specifier (%s), which will be substituted by the object type. The initial value is '%s object'.

- *maxElementsInSequence*

  An Int or the SymbolicConstant UNLIMITED specifying the maximum number of elements of a sequence to return. Possible values are UNLIMITED or Ints >> 0. The initial value is 100. After the maximum number of elements, the remainder are indicated by the string '...'.

### Return value

None.

### Exceptions

None.



## Members

The TextReprOptions object has members with the same names and descriptions as the arguments to the [setValues](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-txttextrepoppyc.htm?ContextScope=all#simaker-txttextrepopsetvaluespyc) method.