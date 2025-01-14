from abaqusConstants import *
from .BoundaryCondition import BoundaryCondition
from ..Region.Region import Region


class SubmodelBC(BoundaryCondition):
    """The SubmodelBC object stores the data for a submodel boundary condition.
    The SubmodelBC object is derived from the BoundaryCondition object. 

    Attributes
    ----------
    name: str
        A String specifying the boundary condition repository key.
    shellThickness: float
        A Float specifying the thickness of the shell in the global model. This argument is
        required for shell-to-solid submodeling and is not applicable to other submodels. The
        default value is 0.0.
    absoluteExteriorTolerance: float
        None or a Float specifying the absolute value by which a driven node of the submodel can
        lie outside the region of the elements of the global model. The default value is None.
    exteriorTolerance: float
        None or a Float specifying the fraction of the average element size in the global model
        by which a driven node of the submodel can lie outside the region of the elements of the
        global model. The default value is 0.05.
    globalDrivingRegion: str
        A String specifying the element set in the global model that will be searched for
        elements whose responses will be used to drive the submodel. An empty string indicates
        that the entire global model will be searched. The default value is an empty string.
    category: SymbolicConstant
        A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.
    region: Region
        A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
    localCsys: str
        None or a :py:class:`~abaqus.Datum.DatumCsys.DatumCsys` object specifying the local coordinate system of the boundary
        condition's degrees of freedom. If **localCsys=None**, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import load
        mdb.models[name].boundaryConditions[name]

    """

    # A String specifying the boundary condition repository key. 
    name: str = ''

    # A Float specifying the thickness of the shell in the global model. This argument is 
    # required for shell-to-solid submodeling and is not applicable to other submodels. The 
    # default value is 0.0. 
    shellThickness: float = 0

    # None or a Float specifying the absolute value by which a driven node of the submodel can 
    # lie outside the region of the elements of the global model. The default value is None. 
    absoluteExteriorTolerance: float = None

    # None or a Float specifying the fraction of the average element size in the global model 
    # by which a driven node of the submodel can lie outside the region of the elements of the 
    # global model. The default value is 0.05. 
    exteriorTolerance: float = 0

    # A String specifying the element set in the global model that will be searched for 
    # elements whose responses will be used to drive the submodel. An empty string indicates 
    # that the entire global model will be searched. The default value is an empty string. 
    globalDrivingRegion: str = ''

    # A SymbolicConstant specifying the category of the boundary condition. Possible values 
    # are MECHANICAL and THERMAL. 
    category: SymbolicConstant = None

    # A Region object specifying the region to which the boundary condition is applied. 
    region: Region = Region()

    # None or a DatumCsys object specifying the local coordinate system of the boundary 
    # condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
    # in the global coordinate system. The default value is None. 
    localCsys: str = None

    def __init__(self, name: str, createStepName: str, region: Region, dof: tuple, globalStep: str,
                 timeScale: Boolean, shellThickness: float, globalDrivingRegion: str = '',
                 absoluteExteriorTolerance: float = None, exteriorTolerance: float = 0,
                 localCsys: str = None, globalIncrement: int = 0, centerZoneSize: float = None,
                 intersectionOnly: Boolean = OFF):
        """This method creates a SubmodelBC object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].SubmodelBC
        
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        dof
            A sequence of Ints specifying the degrees of freedom to which the boundary condition is 
            applied. 
        globalStep
            A String specifying the step in the global model from which Abaqus reads the values of 
            the variables that will drive the submodel analysis. The String indicates the position 
            of the step in the sequence of analysis steps. For example, *globalStep*='1' indicates 
            the first step. 
        timeScale
            A Boolean specifying whether to scale the time variable for the driven nodes' amplitude 
            functions to match the submodel analysis step time. The default value is OFF. 
        shellThickness
            A Float specifying the thickness of the shell in the global model. This argument is 
            required for shell-to-solid submodeling and is not applicable to other submodels. The 
            default value is 0.0. 
        globalDrivingRegion
            A String specifying the element set in the global model that will be searched for 
            elements whose responses will be used to drive the submodel. An empty string indicates 
            that the entire global model will be searched. The default value is an empty string. 
        absoluteExteriorTolerance
            None or a Float specifying the absolute value by which a driven node of the submodel can 
            lie outside the region of the elements of the global model. The default value is None. 
        exteriorTolerance
            None or a Float specifying the fraction of the average element size in the global model 
            by which a driven node of the submodel can lie outside the region of the elements of the 
            global model. The default value is 0.05. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 
        globalIncrement
            An Int specifying the increment number in the global model step from which the solution 
            will be used to specify the values of the driven variables. If *globalIncrement*=0, the 
            solution from the last increment will be used. The *globalIncrement* argument is 
            applicable only for linear perturbation steps. The default value is 0. 
        centerZoneSize
            A Float specifying the thickness of the center zone size around the shell midsurface. 
            The default value is None. 
        intersectionOnly
            A Boolean specifying whether to ignore driven nodes that lie outside the region of 
            elements of the global model after accounting for the exterior search tolerance. The 
            default value is OFF. 

        Returns
        -------
            A SubmodelBC object.
        """
        super().__init__()
        pass

    def setValues(self, globalDrivingRegion: str = '', absoluteExteriorTolerance: float = None,
                  exteriorTolerance: float = 0, localCsys: str = None, globalIncrement: int = 0,
                  centerZoneSize: float = None, intersectionOnly: Boolean = OFF):
        """This method modifies the data for an existing SubmodelBC object in the step where it is
        created.
        
        Parameters
        ----------
        globalDrivingRegion
            A String specifying the element set in the global model that will be searched for 
            elements whose responses will be used to drive the submodel. An empty string indicates 
            that the entire global model will be searched. The default value is an empty string. 
        absoluteExteriorTolerance
            None or a Float specifying the absolute value by which a driven node of the submodel can 
            lie outside the region of the elements of the global model. The default value is None. 
        exteriorTolerance
            None or a Float specifying the fraction of the average element size in the global model 
            by which a driven node of the submodel can lie outside the region of the elements of the 
            global model. The default value is 0.05. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 
        globalIncrement
            An Int specifying the increment number in the global model step from which the solution 
            will be used to specify the values of the driven variables. If *globalIncrement*=0, the 
            solution from the last increment will be used. The *globalIncrement* argument is 
            applicable only for linear perturbation steps. The default value is 0. 
        centerZoneSize
            A Float specifying the thickness of the center zone size around the shell midsurface. 
            The default value is None. 
        intersectionOnly
            A Boolean specifying whether to ignore driven nodes that lie outside the region of 
            elements of the global model after accounting for the exterior search tolerance. The 
            default value is OFF. 
        """
        pass

    def setValuesInStep(self, stepName: str, fixed: Boolean = ON, dof: tuple = (), globalStep: str = '',
                        globalIncrement: int = 0, centerZoneSize: float = None):
        """This method modifies the propagating data for an existing SubmodelBC object in the
        specified step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified. 
        fixed
            A Boolean specifying whether the boundary condition should remain fixed at the current 
            values at the start of the step. The default value is ON. 
        dof
            A sequence of Ints specifying the degrees of freedom to which the boundary condition is 
            applied. The *dof* argument is applicable only if *fixed*=OFF. 
        globalStep
            A String specifying the step in the global model from which Abaqus reads the values of 
            the variables that will drive the submodel analysis. The String indicates the position 
            of the step in the sequence of analysis steps. For example, *globalStep*='1' indicates 
            the first step. The *globalStep* argument is applicable only if *fixed*=OFF. 
        globalIncrement
            An Int specifying the increment number in the global model step at which the solution 
            will be used to specify the values of the driven variables. If *globalIncrement*=0, the 
            solution from the last increment will be used. The *globalIncrement* argument is 
            applicable only for linear perturbation steps and if *fixed*=OFF. The default value is 
            0. 
        centerZoneSize
            A Float specifying the thickness of the center zone size around the shell midsurface. 
            The default value is None.The *centerZoneSize* argument is applicable only if 
            *fixed*=OFF. 
        """
        pass
