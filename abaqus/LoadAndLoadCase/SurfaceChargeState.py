from abaqusConstants import *
from .LoadState import LoadState


class SurfaceChargeState(LoadState):

    """The SurfaceChargeState object stores the propagating data of a surface charge in a step. 
    One instance of this object is created internally by the SurfaceCharge object for each 
    step. The instance is also deleted internally by the SurfaceCharge object. 
    The SurfaceChargeState object has no constructor or methods. 
    The SurfaceChargeState object is derived from the LoadState object. 

    Access
    ------
        - import load
        - mdb.models[name].steps[name].loadStates[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - DSECHARGE

    """

    # A Float specifying the load magnitude. 
    magnitude: float = None

    # A SymbolicConstant specifying the propagation state of the load magnitude. Possible 
    # values are UNSET, SET, UNCHANGED, and FREED. 
    magnitudeState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the *amplitude* member. Possible 
    # values are UNSET, SET, UNCHANGED, and FREED. 
    amplitudeState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the LoadState object. Possible 
    # values are: 
    # - NOT_YET_ACTIVE 
    # - CREATED 
    # - PROPAGATED 
    # - MODIFIED 
    # - DEACTIVATED 
    # - NO_LONGER_ACTIVE 
    # - TYPE_NOT_APPLICABLE 
    # - INSTANCE_NOT_APPLICABLE 
    # - BUILT_INTO_BASE_STATE 
    status: SymbolicConstant = None

    # A String specifying the name of the amplitude reference. The String is empty if the load 
    # has no amplitude reference. 
    amplitude: str = ''
