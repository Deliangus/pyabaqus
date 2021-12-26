from abaqusConstants import *
from .BoundaryConditionState import BoundaryConditionState


class AcousticPressureBCState(BoundaryConditionState):

    """The AcousticPressureBCState object stores the propagating data for an acoustic pressure 
    boundary condition in a step. One instance of this object is created internally by the 
    AcousticPressureBC object for each step. The instance is also deleted internally by the 
    AcousticPressureBC object. 
    The AcousticPressureBCState object has no constructor or methods. 
    The AcousticPressureBCState object is derived from the BoundaryConditionState object. 

    Access
    ------
        - import load
        - mdb.models[name].steps[name].boundaryConditionStates[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - BOUNDARY

    """

    # A Float specifying the acoustic pressure magnitude. 
    magnitude: float = None

    # A SymbolicConstant specifying the propagation state of the acoustic pressure magnitude. 
    # Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED. 
    magnitudeState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the amplitude reference. Possible 
    # values are UNSET, SET, UNCHANGED, FREED, and MODIFIED. 
    amplitudeState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the BoundaryConditionState 
    # object. Possible values 
    # are:NOT_YET_ACTIVECREATEDPROPAGATEDMODIFIEDDEACTIVATEDNO_LONGER_ACTIVETYPE_NOT_APPLICABLEINSTANCE_NOT_APPLICABLEPROPAGATED_FROM_BASE_STATEMODIFIED_FROM_BASE_STATEDEACTIVATED_FROM_BASE_STATEBUILT_INTO_MODES 
    status: SymbolicConstant = None

    # A String specifying the name of the amplitude reference. The String is empty if the 
    # boundary condition has no amplitude reference. 
    amplitude: str = ''
