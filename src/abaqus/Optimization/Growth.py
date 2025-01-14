from abaqusConstants import *
from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


class Growth(GeometricRestriction):
    """The Growth object defines a growth geometric restriction.
    The Growth object is derived from the GeometricRestriction object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]

    """

    def __init__(self, name: str, region: Region, growth: float = 0,
                 presumeFeasibleRegionAtStart: Boolean = ON, shrink: float = 0):
        """This method creates a Growth object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      mdb.models[name].optimizationTasks[name].Growth
        
        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key. 
        region
            A Region object specifying the region to which the geometric restriction is applied. 
            When used with a TopologyTask, there is no default value. When used with a ShapeTask, 
            the default value is MODEL. 
        growth
            A Float specifying the maximum optimization displacement in the growth direction. Either 
            *growth* or *shrink* or both must be specified. The default value is 0.0. 
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design 
            cycle. The default value is ON. 
        shrink
            A Float specifying the maximum optimization displacement in the shrink direction. Either 
            *growth* or *shrink* or both must be specified The default value is 0.0. 

        Returns
        -------
            A Growth object.
        """
        super().__init__()
        pass

    def setValues(self, growth: float = 0, presumeFeasibleRegionAtStart: Boolean = ON, shrink: float = 0):
        """This method modifies the Growth object.
        
        Parameters
        ----------
        growth
            A Float specifying the maximum optimization displacement in the growth direction. Either 
            *growth* or *shrink* or both must be specified. The default value is 0.0. 
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design 
            cycle. The default value is ON. 
        shrink
            A Float specifying the maximum optimization displacement in the shrink direction. Either 
            *growth* or *shrink* or both must be specified The default value is 0.0. 
        """
        pass
