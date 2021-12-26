# DamageInitiation object

The DamageInitiation object specifies material properties to define the initiation of damage.

## Access

```
import material
mdb.models[name].materials[name].ductileDamageInitiation
mdb.models[name].materials[name].fldDamageInitiation
mdb.models[name].materials[name].flsdDamageInitiation
mdb.models[name].materials[name].hashinDamageInitiation
mdb.models[name].materials[name].johnsonCookDamageInitiation
mdb.models[name].materials[name].maxeDamageInitiation
mdb.models[name].materials[name].maxpeDamageInitiation
mdb.models[name].materials[name].maxpsDamageInitiation
mdb.models[name].materials[name].maxsDamageInitiation
mdb.models[name].materials[name].mkDamageInitiation
mdb.models[name].materials[name].msfldDamageInitiation
mdb.models[name].materials[name].quadeDamageInitiation
mdb.models[name].materials[name].quadsDamageInitiation
mdb.models[name].materials[name].shearDamageInitiation
import odbMaterial
session.odbs[name].materials[name].ductileDamageInitiation
session.odbs[name].materials[name].fldDamageInitiation
session.odbs[name].materials[name].flsdDamageInitiation
session.odbs[name].materials[name].hashinDamageInitiation
session.odbs[name].materials[name].johnsonCookDamageInitiation
session.odbs[name].materials[name].maxeDamageInitiation
session.odbs[name].materials[name].maxpeDamageInitiation
session.odbs[name].materials[name].maxpsDamageInitiation
session.odbs[name].materials[name].maxsDamageInitiation
session.odbs[name].materials[name].mkDamageInitiation
session.odbs[name].materials[name].msfldDamageInitiation
session.odbs[name].materials[name].quadeDamageInitiation
session.odbs[name].materials[name].quadsDamageInitiation
session.odbs[name].materials[name].shearDamageInitiation
```

## DuctileDamageInitiation(...)



This method creates a DamageInitiation object.



### Path

