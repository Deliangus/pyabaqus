# SoilsStep object

The SoilsStep object is used to specify transient (consolidation) or steady-state response analysis of partially or fully saturated fluid-filled porous media.

The SoilsStep object is derived from the [AnalysisStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analysissteppyc.htm?ContextScope=all) object.

## Access

```
import step
mdb.models[name].steps[name]
```

## SoilsStep(...)



This method creates a SoilsStep object.



### Path

```
mdb.models[name].SoilsStep
```

### Required arguments

- *name*

  A String specifying the repository key.

- *previous*

  A String specifying the name of the previous step. The new step appears after this step in the list of analysis steps.

### Optional arguments

- *description*

  A String specifying a description of the new step. The default value is an empty string.

- *response*

  A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and TRANSIENT. The default value is TRANSIENT.

- *timePeriod*

  A Float specifying the total time period. The default value is 1.0.

- *nlgeom*

  A Boolean specifying whether geometric nonlinearities should be accounted for during the step. The default value is OFF.

- *stabilizationMethod*

  A SymbolicConstant specifying the stabilization type. Possible values are NONE, DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE.

- *stabilizationMagnitude*

  A Float specifying the damping intensity of the automatic damping algorithm if the problem is expected to be unstable, and *stabilizationMethod* is not NONE. The default value is 2×10–4.

- *creep*

  A Boolean specifying whether a creep response occurs during this step. The default value is ON.

- *timeIncrementationMethod*

  A SymbolicConstant specifying the time incrementation method to be used. Possible values are FIXED and AUTOMATIC. The default value is AUTOMATIC.

- *initialInc*

  A Float specifying the initial time increment. The default value is the total time period for the step.

- *minInc*

  A Float specifying the minimum time increment allowed. The default value is the smaller of the suggested initial time increment or 10−5 times the total time period.

- *maxInc*

  A Float specifying the maximum time increment allowed. The default value is the total time period for the step.

- *maxNumInc*

  An Int specifying the maximum number of increments in a step. The default value is 100.

- *end*

  A SymbolicConstant specifying the time period to be analyzed in a transient analysis. Possible values are PERIOD and SS. The default value is PERIOD.

- *utol*

  None or a Float specifying the maximum pore pressure change permitted in any increment (in pressure units) in a transient consolidation analysis. The default value is None.

- *cetol*

  A Float specifying the maximum allowable difference in the creep strain increment calculated from the creep strain rates at the beginning and end of the increment. The default value is 0.0.

- *amplitude*

  A SymbolicConstant specifying the amplitude variation for loading magnitudes during the step. The default value is STEP. Possible values are STEP and RAMP.

- *extrapolation*

  A SymbolicConstant specifying the type of extrapolation to use in determining the incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and PARABOLIC. The default value is LINEAR.

- *matrixSolver*

  A SymbolicConstant specifying the type of solver. Possible values are DIRECT and ITERATIVE. The default value is DIRECT.

- *matrixStorage*

  A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.

- *maintainAttributes*

  A Boolean specifying whether to retain attributes from an existing step with the same name. The default value is False.

- *solutionTechnique*

  A SymbolicConstant specifying the technique used to for solving nonlinear equations. Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON.

- *reformKernel*

  An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix is reformed.. The default value is 8.

- *convertSDI*

  A SymbolicConstant specifying whether to force a new iteration if severe discontinuities occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and CONVERT_SDI_ON. The default value is PROPAGATED.

- *adaptiveDampingRatio*

  A Float specifying the maximum allowable ratio of the stabilization energy to the total strain energy and can be used only if *stabilizationMethod* is not NONE. The default value is 0.05.

- *continueDampingFactors*

  A Boolean specifying whether this step will carry over the damping factors from the results of the preceding general step. This parameter must be used in conjunction with the *adaptiveDampingRatio* parameter. The default value is OFF.

### Return value

A SoilsStep object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the SoilsStep object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SoilsStep ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-soilssteppyc.htm?ContextScope=all#simaker-soilsstepsoilssteppyc)method, except for the *name*, *previous*, and *maintainAttributes* arguments.

### Return value

None.

### Exceptions

RangeError.



## Members

The SoilsStep object can have the following members:

- *name*

  A String specifying the repository key.

- *response*

  A SymbolicConstant specifying the analysis type. Possible values are STEADY_STATE and TRANSIENT. The default value is TRANSIENT.

- *timePeriod*

  A Float specifying the total time period. The default value is 1.0.

- *nlgeom*

  A Boolean specifying whether geometric nonlinearities should be accounted for during the step. The default value is OFF.

- *stabilizationMethod*

  A SymbolicConstant specifying the stabilization type. Possible values are NONE, DISSIPATED_ENERGY_FRACTION, and DAMPING_FACTOR. The default value is NONE.

- *stabilizationMagnitude*

  A Float specifying the damping intensity of the automatic damping algorithm if the problem is expected to be unstable, and *stabilizationMethod* is not NONE. The default value is 2×10–4.

- *creep*

  A Boolean specifying whether a creep response occurs during this step. The default value is ON.

- *timeIncrementationMethod*

  A SymbolicConstant specifying the time incrementation method to be used. Possible values are FIXED and AUTOMATIC. The default value is AUTOMATIC.

- *initialInc*

  A Float specifying the initial time increment. The default value is the total time period for the step.

- *minInc*

  A Float specifying the minimum time increment allowed. The default value is the smaller of the suggested initial time increment or 10−5 times the total time period.

- *maxInc*

  A Float specifying the maximum time increment allowed. The default value is the total time period for the step.

