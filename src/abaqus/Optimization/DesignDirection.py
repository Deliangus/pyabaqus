from abaqusConstants import *
from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


class DesignDirection(GeometricRestriction):
    """The DesignDirection object defines a design direction geometric restriction.
    The DesignDirection object is derived from the GeometricRestriction object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]

    """

    def __init__(self, name: str, region: Region, csys: int = None, mainPoint: str = None,
                 mainPointDetermination: SymbolicConstant = MAXIMUM,
                 movementRestriction: SymbolicConstant = VECTOR,
                 presumeFeasibleRegionAtStart: Boolean = ON, u1: Boolean = ON, u2: Boolean = ON,
                 u3: Boolean = ON):
        """This method creates a DesignDirection object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      mdb.models[name].optimizationTasks[name].DesignDirection
        
        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key. 
        region
            A Region object specifying the region to which the geometric restriction is applied. 
            When used with a TopologyTask, there is no default value. When used with a ShapeTask, 
            the default value is MODEL. 
        csys
            None or a DatumCsys object specifying the local coordinate system. If *csys*=None, the 
            global coordinate system is used. When this member is queried, it returns an Int. The 
            default value is None. 
        mainPoint
            None or a Region object specifying the main point used when *mainPointDetermination* is 
            SPECIFY. The default value is None. 
        mainPointDetermination
            A SymbolicConstant specifying the rule for assigning point priority. Possible values are 
            MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM. 
        movementRestriction
            A SymbolicConstant specifying whether movement in the region should follow only the 
            direction of the *mainPoint*, only the magnitude, or both the magnitude of the 
            *mainPoint* and the directions specified by *u1*, *u2* and *u3*. Possible values are 
            DIRECTION, MAGNITUDE, and VECTOR. The default value is VECTOR. 
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design 
            cycle. The default value is ON. 
        u1
            A Boolean specifying whether movement in the region should follow the *masterPoint* in 
            the 1-direction. This is used when *movementRestriction* is VECTOR. The default value is 
            ON. 
        u2
            A Boolean specifying whether movement in the region should follow the *masterPoint* in 
            the 2-direction. This is used when *movementRestriction* is VECTOR. The default value is 
            ON. 
        u3
            A Boolean specifying whether movement in the region should follow the *masterPoint* in 
            the 3-direction. This is used when *movementRestriction* is VECTOR. The default value is 
            ON. 

        Returns
        -------
            A DesignDirection object.
        """
        super().__init__()
        pass

    def setValues(self, csys: int = None, mainPoint: str = None,
                  mainPointDetermination: SymbolicConstant = MAXIMUM,
                  movementRestriction: SymbolicConstant = VECTOR,
                  presumeFeasibleRegionAtStart: Boolean = ON, u1: Boolean = ON, u2: Boolean = ON,
                  u3: Boolean = ON):
        """This method modifies the DesignDirection object.
        
        Parameters
        ----------
        csys
            None or a DatumCsys object specifying the local coordinate system. If *csys*=None, the 
            global coordinate system is used. When this member is queried, it returns an Int. The 
            default value is None. 
        mainPoint
            None or a Region object specifying the main point used when *mainPointDetermination* is 
            SPECIFY. The default value is None. 
        mainPointDetermination
            A SymbolicConstant specifying the rule for assigning point priority. Possible values are 
            MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM. 
        movementRestriction
            A SymbolicConstant specifying whether movement in the region should follow only the 
            direction of the *mainPoint*, only the magnitude, or both the magnitude of the 
            *mainPoint* and the directions specified by *u1*, *u2* and *u3*. Possible values are 
            DIRECTION, MAGNITUDE, and VECTOR. The default value is VECTOR. 
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design 
            cycle. The default value is ON. 
        u1
            A Boolean specifying whether movement in the region should follow the *masterPoint* in 
            the 1-direction. This is used when *movementRestriction* is VECTOR. The default value is 
            ON. 
        u2
            A Boolean specifying whether movement in the region should follow the *masterPoint* in 
            the 2-direction. This is used when *movementRestriction* is VECTOR. The default value is 
            ON. 
        u3
            A Boolean specifying whether movement in the region should follow the *masterPoint* in 
            the 3-direction. This is used when *movementRestriction* is VECTOR. The default value is 
            ON. 
        """
        pass
