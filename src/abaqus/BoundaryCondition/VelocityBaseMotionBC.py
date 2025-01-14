from abaqusConstants import *
from .BoundaryCondition import BoundaryCondition
from ..Amplitude.CorrelationArray import CorrelationArray
from ..Region.Region import Region


class VelocityBaseMotionBC(BoundaryCondition):
    """The VelocityBaseMotionBC object stores the data for a velocity base motion boundary
    condition. 
    The VelocityBaseMotionBC object is derived from the BoundaryCondition object. 

    Attributes
    ----------
    name: str
        A String specifying the boundary condition repository key.
    amplitudeScaleFactor: float
        A Float specifying the scale factor for the amplitude curve. The default value is 1.0.
    useComplex: Boolean
        A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base
        motion record given by amplitude definition. The default value is OFF.
    centerOfRotation: tuple
        A :py:class:`~abaqus.BasicGeometry.ModelDot.ModelDot` object specifying a tuple containing one center of rotation. The default
        value is the global origin. This argument applies only when **dof=UR1**, UR2, or UR3.
    correlation: CorrelationArray
        A :py:class:`~abaqus.Amplitude.CorrelationArray.CorrelationArray` object.
    secondaryBase: str
        A String specifying the name of the :py:class:`~abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC` object associated with this boundary
        condition. The default value is an empty string.
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

    # A Float specifying the scale factor for the amplitude curve. The default value is 1.0. 
    amplitudeScaleFactor: float = 1

    # A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base 
    # motion record given by amplitude definition. The default value is OFF. 
    useComplex: Boolean = OFF

    # A ModelDot object specifying a tuple containing one center of rotation. The default 
    # value is the global origin. This argument applies only when *dof*=UR1, UR2, or UR3. 
    centerOfRotation: tuple = ()

    # A CorrelationArray object. 
    correlation: CorrelationArray = CorrelationArray()

    # A String specifying the name of the SecondaryBaseBC object associated with this boundary 
    # condition. The default value is an empty string. 
    secondaryBase: str = ''

    # A SymbolicConstant specifying the category of the boundary condition. Possible values 
    # are MECHANICAL and THERMAL. 
    category: SymbolicConstant = None

    # A Region object specifying the region to which the boundary condition is applied. 
    region: Region = Region()

    # None or a DatumCsys object specifying the local coordinate system of the boundary 
    # condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
    # in the global coordinate system. The default value is None. 
    localCsys: str = None

    def __init__(self, name: str, createStepName: str, dof: SymbolicConstant, amplitudeScaleFactor: float = 1,
                 centerOfRotation: tuple = (), correlation: CorrelationArray = None,
                 secondaryBase: str = '', useComplex: Boolean = OFF, amplitude: str = UNSET):
        """This method creates a VelocityBaseMotionBC object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].VelocityBaseMotionBC
        
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        dof
            A SymbolicConstant specifying the constrained degree-of-freedom. Possible values for the 
            SymbolicConstant are U1, U2, U3, UR1, UR2, UR3. The default value is U1. 
        amplitudeScaleFactor
            A Float specifying the scale factor for the amplitude curve. The default value is 1.0. 
        centerOfRotation
            A ModelDot object specifying a tuple containing one center of rotation. The default 
            value is the global origin. This argument applies only when *dof*=UR1, UR2, or UR3. 
        correlation
            A CorrelationArray object. 
        secondaryBase
            A String specifying the name of the SecondaryBaseBC object associated with this boundary 
            condition. The default value is an empty string. 
        useComplex
            A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base 
            motion record given by amplitude definition. The default value is OFF. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 

        Returns
        -------
            A VelocityBaseMotionBC object.
        """
        super().__init__()
        pass

    def setValues(self, amplitudeScaleFactor: float = 1, centerOfRotation: tuple = (),
                  correlation: CorrelationArray = None, secondaryBase: str = '',
                  useComplex: Boolean = OFF, amplitude: str = UNSET):
        """This method modifies the data for an existing VelocityBaseMotionBC object in the step
        where it is created.
        
        Parameters
        ----------
        amplitudeScaleFactor
            A Float specifying the scale factor for the amplitude curve. The default value is 1.0. 
        centerOfRotation
            A ModelDot object specifying a tuple containing one center of rotation. The default 
            value is the global origin. This argument applies only when *dof*=UR1, UR2, or UR3. 
        correlation
            A CorrelationArray object. 
        secondaryBase
            A String specifying the name of the SecondaryBaseBC object associated with this boundary 
            condition. The default value is an empty string. 
        useComplex
            A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base 
            motion record given by amplitude definition. The default value is OFF. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        """
        pass

    def setValuesInStep(self, stepName: str, amplitude: str = ''):
        """This method modifies the propagating data for an existing VelocityBaseMotionBC object in
        the specified step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified. 
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible 
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the 
            amplitude is propagated from the previous analysis step. FREED should be used if the 
            boundary condition is changed to have no amplitude reference. You should provide the 
            *amplitude* argument only if it is valid for the specified step. 
        """
        pass
