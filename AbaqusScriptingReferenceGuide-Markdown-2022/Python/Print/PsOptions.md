# PsOptions object

The PsOptions object stores the settings that Abaqus uses when printing using PostScript format. The PsOptions object has no constructor. Abaqus creates the *psOptions* member when a session is started.

## Access

```
session.psOptions
```

## setValues(...)



This method modifies the PsOptions object.



### Required arguments

None.

### Optional arguments

- *paperSize*

  A SymbolicConstant specifying the paper size. Possible values are:

  - LETTER
  - LEGAL
  - LEDGER
  - A0
  - A1
  - A2
  - A3
  - A4
  - A5

  The default value is LETTER.

- *topMargin*

  A Float specifying the top margin of the paper in inches. Possible values are *topMargin* ≥≥ 0. The default value is 0.5.

- *bottomMargin*

  A Float specifying the bottom margin of the paper in inches. Possible values are *bottomMargin* ≥≥ 0. The default value is 0.5.

- *leftMargin*

  A Float specifying the left margin of the paper in inches. Possible values are *leftMargin* ≥≥ 0. The default value is 0.5.

- *rightMargin*

  A Float specifying the right margin of the paper in inches. Possible values are *rightMargin* ≥≥ 0. The default value is 0.5.

- *orientation*

  A SymbolicConstant specifying the orientation of the image. Possible values are PORTRAIT and LANDSCAPE. The default value is PORTRAIT.

- *logo*

  A Boolean specifying whether the output includes the Abaqus logo. The default value is ON.

- *date*

  A Boolean specifying whether the output includes the date. The default value is ON.

- *resolution*

  A SymbolicConstant specifying the resolution of the image in dots per inch (dpi). The *resolution* can be DPI_1200 only if *imageFormat* = VECTOR. Possible values are DPI_75, DPI_150, DPI_300, DPI_450, DPI_600, and DPI_1200. The default value is DPI_150.

- *fontType*

  A SymbolicConstant specifying the PostScript font substitution rules to be applied. Possible values are PS_ALWAYS, PS_IF_AVAILABLE, and AS_DISPLAYED. The default value is PS_IF_AVAILABLE.

- *imageFormat*

  A SymbolicConstant specifying how the viewport display will be represented. Possible values are VECTOR and RASTER. The default value is VECTOR.

- *shadingQuality*

  A SymbolicConstant specifying how fine the shading of curved surfaces will be for vector images. Possible values are EXTRA COARSE, COARSE, MEDIUM, FINE, and EXTRA FINE. The default value is MEDIUM.

### Return value

None.

### Exceptions

RangeError.

Note:The minimum value of width and height (*minWidth* and *minHeight*) is 10 mm (approximately 0.4 inches).



- If *leftMargin* + *rightMargin* is out of range:

  RangeError: leftMargin and rightMargin must produce image width >= minWidth

- If *topMargin* + *bottomMargin* is out of range:

  RangeError: topMargin and bottomMargin must produce image height >= minHeight



## Members

The PsOptions object has members with the same names and descriptions as the arguments to the [setValues ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-psoptionspyc.htm?ContextScope=all#simaker-psoptionssetvaluespyc)method.