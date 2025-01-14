from abaqusConstants import *
from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


class TopologyRotationalSymmetry(GeometricRestriction):
    """The TopologyRotationalSymmetry object defines a topology rotational symmetry geometric
    restriction. 
    The TopologyRotationalSymmetry object is derived from the GeometricRestriction object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]

    """

    def __init__(self, name: str, angle: float, region: Region, axis: SymbolicConstant = AXIS_1,
                 csys: int = None, ignoreFrozenArea: Boolean = OFF):
        """This method creates a TopologyRotationalSymmetry object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      mdb.models[name].optimizationTasks[name].TopologyRotationalSymmetry
        
        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key. 
        angle
            A Float specifying the repeating segment size, an angle in degrees. 
        region
            A Region object specifying the region to which the geometric restriction is applied. 
            When used with a TopologyTask, there is no default value. When used with a ShapeTask, 
            the default value is MODEL. 
        axis
            A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2, 
            and AXIS_3. The default value is AXIS_1. 
        csys
            None or a DatumCsys object specifying the local coordinate system. If *csys*=None, the 
            global coordinate system is used. When this member is queried, it returns an Int. The 
            default value is None. 
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF. 

        Returns
        -------
            A TopologyRotationalSymmetry object.
        """
        super().__init__()
        pass

    def setValues(self, axis: SymbolicConstant = AXIS_1, csys: int = None, ignoreFrozenArea: Boolean = OFF):
        """This method modifies the TopologyRotationalSymmetry object.
        
        Parameters
        ----------
        axis
            A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2, 
            and AXIS_3. The default value is AXIS_1. 
        csys
            None or a DatumCsys object specifying the local coordinate system. If *csys*=None, the 
            global coordinate system is used. When this member is queried, it returns an Int. The 
            default value is None. 
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF. 
        """
        pass
