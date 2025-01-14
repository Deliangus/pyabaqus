from abaqusConstants import *
from .Interaction import Interaction
from ..Region.Region import Region


class ConcentratedRadiationToAmbient(Interaction):
    """The ConcentratedRadiationToAmbient object defines radiant heat transfer between a point
    and its nonreflecting environment. 
    The ConcentratedRadiationToAmbient object is derived from the Interaction object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].interactions[name]

    """

    def __init__(self, name: str, createStepName: str, region: Region, ambientTemperature: float,
                 ambientTemperatureAmp: str, emissivity: float, nodalArea: float = 1,
                 explicitRegionType: SymbolicConstant = LAGRANGIAN, field: str = '',
                 distributionType: SymbolicConstant = UNIFORM):
        """This method creates a ConcentratedRadiationToAmbient object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].ConcentratedRadiationToAmbient
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the ConcentratedRadiationToAmbient 
            object is created. 
        region
            A Region object specifying the region to which the concentrated radiation interaction is 
            applied. The interaction is applied to each node in the region. 
        ambientTemperature
            A Float specifying the reference ambient temperature, θ0θ0. 
        ambientTemperatureAmp
            A String specifying the name of the Amplitude object that gives the variation of the 
            ambient temperature with time.Note:Use None in an Abaqus/Standard analysis to specify 
            that the reference ambient temperature is applied immediately at the beginning of the 
            step or linearly over the step. Use None in an Abaqus/Explicit analysis to specify that 
            the reference ambient temperature is applied throughout the step. 
        emissivity
            A Float specifying the emissivity, ϵϵ. 
        nodalArea
            A Float specifying the area associated with the node where the concentrated radiation 
            interaction is applied. The default value is 1.0. 
        explicitRegionType
            A SymbolicConstant specifying how the concentrated radiation is applied to the boundary 
            of an adaptive mesh domain. Possible values are LAGRANGIAN, SLIDING, and EULERIAN. The 
            default value is LAGRANGIAN.Note:*explicitRegionType* applies only during an 
            Abaqus/Explicit analysis. 
        field
            A String specifying the name of the AnalyticalField object associated with this 
            interaction. The *field* argument applies only when *distributionType*=ANALYTICAL_FIELD. 
            The default value is an empty string. 
        distributionType
            A SymbolicConstant specifying how the radiation is defined. Possible values are UNIFORM 
            and ANALYTICAL_FIELD. The default value is UNIFORM. 

        Returns
        -------
            A ConcentratedRadiationToAmbient object.
        """
        super().__init__()
        pass

    def setValues(self, nodalArea: float = 1, explicitRegionType: SymbolicConstant = LAGRANGIAN,
                  field: str = '', distributionType: SymbolicConstant = UNIFORM):
        """This method modifies the data for an existing ConcentratedRadiationToAmbient object in
        the step where it is created.
        
        Parameters
        ----------
        nodalArea
            A Float specifying the area associated with the node where the concentrated radiation 
            interaction is applied. The default value is 1.0. 
        explicitRegionType
            A SymbolicConstant specifying how the concentrated radiation is applied to the boundary 
            of an adaptive mesh domain. Possible values are LAGRANGIAN, SLIDING, and EULERIAN. The 
            default value is LAGRANGIAN.Note:*explicitRegionType* applies only during an 
            Abaqus/Explicit analysis. 
        field
            A String specifying the name of the AnalyticalField object associated with this 
            interaction. The *field* argument applies only when *distributionType*=ANALYTICAL_FIELD. 
            The default value is an empty string. 
        distributionType
            A SymbolicConstant specifying how the radiation is defined. Possible values are UNIFORM 
            and ANALYTICAL_FIELD. The default value is UNIFORM. 
        """
        pass

    def setValuesInStep(self, stepName: str, nodalArea: float = 1, field: str = '',
                        distributionType: SymbolicConstant = UNIFORM):
        """This method modifies the propagating data of an existing ConcentratedRadiationToAmbient
        object in the specified step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified. 
        nodalArea
            A Float specifying the area associated with the node where the concentrated radiation 
            interaction is applied. The default value is 1.0. 
        field
            A String specifying the name of the AnalyticalField object associated with this 
            interaction. The *field* argument applies only when *distributionType*=ANALYTICAL_FIELD. 
            The default value is an empty string. 
        distributionType
            A SymbolicConstant specifying how the radiation is defined. Possible values are UNIFORM 
            and ANALYTICAL_FIELD. The default value is UNIFORM. 
        """
        pass
