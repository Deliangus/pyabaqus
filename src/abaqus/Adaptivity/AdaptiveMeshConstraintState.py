from abaqusConstants import *


class AdaptiveMeshConstraintState:
    """The AdaptiveMeshConstraintState object is the abstract base type for other Arbitrary
    Lagrangian Eularian (ALE) style AdaptiveMeshConstraintState objects. The 
    AdaptiveMeshConstraintState object has no explicit constructor or methods. The members 
    of the AdaptiveMeshConstraintState object are common to all objects derived from the 
    AdaptiveMeshConstraintState object. 

    Attributes
    ----------
    amplitudeState: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    status: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the AdaptiveMeshConstraintState
        object. Possible values are:
            - NOT_YET_ACTIVE
            - CREATED
            - PROPAGATED
            - MODIFIED
            - DEACTIVATED
            - NO_LONGER_ACTIVE
            - TYPE_NOT_APPLICABLE
            - INSTANCE_NOT_APPLICABLE
            - PROPAGATED_FROM_BASE_STATE
            - MODIFIED_FROM_BASE_STATE
            - DEACTIVATED_FROM_BASE_STATE
            - BUILT_INTO_MODES
    amplitude: str
        A String specifying the name of the amplitude reference. The String is empty if the
        adaptive mesh constraint has no amplitude reference.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import step
        mdb.models[name].steps[name].adaptiveMeshConstraintStates[name]

    """

    # A SymbolicConstant specifying the propagation state of the amplitude reference. Possible 
    # values are UNSET, SET, UNCHANGED, FREED, and MODIFIED. 
    amplitudeState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the AdaptiveMeshConstraintState 
    # object. Possible values are: 
    # - NOT_YET_ACTIVE 
    # - CREATED 
    # - PROPAGATED 
    # - MODIFIED 
    # - DEACTIVATED 
    # - NO_LONGER_ACTIVE 
    # - TYPE_NOT_APPLICABLE 
    # - INSTANCE_NOT_APPLICABLE 
    # - PROPAGATED_FROM_BASE_STATE 
    # - MODIFIED_FROM_BASE_STATE 
    # - DEACTIVATED_FROM_BASE_STATE 
    # - BUILT_INTO_MODES 
    status: SymbolicConstant = None

    # A String specifying the name of the amplitude reference. The String is empty if the 
    # adaptive mesh constraint has no amplitude reference. 
    amplitude: str = ''

    def __init__(self, amplitudeState: SymbolicConstant = None, status: SymbolicConstant = None, amplitude: str = ''):
        """The AdaptiveMeshConstraintState object is the abstract base type for other Arbitrary
        Lagrangian Eularian (ALE) style AdaptiveMeshConstraintState objects. The
        AdaptiveMeshConstraintState object has no explicit constructor or methods. The members
        of the AdaptiveMeshConstraintState object are common to all objects derived from the
        AdaptiveMeshConstraintState object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].steps[name].AdaptiveMeshConstraintState
            
        Parameters
        ----------
        amplitudeState
             A SymbolicConstant specifying the propagation state of the amplitude reference. Possible  values are
             UNSET, SET, UNCHANGED, FREED, and MODIFIED.
        status
             A SymbolicConstant specifying the propagation state of the AdaptiveMeshConstraintState  object. Possible
             values are:
             - NOT_YET_ACTIVE
             - CREATED
             - PROPAGATED
             - MODIFIED
             - DEACTIVATED
             - NO_LONGER_ACTIVE
             - TYPE_NOT_APPLICABLE
             - INSTANCE_NOT_APPLICABLE
             - PROPAGATED_FROM_BASE_STATE
             - MODIFIED_FROM_BASE_STATE
             - DEACTIVATED_FROM_BASE_STATE
             - BUILT_INTO_MODES
        amplitude
             A String specifying the name of the amplitude reference. The String is empty if the  adaptive mesh
             constraint has no amplitude reference.
        """
        pass
