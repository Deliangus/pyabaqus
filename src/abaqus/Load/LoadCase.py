from abaqusConstants import *


class LoadCase:
    """The LoadCase object is used to define the loads and constraints comprising a particular
    loading condition and the linear response of a structure subjected to that loading 
    condition. 

    Attributes
    ----------
    suppressed: Boolean
        A Boolean specifying whether the load case is suppressed or not. The default value is
        OFF.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import step
        mdb.models[name].steps[name].loadCases[name]

    """

    # A Boolean specifying whether the load case is suppressed or not. The default value is 
    # OFF. 
    suppressed: Boolean = OFF

    def __init__(self, name: str, boundaryConditions: tuple = (), loads: tuple = (),
                 includeActiveBaseStateBC: Boolean = ON):
        """This method creates a load case in a step.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].steps[name].LoadCase
        
        Parameters
        ----------
        name
            A String specifying the name of the object. 
        boundaryConditions
            A sequence of (String, Float) sequences specifying the name of a BoundaryCondition 
            followed by a nonzero Float scaling factor. The default value is an empty sequence. 
        loads
            A sequence of (String, Float) sequences specifying the name of a Load followed by a 
            nonzero Float specifying a scale factor. The default value is an empty sequence. 
        includeActiveBaseStateBC
            A Boolean specifying whether to include all active boundary conditions propagated or 
            modified from the base state. The default value is ON. 

        Returns
        -------
        case: LoadCase
            A LoadCase object
        """
        pass

    def resume(self):
        """This method resumes the load case that was previously suppressed.
        """
        pass

    def suppress(self):
        """This method suppresses the load case.
        """
        pass

    def setValues(self, boundaryConditions: tuple = (), loads: tuple = (),
                  includeActiveBaseStateBC: Boolean = ON):
        """This method modifies the LoadCase object.
        
        Parameters
        ----------
        boundaryConditions
            A sequence of (String, Float) sequences specifying the name of a BoundaryCondition 
            followed by a nonzero Float scaling factor. The default value is an empty sequence. 
        loads
            A sequence of (String, Float) sequences specifying the name of a Load followed by a 
            nonzero Float specifying a scale factor. The default value is an empty sequence. 
        includeActiveBaseStateBC
            A Boolean specifying whether to include all active boundary conditions propagated or 
            modified from the base state. The default value is ON. 
        """
        pass
