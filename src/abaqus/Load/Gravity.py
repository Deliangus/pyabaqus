import typing

from abaqusConstants import *
from .Load import Load
from ..Region.Region import Region


class Gravity(Load):
    """The Gravity object stores the data of a gravity load.
    The Gravity object is derived from the Load object. 

    Attributes
    ----------
    name: str
        A String specifying the load repository key.
    distributionType: SymbolicConstant
        A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.
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

    # A String specifying the name of the AnalyticalField object associated with this load. 
    # The *field* argument applies only when *distributionType*=FIELD. The default value is an 
    # empty string. 
    field: str = ''

    # A Region object specifying the region to which the load is applied. 
    region: Region = Region()

    def __init__(self, name: str, createStepName: str, distributionType: SymbolicConstant = UNIFORM,
                 field: str = '', region: Region = Region(), comp1: float = None, comp2: float = None,
                 comp3: float = None, amplitude: str = UNSET):
        """This method creates a Gravity object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Gravity
        
        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        region
            A Region object specifying the region to which the load is applied. 
        comp1
            A Float or a Complex specifying the component of the load in the 
            1-direction.Note:Although *comp1*, *comp2*, and *comp3* are optional arguments, at least 
            one of them must be nonzero. 
        comp2
            A Float or a Complex specifying the component of the load in the 2-direction. 
        comp3
            A Float or a Complex specifying the component of the load in the 3-direction. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A Gravity object.
        """
        super().__init__()
        pass

    def setValues(self, distributionType: SymbolicConstant = UNIFORM, field: str = '',
                  region: Region = Region(), comp1: float = None, comp2: float = None,
                  comp3: float = None, amplitude: str = UNSET):
        """This method modifies the data for an existing Gravity object in the step where it is
        created.
        
        Parameters
        ----------
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        region
            A Region object specifying the region to which the load is applied. 
        comp1
            A Float or a Complex specifying the component of the load in the 
            1-direction.Note:Although *comp1*, *comp2*, and *comp3* are optional arguments, at least 
            one of them must be nonzero. 
        comp2
            A Float or a Complex specifying the component of the load in the 2-direction. 
        comp3
            A Float or a Complex specifying the component of the load in the 3-direction. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        """
        pass

    def setValuesInStep(self, stepName: str,
                        comp1: typing.Union[SymbolicConstant, float] = None,
                        comp2: typing.Union[SymbolicConstant, float] = None,
                        comp3: typing.Union[SymbolicConstant, float] = None,
                        amplitude: str = ''):
        """This method modifies the propagating data for an existing Gravity object in the
        specified step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified. 
        comp1
            A Float, a Complex, or a SymbolicConstant specifying the load component in the 
            1-direction. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED 
            should be used if the load component is propagated from the previous static analysis 
            step. Use FREED to remove a previously defined load component. 
        comp2
            A Float, a Complex, or a SymbolicConstant specifying the load component in the 
            2-direction. For details see *comp1*. 
        comp3
            A Float, a Complex, or a SymbolicConstant specifying the load component in the 
            3-direction. For details see *comp1*. 
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible 
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the 
            amplitude is propagated from the previous static analysis step. FREED should be used if 
            the load is changed to have no amplitude reference. You should provide the *amplitude* 
            argument only if it is valid for the specified step. 
        """
        pass
