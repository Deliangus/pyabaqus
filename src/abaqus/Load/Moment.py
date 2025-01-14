import typing

from abaqusConstants import *
from .Load import Load
from ..Region.Region import Region


class Moment(Load):
    """The Moment object stores the data for a moment.
    The Moment object is derived from the Load object. 

    Attributes
    ----------
    name: str
        A String specifying the load repository key.
    distributionType: SymbolicConstant
        A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.
    follower: Boolean
        A Boolean specifying whether the direction of the force rotates with the rotation of the
        node. You should provide the **follower** argument only if it is valid for the specified
        step. The default value is OFF.
    localCsys: int
        None or a :py:class:`~abaqus.Datum.DatumCsys.DatumCsys` object specifying the ID of the Datum coordinate system used as the
        local coordinate system of the load. If **localCsys=None**, the load is defined in the
        global coordinate system. When this member is queried, it returns an Int. The default
        value is None.
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

    # A Boolean specifying whether the direction of the force rotates with the rotation of the 
    # node. You should provide the *follower* argument only if it is valid for the specified 
    # step. The default value is OFF. 
    follower: Boolean = OFF

    # None or a DatumCsys object specifying the ID of the Datum coordinate system used as the 
    # local coordinate system of the load. If *localCsys*=None, the load is defined in the 
    # global coordinate system. When this member is queried, it returns an Int. The default 
    # value is None. 
    localCsys: int = None

    # A String specifying the name of the AnalyticalField object associated with this load. 
    # The *field* argument applies only when *distributionType*=FIELD. The default value is an 
    # empty string. 
    field: str = ''

    # A Region object specifying the region to which the load is applied. 
    region: Region = Region()

    def __init__(self, name: str, createStepName: str, region: Region, cm1: float = None, cm2: float = None,
                 cm3: float = None, amplitude: str = UNSET, follower: Boolean = OFF,
                 localCsys: int = None, distributionType: SymbolicConstant = UNIFORM, field: str = ''):
        """This method creates a Moment object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Moment
        
        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            A Region object specifying the region to which the load is applied. 
        cm1
            A Float or a Complex specifying the load component in the 4-direction.Note:Although 
            *comp1*, *comp2*, and *comp3* are optional arguments, at least one of them must be 
            nonzero. 
        cm2
            A Float or a Complex specifying the load component in the 5- direction. 
        cm3
            A Float or a Complex specifying the load component in the 6-direction. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        follower
            A Boolean specifying whether the direction of the force rotates with the rotation of the 
            node. You should provide the *follower* argument only if it is valid for the specified 
            step. The default value is OFF. 
        localCsys
            None or a DatumCsys object specifying the ID of the Datum coordinate system used as the 
            local coordinate system of the load. If *localCsys*=None, the load is defined in the 
            global coordinate system. When this member is queried, it returns an Int. The default 
            value is None. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 

        Returns
        -------
            A Moment object.
        """
        super().__init__()
        pass

    def setValues(self, cm1: float = None, cm2: float = None, cm3: float = None, amplitude: str = UNSET,
                  follower: Boolean = OFF, localCsys: int = None,
                  distributionType: SymbolicConstant = UNIFORM, field: str = ''):
        """This method modifies the data for an existing Moment object in the step where it is
        created.
        
        Parameters
        ----------
        cm1
            A Float or a Complex specifying the load component in the 4-direction.Note:Although 
            *comp1*, *comp2*, and *comp3* are optional arguments, at least one of them must be 
            nonzero. 
        cm2
            A Float or a Complex specifying the load component in the 5- direction. 
        cm3
            A Float or a Complex specifying the load component in the 6-direction. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        follower
            A Boolean specifying whether the direction of the force rotates with the rotation of the 
            node. You should provide the *follower* argument only if it is valid for the specified 
            step. The default value is OFF. 
        localCsys
            None or a DatumCsys object specifying the ID of the Datum coordinate system used as the 
            local coordinate system of the load. If *localCsys*=None, the load is defined in the 
            global coordinate system. When this member is queried, it returns an Int. The default 
            value is None. 
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are 
            UNIFORM and FIELD. The default value is UNIFORM. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        """
        pass

    def setValuesInStep(self, stepName: str,
                        comp1: typing.Union[SymbolicConstant, float] = None,
                        comp2: typing.Union[SymbolicConstant, float] = None,
                        comp3: typing.Union[SymbolicConstant, float] = None,
                        amplitude: str = ''):
        """This method modifies the propagating data for an existing Moment object in the specified
        step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified. 
        comp1
            A Float, a Complex, or a SymbolicConstant specifying the load component in the 
            4-direction. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED 
            should be used if the load component is propagated from the previous static analysis 
            step. Use FREED to remove a previously defined load component. 
        comp2
            A Float, a Complex, or a SymbolicConstant specifying the load component in the 
            5-direction. For details see *comp1*. 
        comp3
            A Float, a Complex, or a SymbolicConstant specifying the load component in the 
            6-direction. For details see *comp1*. 
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible 
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the 
            amplitude is propagated from the previous static analysis step. FREED should be used if 
            the load is changed to have no amplitude reference. You should provide the *amplitude* 
            argument only if it is valid for the specified step. 
        """
        pass