```
mdb.models[name].materials[name].DuctileDamageInitiation
session.odbs[name].materials[name].DuctileDamageInitiation
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described in the "Table data" section.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the damage initiation definition. Possible values are FLD and MSFLD. The default value is MSFLD.

- *feq*

  A Float specifying the critical value of the deformation severity index for equivalent plastic strains. The default value is 10.0.

- *fnn*

  A Float specifying the critical value of the deformation severity index for strains normal to the groove direction. The default value is 10.0.

- *fnt*

  A Float specifying the critical value of the deformation severity index for shear strains. The default value is 10.0.

- *frequency*

  An Int specifying the frequency, in increments, at which the Marciniak-Kuczynski analysis is going to be performed. The default value is 1.

- *ks*

  A Float specifying the value of Ks. The default value is 0.0.

- *numberImperfections*

  An Int specifying the number of imperfections to be considered for the evaluation of the Marciniak-Kuczynski analysis. These imperfections are assumed to be equally spaced in the angular direction. The default value is 4.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *alpha*

  A Float specifying the value of the coefficient that will multiply the shear contribution to the Hashin's fiber initiation criterion. The default value is 0.0.

- *omega*

  A Float specifying the factor used for filtering the ratio of principal strain rates used for the evaluation of the MSFLD damage initiation criterion. The default value is 1.0.

- *tolerance*

  A Float specifying the tolerance within which the damage initiation criterion must be satisfied. The default value is 0.05.

- *direction*

  A SymbolicConstant specifying the damage initiation direction. Possible values are NMORI and TMORI. The default value is NMORI.

### Table data

If constructor is DuctileDamageInitiation, the table data specify the following:

- Equivalent fracture strain at damage initiation.
- Stress triaxiality.
- Strain rate.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If constructor is FldDamageInitiation, the table data specify the following:

- Major principal strain at damage initiation.
- Minor principal strain.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If constructor FlsdDamageInitiation, the table data specify the following:

- Major principal stress at damage initiation.
- Minor principal stress.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If constructor is JohnsonCookDamageInitiation, the table data specify the following:

- Johnson-Cook failure parameter D1.
- Johnson-Cook failure parameter D2.
- Johnson-Cook failure parameter D3.
- Johnson-Cook failure parameter D4.
- Johnson-Cook failure parameter D5.
- Melting temperature.
- Transition temperature.
- Reference strain rate.

If constructor MkDamageInitiation, the table data specify the following:

- Flaw size relative to nominal thickness of the section.
- Angle (in degrees) with respect to the 1-direction of the local material orientation.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If constructor is MsfldDamageInitiation and *definition*=MSFLD, the table data specify the following:

- Nominal strain at damage initiation in a normal-only mode.
- Equivalent plastic strain at initiation of localized necking.
- Ratio of minor to major principal strains.
- Equivalent plastic strain rate.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If constructor is MsfldDamageInitiation and *definition*=FLD, the table data specify the following:

- Major principal strain at initiation of localized necking.
- Equivalent plastic strain at initiation of localized necking.
- Ratio of minor to major principal strains.
- Equivalent plastic strain rate.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If constructor is QuadeDamageInitiation or MaxeDamageInitiation, the table data specify the following:

- Nominal strain at damage initiation in a normal-only mode.
- Nominal strain at damage initiation in a shear-only mode that involves separation only along the first shear direction.
- Nominal strain at damage initiation in a shear-only mode that involves separation only along the second shear direction.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If constructor is QuadsDamageInitiation or MaxsDamageInitiation, the table data specify the following:

- Nominal strain at damage initiation in a normal-only mode.
- Nominal strain at damage initiation in a shear-only mode that involves separation only along the first shear direction.
- Nominal strain at damage initiation in a shear-only mode that involves separation only along the second shear direction.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If constructor is MaxpeDamageInitiation, the table data specify the following:

- Maximum principal strain at damage initiation.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If constructor is MaxpsDamageInitiation, the table data specify the following:

- Maximum principal stress at damage initiation.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If constructor is ShearDamageInitiation, the table data specify the following:

- Equivalent fracture strain at damage initiation.
- Shear stress ratio.
- Strain rate.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If constructor is HashinDamageInitiation, the table data specify the following:

- Fiber tensile strength.
- Fiber compressive strength.
- Matrix tensile strength.
- Matrix compressive strength.
- Longitudinal shear strength.
- Transverse shear strength.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A DamageInitiation object.

### Exceptions

RangeError.



## FldDamageInitiation(...)



This method creates a DamageInitiation object.



### Path

```
mdb.models[name].materials[name].FldDamageInitiation
session.odbs[name].materials[name].FldDamageInitiation
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described in the "Table data" section.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the damage initiation definition. Possible values are FLD and MSFLD. The default value is MSFLD.

- *feq*

  A Float specifying the critical value of the deformation severity index for equivalent plastic strains. The default value is 10.0.

- *fnn*

  A Float specifying the critical value of the deformation severity index for strains normal to the groove direction. The default value is 10.0.

- *fnt*

  A Float specifying the critical value of the deformation severity index for shear strains. The default value is 10.0.

- *frequency*

  An Int specifying the frequency, in increments, at which the Marciniak-Kuczynski analysis is going to be performed. The default value is 1.

- *ks*

  A Float specifying the value of Ks. The default value is 0.0.

- *numberImperfections*

  An Int specifying the number of imperfections to be considered for the evaluation of the Marciniak-Kuczynski analysis. These imperfections are assumed to be equally spaced in the angular direction. The default value is 4.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *alpha*

  A Float specifying the value of the coefficient that will multiply the shear contribution to the Hashin's fiber initiation criterion. The default value is 0.0.

- *omega*

  A Float specifying the factor used for filtering the ratio of principal strain rates used for the evaluation of the MSFLD damage initiation criterion. The default value is 1.0.

- *tolerance*

  A Float specifying the tolerance within which the damage initiation criterion must be satisfied. The default value is 0.05.

- *direction*

  A SymbolicConstant specifying the damage initiation direction. Possible values are NMORI and TMORI. The default value is NMORI.

