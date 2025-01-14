from abaqusConstants import *
from .StopCondition import StopCondition


class LocalStopCondition(StopCondition):
    """The LocalStopCondition object defines a local stop condition.
    The LocalStopCondition object is derived from the StopCondition object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import optimization
        mdb.models[name].optimizationTasks[name].stopConditions[name]

    """

    def __init__(self, name: str, referenceFactor: float, comparisonOperation: SymbolicConstant = LESS_THAN,
                 identifier: SymbolicConstant = MOVEMENT,
                 identifierOperation: SymbolicConstant = MAXIMUM,
                 referenceDesignCycle: SymbolicConstant = PREVIOUS,
                 referenceOperation: SymbolicConstant = ADD, region: SymbolicConstant = MODEL):
        """This method creates a LocalStopCondition object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      mdb.models[name].optimizationTasks[name].LocalStopCondition
        
        Parameters
        ----------
        name
            A String specifying the stop condition repository key. 
        referenceFactor
            A Float specifying the factor used to modify the reference value. 
        comparisonOperation
            A SymbolicConstant specifying the operation used to compare the selected value to the 
            reference value. Possible values are LESS_THAN, LESS_THAN_EQUAL, EQUAL, 
            GREATER_THAN_EQUAL, and GREATER_THAN. The default value is LESS_THAN. 
        identifier
            A SymbolicConstant specifying the variable identifier of the compared value. Possible 
            values are: 
            - ABSOLUTE_GROWTH_MOVEMENT 
            - ABSOLUTE_SHRINK_MOVEMENT 
            - GROWTH_MOVEMENT 
            - SHRINK_MOVEMENT 
            - MOVEMENT 
            - TOTAL_ABSOLUTE_MOVEMENT 
            - EQUIV_STRESS 
            - FREE_TASK_REGION_EQUIV_STRESS 
            - RESTRICTED_TASK_REGION_EQUIV_STRESS 
            - SURFACE_POINT_EQUIV_STRESS 
            - TASK_REGION_EQUIV_STRESS 
            The default value is MOVEMENT. 
        identifierOperation
            A SymbolicConstant specifying the operation used to evaluate values in the region. 
            Possible values are MAXIMUM, MINIMUM, and SUM. The default value is MAXIMUM. 
        referenceDesignCycle
            A SymbolicConstant specifying the iteration from which a value is compared to the 
            reference value. Possible values are FIRST and PREVIOUS. The default value is PREVIOUS. 
        referenceOperation
            A SymbolicConstant specifying the operation used to modify the reference value by the 
            reference factor. Possible values are ADD, DIVIDE, MULTIPLY, and SUBTRACT. The default 
            value is ADD. 
        region
            The SymbolicConstant MODEL or a Region object specifying the region to which the stop 
            condition is applied. The default value is MODEL. 

        Returns
        -------
            A LocalStopCondition object.
        """
        super().__init__()
        pass

    def setValues(self, comparisonOperation: SymbolicConstant = LESS_THAN,
                  identifier: SymbolicConstant = MOVEMENT,
                  identifierOperation: SymbolicConstant = MAXIMUM,
                  referenceDesignCycle: SymbolicConstant = PREVIOUS,
                  referenceOperation: SymbolicConstant = ADD, region: SymbolicConstant = MODEL):
        """This method modifies the LocalStopCondition object.
        
        Parameters
        ----------
        comparisonOperation
            A SymbolicConstant specifying the operation used to compare the selected value to the 
            reference value. Possible values are LESS_THAN, LESS_THAN_EQUAL, EQUAL, 
            GREATER_THAN_EQUAL, and GREATER_THAN. The default value is LESS_THAN. 
        identifier
            A SymbolicConstant specifying the variable identifier of the compared value. Possible 
            values are: 
            - ABSOLUTE_GROWTH_MOVEMENT 
            - ABSOLUTE_SHRINK_MOVEMENT 
            - GROWTH_MOVEMENT 
            - SHRINK_MOVEMENT 
            - MOVEMENT 
            - TOTAL_ABSOLUTE_MOVEMENT 
            - EQUIV_STRESS 
            - FREE_TASK_REGION_EQUIV_STRESS 
            - RESTRICTED_TASK_REGION_EQUIV_STRESS 
            - SURFACE_POINT_EQUIV_STRESS 
            - TASK_REGION_EQUIV_STRESS 
            The default value is MOVEMENT. 
        identifierOperation
            A SymbolicConstant specifying the operation used to evaluate values in the region. 
            Possible values are MAXIMUM, MINIMUM, and SUM. The default value is MAXIMUM. 
        referenceDesignCycle
            A SymbolicConstant specifying the iteration from which a value is compared to the 
            reference value. Possible values are FIRST and PREVIOUS. The default value is PREVIOUS. 
        referenceOperation
            A SymbolicConstant specifying the operation used to modify the reference value by the 
            reference factor. Possible values are ADD, DIVIDE, MULTIPLY, and SUBTRACT. The default 
            value is ADD. 
        region
            The SymbolicConstant MODEL or a Region object specifying the region to which the stop 
            condition is applied. The default value is MODEL. 
        """
        pass
