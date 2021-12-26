from abaqusConstants import *

class LoadCase:

    """The LoadCase object is used to define the loads and constraints comprising a particular 
    loading condition and the linear response of a structure subjected to that loading 
    condition. 

    Access
    ------
        - import step
        - mdb.models[name].steps[name].loadCases[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A Boolean specifying whether the load case is suppressed or not. The default value is 
    # OFF. 
    suppressed: Boolean = OFF

    def __init__(self, name: str, boundaryConditions: tuple = (), loads: tuple = (), 
                 includeActiveBaseStateBC: Boolean = ON):
        """This method creates a load case in a step.

        Path
        ----
            - mdb.models[name].steps[name].LoadCase

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
            A LoadCase object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def resume(self):
        """This method resumes the load case that was previously suppressed.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def suppress(self):
        """This method suppresses the load case.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
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

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
        """
        pass