### Return value

A DamageInitiation object.

### Exceptions

RangeError.



## FlsdDamageInitiation(...)



This method creates a DamageInitiation object.



### Path

```
mdb.models[name].materials[name].FlsdDamageInitiation
session.odbs[name].materials[name].FlsdDamageInitiation
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described in the "Table data" section.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the damage initiation definition. Possible values are FLD and MSFLD. The default value is MSFLD.

- *feq*

  A Float specifying the critical value of the deformation severity index for equivalent plastic strains. The default value is 10.0.

- *fnn*

  A Float specifying the critical value of the deformation severity index for strains normal to the groove direction. The default value is 10.0.

- *fnt*

  A Float specifying the critical value of the deformation severity index for shear strains. The default value is 10.0.

- *frequency*

  An Int specifying the frequency, in increments, at which the Marciniak-Kuczynski analysis is going to be performed. The default value is 1.

- *ks*

  A Float specifying the value of Ks. The default value is 0.0.

- *numberImperfections*

  An Int specifying the number of imperfections to be considered for the evaluation of the Marciniak-Kuczynski analysis. These imperfections are assumed to be equally spaced in the angular direction. The default value is 4.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *alpha*

  A Float specifying the value of the coefficient that will multiply the shear contribution to the Hashin's fiber initiation criterion. The default value is 0.0.

- *omega*

  A Float specifying the factor used for filtering the ratio of principal strain rates used for the evaluation of the MSFLD damage initiation criterion. The default value is 1.0.

- *tolerance*

  A Float specifying the tolerance within which the damage initiation criterion must be satisfied. The default value is 0.05.

- *direction*

  A SymbolicConstant specifying the damage initiation direction. Possible values are NMORI and TMORI. The default value is NMORI.

### Return value

A DamageInitiation object.

### Exceptions

RangeError.



## JohnsonCookDamageInitiation(...)



This method creates a DamageInitiation object.



### Path

```
mdb.models[name].materials[name].JohnsonCookDamageInitiation
session.odbs[name].materials[name].JohnsonCookDamageInitiation
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described in the "Table data" section.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the damage initiation definition. Possible values are FLD and MSFLD. The default value is MSFLD.

- *feq*

  A Float specifying the critical value of the deformation severity index for equivalent plastic strains. The default value is 10.0.

- *fnn*

  A Float specifying the critical value of the deformation severity index for strains normal to the groove direction. The default value is 10.0.

- *fnt*

  A Float specifying the critical value of the deformation severity index for shear strains. The default value is 10.0.

- *frequency*

  An Int specifying the frequency, in increments, at which the Marciniak-Kuczynski analysis is going to be performed. The default value is 1.

- *ks*

  A Float specifying the value of Ks. The default value is 0.0.

- *numberImperfections*

  An Int specifying the number of imperfections to be considered for the evaluation of the Marciniak-Kuczynski analysis. These imperfections are assumed to be equally spaced in the angular direction. The default value is 4.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *alpha*

  A Float specifying the value of the coefficient that will multiply the shear contribution to the Hashin's fiber initiation criterion. The default value is 0.0.

- *omega*

  A Float specifying the factor used for filtering the ratio of principal strain rates used for the evaluation of the MSFLD damage initiation criterion. The default value is 1.0.

- *tolerance*

  A Float specifying the tolerance within which the damage initiation criterion must be satisfied. The default value is 0.05.

- *direction*

  A SymbolicConstant specifying the damage initiation direction. Possible values are NMORI and TMORI. The default value is NMORI.

### Return value

A DamageInitiation object.

### Exceptions

RangeError.



## MaxeDamageInitiation(...)



This method creates a DamageInitiation object.



### Path

