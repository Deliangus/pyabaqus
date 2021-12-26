from abaqusConstants import *
from .BoundaryCondition import BoundaryCondition
from ..Region.Region import Region


class EulerianBC(BoundaryCondition):

    """The EulerianBC object stores the data for an Eulerian boundary condition. 
    The EulerianBC object is derived from the BoundaryCondition object. 

    Access
    ------
        - import load
        - mdb.models[name].boundaryConditions[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the boundary condition repository key. 
    name: str = ''

    # A SymbolicConstant specifying the flow conditions to be defined. Possible values are 
    # INFLOW, OUTFLOW, and BOTH. The default value is INFLOW. 
    definition: SymbolicConstant = INFLOW

    # A SymbolicConstant specifying the control of material flow into the Eulerian domain. 
    # Possible values are FREE, NONE, and VOID. The default value is FREE. 
    inflowType: SymbolicConstant = FREE

    # A SymbolicConstant specifying the control of flow of material out of the Eulerian 
    # domain. Possible values are ZERO_PRESSURE, FREE, NON_REFLECTING, and EQUILIBRIUM. The 
    # default value is ZERO_PRESSURE. 
    outflowType: SymbolicConstant = ZERO_PRESSURE

    # A SymbolicConstant specifying the category of the boundary condition. Possible values 
    # are MECHANICAL and THERMAL. 
    category: SymbolicConstant = None

    # A Region object specifying the region to which the boundary condition is applied. 
    region: Region = None

    # None or a DatumCsys object specifying the local coordinate system of the boundary 
    # condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
    # in the global coordinate system. The default value is None. 
    localCsys: str = None

    def __init__(self, name: str, createStepName: str, region: Region, definition: SymbolicConstant = INFLOW, 
                 inflowType: SymbolicConstant = FREE, outflowType: SymbolicConstant = ZERO_PRESSURE):
        """This method creates a EulerianBC object.

        Path
        ----
            - mdb.models[name].EulerianBC

        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        definition
            A SymbolicConstant specifying the flow conditions to be defined. Possible values are 
            INFLOW, OUTFLOW, and BOTH. The default value is INFLOW. 
        inflowType
            A SymbolicConstant specifying the control of material flow into the Eulerian domain. 
            Possible values are FREE, NONE, and VOID. The default value is FREE. 
        outflowType
            A SymbolicConstant specifying the control of flow of material out of the Eulerian 
            domain. Possible values are ZERO_PRESSURE, FREE, NON_REFLECTING, and EQUILIBRIUM. The 
            default value is ZERO_PRESSURE. 

        Returns
        -------
            An EulerianBC object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def setValues(self, region: Region = None, definition: SymbolicConstant = INFLOW, 
                  inflowType: SymbolicConstant = FREE, outflowType: SymbolicConstant = ZERO_PRESSURE):
        """This method modifies the data for an existing EulerianBC object in the step where it is
        created.

        Parameters
        ----------
        region
            A Region object specifying the region to which the boundary condition is applied. 
        definition
            A SymbolicConstant specifying the material flow conditions to be defined. Possible 
            values are INFLOW, OUTFLOW, and BOTH. The default value is INFLOW. 
        inflowType
            A SymbolicConstant specifying the control of material flow into the Eulerian domain. 
            Possible values are FREE, NONE, and VOID. The default value is FREE. 
        outflowType
            A SymbolicConstant specifying the control of material flow out of the Eulerian domain. 
            Possible values are ZERO_PRESSURE, FREE, NON_REFLECTING, and EQUILIBRIUM. The default 
            value is ZERO_PRESSURE. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValuesInStep(self, stepName: str, definition: SymbolicConstant = INFLOW, 
                        inflowType: SymbolicConstant = FREE, outflowType: SymbolicConstant = ZERO_PRESSURE):
        """This method modifies the propagating data for an existing EulerianBC object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified. 
        definition
            A SymbolicConstant specifying the material flow conditions to be defined. Possible 
            values are INFLOW, OUTFLOW, and BOTH. The default value is INFLOW. 
        inflowType
            A SymbolicConstant specifying the control of material flow into the Eulerian domain. 
            Possible values are FREE, NONE, and VOID. The default value is FREE. 
        outflowType
            A SymbolicConstant specifying the control of material flow out of the Eulerian domain. 
            Possible values are ZERO_PRESSURE, FREE, NON_REFLECTING, and EQUILIBRIUM. The default 
            value is ZERO_PRESSURE. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
