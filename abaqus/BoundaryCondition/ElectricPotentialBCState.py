from abaqusConstants import *
from .BoundaryConditionState import BoundaryConditionState


class ElectricPotentialBCState(BoundaryConditionState):
    """The ElectricPotentialBCState object stores the propagating data for a electrical
    potential boundary condition in a step. One instance of this object is created 
    internally by the ElectricPotentialBC object for each step. The instance is also deleted 
    internally by the ElectricPotentialBC object. 
    The ElectricPotentialBCState object has no constructor or methods. 
    The ElectricPotentialBCState object is derived from the BoundaryConditionState object. 

    Notes
    -----
        This object can be accessed by:
        - import load
        - mdb.models[name].steps[name].boundaryConditionStates[name]

    Corresponding analysis keywords
    -------------------------------
        - BOUNDARY

    """

    # A Float specifying the electrical potential magnitude. 
    magnitude: float = None

    # A SymbolicConstant specifying the propagation state of the electrical potential 
    # magnitude. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED. 
    magnitudeState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the amplitude reference. Possible 
    # values are UNSET, SET, UNCHANGED, FREED, and MODIFIED. 
    amplitudeState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:
    # NOT_YET_ACTIVE
    # CREATED
    # PROPAGATED
    # MODIFIED
    # DEACTIVATED
    # NO_LONGER_ACTIVE
    # TYPE_NOT_APPLICABLE
    # INSTANCE_NOT_APPLICABLE
    # PROPAGATED_FROM_BASE_STATE
    # MODIFIED_FROM_BASE_STATE
    # DEACTIVATED_FROM_BASE_STATE
    # BUILT_INTO_MODES
    status: SymbolicConstant = None

    # A String specifying the name of the amplitude reference. The String is empty if the 
    # boundary condition has no amplitude reference. 
    amplitude: str = ''