```
mdb.models[name].materials[name].MaxeDamageInitiation
session.odbs[name].materials[name].MaxeDamageInitiation
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described in the "Table data" section.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the damage initiation definition. Possible values are FLD and MSFLD. The default value is MSFLD.

- *feq*

  A Float specifying the critical value of the deformation severity index for equivalent plastic strains. The default value is 10.0.

- *fnn*

  A Float specifying the critical value of the deformation severity index for strains normal to the groove direction. The default value is 10.0.

- *fnt*

  A Float specifying the critical value of the deformation severity index for shear strains. The default value is 10.0.

- *frequency*

  An Int specifying the frequency, in increments, at which the Marciniak-Kuczynski analysis is going to be performed. The default value is 1.

- *ks*

  A Float specifying the value of Ks. The default value is 0.0.

- *numberImperfections*

  An Int specifying the number of imperfections to be considered for the evaluation of the Marciniak-Kuczynski analysis. These imperfections are assumed to be equally spaced in the angular direction. The default value is 4.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *alpha*

  A Float specifying the value of the coefficient that will multiply the shear contribution to the Hashin's fiber initiation criterion. The default value is 0.0.

- *omega*

  A Float specifying the factor used for filtering the ratio of principal strain rates used for the evaluation of the MSFLD damage initiation criterion. The default value is 1.0.

- *tolerance*

  A Float specifying the tolerance within which the damage initiation criterion must be satisfied. The default value is 0.05.

- *direction*

  A SymbolicConstant specifying the damage initiation direction. Possible values are NMORI and TMORI. The default value is NMORI.

- *position*

  An SymbolicConstant specifying the damage initiation position. Possible values are CENTROID, CRACKTIP and COMBINED. The default value is CENTROID.

### Return value

A DamageInitiation object.

### Exceptions

RangeError.



## MaxsDamageInitiation(...)



This method creates a DamageInitiation object.



### Path

```
mdb.models[name].materials[name].MaxsDamageInitiation
session.odbs[name].materials[name].MaxsDamageInitiation
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described in the "Table data" section.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the damage initiation definition. Possible values are FLD and MSFLD. The default value is MSFLD.

- *feq*

  A Float specifying the critical value of the deformation severity index for equivalent plastic strains. The default value is 10.0.

- *fnn*

  A Float specifying the critical value of the deformation severity index for strains normal to the groove direction. The default value is 10.0.

- *fnt*

  A Float specifying the critical value of the deformation severity index for shear strains. The default value is 10.0.

- *frequency*

  An Int specifying the frequency, in increments, at which the Marciniak-Kuczynski analysis is going to be performed. The default value is 1.

- *ks*

  A Float specifying the value of Ks. The default value is 0.0.

- *numberImperfections*

  An Int specifying the number of imperfections to be considered for the evaluation of the Marciniak-Kuczynski analysis. These imperfections are assumed to be equally spaced in the angular direction. The default value is 4.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *alpha*

  A Float specifying the value of the coefficient that will multiply the shear contribution to the Hashin's fiber initiation criterion. The default value is 0.0.

- *omega*

  A Float specifying the factor used for filtering the ratio of principal strain rates used for the evaluation of the MSFLD damage initiation criterion. The default value is 1.0.

- *tolerance*

  A Float specifying the tolerance within which the damage initiation criterion must be satisfied. The default value is 0.05.

- *direction*

  A SymbolicConstant specifying the damage initiation direction. Possible values are NMORI and TMORI. The default value is NMORI.

- *position*

  An SymbolicConstant specifying the damage initiation position. Possible values are CENTROID, CRACKTIP and COMBINED. The default value is CENTROID.

### Return value

A DamageInitiation object.

### Exceptions

RangeError.



## MkDamageInitiation(...)



This method creates a DamageInitiation object.



### Path

