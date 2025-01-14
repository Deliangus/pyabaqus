import typing

from abaqusConstants import *
from .BoundaryCondition import BoundaryCondition
from ..Region.Region import Region


class VelocityBC(BoundaryCondition):
    """The VelocityBC object stores the data for a velocity boundary condition.
    The VelocityBC object is derived from the BoundaryCondition object. 

    Attributes
    ----------
    name: str
        A String specifying the boundary condition repository key.
    distributionType: SymbolicConstant
        A SymbolicConstant specifying how the boundary condition is distributed spatially.
        Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
    fieldName: str
        A String specifying the name of the :py:class:`~abaqus.Field.AnalyticalField.AnalyticalField` object associated with this boundary
        condition. The **fieldName** argument applies only when **distributionType=FIELD**. The
        default value is an empty string.
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
    # Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 
    distributionType: SymbolicConstant = UNIFORM

    # A String specifying the name of the AnalyticalField object associated with this boundary 
    # condition. The *fieldName* argument applies only when *distributionType*=FIELD. The 
    # default value is an empty string. 
    fieldName: str = ''

    # A SymbolicConstant specifying the category of the boundary condition. Possible values 
    # are MECHANICAL and THERMAL. 
    category: SymbolicConstant = None

    # A Region object specifying the region to which the boundary condition is applied. 
    region: Region = Region()

    # None or a DatumCsys object specifying the local coordinate system of the boundary 
    # condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
    # in the global coordinate system. The default value is None. 
    localCsys: str = None

    def __init__(self, name: str, createStepName: str, region: Region, fieldName: str = '',
                 v1: typing.Union[SymbolicConstant, float] = UNSET,
                 v2: typing.Union[SymbolicConstant, float] = UNSET,
                 v3: typing.Union[SymbolicConstant, float] = UNSET,
                 vr1: typing.Union[SymbolicConstant, float] = UNSET,
                 vr2: typing.Union[SymbolicConstant, float] = UNSET,
                 vr3: typing.Union[SymbolicConstant, float] = UNSET, amplitude: str = UNSET,
                 localCsys: str = None, distributionType: SymbolicConstant = UNIFORM):
        """This method creates a VelocityBC object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].VelocityBC
        
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary 
            condition. The *fieldName* argument applies only when *distributionType*=FIELD. The 
            default value is an empty string. 
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
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 

        Returns
        -------
            A VelocityBC object.
        """
        super().__init__()
        pass

    def setValues(self, fieldName: str = '', v1: typing.Union[SymbolicConstant, float] = UNSET,
                  v2: typing.Union[SymbolicConstant, float] = UNSET,
                  v3: typing.Union[SymbolicConstant, float] = UNSET,
                  vr1: typing.Union[SymbolicConstant, float] = UNSET,
                  vr2: typing.Union[SymbolicConstant, float] = UNSET,
                  vr3: typing.Union[SymbolicConstant, float] = UNSET, amplitude: str = UNSET,
                  localCsys: str = None, distributionType: SymbolicConstant = UNIFORM):
        """This method modifies the data for an existing VelocityBC object in the step where it is
        created.
        
        Parameters
        ----------
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary 
            condition. The *fieldName* argument applies only when *distributionType*=FIELD. The 
            default value is an empty string. 
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
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 
        """
        pass

    def setValuesInStep(self, stepName: str,
                        v1: typing.Union[SymbolicConstant, float] = SET,
                        v2: typing.Union[SymbolicConstant, float] = SET,
                        v3: typing.Union[SymbolicConstant, float] = SET,
                        vr1: typing.Union[SymbolicConstant, float] = SET,
                        vr2: typing.Union[SymbolicConstant, float] = SET,
                        vr3: typing.Union[SymbolicConstant, float] = SET,
                        amplitude: str = ''):
        """This method modifies the propagating data for an existing VelocityBC object in the
        specified step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified. 
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
            boundary condition is changed to have no amplitude reference. You should provide the 
            *amplitude* argument only if it is valid for the specified step. 
        """
        pass
