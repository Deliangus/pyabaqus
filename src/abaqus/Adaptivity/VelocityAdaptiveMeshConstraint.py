import typing

from abaqusConstants import *
from .AdaptiveMeshConstraint import AdaptiveMeshConstraint
from ..Region.Region import Region


class VelocityAdaptiveMeshConstraint(AdaptiveMeshConstraint):
    """The VelocityAdaptiveMeshConstraint object stores the data for an Arbitrary Lagrangian
    Eularian (ALE) style velocity adaptive mesh constraint. 
    The VelocityAdaptiveMeshConstraint object is derived from the AdaptiveMeshConstraint 
    object. 

    Attributes
    ----------
    name: str
        A String specifying the adaptive mesh constraint repository key.
    category: SymbolicConstant
        A SymbolicConstant specifying the category of the adaptive mesh constraint. Possible
        values are MECHANICAL and THERMAL.
    region: Region
        A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the adaptive mesh constraint is applied.
    localCsys: str
        None or a :py:class:`~abaqus.Datum.DatumCsys.DatumCsys` object specifying the local coordinate system of the adaptive mesh
        constraint's degrees of freedom. If **localCsys=None**, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import step
        mdb.models[name].adaptiveMeshConstraints[name]

    """

    # A String specifying the adaptive mesh constraint repository key. 
    name: str = ''

    # A SymbolicConstant specifying the category of the adaptive mesh constraint. Possible 
    # values are MECHANICAL and THERMAL. 
    category: SymbolicConstant = None

    # A Region object specifying the region to which the adaptive mesh constraint is applied. 
    region: Region = Region()

    # None or a DatumCsys object specifying the local coordinate system of the adaptive mesh 
    # constraint's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
    # in the global coordinate system. The default value is None. 
    localCsys: str = None

    def __init__(self, name: str, createStepName: str, region: Region,
                 v1: typing.Union[SymbolicConstant, float] = UNSET,
                 v2: typing.Union[SymbolicConstant, float] = UNSET,
                 v3: typing.Union[SymbolicConstant, float] = UNSET,
                 vr1: typing.Union[SymbolicConstant, float] = UNSET,
                 vr2: typing.Union[SymbolicConstant, float] = UNSET,
                 vr3: typing.Union[SymbolicConstant, float] = UNSET, amplitude: str = UNSET,
                 localCsys: str = None, motionType: SymbolicConstant = INDEPENDENT):
        """This method creates a VelocityAdaptiveMeshConstraint object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].VelocityAdaptiveMeshConstraint
        
        Parameters
        ----------
        name
            A String specifying the adaptive mesh constraint repository key. 
        createStepName
            A String specifying the name of the step in which the adaptive mesh constraint is 
            created. 
        region
            A Region object specifying the region to which the adaptive mesh constraint is applied. 
        v1
            A Float or a SymbolicConstant specifying the velocity component in the 1-direction. 
            Possible values for the SymbolicConstant are UNSET and SET. The default value is 
            UNSET.Note:Although *v1*, *v2*, *v3*, *vr1*, *vr2*, and *vr3* are optional arguments, at 
            least one of them must be specified. 
        v2
            A Float or a SymbolicConstant specifying the velocity component in the 2-direction. 
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET. 
        v3
            A Float or a SymbolicConstant specifying the velocity component in the 3-direction. 
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET. 
        vr1
            A Float or a SymbolicConstant specifying the rotational velocity component about the 
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        vr2
            A Float or a SymbolicConstant specifying the rotational velocity component about the 
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        vr3
            A Float or a SymbolicConstant specifying the rotational velocity component about the 
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the adaptive mesh constraint has no amplitude reference. The 
            default value is UNSET. You should provide the *amplitude* argument only if it is valid 
            for the specified step. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the adaptive mesh 
            constraint's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 
        motionType
            A SymbolicConstant specifying the mesh motion in relation to the underlying material. 
            Possible values are INDEPENDENT, FOLLOW and USER_DEFINED. The default value is 
            INDEPENDENT. 

        Returns
        -------
            A VelocityAdaptiveMeshConstraint object.
        """
        super().__init__()
        pass

    def setValues(self, v1: typing.Union[SymbolicConstant, float] = UNSET,
                  v2: typing.Union[SymbolicConstant, float] = UNSET,
                  v3: typing.Union[SymbolicConstant, float] = UNSET,
                  vr1: typing.Union[SymbolicConstant, float] = UNSET,
                  vr2: typing.Union[SymbolicConstant, float] = UNSET,
                  vr3: typing.Union[SymbolicConstant, float] = UNSET, amplitude: str = UNSET,
                  localCsys: str = None, motionType: SymbolicConstant = INDEPENDENT):
        """This method modifies the data for an existing VelocityAdaptiveMeshConstraint object in
        the step where it is created.
        
        Parameters
        ----------
        v1
            A Float or a SymbolicConstant specifying the velocity component in the 1-direction. 
            Possible values for the SymbolicConstant are UNSET and SET. The default value is 
            UNSET.Note:Although *v1*, *v2*, *v3*, *vr1*, *vr2*, and *vr3* are optional arguments, at 
            least one of them must be specified. 
        v2
            A Float or a SymbolicConstant specifying the velocity component in the 2-direction. 
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET. 
        v3
            A Float or a SymbolicConstant specifying the velocity component in the 3-direction. 
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET. 
        vr1
            A Float or a SymbolicConstant specifying the rotational velocity component about the 
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        vr2
            A Float or a SymbolicConstant specifying the rotational velocity component about the 
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        vr3
            A Float or a SymbolicConstant specifying the rotational velocity component about the 
            3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the adaptive mesh constraint has no amplitude reference. The 
            default value is UNSET. You should provide the *amplitude* argument only if it is valid 
            for the specified step. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the adaptive mesh 
            constraint's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 
        motionType
            A SymbolicConstant specifying the mesh motion in relation to the underlying material. 
            Possible values are INDEPENDENT, FOLLOW and USER_DEFINED. The default value is 
            INDEPENDENT. 
        """
        pass

    def setValuesInStep(self, stepName: str,
                        v1: typing.Union[SymbolicConstant, float] = None,
                        v2: typing.Union[SymbolicConstant, float] = None,
                        v3: typing.Union[SymbolicConstant, float] = None,
                        vr1: typing.Union[SymbolicConstant, float] = None,
                        vr2: typing.Union[SymbolicConstant, float] = None,
                        vr3: typing.Union[SymbolicConstant, float] = None,
                        amplitude: str = ''):
        """This method modifies the propagating data for an existing VelocityAdaptiveMeshConstraint
        object in the specified step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the adaptive mesh constraint is 
            modified. 
        v1
            A Float or a SymbolicConstant specifying the velocity component in the 1-direction. 
            Possible values for the SymbolicConstant are SET and FREED. 
        v2
            A Float or a SymbolicConstant specifying the velocity component in the 2-direction. 
            Possible values for the SymbolicConstant are SET and FREED. 
        v3
            A Float or a SymbolicConstant specifying the velocity component in the 3-direction. 
            Possible values for the SymbolicConstant are SET and FREED. 
        vr1
            A Float or a SymbolicConstant specifying the rotational velocity component about the 
            1-direction. Possible values for the SymbolicConstant are SET and FREED. 
        vr2
            A Float or a SymbolicConstant specifying the rotational velocity component about the 
            2-direction. Possible values for the SymbolicConstant are SET and FREED. 
        vr3
            A Float or a SymbolicConstant specifying the rotational velocity component about the 
            3-direction. Possible values for the SymbolicConstant are SET and FREED. 
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible 
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the 
            amplitude is propagated from the previous analysis step. FREED should be used if the 
            adaptive mesh constraint is changed to have no amplitude reference. You should provide 
            the *amplitude* argument only if it is valid for the specified step. 
        """
        pass
