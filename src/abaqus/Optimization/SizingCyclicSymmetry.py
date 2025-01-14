from abaqusConstants import *
from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


class SizingCyclicSymmetry(GeometricRestriction):
    """The SizingCyclicSymmetry object defines a sizing cyclic symmetry geometric restriction.
    The SizingCyclicSymmetry object is derived from the GeometricRestriction object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]

    """

    def __init__(self, name: str, region: Region, translation: float, axis: SymbolicConstant = AXIS_1,
                 csys: int = None, ignoreFrozenArea: Boolean = OFF):
        """This method creates a SizingCyclicSymmetry object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      mdb.models[name].optimizationTasks[name].SizingCyclicSymmetry
        
        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key. 
        region
            A Region object specifying the region to which the geometric restriction is applied. 
        translation
            A Float specifying the translation distance. 
        axis
            A SymbolicConstant specifying the translation direction defined along an axis positioned 
            at the *csys* origin. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value 
            is AXIS_1. 
        csys
            None or a DatumCsys object specifying the local coordinate system. If *csys*=None, the 
            global coordinate system is used. When this member is queried, it returns an Int. The 
            default value is None. 
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF. 

        Returns
        -------
            A SizingCyclicSymmetry object.
        """
        super().__init__()
        pass

    def setValues(self, axis: SymbolicConstant = AXIS_1, csys: int = None, ignoreFrozenArea: Boolean = OFF):
        """This method modifies the SizingCyclicSymmetry object.
        
        Parameters
        ----------
        axis
            A SymbolicConstant specifying the translation direction defined along an axis positioned 
            at the *csys* origin. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value 
            is AXIS_1. 
        csys
            None or a DatumCsys object specifying the local coordinate system. If *csys*=None, the 
            global coordinate system is used. When this member is queried, it returns an Int. The 
            default value is None. 
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF. 
        """
        pass
