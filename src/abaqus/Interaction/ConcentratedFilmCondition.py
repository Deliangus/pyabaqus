from abaqusConstants import *
from .Interaction import Interaction
from ..Region.Region import Region


class ConcentratedFilmCondition(Interaction):
    """The ConcentratedFilmCondition object defines concentrated film coefficients and
    associated sink temperatures. 
    The ConcentratedFilmCondition object is derived from the Interaction object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].interactions[name]

    """

    def __init__(self, name: str, createStepName: str, region: Region, definition: SymbolicConstant,
                 nodalArea: float = 1, explicitRegionType: SymbolicConstant = LAGRANGIAN,
                 interactionProperty: str = '', field: str = '', sinkTemperature: float = 0,
                 sinkAmplitude: str = '', filmCoeff: float = 0, filmCoeffAmplitude: str = '',
                 sinkFieldName: str = '', sinkDistributionType: SymbolicConstant = UNIFORM):
        """This method creates a ConcentratedFilmCondition object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].ConcentratedFilmCondition
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the ConcentratedFilmCondition object 
            is created. 
        region
            A Region object specifying the region to which the concentrated film condition 
            interaction is applied. The interaction is applied to each node in the region. 
        definition
            A SymbolicConstant specifying how the concentrated film condition is defined. Possible 
            values are EMBEDDED_COEFF, PROPERTY_REF, USER_SUB, and FIELD. 
        nodalArea
            A Float specifying the area associated with the node where the concentrated film 
            condition is applied. The default value is 1.0. 
        explicitRegionType
            A SymbolicConstant specifying how the concentrated film condition is applied to the 
            boundary of an adaptive mesh domain. Possible values are LAGRANGIAN, SLIDING, and 
            EULERIAN. The default value is LAGRANGIAN. This argument applies only during an 
            Abaqus/Explicit analysis. 
        interactionProperty
            A String specifying the name of the FilmConditionProp object associated with this 
            interaction. The *interactionProperty* argument applies only when 
            *definition*=PROPERTY_REF. The default value is an empty string. 
        field
            A String specifying the name of the AnalyticalField object associated with this 
            interaction. The *field* argument applies only when *definition*=FIELD. The default 
            value is an empty string. 
        sinkTemperature
            A Float specifying the reference sink temperature, θ0θ0. The default value is 0.0. 
        sinkAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the 
            sink temperature, θ0θ0, with time. The default value is an empty string.Note:Use None in 
            an Abaqus/Standard analysis to specify that the reference sink temperature is applied 
            immediately at the beginning of the step or linearly over the step. Use None in an 
            Abaqus/Explicit analysis to specify that the reference sink temperature is applied 
            throughout the step. 
        filmCoeff
            A Float specifying the reference film coefficient value, hh. The *filmCoeff* argument 
            applies when *definition*=EMBEDDED_COEFF, *definition*=USER_SUB, or *definition*=FIELD. 
            The default value is 0.0. 
        filmCoeffAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the 
            film coefficient, hh, with time. The default value is an empty string.Note:Use None in 
            an Abaqus/Standard analysis to specify that the reference film coefficient is applied 
            immediately at the beginning of the step or linearly over the step. Use None in an 
            Abaqus/Explicit analysis to specify that the reference film coefficient is applied 
            throughout the step. 
        sinkFieldName
            A String specifying the name of the AnalyticalField or DiscreteField object associated 
            with the sink temperature. The *sinkFieldName* argument applies only when 
            *sinkDistributionType*=ANALYTICAL_FIELD or *sinkDistributionType*=DISCRETE_FIELD. The 
            default value is an empty string. 
        sinkDistributionType
            A SymbolicConstant specifying how the sink temperature is distributed. Possible values 
            are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM. 

        Returns
        -------
            A ConcentratedFilmCondition object.
        """
        super().__init__()
        pass

    def setValues(self, nodalArea: float = 1, explicitRegionType: SymbolicConstant = LAGRANGIAN,
                  interactionProperty: str = '', field: str = '', sinkTemperature: float = 0,
                  sinkAmplitude: str = '', filmCoeff: float = 0, filmCoeffAmplitude: str = '',
                  sinkFieldName: str = '', sinkDistributionType: SymbolicConstant = UNIFORM):
        """This method modifies the data for an existing ConcentratedFilmCondition object in the
        step where it is created.
        
        Parameters
        ----------
        nodalArea
            A Float specifying the area associated with the node where the concentrated film 
            condition is applied. The default value is 1.0. 
        explicitRegionType
            A SymbolicConstant specifying how the concentrated film condition is applied to the 
            boundary of an adaptive mesh domain. Possible values are LAGRANGIAN, SLIDING, and 
            EULERIAN. The default value is LAGRANGIAN. This argument applies only during an 
            Abaqus/Explicit analysis. 
        interactionProperty
            A String specifying the name of the FilmConditionProp object associated with this 
            interaction. The *interactionProperty* argument applies only when 
            *definition*=PROPERTY_REF. The default value is an empty string. 
        field
            A String specifying the name of the AnalyticalField object associated with this 
            interaction. The *field* argument applies only when *definition*=FIELD. The default 
            value is an empty string. 
        sinkTemperature
            A Float specifying the reference sink temperature, θ0θ0. The default value is 0.0. 
        sinkAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the 
            sink temperature, θ0θ0, with time. The default value is an empty string.Note:Use None in 
            an Abaqus/Standard analysis to specify that the reference sink temperature is applied 
            immediately at the beginning of the step or linearly over the step. Use None in an 
            Abaqus/Explicit analysis to specify that the reference sink temperature is applied 
            throughout the step. 
        filmCoeff
            A Float specifying the reference film coefficient value, hh. The *filmCoeff* argument 
            applies when *definition*=EMBEDDED_COEFF, *definition*=USER_SUB, or *definition*=FIELD. 
            The default value is 0.0. 
        filmCoeffAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the 
            film coefficient, hh, with time. The default value is an empty string.Note:Use None in 
            an Abaqus/Standard analysis to specify that the reference film coefficient is applied 
            immediately at the beginning of the step or linearly over the step. Use None in an 
            Abaqus/Explicit analysis to specify that the reference film coefficient is applied 
            throughout the step. 
        sinkFieldName
            A String specifying the name of the AnalyticalField or DiscreteField object associated 
            with the sink temperature. The *sinkFieldName* argument applies only when 
            *sinkDistributionType*=ANALYTICAL_FIELD or *sinkDistributionType*=DISCRETE_FIELD. The 
            default value is an empty string. 
        sinkDistributionType
            A SymbolicConstant specifying how the sink temperature is distributed. Possible values 
            are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM. 
        """
        pass

    def setValuesInStep(self, stepName: str):
        """This method modifies the propagating data of an existing ConcentratedFilmCondition
        object in the specified step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified. 
        """
        pass
