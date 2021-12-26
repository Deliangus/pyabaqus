from abaqusConstants import *
from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


class BeadPlanarSymmetry(GeometricRestriction):

    """The BeadPlanarSymmetry object defines a bead planar symmetry geometric restriction. 
    The BeadPlanarSymmetry object is derived from the GeometricRestriction object. 

    Access
    ------
        - import optimization
        - mdb.models[name].optimizationTasks[name].geometricRestrictions[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def __init__(self, name: str, region: Region, axis: SymbolicConstant = AXIS_1, csys: int = None):
        """This method creates a BeadPlanarSymmetry object.

        Path
        ----
            -           mdb.models[name].optimizationTasks[name].BeadPlanarSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key. 
        region
            A Region object specifying the region to which the geometric restriction is applied. 
        axis
            A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2, 
            and AXIS_3. The default value is AXIS_1. 
        csys
            None or a DatumCsys object specifying the local coordinate system. If *csys*=None, the 
            global coordinate system is used. When this member is queried, it returns an Int. The 
            default value is None. 

        Returns
        -------
            A BeadPlanarSymmetry object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def setValues(self, axis: SymbolicConstant = AXIS_1, csys: int = None):
        """This method modifies the BeadPlanarSymmetry object.

        Parameters
        ----------
        axis
            A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2, 
            and AXIS_3. The default value is AXIS_1. 
        csys
            None or a DatumCsys object specifying the local coordinate system. If *csys*=None, the 
            global coordinate system is used. When this member is queried, it returns an Int. The 
            default value is None. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