- *maxNumInc*

  An Int specifying the maximum number of increments in a step. The default value is 100.

- *end*

  A SymbolicConstant specifying the time period to be analyzed in a transient analysis. Possible values are PERIOD and SS. The default value is PERIOD.

- *utol*

  None or a Float specifying the maximum pore pressure change permitted in any increment (in pressure units) in a transient consolidation analysis. The default value is None.

- *cetol*

  A Float specifying the maximum allowable difference in the creep strain increment calculated from the creep strain rates at the beginning and end of the increment. The default value is 0.0.

- *amplitude*

  A SymbolicConstant specifying the amplitude variation for loading magnitudes during the step. The default value is STEP. Possible values are STEP and RAMP.

- *extrapolation*

  A SymbolicConstant specifying the type of extrapolation to use in determining the incremental solution for a nonlinear analysis. Possible values are NONE, LINEAR, and PARABOLIC. The default value is LINEAR.

- *matrixSolver*

  A SymbolicConstant specifying the type of solver. Possible values are DIRECT and ITERATIVE. The default value is DIRECT.

- *matrixStorage*

  A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.

- *solutionTechnique*

  A SymbolicConstant specifying the technique used to for solving nonlinear equations. Possible values are FULL_NEWTON and QUASI_NEWTON. The default value is FULL_NEWTON.

- *reformKernel*

  An Int specifying the number of quasi-Newton iterations allowed before the kernel matrix is reformed.. The default value is 8.

- *convertSDI*

  A SymbolicConstant specifying whether to force a new iteration if severe discontinuities occur during an iteration. Possible values are PROPAGATED, CONVERT_SDI_OFF, and CONVERT_SDI_ON. The default value is PROPAGATED.

- *adaptiveDampingRatio*

  A Float specifying the maximum allowable ratio of the stabilization energy to the total strain energy and can be used only if *stabilizationMethod* is not NONE. The default value is 0.05.

- *continueDampingFactors*

  A Boolean specifying whether this step will carry over the damping factors from the results of the preceding general step. This parameter must be used in conjunction with the *adaptiveDampingRatio* parameter. The default value is OFF.

- *previous*

  A String specifying the name of the previous step. The new step appears after this step in the list of analysis steps.

- *description*

  A String specifying a description of the new step. The default value is an empty string.

- *explicit*

  A SymbolicConstant specifying whether the step has an explicit procedure type (*procedureType*=ANNEAL, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT).

- *perturbation*

  A Boolean specifying whether the step has a perturbation procedure type.

- *nonmechanical*

  A Boolean specifying whether the step has a mechanical procedure type.

- *procedureType*

  A SymbolicConstant specifying the Abaqus procedure. Possible values are:

  - ANNEAL
  - BUCKLE
  - COMPLEX_FREQUENCY
  - COUPLED_TEMP_DISPLACEMENT
  - COUPLED_THERMAL_ELECTRIC
  - DIRECT_CYCLIC
  - DYNAMIC_IMPLICIT
  - DYNAMIC_EXPLICIT
  - DYNAMIC_SUBSPACE
  - DYNAMIC_TEMP_DISPLACEMENT
  - COUPLED_THERMAL_ELECTRICAL_STRUCTURAL
  - FREQUENCY
  - GEOSTATIC
  - HEAT_TRANSFER
  - MASS_DIFFUSION
  - MODAL_DYNAMICS
  - RANDOM_RESPONSE
  - RESPONSE_SPECTRUM
  - SOILS
  - STATIC_GENERAL
  - STATIC_LINEAR_PERTURBATION
  - STATIC_RIKS
  - STEADY_STATE_DIRECT
  - STEADY_STATE_MODAL
  - STEADY_STATE_SUBSPACE
  - VISCO

- *suppressed*

  A Boolean specifying whether the step is suppressed or not. The default value is OFF.

- *fieldOutputRequestState*

  A repository of [FieldOutputRequestState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputrequeststatepyc.htm?ContextScope=all) objects.

- *historyOutputRequestState*

  A repository of [HistoryOutputRequestState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyoutputrequeststatepyc.htm?ContextScope=all) objects.

- *diagnosticPrint*

  A [DiagnosticPrint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-diagnosticprintpyc.htm?ContextScope=all) object.

- *monitor*

  A [Monitor](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-monitorpyc.htm?ContextScope=all) object.

- *restart*

  A [Restart](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-restartpyc.htm?ContextScope=all) object.

- *adaptiveMeshConstraintStates*

  A repository of [AdaptiveMeshConstraintState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-adaptivemeshconstraintstatepyc.htm?ContextScope=all) objects.

- *adaptiveMeshDomains*

  A repository of [AdaptiveMeshDomain](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-adaptivemeshdomainpyc.htm?ContextScope=all) objects.

- *control*

  A [Control](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-controlpyc.htm?ContextScope=all) object.

- *solverControl*

  A [SolverControl](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-solvercontrolpyc.htm?ContextScope=all) object.

- *boundaryConditionStates*

  A repository of [BoundaryConditionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?ContextScope=all) objects.

- *interactionStates*

  A repository of [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) objects.

- *loadStates*

  A repository of [LoadState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?ContextScope=all) objects.

- *loadCases*

  A repository of [LoadCase](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadcasepyc.htm?ContextScope=all) objects.

- *predefinedFieldStates*

  A repository of [PredefinedFieldState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-predefinedfieldstatepyc.htm?ContextScope=all) objects.



## Corresponding analysis keywords

- [SOILS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-soils.htm?ContextScope=all#simakey-r-soils)
- [STEP](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-step.htm?ContextScope=all#simakey-r-step)