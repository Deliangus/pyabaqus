# ConnectorElasticity object

The ConnectorElasticity object defines elastic behavior for one or more components of a connector's relative motion.

The ConnectorElasticity object is derived from the [ConnectorBehaviorOption](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorbehavioroptionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].sections[name].behaviorOptions[i]
import odbSection
session.odbs[name].sections[name].behaviorOptions[i]
```

## ConnectorElasticity(...)



This method creates a connector elasticity behavior option for a [ConnectorSection](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorsectionpyc.htm?ContextScope=all) object.



### Path

```
          import connectorBehavior
          connectorBehavior.ConnectorElasticity
          import odbConnectorBehavior
          odbConnectorBehavior.ConnectorElasticity
        
```

### Required arguments

None.

### Optional arguments

- *behavior*

  A SymbolicConstant specifying whether the elastic behavior is linear, nonlinear, or rigid. Possible values are LINEAR, NONLINEAR, and RIGID. The default value is LINEAR.

- *coupling*

  A SymbolicConstant specifying whether the elastic behavior is coupled between the connector's components of relative motion. If *behavior*=LINEAR, then possible values are UNCOUPLED and COUPLED. If *behavior*=NONLINEAR, then possible values are UNCOUPLED, COUPLED_POSITION, and COUPLED_MOTION. Possible values are UNCOUPLED, COUPLED, COUPLED_POSITION, and COUPLED_MOTION. The default value is UNCOUPLED.This argument is not applicable if *behavior*=RIGID.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.This argument is not applicable if *behavior*=RIGID.

- *temperatureDependency*

  A Boolean specifying whether the behavior data depend on temperature. The default value is OFF.This argument is not applicable if *behavior*=RIGID.

- *frequencyDependency*

  A Boolean specifying whether the behavior data depend on frequency. This value is applicable only if *behavior*=LINEAR and *coupling*=UNCOUPLED. The default value is OFF.This argument is not applicable if *behavior*=RIGID.

- *table*

  A sequence of sequences of Floats specifying elasticity properties. Items in the table data are described below. This argument is not applicable if *behavior*=RIGID. The default value is an empty sequence.

- *independentComponents*

  A sequence of Ints specifying the list of independent components that are included in the definition of the connector elasticity data. This argument is applicable only if *behavior*=NONLINEAR and *coupling*=COUPLED_POSITION or COUPLED_MOTION. If this argument is applicable, at least one value must be specified. Only available components can be specified. The default value is an empty sequence.

- *components*

  A sequence of Ints specifying the components of relative motion for which the behavior is defined. Possible values are 1 ≤≤ *components* ≤≤ 6. Only available components can be specified. The default value is an empty sequence.

### Table data

If *behavior*=LINEAR and *coupling*=UNCOUPLED, then each sequence of the table data specifies the following:

- Elastic stiffness (per each specified force/moment component).
- Frequency (cycles/time), if the data depend on frequency.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *behavior*=NONLINEAR and *coupling*=UNCOUPLED, then each sequence of the table data specifies the following:

- Force or moment.
- Relative displacement or rotation.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *behavior*=LINEAR and *coupling*=COUPLED, the table data specify the symmetric portion of the elastic stiffness matrix for the specified components followed by any temperature data and then any field data. For example, if components 2, 3, and 5 are specified, the table portion of the command is as follows:

```
table=( (D22D22, D23D23, D25D25, D33D33, D35D35, D55D55,),
)
```

The following items should then be specified as comma-separated data:

- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *behavior*=NONLINEAR and *coupling*=COUPLED_POSITION or COUPLED_MOTION, each sequence of the table data specifies the following:

- Force or moment for the directions in the *components* list.
- Relative position or angle for the first *independentComponents* direction if *coupling*=COUPLED_POSITION. Relative displacement or rotation for the first *independentComponents* direction if *coupling*=COUPLED_MOTION.
- Relative position or angle for the second *independentComponents* direction if *coupling*=COUPLED_POSITION. Relative displacement or rotation for the second *independentComponents* direction if *coupling*=COUPLED_MOTION.
- Etc. up to the Nth *independentComponents* direction.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A ConnectorElasticity object.

### Exceptions

ValueError and TextError.



## setValues(...)



This method modifies the ConnectorElasticity object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ConnectorElasticity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorelasticitypyc.htm?ContextScope=all#simaker-connectorelasticityconnectorelasticitypyc)method.

### Return value

None.

### Exceptions

ValueError.



## Members

The ConnectorElasticity object has members with the same names and descriptions as the arguments to the [ConnectorElasticity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorelasticitypyc.htm?ContextScope=all#simaker-connectorelasticityconnectorelasticitypyc)method.

In addition, the ConnectorElasticity object can have the following member:

- *options*

  A [ConnectorOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectoroptionspyc.htm?ContextScope=all) object specifying the [ConnectorOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectoroptionspyc.htm?ContextScope=all) used to define tabular options for this [ConnectorBehaviorOption](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorbehavioroptionpyc.htm?ContextScope=all).



## Corresponding analysis keywords

- [CONNECTOR ELASTICITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectorelasticity.htm?ContextScope=all#simakey-r-connectorelasticity)