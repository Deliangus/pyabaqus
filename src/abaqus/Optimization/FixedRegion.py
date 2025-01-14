from abaqusConstants import *
from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


class FixedRegion(GeometricRestriction):
    """The FixedRegion object defines a fixed region geometric restriction.
    The FixedRegion object is derived from the GeometricRestriction object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]

    """

    def __init__(self, name: str, region: Region, csys: int = None, presumeFeasibleRegionAtStart: Boolean = ON,
                 u1: Boolean = OFF, u2: Boolean = OFF, u3: Boolean = OFF):
        """This method creates a FixedRegion object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

              mdb.models[name].optimizationTasks[name].FixedRegion
        
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
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design 
            cycle. The default value is ON. 
        u1
            A Boolean specifying whether to fix the region in the 1-direction. The default value is 
            OFF. 
        u2
            A Boolean specifying whether to fix the region in the 2-direction. The default value is 
            OFF. 
        u3
            A Boolean specifying whether to fix the region in the 3-direction. The default value is 
            OFF. 

        Returns
        -------
            A FixedRegion object.
        """
        super().__init__()
        pass

    def setValues(self, csys: int = None, presumeFeasibleRegionAtStart: Boolean = ON, u1: Boolean = OFF,
                  u2: Boolean = OFF, u3: Boolean = OFF):
        """This method modifies the FixedRegion object.
        
        Parameters
        ----------
        csys
            None or a DatumCsys object specifying the local coordinate system. If *csys*=None, the 
            global coordinate system is used. When this member is queried, it returns an Int. The 
            default value is None. 
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design 
            cycle. The default value is ON. 
        u1
            A Boolean specifying whether to fix the region in the 1-direction. The default value is 
            OFF. 
        u2
            A Boolean specifying whether to fix the region in the 2-direction. The default value is 
            OFF. 
        u3
            A Boolean specifying whether to fix the region in the 3-direction. The default value is 
            OFF. 
        """
        pass
