from abaqusConstants import *
from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


class ShapeRotationalSymmetry(GeometricRestriction):
    """The ShapeRotationalSymmetry object defines a shape rotational symmetry geometric
    restriction. 
    The ShapeRotationalSymmetry object is derived from the GeometricRestriction object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]

    """

    def __init__(self, name: str, clientDirection: tuple, region: Region,
                 allowNonSymmetricMesh: Boolean = TRUE, angle: float = 0, csys: int = None,
                 mainPoint: str = None, mainPointDetermination: SymbolicConstant = MAXIMUM,
                 presumeFeasibleRegionAtStart: Boolean = ON, startPoint: float = None,
                 tolerance1: float = 0, tolerance2: float = 0, tolerance3: float = 0):
        """This method creates a ShapeRotationalSymmetry object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      mdb.models[name].optimizationTasks[name].ShapeRotationalSymmetry
        
        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key. 
        clientDirection
            A VertexArray object of length 2 specifying the vector positioned at the *csys* origin, 
            used as the axis of symmetry. Instead of through a ConstrainedSketchVertex, each point might be specified
            through a tuple of coordinates. 
        region
            A Region object specifying the region to which the geometric restriction is applied. 
            When used with a TopologyTask, there is no default value. When used with a ShapeTask, 
            the default value is MODEL. 
        allowNonSymmetricMesh
            A Boolean specifying whether to allow a nonsymmetric mesh for this geometric 
            restriction. The default value is TRUE. 
        angle
            A Float specifying the segment size of the repeating pattern in degrees. If the *angle* 
            value is 0, no repeating pattern is created. The default value is 0.0. 
        csys
            None or a DatumCsys object specifying the local coordinate system. If *csys*=None, the 
            global coordinate system is used. When this member is queried, it returns an Int. The 
            default value is None. 
        mainPoint
            None or a Region object specifying the main point used when *mainPointDetermination* is 
            SPECIFY. The default value is None. 
        mainPointDetermination
            A SymbolicConstant specifying the rule for determining the main node. Possible values 
            are MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM. 
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design 
            cycle. The default value is ON. 
        startPoint
            A tuple of Floats representing the coordinates of a start point of the rotational 
            symmetry. 
        tolerance1
            A Float specifying the geometric tolerance in the 1-direction. The default value is 
            0.01. 
        tolerance2
            A Float specifying the geometric tolerance in the 2-direction. The default value is 
            0.01. 
        tolerance3
            A Float specifying the geometric tolerance in the 3-direction. The default value is 
            0.01. 

        Returns
        -------
            A ShapeRotationalSymmetry object.
        """
        super().__init__()
        pass

    def setValues(self, allowNonSymmetricMesh: Boolean = TRUE, angle: float = 0, csys: int = None,
                  mainPoint: str = None, mainPointDetermination: SymbolicConstant = MAXIMUM,
                  presumeFeasibleRegionAtStart: Boolean = ON, startPoint: float = None,
                  tolerance1: float = 0, tolerance2: float = 0, tolerance3: float = 0):
        """This method modifies the ShapeRotationalSymmetry object.
        
        Parameters
        ----------
        allowNonSymmetricMesh
            A Boolean specifying whether to allow a nonsymmetric mesh for this geometric 
            restriction. The default value is TRUE. 
        angle
            A Float specifying the segment size of the repeating pattern in degrees. If the *angle* 
            value is 0, no repeating pattern is created. The default value is 0.0. 
        csys
            None or a DatumCsys object specifying the local coordinate system. If *csys*=None, the 
            global coordinate system is used. When this member is queried, it returns an Int. The 
            default value is None. 
        mainPoint
            None or a Region object specifying the main point used when *mainPointDetermination* is 
            SPECIFY. The default value is None. 
        mainPointDetermination
            A SymbolicConstant specifying the rule for determining the main node. Possible values 
            are MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM. 
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design 
            cycle. The default value is ON. 
        startPoint
            A tuple of Floats representing the coordinates of a start point of the rotational 
            symmetry. 
        tolerance1
            A Float specifying the geometric tolerance in the 1-direction. The default value is 
            0.01. 
        tolerance2
            A Float specifying the geometric tolerance in the 2-direction. The default value is 
            0.01. 
        tolerance3
            A Float specifying the geometric tolerance in the 3-direction. The default value is 
            0.01. 
        """
        pass
