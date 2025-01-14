from abaqusConstants import *


class OptimizationConstraint:
    """The OptimizationConstraint object constrains an optimization from making changes to the
    topology of the model. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import optimization
        mdb.models[name].optimizationTasks[name].optimizationConstraints[name]

    """

    def __init__(self, name: str, designResponse: str, restrictionValue: float,
                 restrictionMethod: SymbolicConstant = ABSOLUTE_EQUAL):
        """This method creates an OptimizationConstraint object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      mdb.models[name].optimizationTasks[name].OptimizationConstraint
        
        Parameters
        ----------
        name
            A String specifying the optimization constraint repository key. 
        designResponse
            A String specifying the name of the design response to constrain. 
        restrictionValue
            A Float specifying the value to which the design response should be constrained. 
        restrictionMethod
            A SymbolicConstant specifying the method used to constrain the design response. Possible 
            values are ABSOLUTE_EQUAL, ABSOLUTE_GREATER_THAN_EQUAL, ABSOLUTE_LESS_THAN_EQUAL, 
            RELATIVE_EQUAL, RELATIVE_GREATER_THAN_EQUAL, and RELATIVE_LESS_THAN_EQUAL. The default 
            value is ABSOLUTE_EQUAL. 

        Returns
        -------
            An OptimizationConstraint object. 
            
        Raises
        ------
        InvalidNameError
        RangeError 
        """
        pass

    def setValues(self, restrictionMethod: SymbolicConstant = ABSOLUTE_EQUAL):
        """This method modifies the OptimizationConstraint object.
        
        Parameters
        ----------
        restrictionMethod
            A SymbolicConstant specifying the method used to constrain the design response. Possible 
            values are ABSOLUTE_EQUAL, ABSOLUTE_GREATER_THAN_EQUAL, ABSOLUTE_LESS_THAN_EQUAL, 
            RELATIVE_EQUAL, RELATIVE_GREATER_THAN_EQUAL, and RELATIVE_LESS_THAN_EQUAL. The default 
            value is ABSOLUTE_EQUAL.

        Raises
        ------
        RangeError
        """
        pass
