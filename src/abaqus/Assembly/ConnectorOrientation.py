from abaqusConstants import *
from ..Datum.DatumCsys import DatumCsys
from ..Region.Set import Set


class ConnectorOrientation:
    """The ConnectorOrientation object is used to assign a connector orientation to a
    connector. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import assembly
        mdb.models[name].rootAssembly.connectorOrientations[i]
        import odbAccess
        session.odbs[name].rootAssembly.connectorOrientations[i]

    """
    region: Set
    localCsys1: DatumCsys = DatumCsys()
    axis1: SymbolicConstant = AXIS_1,
    angle1: float = 0
    orient2sameAs1: Boolean = ON
    localCsys2: DatumCsys = DatumCsys()
    axis2: SymbolicConstant = AXIS_1
    angle2: float = 0

    def __init__(self, region: Set, localCsys1: DatumCsys = DatumCsys(), axis1: SymbolicConstant = AXIS_1,
                 angle1: float = 0, orient2sameAs1: Boolean = ON, localCsys2: DatumCsys = DatumCsys(),
                 axis2: SymbolicConstant = AXIS_1, angle2: float = 0):
        """This method creates a ConnectorOrientation object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].rootAssembly.ConnectorOrientation
            session.odbs[name].rootAssembly.ConnectorOrientation
        
        Parameters
        ----------
        region
            A Set object specifying the region to which the orientation is assigned. 
        localCsys1
            A DatumCsys object specifying the local coordinate system of the first connector point. 
            This value may be None, indicating the global coordinate system. 
        axis1
            A SymbolicConstant specifying the axis of a datum coordinate system about which an 
            additional rotation is applied. Possible values are AXIS_1, AXIS_2, and AXIS_3. The 
            default value is AXIS_1. 
        angle1
            A Float specifying the angle of the additional rotation. The default value is 0.0. 
        orient2sameAs1
            A Boolean specifying whether or not the second connector point is to use the same local 
            coordinate system, axis, and angle as the first point. The default value is ON. 
        localCsys2
            A DatumCsys object specifying the local coordinate system of the second connector point. 
            This value may be None, indicating the global coordinate system. 
        axis2
            A SymbolicConstant specifying the axis of a datum coordinate system about which an 
            additional rotation is applied. Possible values are AXIS_1, AXIS_2, and AXIS_3. The 
            default value is AXIS_1. 
        angle2
            A Float specifying the angle of the additional rotation. The default value is 0.0. 

        Returns
        -------
            A ConnectorOrientation object.
        """
        pass

    def setValues(self):
        """This method modifies the ConnectorOrientation object.
        """
        pass
