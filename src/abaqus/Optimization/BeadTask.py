from abaqusConstants import *
from .DesignResponse import DesignResponse
from .GeometricRestriction import GeometricRestriction
from .ObjectiveFunction import ObjectiveFunction
from .OptimizationConstraint import OptimizationConstraint
from .OptimizationTask import OptimizationTask


class BeadTask(OptimizationTask):
    """The BeadTask object defines a bead task.
    The BeadTask object is derived from the OptimizationTask object. 

    Attributes
    ----------
    designResponses: dict[str, DesignResponse]
        A repository of :py:class:`~abaqus.Optimization.DesignResponse.DesignResponse` objects.
    objectiveFunctions: dict[str, ObjectiveFunction]
        A repository of :py:class:`~abaqus.Optimization.ObjectiveFunction.ObjectiveFunction` objects.
    optimizationConstraints: dict[str, OptimizationConstraint]
        A repository of :py:class:`~abaqus.Optimization.OptimizationConstraint.OptimizationConstraint` objects.
    geometricRestrictions: dict[str, GeometricRestriction]
        A repository of :py:class:`~abaqus.Optimization.GeometricRestriction.GeometricRestriction` objects.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import optimization
        mdb.models[name].optimizationTasks[name]

    """

    # A repository of DesignResponse objects. 
    designResponses: dict[str, DesignResponse] = dict[str, DesignResponse]()

    # A repository of ObjectiveFunction objects. 
    objectiveFunctions: dict[str, ObjectiveFunction] = dict[str, ObjectiveFunction]()

    # A repository of OptimizationConstraint objects. 
    optimizationConstraints: dict[str, OptimizationConstraint] = dict[str, OptimizationConstraint]()

    # A repository of GeometricRestriction objects. 
    geometricRestrictions: dict[str, GeometricRestriction] = dict[str, GeometricRestriction]()

    def __init__(self, name: str, abaqusSensitivities: Boolean = True,
                 algorithm: SymbolicConstant = GENERAL_OPTIMIZATION, areBCRegionsFrozen: Boolean = OFF,
                 beadIter: str = 1, beadMaxMembraneStress: str = 0, beadMinStress: str = 0,
                 beadPerturbation: str = 0, beadWidth: SymbolicConstant = DEFAULT, curveSmooth: str = 5,
                 filterRadius: str = 4, filterRadiusBy: SymbolicConstant = VALUE,
                 flipNormalDir: Boolean = OFF, frozenBoundaryConditionRegion: SymbolicConstant = MODEL,
                 isSensCalcOnlyOnDesignNodes: Boolean = OFF,
                 modeTrackingRegion: SymbolicConstant = MODEL, nodalMoveLimit: float = 0,
                 nodeSmooth: SymbolicConstant = DEFAULT,
                 nodeUpdateStrategy: SymbolicConstant = CONSERVATIVE, numTrackedModes: int = 5,
                 updateShapeBasisVectors: SymbolicConstant = EVERY_CYCLE, groupOperator: Boolean = OFF):
        """This method creates a BeadTask object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      mdb.models[name].BeadTask
        
        Parameters
        ----------
        name
            A String specifying the optimization task repository key. 
        abaqusSensitivities
            A Boolean specifying whether to use Abaqus to compute the design responses and their 
            sensitivities. The default value is True. 
        algorithm
            A SymbolicConstant specifying the optimization task algorithm. Possible values are 
            GENERAL_OPTIMIZATION and CONDITION_BASED_OPTIMIZATION. The default value is 
            GENERAL_OPTIMIZATION. 
        areBCRegionsFrozen
            A Boolean specifying whether to exclude elements with boundary conditions from the 
            optimization. The default value is OFF. 
        beadIter
            An int specifying the step size of the optimization. The default value is 1. 
        beadMaxMembraneStress
            A float specifying maximum membrane/bending stress. The default value is 0.1. 
        beadMinStress
            A float specifying minimum stress. The default value is 0.001. 
        beadPerturbation
            A Sets perturbation size for finite differences. The default value is 0.0001. 
        beadWidth
            A SymbolicConstant specifying the Optimization product default or a float specifying the 
            bead width. The default value is DEFAULT. 
        curveSmooth
            A float specifying relative value to the middle element edge length such that normals in 
            this area do not cross each other. The default value is 5. 
        filterRadius
            A float specifying the filter radius. The default value is 4. 
        filterRadiusBy
            A SymbolicConstant specifying the method used to define filter radius. Possible values 
            are VALUE and REFERENCE. The default is VALUE. 
        flipNormalDir
            A Boolean specifying whether the growth direction is along the normal direction of 
            elements or opposite to the normal direction. The default value is OFF 
        frozenBoundaryConditionRegion
            When nodes with boundary conditions are excluded from the optimization 
            (*frozenBoundaryConditionRegions* = ON). you can specify that this exclusion apply to 
            nodes throughout the model or only to those nodes from a specific region. Set this 
            parameter to the SymbolicConstant MODEL to apply the freeze to the entire model, or set 
            this parameter to a Region object to specify an individual region over which nodes with 
            boundary conditions should be frozen. The default value is MODEL. 
        isSensCalcOnlyOnDesignNodes
            A Boolean specifying whether to calculate the sensitivities only on design nodes or the 
            whole model. The default value is ON 
        modeTrackingRegion
            The SymbolicConstant MODEL or a Region object specifying the region to use for mode 
            tracking. The default value is MODEL. 
        nodalMoveLimit
            A Float specifying the maximum change in nodal displacement per design cycle. The 
            default value is 0.1. 
        nodeSmooth
            A SymbolicConstant specifying the Optimization product default or a float specifying the 
            node smooth. The default value is DEFAULT. 
        nodeUpdateStrategy
            A SymbolicConstant specifying the strategy for how the nodal displacements are updated 
            in the method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and 
            AGGRESSIVE. The default value is CONSERVATIVE. 
        numTrackedModes
            An Int specifying the number of modes included in mode tracking. The default value is 5. 
        updateShapeBasisVectors
            A SymbolicConstant specifying whether to update shape basis vectors in the first design 
            cycle or every design cycle. Possible values are EVERY_CYCLE and FIRST_CYCLE. The 
            default value is EVERY_CYCLE. 
        groupOperator
            A Boolean specifying whether the group in the design response will be evaluated using 
            the existing algorithm or a new algorithm based on Abaqus sensitivities. The default 
            value of False means that the existing algorithm will be used. 

        Returns
        -------
            A BeadTask object.
        """
        super().__init__()
        pass

    def setValues(self, abaqusSensitivities: Boolean = True, algorithm: SymbolicConstant = GENERAL_OPTIMIZATION,
                  areBCRegionsFrozen: Boolean = OFF, beadIter: str = 1, beadMaxMembraneStress: str = 0,
                  beadMinStress: str = 0, beadPerturbation: str = 0,
                  beadWidth: SymbolicConstant = DEFAULT, curveSmooth: str = 5, filterRadius: str = 4,
                  filterRadiusBy: SymbolicConstant = VALUE, flipNormalDir: Boolean = OFF,
                  frozenBoundaryConditionRegion: SymbolicConstant = MODEL,
                  isSensCalcOnlyOnDesignNodes: Boolean = OFF,
                  modeTrackingRegion: SymbolicConstant = MODEL, nodalMoveLimit: float = 0,
                  nodeSmooth: SymbolicConstant = DEFAULT,
                  nodeUpdateStrategy: SymbolicConstant = CONSERVATIVE, numTrackedModes: int = 5,
                  updateShapeBasisVectors: SymbolicConstant = EVERY_CYCLE, groupOperator: Boolean = OFF):
        """This method modifies the BeadTask object.
        
        Parameters
        ----------
        abaqusSensitivities
            A Boolean specifying whether to use Abaqus to compute the design responses and their 
            sensitivities. The default value is True. 
        algorithm
            A SymbolicConstant specifying the optimization task algorithm. Possible values are 
            GENERAL_OPTIMIZATION and CONDITION_BASED_OPTIMIZATION. The default value is 
            GENERAL_OPTIMIZATION. 
        areBCRegionsFrozen
            A Boolean specifying whether to exclude elements with boundary conditions from the 
            optimization. The default value is OFF. 
        beadIter
            An int specifying the step size of the optimization. The default value is 1. 
        beadMaxMembraneStress
            A float specifying maximum membrane/bending stress. The default value is 0.1. 
        beadMinStress
            A float specifying minimum stress. The default value is 0.001. 
        beadPerturbation
            A Sets perturbation size for finite differences. The default value is 0.0001. 
        beadWidth
            A SymbolicConstant specifying the Optimization product default or a float specifying the 
            bead width. The default value is DEFAULT. 
        curveSmooth
            A float specifying relative value to the middle element edge length such that normals in 
            this area do not cross each other. The default value is 5. 
        filterRadius
            A float specifying the filter radius. The default value is 4. 
        filterRadiusBy
            A SymbolicConstant specifying the method used to define filter radius. Possible values 
            are VALUE and REFERENCE. The default is VALUE. 
        flipNormalDir
            A Boolean specifying whether the growth direction is along the normal direction of 
            elements or opposite to the normal direction. The default value is OFF 
        frozenBoundaryConditionRegion
            When nodes with boundary conditions are excluded from the optimization 
            (*frozenBoundaryConditionRegions* = ON). you can specify that this exclusion apply to 
            nodes throughout the model or only to those nodes from a specific region. Set this 
            parameter to the SymbolicConstant MODEL to apply the freeze to the entire model, or set 
            this parameter to a Region object to specify an individual region over which nodes with 
            boundary conditions should be frozen. The default value is MODEL. 
        isSensCalcOnlyOnDesignNodes
            A Boolean specifying whether to calculate the sensitivities only on design nodes or the 
            whole model. The default value is ON 
        modeTrackingRegion
            The SymbolicConstant MODEL or a Region object specifying the region to use for mode 
            tracking. The default value is MODEL. 
        nodalMoveLimit
            A Float specifying the maximum change in nodal displacement per design cycle. The 
            default value is 0.1. 
        nodeSmooth
            A SymbolicConstant specifying the Optimization product default or a float specifying the 
            node smooth. The default value is DEFAULT. 
        nodeUpdateStrategy
            A SymbolicConstant specifying the strategy for how the nodal displacements are updated 
            in the method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and 
            AGGRESSIVE. The default value is CONSERVATIVE. 
        numTrackedModes
            An Int specifying the number of modes included in mode tracking. The default value is 5. 
        updateShapeBasisVectors
            A SymbolicConstant specifying whether to update shape basis vectors in the first design 
            cycle or every design cycle. Possible values are EVERY_CYCLE and FIRST_CYCLE. The 
            default value is EVERY_CYCLE. 
        groupOperator
            A Boolean specifying whether the group in the design response will be evaluated using 
            the existing algorithm or a new algorithm based on Abaqus sensitivities. The default 
            value of False means that the existing algorithm will be used. 
        """
        pass
