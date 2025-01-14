from abaqusConstants import *
from .BodyCharge import BodyCharge
from .BodyConcentrationFlux import BodyConcentrationFlux
from .BodyCurrent import BodyCurrent
from .BodyCurrentDensity import BodyCurrentDensity
from .BodyForce import BodyForce
from .BodyHeatFlux import BodyHeatFlux
from .BoltLoad import BoltLoad
from .ConcCharge import ConcCharge
from .ConcConcFlux import ConcConcFlux
from .ConcCurrent import ConcCurrent
from .ConcPoreFluid import ConcPoreFluid
from .ConcentratedForce import ConcentratedForce
from .ConcentratedHeatFlux import ConcentratedHeatFlux
from .ConnectorForce import ConnectorForce
from .ConnectorMoment import ConnectorMoment
from .CoriolisForce import CoriolisForce
from .Gravity import Gravity
from .InertiaRelief import InertiaRelief
from .InwardVolAccel import InwardVolAccel
from .LineLoad import LineLoad
from .Moment import Moment
from .PEGLoad import PEGLoad
from .PipePressure import PipePressure
from .Pressure import Pressure
from .RotationalBodyForce import RotationalBodyForce
from .ShellEdgeLoad import ShellEdgeLoad
from .SubmodelSB import SubmodelSB
from .SubstructureLoad import SubstructureLoad
from .SurfaceCharge import SurfaceCharge
from .SurfaceConcentrationFlux import SurfaceConcentrationFlux
from .SurfaceCurrent import SurfaceCurrent
from .SurfaceCurrentDensity import SurfaceCurrentDensity
from .SurfaceHeatFlux import SurfaceHeatFlux
from .SurfacePoreFluid import SurfacePoreFluid
from .SurfaceTraction import SurfaceTraction
from ..Datum.DatumAxis import DatumAxis
from ..Model.ModelBase import ModelBase
from ..Region.Region import Region


