# textRepr module

The Python module textRepr contains functions to print an Abaqus object and to convert the output from the str() function into a formatted string, indented for each object in the recursive listing of a Python object.

## Access

```
import textRepr
```

## getIndentedRepr(...)



This method returns a String with each level of parentheses indented.



### Required arguments

- *object*

  A Python object to be processed. (The Python object can be an Abaqus object.) This argument can also be a String representation of a Python object obtained from str(*object*).

### Optional arguments

- *maxRecursionDepth*

  An Int specifying the maximum depth to which the object will be printed, the SymbolicConstant UNLIMITED, or None. A value of None implies that the current setting in the TextReprOptions object will be used. If *object* is not an Abaqus object, *maxRecursionDepth* has no effect. The default value is None.You should take care when setting *maxRecursionDepth*=UNLIMITED because the resulting output can be very large. To limit the output, you should set *maxElementsInSequence* to a small number.

- *maxElementsInSequence*

  An Int specifying the maximum number of elements of a sequence to return or the SymbolicConstant UNLIMITED. The initial value is 100. After the maximum number of elements have been printed, the remainder are indicated by the string '...'.

- *significantDigits*

  An Int specifying the number of significant digits for Floats in the output. Possible values are 0 << *significantDigits* ≤≤ 15. The default value is 6.

### Return value

A String.

### Exceptions

None.



## getPaths(...)



This method processes the argument and interprets its structure. It then returns a String containing the object paths of all the child objects found.



### Required arguments

- *object*

  A Python object to be processed. (The Python object can be an Abaqus object.) This argument can also be a String representation of a Python object.

### Optional arguments

- *maxRecursionDepth*

  An Int specifying the maximum depth to which the object will be printed, the SymbolicConstant UNLIMITED, or None. A value of None implies that the current setting in the TextReprOptions object will be used. If *object* is not an Abaqus object, *maxRecursionDepth* has no effect. The default value is None.You should take care when setting *maxRecursionDepth*=UNLIMITED because the resulting output can be very large. To limit the output, you should set *maxElementsInSequence* to a small number.

- *maxElementsInSequence*

  An Int specifying the maximum number of elements of a sequence to return or the SymbolicConstant UNLIMITED. The initial value is 100. After the maximum number of elements have been printed, the remainder are indicated by the string '...'.

- *pathRoot*

  A String specifying the root of the paths. This String is prepended to each path found. The default value is None, implying that the path to *object* will be used unless *object* is a String.

### Return value

A String.

### Exceptions

None.



## getTypes(...)



This method processes the argument, interprets its structure, and returns a String containing all the object types within the object in the form '*TypeName* *Path*'.



### Required arguments

- *object*

  An Abaqus object.

### Optional arguments

- *maxRecursionDepth*

  An Int specifying the maximum depth to which the object will be printed, the SymbolicConstant UNLIMITED, or None. A value of None implies that the current setting in the TextReprOptions object will be used. The default value is None.You should take care when setting *maxRecursionDepth*=UNLIMITED because the resulting output can be very large. To limit the output, you should set *maxElementsInSequence* to a small number.

- *maxElementsInSequence*

  An Int specifying the maximum number of elements of a sequence to return or the SymbolicConstant UNLIMITED. The initial value is 100. After the maximum number of elements have been printed, the remainder are indicated by the string '...'.

- *pathRoot*

  A String specifying the root of the paths. This String is prepended to each path found. The default value is None, implying that the path to *object* will be used unless *object* is a String.

### Return value

A String.

### Exceptions

None.



## prettyPrint(...)



This method prints a formatted version of the object. The prettyPrint function uses getIndentedRepr to format the String representation, but does not save the full text output of getIndentedRepr. Therefore this function can be used in cases where getIndentedRepr would run out of memory.



### Required arguments

- *object*

  An Abaqus object.

### Optional arguments

- *maxRecursionDepth*

  An Int specifying the maximum depth to which the object will be printed, the SymbolicConstant UNLIMITED, or None. A value of None implies that the current setting in the TextReprOptions object will be used. The default value is None.You should take care when setting *maxRecursionDepth*=UNLIMITED because the resulting output can be very large. To limit the output, you should set *maxElementsInSequence* to a small number.

- *maxElementsInSequence*

  An Int specifying the maximum number of elements of a sequence to return or the SymbolicConstant UNLIMITED. The initial value is 100. After the maximum number of elements have been printed, the remainder are indicated by the string '...'.

- *significantDigits*

  An Int specifying the number of significant digits for Floats in the output. Possible values are 0 << *significantDigits* ≤≤ 15. The default value is 6.

### Return value

None.

### Exceptions

None.



## printPaths(...)



This method prints the object path of the *object* argument and its members, depending on the *maxRecursionDepth* argument. The printPaths function uses getPaths to print a list of paths to each of the child objects in *object*.



### Required arguments

- *object*

  An Abaqus object. This argument can also be a String representation of an Abaqus object obtained from str(*object*).

### Optional arguments

- *maxRecursionDepth*

  An Int specifying the maximum depth to which the object will be printed, the SymbolicConstant UNLIMITED, or None. A value of None implies that the current setting in the TextReprOptions object will be used. The default value is None.You should take care when setting *maxRecursionDepth*=UNLIMITED because the resulting output can be very large. To limit the output, you should set *maxElementsInSequence* to a small number.

- *maxElementsInSequence*

  An Int specifying the maximum number of elements of a sequence to return or the SymbolicConstant UNLIMITED. The initial value is 100. After the maximum number of elements have been printed, the remainder are indicated by the string '...'.

- *pathRoot*

  A String specifying the root of the paths to be printed. This String is prepended to each path found. The default value is None, implying that the path to *object* will be used.

### Return value

None.

### Exceptions

None.



## printTypes(...)



This method prints the object type. The printTypes function uses getTypes to print a list of all the object types in *object*.



### Required arguments

- *object*

  An Abaqus object.

### Optional arguments

- *maxRecursionDepth*

  An Int specifying the maximum depth to which the object will be printed, the SymbolicConstant UNLIMITED, or None. A value of None implies that the current setting in the TextReprOptions object will be used. The default value is None.You should take care when setting *maxRecursionDepth*=UNLIMITED because the resulting output can be very large. To limit the output, you should set *maxElementsInSequence* to a small number.

- *maxElementsInSequence*

  An Int specifying the maximum number of elements of a sequence to return or the SymbolicConstant UNLIMITED. The initial value is 100. After the maximum number of elements have been printed, the remainder are indicated by the string '...'.

- *pathRoot*

  A String specifying the root of the paths to be printed. This String is prepended to each path found. The default value is None, implying that the path to *object* will be used.

### Return value

None.

### Exceptions

None.