```
mdb.models[name].materials[name].MkDamageInitiation
session.odbs[name].materials[name].MkDamageInitiation
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described in the "Table data" section.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the damage initiation definition. Possible values are FLD and MSFLD. The default value is MSFLD.

- *feq*

  A Float specifying the critical value of the deformation severity index for equivalent plastic strains. The default value is 10.0.

- *fnn*

  A Float specifying the critical value of the deformation severity index for strains normal to the groove direction. The default value is 10.0.

- *fnt*

  A Float specifying the critical value of the deformation severity index for shear strains. The default value is 10.0.

- *frequency*

  An Int specifying the frequency, in increments, at which the Marciniak-Kuczynski analysis is going to be performed. The default value is 1.

- *ks*

  A Float specifying the value of Ks. The default value is 0.0.

- *numberImperfections*

  An Int specifying the number of imperfections to be considered for the evaluation of the Marciniak-Kuczynski analysis. These imperfections are assumed to be equally spaced in the angular direction. The default value is 4.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *alpha*

  A Float specifying the value of the coefficient that will multiply the shear contribution to the Hashin's fiber initiation criterion. The default value is 0.0.

- *omega*

  A Float specifying the factor used for filtering the ratio of principal strain rates used for the evaluation of the MSFLD damage initiation criterion. The default value is 1.0.

- *tolerance*

  A Float specifying the tolerance within which the damage initiation criterion must be satisfied. The default value is 0.05.

- *direction*

  A SymbolicConstant specifying the damage initiation direction. Possible values are NMORI and TMORI. The default value is NMORI.

### Return value

A DamageInitiation object.

### Exceptions

RangeError.



## MsfldDamageInitiation(...)



This method creates a DamageInitiation object.



### Path

```
mdb.models[name].materials[name].MsfldDamageInitiation
session.odbs[name].materials[name].MsfldDamageInitiation
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described in the "Table data" section.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the damage initiation definition. Possible values are FLD and MSFLD. The default value is MSFLD.

- *feq*

  A Float specifying the critical value of the deformation severity index for equivalent plastic strains. The default value is 10.0.

- *fnn*

  A Float specifying the critical value of the deformation severity index for strains normal to the groove direction. The default value is 10.0.

- *fnt*

  A Float specifying the critical value of the deformation severity index for shear strains. The default value is 10.0.

- *frequency*

  An Int specifying the frequency, in increments, at which the Marciniak-Kuczynski analysis is going to be performed. The default value is 1.

- *ks*

  A Float specifying the value of Ks. The default value is 0.0.

- *numberImperfections*

  An Int specifying the number of imperfections to be considered for the evaluation of the Marciniak-Kuczynski analysis. These imperfections are assumed to be equally spaced in the angular direction. The default value is 4.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *alpha*

  A Float specifying the value of the coefficient that will multiply the shear contribution to the Hashin's fiber initiation criterion. The default value is 0.0.

- *omega*

  A Float specifying the factor used for filtering the ratio of principal strain rates used for the evaluation of the MSFLD damage initiation criterion. The default value is 1.0.

- *tolerance*

  A Float specifying the tolerance within which the damage initiation criterion must be satisfied. The default value is 0.05.

- *direction*

  A SymbolicConstant specifying the damage initiation direction. Possible values are NMORI and TMORI. The default value is NMORI.

### Return value

A DamageInitiation object.

### Exceptions

RangeError.



## QuadeDamageInitiation(...)



This method creates a DamageInitiation object.



### Path

```
mdb.models[name].materials[name].QuadeDamageInitiation
session.odbs[name].materials[name].QuadeDamageInitiation
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described in the "Table data" section.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the damage initiation definition. Possible values are FLD and MSFLD. The default value is MSFLD.

- *feq*

  A Float specifying the critical value of the deformation severity index for equivalent plastic strains. The default value is 10.0.

- *fnn*

  A Float specifying the critical value of the deformation severity index for strains normal to the groove direction. The default value is 10.0.

- *fnt*

  A Float specifying the critical value of the deformation severity index for shear strains. The default value is 10.0.

- *frequency*

  An Int specifying the frequency, in increments, at which the Marciniak-Kuczynski analysis is going to be performed. The default value is 1.

- *ks*

  A Float specifying the value of Ks. The default value is 0.0.

- *numberImperfections*

  An Int specifying the number of imperfections to be considered for the evaluation of the Marciniak-Kuczynski analysis. These imperfections are assumed to be equally spaced in the angular direction. The default value is 4.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *alpha*

  A Float specifying the value of the coefficient that will multiply the shear contribution to the Hashin's fiber initiation criterion. The default value is 0.0.

- *omega*

  A Float specifying the factor used for filtering the ratio of principal strain rates used for the evaluation of the MSFLD damage initiation criterion. The default value is 1.0.

- *tolerance*

  A Float specifying the tolerance within which the damage initiation criterion must be satisfied. The default value is 0.05.

- *direction*

  A SymbolicConstant specifying the damage initiation direction. Possible values are NMORI and TMORI. The default value is NMORI.

- *position*

  An SymbolicConstant specifying the damage initiation position. Possible values are CENTROID, CRACKTIP and COMBINED. The default value is CENTROID.

### Return value

A DamageInitiation object.

### Exceptions

RangeError.



## QuadsDamageInitiation(...)



This method creates a DamageInitiation object.



### Path

```
mdb.models[name].materials[name].QuadsDamageInitiation
session.odbs[name].materials[name].QuadsDamageInitiation
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described in the "Table data" section.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the damage initiation definition. Possible values are FLD and MSFLD. The default value is MSFLD.

