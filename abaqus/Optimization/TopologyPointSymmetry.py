from abaqusConstants import *
from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


class TopologyPointSymmetry(GeometricRestriction):

    """The TopologyPointSymmetry object defines a topology point symmetry geometric 
    restriction. 
    The TopologyPointSymmetry object is derived from the GeometricRestriction object. 

    Access
    ------
        - import optimization
        - mdb.models[name].optimizationTasks[name].geometricRestrictions[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def __init__(self, name: str, region: Region, csys: int = None, ignoreFrozenArea: Boolean = OFF):
        """This method creates a TopologyPointSymmetry object.

        Path
        ----
            -           mdb.models[name].optimizationTasks[name].TopologyPointSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key. 
        region
            A Region object specifying the region to which the geometric restriction is applied. 
            When used with a TopologyTask, there is no default value. When used with a ShapeTask, 
            the default value is MODEL. 
        csys
            None or a DatumCsys object specifying the position of the symmetry point defined as the 
            origin of a local coordinate system. If *csys*=None, the global coordinate system is 
            used. When this member is queried, it returns an Int. The default value is None. 
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF. 

        Returns
        -------
            A TopologyPointSymmetry object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def setValues(self, csys: int = None, ignoreFrozenArea: Boolean = OFF):
        """This method modifies the TopologyPointSymmetry object.

        Parameters
        ----------
        csys
            None or a DatumCsys object specifying the position of the symmetry point defined as the 
            origin of a local coordinate system. If *csys*=None, the global coordinate system is 
            used. When this member is queried, it returns an Int. The default value is None. 
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
