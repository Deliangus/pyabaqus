from abaqusConstants import *
from .Load import Load
from ..Region.Region import Region


class ConcentratedHeatFlux(Load):
    """The ConcentratedHeatFlux object stores the data for a concentrated heat flux load.
    The ConcentratedHeatFlux object is derived from the Load object. 

    Attributes
    ----------
    name: str
        A String specifying the load repository key.
    distributionType: SymbolicConstant
        A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.
    dof: int
        An Int specifying the degree of freedom of the node, to which the concentrated heat flux
        should be applied. The default value is 11.
    field: str
        A String specifying the name of the :py:class:`~abaqus.Field.AnalyticalField.AnalyticalField` object associated with this load.
        The **field** argument applies only when **distributionType=FIELD**. The default value is an
        empty string.
    region: Region
        A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the load is applied.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import load
        mdb.models[name].loads[name]

    """

    # A String specifying the load repository key. 
    name: str = ''

    # A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
    # UNIFORM and FIELD. The default value is UNIFORM. 
    distributionType: SymbolicConstant = UNIFORM

    # An Int specifying the degree of freedom of the node, to which the concentrated heat flux 
    # should be applied. The default value is 11. 
    dof: int = 11

    # A String specifying the name of the AnalyticalField object associated with this load. 
    # The *field* argument applies only when *distributionType*=FIELD. The default value is an 
    # empty string. 
    field: str = ''

    # A Region object specifying the region to which the load is applied. 
    region: Region = Region()

    def __init__(self, name: str, createStepName: str, region: Region, magnitude: float,
                 distributionType: SymbolicConstant = UNIFORM, field: str = '', amplitude: str = UNSET,
                 dof: int = 11):
        """This method creates a ConcentratedHeatFlux object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].ConcentratedHeatFlux
        
        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. This must be the 
            first analysis step name. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the load magnitude. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        dof
            An Int specifying the degree of freedom of the node, to which the concentrated heat flux 
            should be applied. The default value is 11. 

        Returns
        -------
            A ConcentratedHeatFlux object.
        """
        super().__init__()
        pass

    def setValues(self, distributionType: SymbolicConstant = UNIFORM, field: str = '', amplitude: str = UNSET,
                  dof: int = 11):
        """This method modifies the data for an existing ConcentratedHeatFlux object in the step
        where it is created.
        
        Parameters
        ----------
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        dof
            An Int specifying the degree of freedom of the node, to which the concentrated heat flux 
            should be applied. The default value is 11. 
        """
        pass

    def setValuesInStep(self, stepName: str, magnitude: float = None, amplitude: str = ''):
        """This method modifies the propagating data for an existing ConcentratedHeatFlux object in
        the specified step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified. 
        magnitude
            A Float specifying the load magnitude. 
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible 
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the 
            amplitude is propagated from the previous static analysis step. FREED should be used if 
            the load is changed to have no amplitude reference. You should provide the *amplitude* 
            argument only if it is valid for the specified step. 
        """
        pass