- *feq*

  A Float specifying the critical value of the deformation severity index for equivalent plastic strains. The default value is 10.0.

- *fnn*

  A Float specifying the critical value of the deformation severity index for strains normal to the groove direction. The default value is 10.0.

- *fnt*

  A Float specifying the critical value of the deformation severity index for shear strains. The default value is 10.0.

- *frequency*

  An Int specifying the frequency, in increments, at which the Marciniak-Kuczynski analysis is going to be performed. The default value is 1.

- *ks*

  A Float specifying the value of Ks. The default value is 0.0.

- *numberImperfections*

  An Int specifying the number of imperfections to be considered for the evaluation of the Marciniak-Kuczynski analysis. These imperfections are assumed to be equally spaced in the angular direction. The default value is 4.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *alpha*

  A Float specifying the value of the coefficient that will multiply the shear contribution to the Hashin's fiber initiation criterion. The default value is 0.0.

- *omega*

  A Float specifying the factor used for filtering the ratio of principal strain rates used for the evaluation of the MSFLD damage initiation criterion. The default value is 1.0.

- *tolerance*

  A Float specifying the tolerance within which the damage initiation criterion must be satisfied. The default value is 0.05.

- *direction*

  A SymbolicConstant specifying the damage initiation direction. Possible values are NMORI and TMORI. The default value is NMORI.

- *position*

  An SymbolicConstant specifying the damage initiation position. Possible values are CENTROID, CRACKTIP and COMBINED. The default value is CENTROID.

### Return value

A DamageInitiation object.

### Exceptions

RangeError.



## MaxpeDamageInitiation(...)



This method creates a DamageInitiation object.



### Path

```
mdb.models[name].materials[name].MaxpeDamageInitiation
session.odbs[name].materials[name].MaxpeDamageInitiation
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described in the "Table data" section.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the damage initiation definition. Possible values are FLD and MSFLD. The default value is MSFLD.

- *feq*

  A Float specifying the critical value of the deformation severity index for equivalent plastic strains. The default value is 10.0.

- *fnn*

  A Float specifying the critical value of the deformation severity index for strains normal to the groove direction. The default value is 10.0.

- *fnt*

  A Float specifying the critical value of the deformation severity index for shear strains. The default value is 10.0.

- *frequency*

  An Int specifying the frequency, in increments, at which the Marciniak-Kuczynski analysis is going to be performed. The default value is 1.

- *ks*

  A Float specifying the value of Ks. The default value is 0.0.

- *numberImperfections*

  An Int specifying the number of imperfections to be considered for the evaluation of the Marciniak-Kuczynski analysis. These imperfections are assumed to be equally spaced in the angular direction. The default value is 4.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *alpha*

  A Float specifying the value of the coefficient that will multiply the shear contribution to the Hashin's fiber initiation criterion. The default value is 0.0.

- *omega*

  A Float specifying the factor used for filtering the ratio of principal strain rates used for the evaluation of the MSFLD damage initiation criterion. The default value is 1.0.

- *tolerance*

  A Float specifying the tolerance within which the damage initiation criterion must be satisfied. The default value is 0.05.

- *direction*

  A SymbolicConstant specifying the damage initiation direction. Possible values are NMORI and TMORI. The default value is NMORI.

- *position*

  An SymbolicConstant specifying the damage initiation position. Possible values are CENTROID, CRACKTIP and COMBINED. The default value is CENTROID.

### Return value

A DamageInitiation object.

### Exceptions

RangeError.



## MaxpsDamageInitiation(...)



This method creates a DamageInitiation object.



### Path

```
mdb.models[name].materials[name].MaxpsDamageInitiation
session.odbs[name].materials[name].MaxpsDamageInitiation
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described in the "Table data" section.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the damage initiation definition. Possible values are FLD and MSFLD. The default value is MSFLD.