class LoadModel(ModelBase):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        mdb.models[name]

    """

    def BodyCharge(self, name: str, createStepName: str, region: Region, magnitude: float,
                   amplitude: str = UNSET, distributionType: SymbolicConstant = UNIFORM, field: str = '') -> BodyCharge:
        """This method creates a BodyCharge object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].BodyCharge
        
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
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The *field* argument applies only when *distributionType*=FIELD. The default value is an
            empty string.

        Returns
        -------
            A BodyCharge object.
        """
        self.loads[name] = load = BodyCharge(name, createStepName, region, magnitude, amplitude, distributionType,
                                             field)
        return load

    def BodyConcentrationFlux(self, name: str, createStepName: str, region: Region, magnitude: float, field: str = '',
                              distributionType: SymbolicConstant = UNIFORM,
                              amplitude: str = UNSET) -> BodyConcentrationFlux:
        """This method creates a BodyConcentrationFlux object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].BodyConcentrationFlux
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            A Region object specifying the region to which the load is applied.
        magnitude
            A Float specifying the body concentration flux magnitude. *magnitude* is optional if
            *distributionType*=USER_DEFINED.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The *field* argument applies only when *distributionType*=FIELD. The default value is an
            empty string.
        distributionType
            A SymbolicConstant specifying how the body concentration flux is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.

        Returns
        -------
            A BodyConcentrationFlux object.
        """
        self.loads[name] = load = BodyConcentrationFlux(name, createStepName, region, magnitude, field,
                                                        distributionType, amplitude)
        return load

    def BodyCurrent(self, name: str, createStepName: str, region: Region, magnitude: float,
                    amplitude: str = UNSET, distributionType: SymbolicConstant = UNIFORM,
                    field: str = '') -> BodyCurrent:
        """This method creates a BodyCurrent object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].BodyCurrent
        
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
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The *field* argument applies only when *distributionType*=FIELD. The default value is an
            empty string.

        Returns
        -------
            A BodyCurrent object.
        """
        self.loads[name] = load = BodyCurrent(name, createStepName, region, magnitude, amplitude, distributionType,
                                              field)
        return load

    def BodyCurrentDensity(self, name: str, createStepName: str, region: Region, comp1: str, comp2: str, comp3: str,
                           amplitude: str = UNSET, distributionType: SymbolicConstant = UNIFORM) -> BodyCurrentDensity:
        """This method creates a BodyCurrentDensity object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].BodyCurrentDensity
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created. This must be the
            first analysis step name.
        region
            A Region object specifying the region to which the load is applied.
        comp1
            A Complex specifying the first component of the load.
        comp2
            A Complex specifying the second component of the load.
        comp3
            A Complex specifying the third component of the load.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM and USER_DEFINED. The default value is UNIFORM.

        Returns
        -------
            A BodyCurrentDensity object.
        """
        self.loads[name] = load = BodyCurrentDensity(name, createStepName, region, comp1, comp2, comp3, amplitude,
                                                     distributionType)
        return load

    def BodyForce(self, name: str, createStepName: str, region: Region, field: str = '',
                  distributionType: SymbolicConstant = UNIFORM, comp1: float = None, comp2: float = None,
                  comp3: float = None, amplitude: str = UNSET) -> BodyForce:
        """This method creates a BodyForce object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].BodyForce
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            A Region object specifying the region to which the load is applied.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The *field* argument applies only when *distributionType*=FIELD. The default value is an
            empty string.
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        comp1
            A Float or a Complex specifying the body force component in the
            1-direction.Note:Although *comp1*, *comp2*, and *comp3* are optional arguments, at least
            one of them must be nonzero unless *distributionType*=USER_DEFINED.
        comp2
            A Float or a Complex specifying the body force component in the 2-direction.
        comp3
            A Float or a Complex specifying the body force component in the 3-direction.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.

        Returns
        -------
            A BodyForce object.
        """
        self.loads[name] = load = BodyForce(name, createStepName, region, field, distributionType, comp1, comp2, comp3,
                                            amplitude)
        return load

    def BodyHeatFlux(self, name: str, createStepName: str, region: Region, magnitude: float, field: str = '',
                     distributionType: SymbolicConstant = UNIFORM, amplitude: str = UNSET) -> BodyHeatFlux:
        """This method creates a BodyHeatFlux object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].BodyHeatFlux
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            A Region object specifying the region to which the load is applied.
        magnitude
            A Float specifying the body heat flux magnitude. *magnitude* is optional if
            *distributionType*=USER_DEFINED.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The *field* argument applies only when *distributionType*=FIELD. The default value is an
            empty string.
        distributionType
            A SymbolicConstant specifying how the body heat flux is distributed spatially. Possible
            values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.

        Returns
        -------
            A BodyHeatFlux object.
        """
        self.loads[name] = load = BodyHeatFlux(name, createStepName, region, magnitude, field, distributionType,
                                               amplitude)
        return load

    def BoltLoad(self, name: str, createStepName: str, region: Region, magnitude: float,
                 boltMethod: SymbolicConstant = APPLY_FORCE, datumAxis: DatumAxis = DatumAxis(),
                 amplitude: str = UNSET, preTenSecPartLevel: Boolean = False) -> BoltLoad:
        """This method creates a BoltLoad object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].BoltLoad
        
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
            A Float specifying the bolt load magnitude.
        boltMethod
            A SymbolicConstant specifying the method of applying the bolt load. Possible values are
            APPLY_FORCE and ADJUST_LENGTH. The default value is APPLY_FORCE.
        datumAxis
            A DatumAxis object specifying the orientation of the pre-tension section normal.Note:
            *datumAxis* is applicable only for Solid and Shell regions; it has no meaning for Wire
            regions.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.
        preTenSecPartLevel
            A Boolean specifying whether the pre-tension section is to be defined at the part level.
            The default value is False. You should provide the *preTenSecPartLevel* argument only if
            the selected region belongs to a dependent part instance. A pre-tension section cannot
            be defined at the part level for independent and model instances.

        Returns
        -------
            A BoltLoad object.

        Raises
        ------
            TextError.
        """
        self.loads[name] = load = BoltLoad(name, createStepName, region, magnitude, boltMethod, datumAxis, amplitude,
                                           preTenSecPartLevel)
        return load

    def ConcCharge(self, name: str, createStepName: str, region: Region, magnitude: float,
                   distributionType: SymbolicConstant = UNIFORM, field: str = '', amplitude: str = UNSET) -> ConcCharge:
        """This method creates a ConcCharge object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].ConcCharge
        
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

        Returns
        -------
            A ConcCharge object.
        """
        self.loads[name] = load = ConcCharge(name, createStepName, region, magnitude, distributionType, field,
                                             amplitude)
        return load

    def ConcConcFlux(self, name: str, createStepName: str, region: Region, magnitude: float,
                     distributionType: SymbolicConstant = UNIFORM, field: str = '',
                     amplitude: str = UNSET) -> ConcConcFlux:
        """This method creates a ConcConcFlux object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].ConcConcFlux
        
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

        Returns
        -------
            A ConcConcFlux object.
        """
        self.loads[name] = load = ConcConcFlux(name, createStepName, region, magnitude, distributionType, field,
                                               amplitude)
        return load

    def ConcCurrent(self, name: str, createStepName: str, region: Region, magnitude: float,
                    distributionType: SymbolicConstant = UNIFORM, field: str = '',
                    amplitude: str = UNSET) -> ConcCurrent:
        """This method creates a ConcCurrent object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].ConcCurrent
        
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

        Returns
        -------
            A ConcCurrent object.
        """
        self.loads[name] = load = ConcCurrent(name, createStepName, region, magnitude, distributionType, field,
                                              amplitude)
        return load

    def ConcentratedForce(self, name: str, createStepName: str, region: Region,
                          distributionType: SymbolicConstant = UNIFORM, field: str = '', cf1: float = None,
                          cf2: float = None, cf3: float = None, amplitude: str = UNSET, follower: Boolean = OFF,
                          localCsys: int = None) -> ConcentratedForce:
        """This method creates a ConcentratedForce object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].ConcentratedForce
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            A Region object specifying the region to which the load is applied.
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The *field* argument applies only when *distributionType*=FIELD. The default value is an
            empty string.
        cf1
            A Float or a Complex specifying the concentrated force component in the 1-direction.
            Although *cf1*, *cf2*, and *cf3* are optional arguments, at least one of them must be
            nonzero.
        cf2
            A Float or a Complex specifying the concentrated force component in the 2-direction.
        cf3
            A Float or a Complex specifying the concentrated force component in the 3-direction.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.
        follower
            A Boolean specifying whether the direction of the force rotates with the rotation at
            each node of the region. You should provide the *follower* argument only if it is valid
            for the specified step. The default value is OFF.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the load's degrees
            of freedom. If *localCsys*=None, the degrees of freedom are defined in the global
            coordinate system. When this member is queried, it returns an Int. The default value is
            None.

        Returns
        -------
            A ConcentratedForce object.
        """
        self.loads[name] = load = ConcentratedForce(name, createStepName, region, distributionType, field, cf1, cf2,
                                                    cf3, amplitude, follower, localCsys)
        return load

    def ConcentratedHeatFlux(self, name: str, createStepName: str, region: Region, magnitude: float,
                             distributionType: SymbolicConstant = UNIFORM, field: str = '', amplitude: str = UNSET,
                             dof: int = 11) -> ConcentratedHeatFlux:
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
        self.loads[name] = load = ConcentratedHeatFlux(name, createStepName, region, magnitude, distributionType, field,
                                                       amplitude, dof)
        return load

    def ConcPoreFluid(self, name: str, createStepName: str, region: Region, magnitude: float,
                      distributionType: SymbolicConstant = UNIFORM, field: str = '',
                      amplitude: str = UNSET) -> ConcPoreFluid:
        """This method creates a ConcPoreFluid object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].ConcPoreFluid
        
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

        Returns
        -------
            A ConcPoreFluid object.
        """
        self.loads[name] = load = ConcPoreFluid(name, createStepName, region, magnitude, distributionType, field,
                                                amplitude)
        return load

    def ConnectorForce(self, name: str, createStepName: str, region: str = '', fastenerName: str = '',
                       fastenerSetName: str = '', f1: float = None, f2: float = None, f3: float = None,
                       amplitude: str = UNSET) -> ConnectorForce:
        """This method creates a ConnectorForce object on a wire region. Alternatively, the load
        may also be applied to a wire set referenced from an assembled fastener template model.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].ConnectorForce
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            The wire region to which the load is applied. This argument is not valid when
            *fastenerName* and *fastenerSetName* are specified.
        fastenerName
            A String specifying the name of the assembled fastener to which the load will be
            applied. This argument is not valid when *region* is specified. When this argument is
            specified, *fastenerSetName* must also be specified. The default value is an empty
            string.
        fastenerSetName
            A String specifying the assembled fastener template model set to which the load will be
            applied. This argument is not valid when *region* is specified. When this argument is
            specified, *fastenerName* must also be specified. The default value is an empty string.
        f1
            A Float or a Complex specifying the connector force component in the connector's local
            1-direction.Note:Although *f1*, *f2*, and *f3* are optional arguments, at least one of
            them must be nonzero.
        f2
            A Float or a Complex specifying the connector force component in the connector's local
            2-direction.
        f3
            A Float or a Complex specifying the connector force component in the connector's local
            3-direction.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.

        Returns
        -------
            A ConnectorForce object.
        """
        self.loads[name] = load = ConnectorForce(name, createStepName, region, fastenerName, fastenerSetName, f1, f2,
                                                 f3, amplitude)
        return load

    def ConnectorMoment(self, name: str, createStepName: str, region: str = '', fastenerName: str = '',
                        fastenerSetName: str = '', m1: float = None, m2: float = None, m3: float = None,
                        amplitude: str = UNSET) -> ConnectorMoment:
        """This method creates a ConnectorMoment object on a wire region. Alternatively, the load
        may also be applied to a wire set referenced from an assembled fastener template model.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].ConnectorMoment
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            The wire region to which the load is applied. This argument is not valid when
            *fastenerName* and *fastenerSetName* are specified.
        fastenerName
            A String specifying the name of the assembled fastener to which the load will be
            applied. This argument is not valid when *region* is specified. When this argument is
            specified, *fastenerSetName* must also be specified. The default value is an empty
            string.
        fastenerSetName
            A String specifying the assembled fastener template model set to which the load will be
            applied. This argument is not valid when *region* is specified. When this argument is
            specified, *fastenerName* must also be specified. The default value is an empty string.
        m1
            A Float or a Complex specifying the moment component in the connector's local
            4-direction.
        m2
            A Float or a Complex specifying the moment component in the connector's local
            5-direction.
        m3
            A Float or a Complex specifying the moment component in the connector's local
            6-direction.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.

        Returns
        -------
            A ConnectorMoment object.
        """
        self.loads[name] = load = ConnectorMoment(name, createStepName, region, fastenerName, fastenerSetName, m1, m2,
                                                  m3, amplitude)
        return load

    def CoriolisForce(self, name: str, createStepName: str, region: Region, magnitude: float, point1: tuple,
                      point2: tuple, amplitude: str = UNSET, distributionType: SymbolicConstant = UNIFORM,
                      field: str = '') -> CoriolisForce:
        """This method creates a CoriolisForce object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].CoriolisForce
        
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
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The *field* argument applies only when *distributionType*=FIELD. The default value is an
            empty string.

        Returns
        -------
            A CoriolisForce object.
        """
        self.loads[name] = load = CoriolisForce(name, createStepName, region, magnitude, point1, point2, amplitude,
                                                distributionType, field)
        return load

    def Gravity(self, name: str, createStepName: str, distributionType: SymbolicConstant = UNIFORM,
                field: str = '', region: Region = Region(), comp1: float = None, comp2: float = None,
                comp3: float = None, amplitude: str = UNSET) -> Gravity:
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
        self.loads[name] = load = Gravity(name, createStepName, distributionType, field, region, comp1, comp2, comp3,
                                          amplitude)
        return load

    def InertiaRelief(self, name: str, createStepName: str, u1: Boolean = OFF, u2: Boolean = OFF, u3: Boolean = OFF,
                      ur1: Boolean = OFF, ur2: Boolean = OFF, ur3: Boolean = OFF, referencePoint: tuple = (),
                      localCoordinates: int = None) -> InertiaRelief:
        """This method creates an InertiaRelief object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].InertiaRelief
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        u1
            A Boolean specifying the 1-direction as a free direction.Note:Although *u1*, *u2*, *u3*,
            *ur1*, *ur2*, and *ur3* are optional arguments, at least one of them must be specified.
            Further, any specified set of free directions cannot include only two rotational degrees
            of freedom.
        u2
            A Boolean specifying the 2-direction as a free direction.
        u3
            A Boolean specifying the 3-direction as a free direction.
        ur1
            A Boolean specifying the rotation about the 1–direction as a free direction.
        ur2
            A Boolean specifying the rotation about the 2–direction as a free direction.
        ur3
            A Boolean specifying the rotation about the 3–direction as a free direction.
        referencePoint
            A sequence of Floats specifying the *X*, *Y* and *Z*-coordinates of a fixed rotation
            point or a point on the rotation axis or a point on the symmetry line, about which
            rotations are defined. Such a point must be specified only for certain combinations of
            free directions.
        localCoordinates
            None or a DatumCsys object specifying the local coordinate system of the rigid body
            degrees of freedom for the inertia relief load. If *localCoordinates*=None, the free
            directions are defined in the global coordinate system. When this member is queried, it
            returns an Int. The default value is None.

        Returns
        -------
            An InertiaRelief object.
        """
        self.loads[name] = load = InertiaRelief(name, createStepName, u1, u2, u3, ur1, ur2, ur3, referencePoint,
                                                localCoordinates)
        return load

    def InwardVolAccel(self, name: str, createStepName: str, region: Region, magnitude: float,
                       distributionType: SymbolicConstant = UNIFORM, field: str = '',
                       amplitude: str = UNSET) -> InwardVolAccel:
        """This method creates a InwardVolAccel object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].InwardVolAccel
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created. This must be the
            name of the first analysis step.
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

        Returns
        -------
            An InwardVolAccel object.
        """
        self.loads[name] = load = InwardVolAccel(name, createStepName, region, magnitude, distributionType, field,
                                                 amplitude)
        return load

    def LineLoad(self, name: str, createStepName: str, region: Region,
                 distributionType: SymbolicConstant = UNIFORM, field: str = '', comp1: float = None,
                 comp2: float = None, comp3: float = None, amplitude: str = UNSET,
                 system: SymbolicConstant = GLOBAL) -> LineLoad:
        """This method creates a LineLoad object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].LineLoad
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            A Region object specifying the region to which the load is applied.
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The *field* argument applies only when *distributionType*=FIELD. The default value is an
            empty string.
        comp1
            A Float or a Complex specifying the component of the load in the global or the beam
            local 1-direction.Note:Although *comp1*, *comp2*, and *comp3* are optional arguments, at
            least one of them must be nonzero unless *distributionType*=USER_DEFINED.
        comp2
            A Float or a Complex specifying the component of the load in the global or the beam
            local 2-direction.
        comp3
            A Float or a Complex specifying the component of the load in the global 3-direction.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.
        system
            A SymbolicConstant specifying whether the load is applied in a global or the beam local
            frame of reference. Possible values are GLOBAL and LOCAL. The default value is GLOBAL.

        Returns
        -------
            A LineLoad object.
        """
        self.loads[name] = load = LineLoad(name, createStepName, region, distributionType, field, comp1, comp2, comp3,
                                           amplitude, system)
        return load

    def Moment(self, name: str, createStepName: str, region: Region, cm1: float = None, cm2: float = None,
               cm3: float = None, amplitude: str = UNSET, follower: Boolean = OFF,
               localCsys: int = None, distributionType: SymbolicConstant = UNIFORM, field: str = '') -> Moment:
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
        self.loads[name] = load = Moment(name, createStepName, region, cm1, cm2, cm3, amplitude, follower, localCsys,
                                         distributionType, field)
        return load

    def PEGLoad(self, name: str, createStepName: str, region: Region,
                distributionType: SymbolicConstant = UNIFORM, field: str = '', comp1: float = None,
                comp2: float = None, comp3: float = None, amplitude: str = UNSET) -> PEGLoad:
        """This method creates a PEGLoad object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].PEGLoad
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            A Region object specifying the region to which the load is applied.
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The *field* argument applies only when *distributionType*=FIELD. The default value is an
            empty string.
        comp1
            A Float or a Complex specifying the load component at dof 1 of reference node
            1.Note:Although *comp1*, *comp2*, and *comp3* are optional arguments, at least one of
            them must be nonzero.
        comp2
            A Float or a Complex specifying the load component at dof 1 of reference node 2.
        comp3
            A Float or a Complex specifying the load component at dof 2 of reference node 2.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.

        Returns
        -------
            A PEGLoad object.
        """
        self.loads[name] = load = PEGLoad(name, createStepName, region, distributionType, field, comp1, comp2, comp3,
                                          amplitude)
        return load

    def PipePressure(self, name: str, createStepName: str, region: Region, magnitude: float, diameter: float,
                     hZero: float, hReference: float, field: str = '', amplitude: str = UNSET,
                     distributionType: SymbolicConstant = UNIFORM, side: SymbolicConstant = INTERNAL) -> PipePressure:
        """This method creates a Pressure object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].PipePressure
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the pressure is created.
        region
            A Region object specifying the region to which the load is applied.
        magnitude
            A Float specifying the pressure magnitude.Note:*magnitude* is optional if
            *distributionType*=USER_DEFINED.
        diameter
            A Float specifying the effective inner or outer diameter.
        hZero
            A Float specifying the height of the zero pressure level when
            *distributionType*=HYDROSTATIC.
        hReference
            A Float specifying the height of the reference pressure level when
            *distributionType*=HYDROSTATIC.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The *field* argument applies only when *distributionType*=FIELD. The default value is an
            empty string.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
            HYDROSTATIC, USER_DEFINED, and FIELD. The default value is UNIFORM.
        side
            A SymbolicConstant specifying whether the pressure is applied internally or externally.
            Possible values are INTERNAL and EXTERNAL. The default value is INTERNAL.

        Returns
        -------
            A PipePressure object.
        """
        self.loads[name] = load = PipePressure(name, createStepName, region, magnitude, diameter, hZero, hReference,
                                               field, amplitude, distributionType, side)
        return load

    def Pressure(self, name: str, createStepName: str, region: Region, magnitude: float = 0.0, hZero: float = 0.0,
                 hReference: float = 0.0, field: str = '', refPoint: str = '',
                 distributionType: SymbolicConstant = UNIFORM, amplitude: str = UNSET) -> Pressure:
        """This method creates a Pressure object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].Pressure
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the pressure is created.
        region
            A Region object specifying the region to which the load is applied.
        magnitude
            A Float or a Complex specifying the pressure magnitude.Note:*magnitude* is optional if
            *distributionType*=USER_DEFINED.
        hZero
            A Float specifying the height of the zero pressure level when
            *distributionType*=HYDROSTATIC.
        hReference
            A Float specifying the height of the reference pressure level when
            *distributionType*=HYDROSTATIC.
        field
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with this load. The *field* argument applies only when *distributionType*=FIELD or
            *distributionType*=DISCRETE_FIELD. The default value is an empty string.
        refPoint
            A Region specifying the reference point from which the relative velocity is determined
            when *distributionType*=STAGNATION or VISCOUS.
        distributionType
            A SymbolicConstant specifying how the pressure is distributed spatially. Possible values
            are UNIFORM, USER_DEFINED, FIELD, HYDROSTATIC, STAGNATION, VISCOUS, TOTAL_FORCE, and
            DISCRETE_FIELD. The default value is UNIFORM.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.

        Returns
        -------
            A Pressure object.
        """
        self.loads[name] = load = Pressure(name, createStepName, region, magnitude, hZero, hReference, field, refPoint,
                                           distributionType, amplitude)
        return load

    def RotationalBodyForce(self, name: str, createStepName: str, region: Region, magnitude: float, point1: tuple,
                            point2: tuple, distributionType: SymbolicConstant = UNIFORM, field: str = '',
                            centrifugal: Boolean = OFF, rotaryAcceleration: Boolean = OFF,
                            amplitude: str = UNSET) -> RotationalBodyForce:
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
        self.loads[name] = load = RotationalBodyForce(name, createStepName, region, magnitude, point1, point2,
                                                      distributionType, field, centrifugal, rotaryAcceleration,
                                                      amplitude)
        return load

    def ShellEdgeLoad(self, name: str, createStepName: str, region: Region, magnitude: float,
                      distributionType: SymbolicConstant = UNIFORM, field: str = '', amplitude: str = UNSET,
                      angle: float = 0, axis: SymbolicConstant = AXIS_1, localCsys: int = GENERAL,
                      userCsys: str = GENERAL, directionVector: tuple = (), follower: Boolean = ON,
                      resultant: Boolean = OFF, traction: SymbolicConstant = NORMAL) -> ShellEdgeLoad:
        """This method creates a ShellEdgeLoad object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].ShellEdgeLoad
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            A Region object specifying the region to which the load is applied.
        magnitude
            A Float or Complex specifying the load magnitude. *magnitude* is optional if
            *distributionType*=USER_DEFINED
        distributionType
            A SymbolicConstant specifying how the shell edge load is distributed spatially. Possible
            values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The *field* argument applies only when *distributionType*=FIELD. The default value is an
            empty string.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.
        angle
            A Float specifying an additional rotation of *directionVector* about an axis. The
            default value is 0.This parameter is available only if *traction* is GENERAL.
        axis
            A SymbolicConstant specifying the axis about which to apply an additional rotation of
            *directionVector*. Possible values are AXIS_1, AXIS_2, AXIS_3. The default value is
            AXIS_1.This parameter is available only if *traction* is GENERAL.
        localCsys
            A DatumCsys object specifying the local coordinate system of the load's degrees of
            freedom. The default value is None, indicating that the degrees of freedom are defined
            in the global coordinate system or by the *userCsys* parameter if defined. This
            parameter is available only if *traction* is GENERAL. When this member is queried, it
            returns an Int.
        userCsys
            A String specifying a CSYS defined by a user-subroutine. The default value is None,
            indicating that the degrees of freedom are defined in the global coordinate system or by
            the *localCsys* parameter if defined. This parameter is available only if *traction* is
            GENERAL.
        directionVector
            A tuple of two points specifying the direction of the load. Each point is specified as a
            point region or a tuple of coordinates. If *traction* is SHEAR, then *directionVector*
            will be projected onto the region surface. This parameter is available only if
            *traction* is GENERAL.
        follower
            A Boolean specifying whether the direction of the force changes with rotation. The
            default value is ON. This parameter may be modified only if *traction* is GENERAL. You
            should provide the *follower* argument only if it is valid for the specified step.
        resultant
            A Boolean specifying whether to maintain a constant resultant force by defining traction
            per unit undeformed area. If *resultant* is OFF, traction is defined per unit deformed
            area. The default value is OFF. You should provide the *resultant* argument only if it
            is valid for the specified step.
        traction
            A SymbolicConstant specifying how to apply surface traction. Possible values are NORMAL,
            TRANSVERSE, SHEAR, MOMENT and GENERAL. The default value is NORMAL.

        Returns
        -------
            A ShellEdgeLoad object.
        """
        self.loads[name] = load = ShellEdgeLoad(name, createStepName, region, magnitude, distributionType, field,
                                                amplitude, angle, axis, localCsys, userCsys, directionVector, follower,
                                                resultant, traction)
        return load

    def SubmodelSB(self, name: str, createStepName: str, region: Region, globalStep: str,
                   globalDrivingRegion: str = '', absoluteExteriorTolerance: float = None,
                   exteriorTolerance: float = 0, globalIncrement: int = 0) -> SubmodelSB:
        """This method creates a SubmodelSB object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].SubmodelSB
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            A Region object specifying the region to which the load is applied.
        globalStep
            A String specifying the step in the global model from which Abaqus reads the values of
            the variables that will drive the submodel analysis. The String indicates the position
            of the step in the sequence of analysis steps. For example, *globalStep*='1' indicates
            the first step.
        globalDrivingRegion
            A String specifying the element set in the global model that will be searched for
            elements whose responses will be used to drive the submodel. An empty string indicates
            that the entire global model will be searched. The default value is an empty string.
        absoluteExteriorTolerance
            None or a Float specifying the absolute value by which a driven node of the submodel can
            lie outside the region of the elements of the global model. The default value is None.
        exteriorTolerance
            None or a Float specifying the fraction of the average element size in the global model
            by which a driven node of the submodel can lie outside the region of the elements of the
            global model. The default value is 0.05.
        globalIncrement
            An Int specifying the increment number in the global model step from which the solution
            will be used to specify the values of the driven variables. If *globalIncrement*=0, the
            solution from the last increment will be used. The *globalIncrement* argument is
            applicable only for linear perturbation steps. The default value is 0.

        Returns
        -------
            A SubmodelSB object.
        """
        self.loads[name] = load = SubmodelSB(name, createStepName, region, globalStep, globalDrivingRegion,
                                             absoluteExteriorTolerance, exteriorTolerance, globalIncrement)
        return load

    def SubstructureLoad(self, name: str, createStepName: str, region: Region, loadCaseNames: str, magnitude: float,
                         amplitude: str = UNSET) -> SubstructureLoad:
        """This method creates a SubstructureLoad object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].SubstructureLoad
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the substructure load is created.
        region
            A Region object specifying the region to which the load is applied.
        loadCaseNames
            A list of names of the load cases that should be activated by this substructure load.
        magnitude
            A Float specifying the multiplier for the load case magnitude.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.

        Returns
        -------
            A SubstructureLoad object.
        """
        self.loads[name] = load = SubstructureLoad(name, createStepName, region, loadCaseNames, magnitude, amplitude)
        return load

    def SurfaceCharge(self, name: str, createStepName: str, region: Region, magnitude: float,
                      distributionType: SymbolicConstant = UNIFORM, field: str = '',
                      amplitude: str = UNSET) -> SurfaceCharge:
        """This method creates a SurfaceCharge object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].SurfaceCharge
        
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

        Returns
        -------
            A SurfaceCharge object.
        """
        self.loads[name] = load = SurfaceCharge(name, createStepName, region, magnitude, distributionType, field,
                                                amplitude)
        return load

    def SurfaceConcentrationFlux(self, name: str, createStepName: str, region: Region, magnitude: float,
                                 field: str = '',
                                 distributionType: SymbolicConstant = UNIFORM,
                                 amplitude: str = UNSET) -> SurfaceConcentrationFlux:
        """This method creates a SurfaceConcentrationFlux object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].SurfaceConcentrationFlux
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            A Region object specifying the region to which the load is applied.
        magnitude
            A Float specifying the surface concentration flux magnitude. *magnitude* is optional if
            *distributionType*=USER_DEFINED.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The *field* argument applies only when *distributionType*=FIELD. The default value is an
            empty string.
        distributionType
            A SymbolicConstant specifying how the surface concentration flux is distributed
            spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is
            UNIFORM.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.

        Returns
        -------
            A SurfaceConcentrationFlux object.
        """
        self.loads[name] = load = SurfaceConcentrationFlux(name, createStepName, region, magnitude, field,
                                                           distributionType, amplitude)
        return load

    def SurfaceCurrent(self, name: str, createStepName: str, region: Region, magnitude: float,
                       distributionType: SymbolicConstant = UNIFORM, field: str = '',
                       amplitude: str = UNSET) -> SurfaceCurrent:
        """This method creates a SurfaceCurrent object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].SurfaceCurrent
        
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

        Returns
        -------
            A SurfaceCurrent object.
        """
        self.loads[name] = load = SurfaceCurrent(name, createStepName, region, magnitude, distributionType, field,
                                                 amplitude)
        return load

    def SurfaceCurrentDensity(self, name: str, createStepName: str, region: Region, comp1: str, comp2: str, comp3: str,
                              distributionType: SymbolicConstant = UNIFORM,
                              amplitude: str = UNSET) -> SurfaceCurrentDensity:
        """This method creates a SurfaceCurrentDensity object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].SurfaceCurrentDensity
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created. This must be the
            first analysis step name.
        region
            A Region object specifying the region to which the load is applied.
        comp1
            A Complex specifying the first component of the load.
        comp2
            A Complex specifying the second component of the load.
        comp3
            A Complex specifying the third component of the load.
        distributionType
            A SymbolicConstant specifying how the load is distributed spatially. Possible values are
            UNIFORM and USER_DEFINED. The default value is UNIFORM.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.

        Returns
        -------
            A SurfaceCurrentDensity object.
        """
        self.loads[name] = load = SurfaceCurrentDensity(name, createStepName, region, comp1, comp2, comp3,
                                                        distributionType, amplitude)
        return load

    def SurfaceHeatFlux(self, name: str, createStepName: str, region: Region, magnitude: float, field: str = '',
                        distributionType: SymbolicConstant = UNIFORM, amplitude: str = UNSET) -> SurfaceHeatFlux:
        """This method creates a SurfaceHeatFlux object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].SurfaceHeatFlux
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            A Region object specifying the region to which the load is applied.
        magnitude
            A Float specifying the surface heat flux magnitude. *magnitude* is optional if
            *distributionType*=USER_DEFINED.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The *field* argument applies only when *distributionType*=FIELD. The default value is an
            empty string.
        distributionType
            A SymbolicConstant specifying how the surface heat flux is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.

        Returns
        -------
            A SurfaceHeatFlux object.
        """
        self.loads[name] = load = SurfaceHeatFlux(name, createStepName, region, magnitude, field, distributionType,
                                                  amplitude)
        return load

    def SurfacePoreFluid(self, name: str, createStepName: str, region: Region, magnitude: float, field: str = '',
                         distributionType: SymbolicConstant = UNIFORM, amplitude: str = UNSET) -> SurfacePoreFluid:
        """This method creates a SurfacePoreFluid object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].SurfacePoreFluid
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            A Region object specifying the region to which the load is applied.
        magnitude
            A Float specifying the surface pore fluid flow magnitude. *magnitude* is optional if
            *distributionType*=USER_DEFINED.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The *field* argument applies only when *distributionType*=FIELD. The default value is an
            empty string.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
            USER_DEFINED, and FIELD. The default value is UNIFORM.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.

        Returns
        -------
            A SurfacePoreFluid object.
        """
        self.loads[name] = load = SurfacePoreFluid(name, createStepName, region, magnitude, field, distributionType,
                                                   amplitude)
        return load

    def SurfaceTraction(self, name: str, createStepName: str, region: Region, magnitude: float,
                        distributionType: SymbolicConstant = UNIFORM, field: str = '', amplitude: str = UNSET,
                        angle: float = 0, axis: SymbolicConstant = AXIS_1, localCsys: int = None,
                        userCsys: str = '', directionVector: tuple = (), follower: Boolean = ON,
                        resultant: Boolean = OFF, traction: SymbolicConstant = SHEAR) -> SurfaceTraction:
        """This method creates a SurfaceTraction object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].SurfaceTraction
        
        Parameters
        ----------
        name
            A String specifying the load repository key.
        createStepName
            A String specifying the name of the step in which the load is created.
        region
            A Region object specifying the region to which the load is applied.
        magnitude
            A Float or Complex specifying the load magnitude. *magnitude* is optional if
            *distributionType*=USER_DEFINED.
        distributionType
            A SymbolicConstant specifying how the surface traction is distributed spatially.
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
        field
            A String specifying the name of the AnalyticalField object associated with this load.
            The *field* argument applies only when *distributionType*=FIELD. The default value is an
            empty string.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the load has no amplitude reference. The default value is UNSET.
            You should provide the *amplitude* argument only if it is valid for the specified step.
        angle
            A Float specifying an additional rotation of *directionVector* about an axis. The
            default value is 0.0.
        axis
            A SymbolicConstant specifying the axis about which to apply an additional rotation of
            *directionVector*. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is
            AXIS_1.
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the load's degrees
            of freedom. If *localCsys*=None, the degrees of freedom are defined in the global
            coordinate system or by the *userCsys* parameter if defined. When this member is
            queried, it returns an Int. The default value is None.
        userCsys
            A String specifying a CSYS defined by a user-subroutine. If *userCsys*=None, the degrees
            of freedom are defined in the global coordinate system or by the *localCsys* parameter
            if defined. The default value is "None".
        directionVector
            A VertexArray object of length 2 specifying the direction of the load. Instead of
            through a ConstrainedSketchVertex, each point may be specified through a tuple of coordinates. If
            *traction* is SHEAR, then *directionVector* will be projected onto the region surface.
            This parameter is available only if *traction* is GENERAL or SHEAR.
        follower
            A Boolean specifying whether the direction of the force changes with rotation. The
            default value is ON.This parameter may be modified only if *traction* is GENERAL. You
            should provide the *follower* argument only if it is valid for the specified step.
        resultant
            A Boolean specifying whether the to maintain a constant resultant force by defining
            traction per unit undeformed area. If *resultant* is OFF, traction is defined per unit
            deformed area. The default value is OFF.You should provide the *resultant* argument only
            if it is valid for the specified step.
        traction
            A SymbolicConstant specifying how to apply surface traction. Possible values are SHEAR
            and GENERAL. The default value is SHEAR.

        Returns
        -------
            A SurfaceTraction object.
        """
        self.loads[name] = load = SurfaceTraction(name, createStepName, region, magnitude, distributionType, field,
                                                  amplitude, angle, axis, localCsys, userCsys, directionVector,
                                                  follower, resultant, traction)
        return load
