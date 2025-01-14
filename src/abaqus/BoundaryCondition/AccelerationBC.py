import typing

from abaqusConstants import *
from .BoundaryCondition import BoundaryCondition
from ..Region.Region import Region


class AccelerationBC(BoundaryCondition):
    """The AccelerationBC object stores the data for an acceleration boundary condition. 
    The AccelerationBC object is derived from the BoundaryCondition object. 

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
                 a1: typing.Union[SymbolicConstant, float] = UNSET,
                 a2: typing.Union[SymbolicConstant, float] = UNSET,
                 a3: typing.Union[SymbolicConstant, float] = UNSET,
                 ar1: typing.Union[SymbolicConstant, float] = UNSET,
                 ar2: typing.Union[SymbolicConstant, float] = UNSET,
                 ar3: typing.Union[SymbolicConstant, float] = UNSET, amplitude: str = UNSET,
                 localCsys: str = None, distributionType: SymbolicConstant = UNIFORM):
        """This method creates an AccelerationBC object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].AccelerationBC
        
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
        a1
            A Float or a SymbolicConstant specifying the acceleration component in the 1-direction. 
            Possible values for the SymbolicConstant are UNSET and SET. The default value is 
            UNSET.Note:Although *a1*, *a2*, *a3*, *ar1*, *ar2*, and *ar3* are optional arguments, at 
            least one of them must be specified. 
        a2
            A Float or a SymbolicConstant specifying the acceleration component in the 2-direction. 
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET. 
        a3
            A Float or a SymbolicConstant specifying the acceleration component in the 3-direction. 
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET. 
        ar1
            A Float or a SymbolicConstant specifying the rotational acceleration component about the 
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        ar2
            A Float or a SymbolicConstant specifying the rotational acceleration component about the 
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        ar3
            A Float or a SymbolicConstant specifying the rotational acceleration component about the 
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
            An AccelerationBC object.
        """
        super().__init__()
        pass

    def setValues(self, fieldName: str = '', a1: typing.Union[SymbolicConstant, float] = UNSET,
                  a2: typing.Union[SymbolicConstant, float] = UNSET,
                  a3: typing.Union[SymbolicConstant, float] = UNSET,
                  ar1: typing.Union[SymbolicConstant, float] = UNSET,
                  ar2: typing.Union[SymbolicConstant, float] = UNSET,
                  ar3: typing.Union[SymbolicConstant, float] = UNSET, amplitude: str = UNSET,
                  localCsys: str = None, distributionType: SymbolicConstant = UNIFORM):
        """This method modifies the data for an existing AccelerationBC object in the step where it
        is created.
        
        Parameters
        ----------
        fieldName
            A String specifying the name of the AnalyticalField object associated with this boundary 
            condition. The *fieldName* argument applies only when *distributionType*=FIELD. The 
            default value is an empty string. 
        a1
            A Float or a SymbolicConstant specifying the acceleration component in the 1-direction. 
            Possible values for the SymbolicConstant are UNSET and SET. The default value is 
            UNSET.Note:Although *a1*, *a2*, *a3*, *ar1*, *ar2*, and *ar3* are optional arguments, at 
            least one of them must be specified. 
        a2
            A Float or a SymbolicConstant specifying the acceleration component in the 2-direction. 
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET. 
        a3
            A Float or a SymbolicConstant specifying the acceleration component in the 3-direction. 
            Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET. 
        ar1
            A Float or a SymbolicConstant specifying the rotational acceleration component about the 
            1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        ar2
            A Float or a SymbolicConstant specifying the rotational acceleration component about the 
            2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default 
            value is UNSET. 
        ar3
            A Float or a SymbolicConstant specifying the rotational acceleration component about the 
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
                        a1: typing.Union[SymbolicConstant, float] = SET,
                        a2: typing.Union[SymbolicConstant, float] = SET,
                        a3: typing.Union[SymbolicConstant, float] = SET,
                        ar1: typing.Union[SymbolicConstant, float] = SET,
                        ar2: typing.Union[SymbolicConstant, float] = SET,
                        ar3: typing.Union[SymbolicConstant, float] = SET,
                        amplitude: str = ''):
        """This method modifies the propagating data for an existing AccelerationBC object in the
        specified step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified. 
        a1
            A Float or a SymbolicConstant specifying the acceleration component in the 1-direction. 
            Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED. 
        a2
            A Float or a SymbolicConstant specifying the acceleration component in the 2-direction. 
            Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED. 
        a3
            A Float or a SymbolicConstant specifying the acceleration component in the 3-direction. 
            Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED. 
        ar1
            A Float or a SymbolicConstant specifying the rotational acceleration component about the 
            1-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED. 
        ar2
            A Float or a SymbolicConstant specifying the rotational acceleration component about the 
            2-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED. 
        ar3
            A Float or a SymbolicConstant specifying the rotational acceleration component about the 
            3-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED. 
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible 
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the 
            amplitude is propagated from the previous analysis step. FREED should be used if the 
            boundary condition is changed to have no amplitude reference. You should provide the 
            *amplitude* argument only if it is valid for the specified step. 
        """
        pass
