from abaqusConstants import *
from .SpringDashpot import SpringDashpot

from __init__ import *


class TwoPointSpringDashpot(SpringDashpot):
    """The TwoPointSpringDashpot object defines springs and/or dashpots between two points on a
    part or an assembly. 
    The TwoPointSpringDashpot object is derived from the SpringDashpot object. 

    Attributes
    ----------
    suppressed: Boolean
        A Boolean specifying whether the spring/dashpot is suppressed or not. The default value
        is OFF.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import part
        mdb.models[name].parts[name].engineeringFeatures.springDashpots[name]
        import assembly
        mdb.models[name].rootAssembly.engineeringFeatures.springDashpots[name]

    The corresponding analysis keywords are:
        - ELEMENT
            - SPRING
            - DASHPOT

    """

    # A Boolean specifying whether the spring/dashpot is suppressed or not. The default value
    # is OFF.
    suppressed: Boolean = OFF

    def __init__(self,
                 name: str,
                 regionPairs: tuple,
                 axis: SymbolicConstant,
                 dof1: int = 0,
                 dof2: int = 0,
                 orientation: str = None,
                 springBehavior: Boolean = OFF,
                 dashpotBehavior: Boolean = OFF,
                 springStiffness: float = 0,
                 dashpotCoefficient: float = 0):
        """This method creates a TwoPointSpringDashpot object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].parts[name].engineeringFeatures.TwoPointSpringDashpot
            mdb.models[name].rootAssembly.engineeringFeatures\
            .TwoPointSpringDashpot
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        regionPairs
            A sequence of pairs of Region objects specifying the points between which the springs 
            and/or dashpots are applied. 
        axis
            A SymbolicConstant specifying whether the axis of the springs and/or dashpots follows 
            the rotation of the nodes or is in a specified direction. Possible values are NODAL_LINE 
            and FIXED_DOF. 
        dof1
            An Int specifying the degree of freedom with which the springs and/or dashpots are 
            associated at their first points. The *dof1* argument applies only when 
            *axis*=FIXED_DOFS. The default value is 0. 
        dof2
            An Int specifying the degree of freedom with which the springs and/or dashpots are 
            associated at their second points. The *dof2* argument applies only when 
            *axis*=FIXED_DOFS. The default value is 0. 
        orientation
            None or a DatumCsys object specifying the local directions for the spring and/or 
            dashpot. If *orientation*=None, the spring and/or dashpot data are defined in the global 
            coordinate system. The default value is None.The *orientation* argument applies only 
            when *axis*=FIXED_DOFS. 
        springBehavior
            A Boolean specifying whether to apply spring behavior to the selected point pairs. The 
            default value is OFF.At least one of the arguments *springBehavior*=ON or 
            *dashpotBehavior*=ON must be specified. 
        dashpotBehavior
            A Boolean specifying whether to apply dashpot behavior to the selected point pairs. The 
            default value is OFF.At least one of the arguments *springBehavior*=ON or 
            *dashpotBehavior*=ON must be specified. 
        springStiffness
            A Float specifying the force per relative displacement for the springs. The default 
            value is 0.0. 
        dashpotCoefficient
            A Float specifying the force per relative velocity for the dashpots. The default value 
            is 0.0. 

        Returns
        -------
            A TwoPointSpringDashpot object.
        """
        super().__init__()
        pass

    def setValues(self,
                  dof1: int = 0,
                  dof2: int = 0,
                  orientation: str = None,
                  springBehavior: Boolean = OFF,
                  dashpotBehavior: Boolean = OFF,
                  springStiffness: float = 0,
                  dashpotCoefficient: float = 0):
        """This method modifies the TwoPointSpringDashpot object.
        
        Parameters
        ----------
        dof1
            An Int specifying the degree of freedom with which the springs and/or dashpots are 
            associated at their first points. The *dof1* argument applies only when 
            *axis*=FIXED_DOFS. The default value is 0. 
        dof2
            An Int specifying the degree of freedom with which the springs and/or dashpots are 
            associated at their second points. The *dof2* argument applies only when 
            *axis*=FIXED_DOFS. The default value is 0. 
        orientation
            None or a DatumCsys object specifying the local directions for the spring and/or 
            dashpot. If *orientation*=None, the spring and/or dashpot data are defined in the global 
            coordinate system. The default value is None.The *orientation* argument applies only 
            when *axis*=FIXED_DOFS. 
        springBehavior
            A Boolean specifying whether to apply spring behavior to the selected point pairs. The 
            default value is OFF.At least one of the arguments *springBehavior*=ON or 
            *dashpotBehavior*=ON must be specified. 
        dashpotBehavior
            A Boolean specifying whether to apply dashpot behavior to the selected point pairs. The 
            default value is OFF.At least one of the arguments *springBehavior*=ON or 
            *dashpotBehavior*=ON must be specified. 
        springStiffness
            A Float specifying the force per relative displacement for the springs. The default 
            value is 0.0. 
        dashpotCoefficient
            A Float specifying the force per relative velocity for the dashpots. The default value 
            is 0.0. 
        """
        pass
