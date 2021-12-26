from abaqusConstants import *
from .LoadState import LoadState


class BoltLoadState(LoadState):

    """The BoltLoadState object stores the propagating data of a bolt load in a step. One 
    instance of this object is created internally by the BoltLoad object for each step. The 
    instance is also deleted internally by the BoltLoad object. 
    The BoltLoadState object has no constructor or methods. 
    The BoltLoadState object is derived from the LoadState object. 

    Access
    ------
        - import load
        - mdb.models[name].steps[name].loadStates[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - CLOAD
        - BOUNDARY

    """

    # A SymbolicConstant specifying the type of bolt load. Possible values are APPLY_FORCE, 
    # ADJUST_LENGTH, and FIX_LENGTH. 
    boltMethod: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the bolt load type. Possible 
    # values are UNSET, SET, UNCHANGED, and MODIFIED. 
    boltMethodState: SymbolicConstant = None

    # A Float specifying the bolt load magnitude. 
    magnitude: float = None

    # A SymbolicConstant specifying the propagation state of the bolt load magnitude. Possible 
    # values are UNSET, SET, UNCHANGED, and MODIFIED. 
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