- *feq*

  A Float specifying the critical value of the deformation severity index for equivalent plastic strains. The default value is 10.0.

- *fnn*

  A Float specifying the critical value of the deformation severity index for strains normal to the groove direction. The default value is 10.0.

- *fnt*

  A Float specifying the critical value of the deformation severity index for shear strains. The default value is 10.0.

- *frequency*

  An Int specifying the frequency, in increments, at which the Marciniak-Kuczynski analysis is going to be performed. The default value is 1.

- *ks*

  A Float specifying the value of Ks. The default value is 0.0.

- *numberImperfections*

  An Int specifying the number of imperfections to be considered for the evaluation of the Marciniak-Kuczynski analysis. These imperfections are assumed to be equally spaced in the angular direction. The default value is 4.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *alpha*

  A Float specifying the value of the coefficient that will multiply the shear contribution to the Hashin's fiber initiation criterion. The default value is 0.0.

- *omega*

  A Float specifying the factor used for filtering the ratio of principal strain rates used for the evaluation of the MSFLD damage initiation criterion. The default value is 1.0.

- *tolerance*

  A Float specifying the tolerance within which the damage initiation criterion must be satisfied. The default value is 0.05.

- *direction*

  A SymbolicConstant specifying the damage initiation direction. Possible values are NMORI and TMORI. The default value is NMORI.

- *position*

  An SymbolicConstant specifying the damage initiation position. Possible values are CENTROID, CRACKTIP and COMBINED. The default value is CENTROID.

### Return value

A DamageInitiation object.

### Exceptions

RangeError.



## ShearDamageInitiation(...)



This method creates a DamageInitiation object.



### Path

```
mdb.models[name].materials[name].ShearDamageInitiation
session.odbs[name].materials[name].ShearDamageInitiation
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described in the "Table data" section.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the damage initiation definition. Possible values are FLD and MSFLD. The default value is MSFLD.

- *feq*

  A Float specifying the critical value of the deformation severity index for equivalent plastic strains. The default value is 10.0.

- *fnn*

  A Float specifying the critical value of the deformation severity index for strains normal to the groove direction. The default value is 10.0.

- *fnt*

  A Float specifying the critical value of the deformation severity index for shear strains. The default value is 10.0.

- *frequency*

  An Int specifying the frequency, in increments, at which the Marciniak-Kuczynski analysis is going to be performed. The default value is 1.

- *ks*

  A Float specifying the value of Ks. The default value is 0.0.

- *numberImperfections*

  An Int specifying the number of imperfections to be considered for the evaluation of the Marciniak-Kuczynski analysis. These imperfections are assumed to be equally spaced in the angular direction. The default value is 4.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *alpha*

  A Float specifying the value of the coefficient that will multiply the shear contribution to the Hashin's fiber initiation criterion. The default value is 0.0.

- *omega*

  A Float specifying the factor used for filtering the ratio of principal strain rates used for the evaluation of the MSFLD damage initiation criterion. The default value is 1.0.

- *tolerance*

  A Float specifying the tolerance within which the damage initiation criterion must be satisfied. The default value is 0.05.

- *direction*

  A SymbolicConstant specifying the damage initiation direction. Possible values are NMORI and TMORI. The default value is NMORI.

### Return value

A DamageInitiation object.

### Exceptions

RangeError.



## HashinDamageInitiation(...)



This method creates a DamageInitiation object.



### Path

```
mdb.models[name].materials[name].HashinDamageInitiation
session.odbs[name].materials[name].HashinDamageInitiation
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described in the "Table data" section.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the damage initiation definition. Possible values are FLD and MSFLD. The default value is MSFLD.

