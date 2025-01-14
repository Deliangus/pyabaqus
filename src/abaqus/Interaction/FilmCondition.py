from abaqusConstants import *
from .Interaction import Interaction
from ..Region.Region import Region


class FilmCondition(Interaction):
    """The FilmCondition object defines film coefficients and associated sink temperatures for
    coupled temperature-displacement analyses. 
    The FilmCondition object is derived from the Interaction object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].interactions[name]

    """

    def __init__(self, name: str, createStepName: str, surface: Region, definition: SymbolicConstant,
                 interactionProperty: str = '', sinkTemperature: float = 0, sinkAmplitude: str = '',
                 filmCoeff: float = 0, filmCoeffAmplitude: str = '', field: str = '',
                 sinkFieldName: str = '', sinkDistributionType: SymbolicConstant = UNIFORM):
        """This method creates a FilmCondition object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].FilmCondition
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the FilmCondition object is created. 
        surface
            A Region object specifying the name of the surface to which the film condition 
            interaction is applied. 
        definition
            A SymbolicConstant specifying how the film condition is defined. Possible values are 
            EMBEDDED_COEFF, PROPERTY_REF, USER_SUB, and FIELD. 
        interactionProperty
            A String specifying the name of the FilmConditionProp object associated with this 
            interaction. The *interactionProperty* argument applies only when 
            *definition*=PROPERTY_REF. The default value is an empty string. 
        sinkTemperature
            A Float specifying the reference sink temperature, θ0θ0. The default value is 0.0. 
        sinkAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the 
            sink temperature, θ0θ0, with time. The default value is an empty string.Note:Use empty 
            string in an Abaqus/Standard analysis to specify that the reference sink temperature is 
            applied immediately at the beginning of the step or linearly over the step. Use empty 
            string in an Abaqus/Explicit analysis to specify that the reference sink temperature is 
            applied throughout the step. 
        filmCoeff
            A Float specifying the reference film coefficient value, hh. The *filmCoeff* argument 
            applies when *definition*=EMBEDDED_COEFF, *definition*=USER_SUB, or *definition*=FIELD. 
            The default value is 0.0. 
        filmCoeffAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the 
            film coefficient, hh, with time. The default value is an empty string. Note: Use empty 
            string in an Abaqus/Standard analysis to specify that the reference film coefficient is 
            applied immediately at the beginning of the step or linearly over the step. Use empty 
            string in an Abaqus/Explicit analysis to specify that the reference film coefficient is 
            applied throughout the step. 
        field
            A String specifying the name of the AnalyticalField object associated with this 
            interaction. The *field* argument applies only when *definition*=FIELD. The default 
            value is an empty string. 
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
            A FilmCondition object.
        """
        super().__init__()
        pass

    def setValues(self, interactionProperty: str = '', sinkTemperature: float = 0, sinkAmplitude: str = '',
                  filmCoeff: float = 0, filmCoeffAmplitude: str = '', field: str = '',
                  sinkFieldName: str = '', sinkDistributionType: SymbolicConstant = UNIFORM):
        """This method modifies the data for an existing FilmCondition object in the step where it
        is created.
        
        Parameters
        ----------
        interactionProperty
            A String specifying the name of the FilmConditionProp object associated with this 
            interaction. The *interactionProperty* argument applies only when 
            *definition*=PROPERTY_REF. The default value is an empty string. 
        sinkTemperature
            A Float specifying the reference sink temperature, θ0θ0. The default value is 0.0. 
        sinkAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the 
            sink temperature, θ0θ0, with time. The default value is an empty string.Note:Use empty 
            string in an Abaqus/Standard analysis to specify that the reference sink temperature is 
            applied immediately at the beginning of the step or linearly over the step. Use empty 
            string in an Abaqus/Explicit analysis to specify that the reference sink temperature is 
            applied throughout the step. 
        filmCoeff
            A Float specifying the reference film coefficient value, hh. The *filmCoeff* argument 
            applies when *definition*=EMBEDDED_COEFF, *definition*=USER_SUB, or *definition*=FIELD. 
            The default value is 0.0. 
        filmCoeffAmplitude
            A String specifying the name of the Amplitude object that gives the variation of the 
            film coefficient, hh, with time. The default value is an empty string. Note: Use empty 
            string in an Abaqus/Standard analysis to specify that the reference film coefficient is 
            applied immediately at the beginning of the step or linearly over the step. Use empty 
            string in an Abaqus/Explicit analysis to specify that the reference film coefficient is 
            applied throughout the step. 
        field
            A String specifying the name of the AnalyticalField object associated with this 
            interaction. The *field* argument applies only when *definition*=FIELD. The default 
            value is an empty string. 
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
        """This method modifies the propagating data of an existing FilmCondition object in the
        specified step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified. 
        """
        pass
