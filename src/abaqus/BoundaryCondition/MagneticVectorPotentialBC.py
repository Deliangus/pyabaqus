from abaqusConstants import *
from .BoundaryCondition import BoundaryCondition
from ..Region.Region import Region


class MagneticVectorPotentialBC(BoundaryCondition):
    """The MagneticVectorPotentialBC object stores the data for a magnetic vector potential
    boundary condition. 
    The MagneticVectorPotentialBC object is derived from the BoundaryCondition object. 

    Attributes
    ----------
    name: str
        A String specifying the boundary condition repository key.
    distributionType: SymbolicConstant
        A SymbolicConstant specifying how the boundary condition is distributed spatially.
        Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM.
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

    # A SymbolicConstant specifying how the boundary condition is distributed spatially. 
    # Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM. 
    distributionType: SymbolicConstant = UNIFORM

    # A SymbolicConstant specifying the category of the boundary condition. Possible values 
    # are MECHANICAL and THERMAL. 
    category: SymbolicConstant = None

    # A Region object specifying the region to which the boundary condition is applied. 
    region: Region = Region()

    # None or a DatumCsys object specifying the local coordinate system of the boundary 
    # condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
    # in the global coordinate system. The default value is None. 
    localCsys: str = None

    def __init__(self, name: str, createStepName: str, region: Region, component1: SymbolicConstant = None,
                 component2: SymbolicConstant = UNSET, component3: SymbolicConstant = UNSET,
                 amplitude: str = UNSET, distributionType: SymbolicConstant = UNIFORM,
                 localCsys: str = None):
        """This method creates a MagneticVectorPotentialBC object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].MagneticVectorPotentialBC
        
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        component1
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in 
            the 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET 
        component2
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in 
            the 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        component3
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in 
            the 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 

        Returns
        -------
            A MagneticVectorPotentialBC object.
        """
        super().__init__()
        pass

    def setValues(self, component1: SymbolicConstant = None, component2: SymbolicConstant = UNSET,
                  component3: SymbolicConstant = UNSET, amplitude: str = UNSET,
                  distributionType: SymbolicConstant = UNIFORM, localCsys: str = None):
        """This method modifies the data for an existing MagneticVectorPotentialBC object in the
        step where it is created.
        
        Parameters
        ----------
        component1
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in 
            the 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET 
        component2
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in 
            the 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        component3
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in 
            the 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 
        """
        pass

    def setValuesInStep(self, stepName: str, component1: SymbolicConstant = None, component2: SymbolicConstant = None,
                        component3: SymbolicConstant = None, amplitude: str = ''):
        """This method modifies the propagating data for an existing MagneticVectorPotentialBC
        object in the specified step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified. 
        component1
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in 
            the 1-direction. Possible values for the SymbolicConstant are SET and UNCHANGED. 
        component2
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in 
            the 2-direction. Possible values for the SymbolicConstant are SET and UNCHANGED. 
        component3
            A Complex, or a SymbolicConstant specifying the magnetic vector potential component in 
            the 3-direction. Possible values for the SymbolicConstant areSET and UNCHANGED. 
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible 
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the 
            amplitude is propagated from the previous analysis step. FREED should be used if the 
            boundary condition is changed to have no amplitude reference. You should provide the 
            *amplitude* argument only if it is valid for the specified step. 
        """
        pass
