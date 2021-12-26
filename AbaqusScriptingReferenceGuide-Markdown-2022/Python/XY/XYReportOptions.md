# XYReportOptions object

The XYReportOptions object stores settings used by the writeXYReport method when you write an [XYData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xydatapyc.htm?ContextScope=all) object to an ASCII file. The XYReportOptions object has no constructor. Abaqus creates the *xyReportOptions* member when you import the Visualization module.

## Access

```
import visualization
session.defaultXYReportOptions
session.xyReportOptions
```

## setValues(...)



This method modifies the XYReportOptions object.



### Required arguments

None.

### Optional arguments

- *pageWidth*

  An Int specifying the number of characters per line of the report file when *pageWidthLimited*=ON. Possible values are *pageWidth* >> 0. The default value is 80.

- *numDigits*

  An Int specifying the number of significant digits to be included for each data value in the report file. Possible values are 0 ≤≤ *numDigits* ≤≤ 9. The default value is 6.

- *interpolation*

  A Boolean specifying whether to perform linear interpolation for missing data values. The default value is OFF.

- *xyData*

  A Boolean specifying whether to print the *X*- and *Y*-values of the selected XYData objects. (If *xyData*=OFF, *totals* and *minMax* can still be printed.) The default value is ON.

- *totals*

  A Boolean specifying whether to print the sum of the *Y*-values of the selected XYData objects. The default value is OFF.

- *minMax*

  A Boolean specifying whether to print the minimum and maximum *X*- and *Y*-values of the selected XYData objects. The default value is OFF.

- *pageWidthLimited*

  A Boolean specifying whether the page width is limited. The default value is OFF.

- *numberFormat*

  A SymbolicConstant specifying the number format to be used in reporting XYData objects. Possible values are AUTOMATIC, ENGINEERING, and SCIENTIFIC. The default value is ENGINEERING.

- *layout*

  A SymbolicConstant specifying the format used in reporting the XYData objects. Possible values are SINGLE_TABLE and SEPARATE_TABLES. The default value is SINGLE_TABLE.

### Return value

None.

### Exceptions

RangeError.

- If *xyData*, *total*, and *minMax* are all OFF:

  At least one of the data print methods must be selected



## Members

The XYReportOptions object has members with the same names and descriptions as the arguments to the [setValues ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xyreportoptionspyc.htm?ContextScope=all#simaker-xyreportoptionssetvaluespyc)method.