- *feq*

  A Float specifying the critical value of the deformation severity index for equivalent plastic strains. The default value is 10.0.

- *fnn*

  A Float specifying the critical value of the deformation severity index for strains normal to the groove direction. The default value is 10.0.

- *fnt*

  A Float specifying the critical value of the deformation severity index for shear strains. The default value is 10.0.

- *frequency*

  An Int specifying the frequency, in increments, at which the Marciniak-Kuczynski analysis is going to be performed. The default value is 1.

- *ks*

  A Float specifying the value of Ks. The default value is 0.0.

- *numberImperfections*

  An Int specifying the number of imperfections to be considered for the evaluation of the Marciniak-Kuczynski analysis. These imperfections are assumed to be equally spaced in the angular direction. The default value is 4.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *alpha*

  A Float specifying the value of the coefficient that will multiply the shear contribution to the Hashin's fiber initiation criterion. The default value is 0.0.

- *omega*

  A Float specifying the factor used for filtering the ratio of principal strain rates used for the evaluation of the MSFLD damage initiation criterion. The default value is 1.0.

- *tolerance*

  A Float specifying the tolerance within which the damage initiation criterion must be satisfied. The default value is 0.05.

- *direction*

  A SymbolicConstant specifying the damage initiation direction. Possible values are NMORI and TMORI. The default value is NMORI.

### Return value

A DamageInitiation object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the DamageInitiation object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [DamageInitiation ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageinitiationpyc.htm?ContextScope=all#simaker-damageinitiationductiledamageinitiationpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The DamageInitiation object can have the following members:

- *definition*

  A SymbolicConstant specifying the damage initiation definition. Possible values are FLD and MSFLD. The default value is MSFLD.

- *feq*

  A Float specifying the critical value of the deformation severity index for equivalent plastic strains. The default value is 10.0.

- *fnn*

  A Float specifying the critical value of the deformation severity index for strains normal to the groove direction. The default value is 10.0.

- *fnt*

  A Float specifying the critical value of the deformation severity index for shear strains. The default value is 10.0.

- *frequency*

  An Int specifying the frequency, in increments, at which the Marciniak-Kuczynski analysis is going to be performed. The default value is 1.

- *ks*

  A Float specifying the value of Ks. The default value is 0.0.

- *numberImperfections*

  An Int specifying the number of imperfections to be considered for the evaluation of the Marciniak-Kuczynski analysis. These imperfections are assumed to be equally spaced in the angular direction. The default value is 4.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *alpha*

  A Float specifying the value of the coefficient that will multiply the shear contribution to the Hashin's fiber initiation criterion. The default value is 0.0.

- *omega*

  A Float specifying the factor used for filtering the ratio of principal strain rates used for the evaluation of the MSFLD damage initiation criterion. The default value is 1.0.

- *tolerance*

  A Float specifying the tolerance within which the damage initiation criterion must be satisfied. The default value is 0.05.

- *direction*

  A SymbolicConstant specifying the damage initiation direction. Possible values are NMORI and TMORI. The default value is NMORI.

- *table*

  A tuple of tuples of Floats specifying the items described in the "Table data" section.

- *damageEvolution*

  A [DamageEvolution](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damageevolutionpyc.htm?ContextScope=all) object.

- *damageStabilization*

  A [DamageStabilization](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damagestabilizationpyc.htm?ContextScope=all) object.

- *damageStabilizationCohesive*

  A [DamageStabilizationCohesive](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-damagestabilizationcohesivepyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [DAMAGE INITIATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-damageinitiation.htm?ContextScope=all#simakey-r-damageinitiation)