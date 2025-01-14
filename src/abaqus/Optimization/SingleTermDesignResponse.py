from abaqusConstants import *
from .DesignResponse import DesignResponse
from .StepOptionArray import StepOptionArray


class SingleTermDesignResponse(DesignResponse):
    """The SingleTermDesignResponse object defines a single-term design response.
    The SingleTermDesignResponse object is derived from the DesignResponse object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import optimization
        mdb.models[name].optimizationTasks[name].designResponses[name]

    """

    def __init__(self, name: str, identifier: str, csys: int = None, drivingRegion: str = None,
                 operation: SymbolicConstant = SUM, region: SymbolicConstant = MODEL,
                 shellLayer: SymbolicConstant = MAXIMUM, stepOperation: SymbolicConstant = SUM,
                 stepOptions: StepOptionArray = None):
        """This method creates a SingleTermDesignResponse object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      mdb.models[name].optimizationTasks[name].SingleTermDesignResponse
        
        Parameters
        ----------
        name
            A String specifying the design response repository key. 
        identifier
            A String specifying the name of the variable identifier. 
        csys
            None or a DatumCsys object specifying the local coordinate system. If *csys*=None, the 
            global coordinate system is used. When this member is queried, it returns an Int. The 
            default value is None. 
        drivingRegion
            None or a sequence of Floats specifying the driving region used when *identifier* is an 
            internal nodal variable. The default value is None. 
        operation
            A SymbolicConstant specifying the operation used on values in the region. Possible 
            values are MAXIMUM, MINIMUM, and SUM. The default value is SUM. 
        region
            The SymbolicConstant MODEL or a Region object specifying the region of the design 
            response variable. The default value is MODEL. 
        shellLayer
            A SymbolicConstant specifying the location used for shell layer values. Possible values 
            are BOTTOM, MAXIMUM, MIDDLE, MINIMUM, and TOP. The default value is MAXIMUM. 
        stepOperation
            A SymbolicConstant specifying the operation used on values across steps and load cases. 
            Possible values are MAXIMUM, MINIMUM, and SUM. The default value is SUM. 
        stepOptions
            A StepOptionArray object. 

        Returns
        -------
            A SingleTermDesignResponse object.
        """
        super().__init__()
        pass

    def setValues(self, csys: int = None, drivingRegion: str = None, operation: SymbolicConstant = SUM,
                  region: SymbolicConstant = MODEL, shellLayer: SymbolicConstant = MAXIMUM,
                  stepOperation: SymbolicConstant = SUM, stepOptions: StepOptionArray = None):
        """This method modifies the SingleTermDesignResponse object.
        
        Parameters
        ----------
        csys
            None or a DatumCsys object specifying the local coordinate system. If *csys*=None, the 
            global coordinate system is used. When this member is queried, it returns an Int. The 
            default value is None. 
        drivingRegion
            None or a sequence of Floats specifying the driving region used when *identifier* is an 
            internal nodal variable. The default value is None. 
        operation
            A SymbolicConstant specifying the operation used on values in the region. Possible 
            values are MAXIMUM, MINIMUM, and SUM. The default value is SUM. 
        region
            The SymbolicConstant MODEL or a Region object specifying the region of the design 
            response variable. The default value is MODEL. 
        shellLayer
            A SymbolicConstant specifying the location used for shell layer values. Possible values 
            are BOTTOM, MAXIMUM, MIDDLE, MINIMUM, and TOP. The default value is MAXIMUM. 
        stepOperation
            A SymbolicConstant specifying the operation used on values across steps and load cases. 
            Possible values are MAXIMUM, MINIMUM, and SUM. The default value is SUM. 
        stepOptions
            A StepOptionArray object. 
        """
        pass
