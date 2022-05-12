import typing

from abaqusConstants import *

from __init__ import *
from __future__ import annotations


class Control:
    """The Control object is used to provide additional optional general solution controls.

    Notes
    -----
        This object can be accessed by:
        
        .. code-block:: python
        
           import step
           mdb.models[name].steps[name].control

    """
    def setValues(self,
                  allowPropagation: Boolean = ON,
                  resetDefaultValues: Boolean = OFF,
                  discontinuous: Boolean = OFF,
                  constraints: typing.Union[SymbolicConstant, float] = DEFAULT,
                  lineSearch: typing.Union[SymbolicConstant, float] = DEFAULT,
                  timeIncrementation: typing.Union[SymbolicConstant,
                                                   float] = DEFAULT,
                  directCyclic: typing.Union[SymbolicConstant,
                                             float] = DEFAULT,
                  concentrationField: typing.Union[SymbolicConstant,
                                                   float] = DEFAULT,
                  displacementField: typing.Union[SymbolicConstant,
                                                  float] = DEFAULT,
                  electricalPotentialField: typing.Union[SymbolicConstant,
                                                         float] = DEFAULT,
                  globalField: typing.Union[SymbolicConstant, float] = DEFAULT,
                  hydrostaticFluidPressureField: typing.Union[SymbolicConstant,
                                                              float] = DEFAULT,
                  poreFluidPressureField: typing.Union[SymbolicConstant,
                                                       float] = DEFAULT,
                  rotationField: typing.Union[SymbolicConstant,
                                              float] = DEFAULT,
                  temperatureField: typing.Union[SymbolicConstant,
                                                 float] = DEFAULT,
                  vcctLinearScaling: typing.Union[SymbolicConstant,
                                                  float] = DEFAULT):
        """This method modifies the Control object.
        
        Parameters
        ----------
        allowPropagation
            A Boolean specifying whether to allow all control values to propagate from a previous 
            step. Setting this argument to ON automatically sets *resetDefaultValues* to OFF. The 
            default value is ON. 
        resetDefaultValues
            A Boolean specifying whether to use all default control values. Setting this argument to 
            ON automatically sets *allowPropagation* to OFF. The default value is OFF. 
        discontinuous
            A Boolean specifying whether to set *timeIncrementation* values that will usually 
            improve efficiency for analyses with severely discontinuous behavior. The default value 
            is OFF. 
        constraints
            The SymbolicConstant DEFAULT or a sequence of Floats specifying tolerances on constraint 
            equations. If a specified sequence contains a value of 0, that item in the sequence will 
            be set to its system-defined value. The value can also be the SymbolicConstant DEFAULT. 
            The default value is DEFAULT. 
        lineSearch
            The SymbolicConstant DEFAULT or a sequence of Floats specifying line search control 
            parameters. If a specified sequence contains a value of 0, that item in the sequence 
            will be set to its system-defined value. The value can also be the SymbolicConstant 
            DEFAULT. The default value is DEFAULT. 
        timeIncrementation
            The SymbolicConstant DEFAULT or a sequence of Floats specifying time incrementation 
            control parameters. If a specified sequence contains a value of 0, that item in the 
            sequence will be set to its system-defined value. The value can also be the 
            SymbolicConstant DEFAULT. The default value is DEFAULT. 
        directCyclic
            The SymbolicConstant DEFAULT or a sequence of Floats specifying direct cyclic control 
            parameters. If a specified sequence contains a value of 0, that item in the sequence 
            will be set to its system-defined value. The value can also be the SymbolicConstant 
            DEFAULT. The default value is DEFAULT. 
        concentrationField
            The SymbolicConstant DEFAULT or a sequence of Floats specifying mass concentration field 
            equilibrium equation parameters. If a specified sequence contains a value of 0, that 
            item in the sequence will be set to its system-defined value. The value can also be the 
            SymbolicConstant DEFAULT. The default value is DEFAULT. 
        displacementField
            The SymbolicConstant DEFAULT or a sequence of Floats specifying displacement field and 
            warping degree of freedom field equilibrium equation parameters. If a specified sequence 
            contains a value of 0, that item in the sequence will be set to its system-defined 
            value. The value can also be the SymbolicConstant DEFAULT. The default value is DEFAULT. 
        electricalPotentialField
            The SymbolicConstant DEFAULT or a sequence of Floats specifying electrical potential 
            field equilibrium equation parameters. If a specified sequence contains a value of 0, 
            that item in the sequence will be set to its system-defined value. The value can also be 
            the SymbolicConstant DEFAULT. The default value is DEFAULT. 
        globalField
            The SymbolicConstant DEFAULT or a sequence of Floats specifying parameters for all 
            applicable field equilibrium equations. This argument overwrites all other field 
            equilibrium equation control values. If a specified sequence contains a value of 0, that 
            item in the sequence will be set to its system-defined value. The value can also be the 
            SymbolicConstant DEFAULT. The default value is DEFAULT. 
        hydrostaticFluidPressureField
            The SymbolicConstant DEFAULT or a sequence of Floats specifying hydrostatic fluid 
            element volume constraint parameters. If a specified sequence contains a value of 0, 
            that item in the sequence will be set to its system-defined value. The value can also be 
            the SymbolicConstant DEFAULT. The default value is DEFAULT. 
        poreFluidPressureField
            The SymbolicConstant DEFAULT or a sequence of Floats specifying pore liquid volumetric 
            continuity equilibrium equation parameters. If a specified sequence contains a value of 
            0, that item in the sequence will be set to its system-defined value. The value can also 
            be the SymbolicConstant DEFAULT. The default value is DEFAULT. 
        rotationField
            The SymbolicConstant DEFAULT or a sequence of Floats specifying rotation field 
            equilibrium equation parameters. If a specified sequence contains a value of 0, that 
            item in the sequence will be set to its system-defined value. The value can also be the 
            SymbolicConstant DEFAULT. The default value is DEFAULT. 
        temperatureField
            The SymbolicConstant DEFAULT or a sequence of Floats specifying temperature field 
            equilibrium equation parameters. If a specified sequence contains a value of 0, that 
            item in the sequence will be set to its system-defined value. The value can also be the 
            SymbolicConstant DEFAULT. The default value is DEFAULT. 
        vcctLinearScaling
            The SymbolicConstant DEFAULT or a Float specifying linear scaling parameter for a VCCT 
            debonding analysis. If a specified value is 0, it will be set to its system-defined 
            value. The value can also be the SymbolicConstant DEFAULT. The default value is DEFAULT.

        Raises
        ------
        RangeError
        """
        pass