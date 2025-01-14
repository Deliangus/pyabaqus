from abaqusConstants import *
from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


class SizingPointSymmetry(GeometricRestriction):
    """The SizingPointSymmetry object defines a sizing point symmetry geometric restriction.
    The SizingPointSymmetry object is derived from the GeometricRestriction object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]

    """

    def __init__(self, name: str, region: Region, csys: int = None, ignoreFrozenArea: Boolean = OFF):
        """This method creates a SizingPointSymmetry object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      mdb.models[name].optimizationTasks[name].SizingPointSymmetry
        
        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key. 
        region
            A Region object specifying the region to which the geometric restriction is applied. 
        csys
            None or a DatumCsys object specifying the position of the symmetry point defined as the 
            origin of a local coordinate system. If *csys*=None, the global coordinate system is 
            used. When this member is queried, it returns an Int. The default value is None. 
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF. 

        Returns
        -------
            A SizingPointSymmetry object.
        """
        super().__init__()
        pass

    def setValues(self, csys: int = None, ignoreFrozenArea: Boolean = OFF):
        """This method modifies the SizingPointSymmetry object.
        
        Parameters
        ----------
        csys
            None or a DatumCsys object specifying the position of the symmetry point defined as the 
            origin of a local coordinate system. If *csys*=None, the global coordinate system is 
            used. When this member is queried, it returns an Int. The default value is None. 
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF. 
        """
        pass
