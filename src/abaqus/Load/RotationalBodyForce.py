from abaqusConstants import *
from .Load import Load
from ..Region.Region import Region


class RotationalBodyForce(Load):
    """The RotationalBodyForce object stores the data for a rotational body force.
    The RotationalBodyForce object is derived from the Load object. 

    Attributes
    ----------
    name: str
        A String specifying the load repository key.
    distributionType: SymbolicConstant
        A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.
    centrifugal: Boolean
        A Boolean specifying whether or not the effect of the load is centrifugal. The default
        value is OFF.Note:At least one of **centrifugal** or **rotaryAcceleration** must be
        specified and only one must have the value ON.
    rotaryAcceleration: Boolean
        A Boolean specifying whether or not the effect of the load is rotary acceleration. The
        default value is OFF.Note:At least one of **centrifugal** or **rotaryAcceleration** must be
        specified and only one must have the value ON.
    point1: float
        A tuple of Floats specifying the first point on the axis of rotation for the load.
    point2: float
        A tuple of Floats specifying the second point on the axis of rotation for the load.
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

    # A Boolean specifying whether or not the effect of the load is centrifugal. The default 
    # value is OFF.Note:At least one of *centrifugal* or *rotaryAcceleration* must be 
    # specified and only one must have the value ON. 
    centrifugal: Boolean = OFF

    # A Boolean specifying whether or not the effect of the load is rotary acceleration. The 
    # default value is OFF.Note:At least one of *centrifugal* or *rotaryAcceleration* must be 
    # specified and only one must have the value ON. 
    rotaryAcceleration: Boolean = OFF

    # A tuple of Floats specifying the first point on the axis of rotation for the load. 
    point1: float = None

    # A tuple of Floats specifying the second point on the axis of rotation for the load. 
    point2: float = None

    # A String specifying the name of the AnalyticalField object associated with this load. 
    # The *field* argument applies only when *distributionType*=FIELD. The default value is an 
    # empty string. 
    field: str = ''

    # A Region object specifying the region to which the load is applied. 
    region: Region = Region()

    def __init__(self, name: str, createStepName: str, region: Region, magnitude: float, point1: tuple,
                 point2: tuple, distributionType: SymbolicConstant = UNIFORM, field: str = '',
                 centrifugal: Boolean = OFF, rotaryAcceleration: Boolean = OFF, amplitude: str = UNSET):
        """This method creates a RotationalBodyForce object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].RotationalBodyForce
        
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
        point1
            A sequence of Floats specifying the first point on the axis of rotation for the load. 
        point2
            A sequence of Floats specifying the second point on the axis of rotation for the load. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        centrifugal
            A Boolean specifying whether or not the effect of the load is centrifugal. The default 
            value is OFF.Note:At least one of *centrifugal* or *rotaryAcceleration* must be 
            specified and only one must have the value ON. 
        rotaryAcceleration
            A Boolean specifying whether or not the effect of the load is rotary acceleration. The 
            default value is OFF.Note:At least one of *centrifugal* or *rotaryAcceleration* must be 
            specified and only one must have the value ON. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A RotationalBodyForce object.
        """
        super().__init__()
        pass

    def setValues(self, distributionType: SymbolicConstant = UNIFORM, field: str = '',
                  centrifugal: Boolean = OFF, rotaryAcceleration: Boolean = OFF, amplitude: str = UNSET):
        """This method modifies the data for an existing RotationalBodyForce object in the step
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
        centrifugal
            A Boolean specifying whether or not the effect of the load is centrifugal. The default 
            value is OFF.Note:At least one of *centrifugal* or *rotaryAcceleration* must be 
            specified and only one must have the value ON. 
        rotaryAcceleration
            A Boolean specifying whether or not the effect of the load is rotary acceleration. The 
            default value is OFF.Note:At least one of *centrifugal* or *rotaryAcceleration* must be 
            specified and only one must have the value ON. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        """
        pass

    def setValuesInStep(self, stepName: str, magnitude: float = None, amplitude: str = ''):
        """This method modifies the propagating data for an existing RotationalBodyForce object in
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
