import typing

from abaqusConstants import *
from .AdjustPoints import AdjustPoints
from .Coupling import Coupling
from .DisplayBody import DisplayBody
from .EmbeddedRegion import EmbeddedRegion
from .Equation import Equation
from .MultipointConstraint import MultipointConstraint
from .RigidBody import RigidBody
from .ShellSolidCoupling import ShellSolidCoupling
from .Tie import Tie
from ..Assembly.PartInstance import PartInstance
from ..BasicGeometry.ModelDotArray import ModelDotArray
from ..Model.ModelBase import ModelBase
from ..Region.Region import Region


class ConstraintModel(ModelBase):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        mdb.models[name]

    """

    def AdjustPoints(self, name: str, surface: Region, controlPoints: Region) -> AdjustPoints:
        """This method creates an AdjustPoints object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].AdjustPoints
        
        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        surface
            A Region object specifying the surface to which the *controlPoints* are adjusted.
        controlPoints
            A Region object specifying the constraint control points.

        Returns
        -------
            An AdjustPoints object.
        """
        self.constraints[name] = constraint = AdjustPoints(name, surface, controlPoints)
        return constraint

    def Coupling(self, name: str, surface: Region, controlPoint: Region,
                 influenceRadius: typing.Union[SymbolicConstant, float], couplingType: SymbolicConstant,
                 adjust: Boolean = OFF, localCsys: str = None, u1: Boolean = ON, u2: Boolean = ON,
                 u3: Boolean = ON, ur1: Boolean = ON, ur2: Boolean = ON, ur3: Boolean = ON,
                 weightingMethod: SymbolicConstant = UNIFORM) -> Coupling:
        """This method creates a Coupling object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].Coupling
        
        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        surface
            A Region object specifying the surface on which the coupling nodes are located.
        controlPoint
            A Region object specifying the constraint control point.
        influenceRadius
            The SymbolicConstant WHOLE_SURFACE or a Float specifying the influence radius.
        couplingType
            A SymbolicConstant specifying the coupling constraint type. Possible values are
            KINEMATIC, DISTRIBUTING, and STRUCTURAL.
        adjust
            A Boolean specifying if the control point will be adjusted (moved) to the surface. The
            point will be adjusted in the direction normal to the specified surface. The default
            value is OFF.
        localCsys
            None or a DatumCsys object specifying the initial orientation of the local coordinate
            system for the coupling's degrees of freedom. If *localCsys*=None, the coupling is
            defined in the global coordinate system. The default value is None.
        u1
            A Boolean specifying if the displacement component in the 1-direction is constrained to
            the reference node for a kinematic coupling constraint. The default value is ON.The *u1*
            argument applies only when *couplingType*=KINEMATIC.
        u2
            A Boolean specifying if the displacement component in the 2-direction is constrained to
            the reference node for a kinematic coupling constraint. The default value is ON.The *u2*
            argument applies only when *couplingType*=KINEMATIC.
        u3
            A Boolean specifying if the displacement component in the 3-direction is constrained to
            the reference node for a kinematic coupling constraint. The default value is ON.The *u3*
            argument applies only when *couplingType*=KINEMATIC.
        ur1
            A Boolean specifying if the rotational displacement component about the 1-direction is
            constrained to the reference node for a kinematic coupling constraint. The default value
            is ON.The *ur1* argument applies only when *couplingType*=KINEMATIC.
        ur2
            A Boolean specifying if the rotational displacement component about the 2-direction is
            constrained to the reference node for a kinematic coupling constraint. The default value
            is ON.The *ur2* argument applies only when *couplingType*=KINEMATIC.
        ur3
            A Boolean specifying if the rotational displacement component about the 3-direction is
            constrained to the reference node for a kinematic coupling constraint. The default value
            is ON.The *ur3* argument applies only when *couplingType*=KINEMATIC.
        weightingMethod
            A SymbolicConstant specifying an optional weighting method used for calculating the
            distributing weight factors. Possible values are UNIFORM, LINEAR, QUADRATIC, and CUBIC.
            The default value is UNIFORM.The *weightingMethod* argument applies only when
            *couplingType*=DISTRIBUTING.

        Returns
        -------
            A Coupling object.
        """
        self.constraints[name] = constraint = Coupling(name, surface, controlPoint, influenceRadius, couplingType,
                                                       adjust, localCsys, u1, u2, u3, ur1, ur2, ur3, weightingMethod)
        return constraint

    def DisplayBody(self, name: str, instance: PartInstance, controlPoints: ModelDotArray) -> DisplayBody:
        """This method creates a DisplayBody object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].DisplayBody
        
        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        instance
            A PartInstance object specifying the part instance that is to be used for display only.
        controlPoints
            A ModelDotArray object specifying the motion of the PartInstance. The control points may
            be ConstrainedSketchVertex, ReferencePoint, or MeshNode objects. Their motion will control the motion of
            the PartInstance. If this argument is set to an empty sequence, the PartInstance will
            remain fixed in space during the analysis. The sequence can have either one object or
            three objects.

        Returns
        -------
            A DisplayBody object.
        """
        self.constraints[name] = constraint = DisplayBody(name, instance, controlPoints)
        return constraint

    def EmbeddedRegion(self, name: str, embeddedRegion: Region, hostRegion: Region,
                       weightFactorTolerance: float = None, toleranceMethod: SymbolicConstant = BOTH,
                       absoluteTolerance: float = 0, fractionalTolerance: float = 0) -> EmbeddedRegion:
        """This method creates a EmbeddedRegion object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].EmbeddedRegion
        
        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        embeddedRegion
            A Region object specifying the body region to be embedded.
        hostRegion
            A Region object specifying the host region. A value of None indicates that the host
            region is the whole model.
        weightFactorTolerance
            A Float specifying a small value below which the weighting factors will be zeroed out.
            The default value is 10–6.
        toleranceMethod
            A SymbolicConstant specifying the method used to determine the embedded element
            tolerance. Possible values are ABSOLUTE, FRACTIONAL, and BOTH. The default value is
            BOTH.
        absoluteTolerance
            A Float specifying the absolute value by which a node on the embedded region may lie
            outside the host region. If *absoluteTolerance*=0.0, the *fractionalTolerance* value
            will be used. The default value is 0.0.This argument applies only when
            *toleranceMethod*=ABSOLUTE or BOTH.
        fractionalTolerance
            A Float specifying the fractional value by which a node on the embedded region may lie
            outside the host region. The fractional value is based on the average element size
            within the host region. The default value is 0.05.If both tolerance arguments are
            specified, the smaller value will be used.This argument applies only when
            *toleranceMethod*=FRACTIONAL or BOTH.

        Returns
        -------
            An EmbeddedRegion object.
        """
        self.constraints[name] = constraint = EmbeddedRegion(name, embeddedRegion, hostRegion, weightFactorTolerance,
                                                             toleranceMethod, absoluteTolerance, fractionalTolerance)
        return constraint

    def Equation(self, name: str, terms: tuple) -> Equation:
        """This method creates an Equation object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].Equation
        
        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        terms
            A sequence of (Float, String, Int, Int) sequences specifying a coefficient, Set name,
            degree of freedom, and coordinate system ID. The coordinate system ID is optional.

        Returns
        -------
            An Equation object.

        Raises
        ------
            - If *terms* does not contain more than one entry:
              Equation must have two or more terms.
        """
        self.constraints[name] = constraint = Equation(name, terms)
        return constraint

    def MultipointConstraint(self, name: str, surface: Region, controlPoint: Region, mpcType: SymbolicConstant,
                             csys: str = None, userType: int = 0,
                             userMode: SymbolicConstant = DOF_MODE_MPC) -> MultipointConstraint:
        """This method creates a MultipointConstraint object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].MultipointConstraint
        
        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        surface
            A Region object specifying the surface on which the MultipointConstraint nodes are
            located.
        controlPoint
            A Region object specifying the constraint control point.
        mpcType
            A SymbolicConstant specifying the MPC type of the constraint. Possible values are
            BEAM_MPC, ELBOW_MPC, PIN_MPC, LINK_MPC, TIE_MPC, and USER_MPC.
        csys
            None or a DatumCsys object specifying the initial orientation of the local coordinate
            system for the MultipointConstraint's degrees of freedom. If *localCsys*=None, the
            MultipointConstraint is defined in the global coordinate system. The default value is
            None.
        userType
            An Int specifying to differentiate between different constraint types in a user-defined
            MultipointConstraint. The default value is 0.The *userType* argument applies only when
            *mpcType*=USER_MPC.
        userMode
            A SymbolicConstant specifying the mode of the constraint when it is user-defined.
            Possible values are DOF_MODE_MPC and NODE_MODE_MPC. The default value is
            DOF_MODE_MPC.The *userMode* argument applies only when *mpcType*=USER_MPC.

        Returns
        -------
            A MultipointConstraint object.
        """
        self.constraints[name] = constraint = MultipointConstraint(name, surface, controlPoint, mpcType, csys, userType,
                                                                   userMode)
        return constraint

    def RigidBody(self, name: str, refPointRegion: Region, bodyRegion: str = None, tieRegion: str = None,
                  pinRegion: str = None, surfaceRegion: str = None, refPointAtCOM: Boolean = OFF,
                  isothermal: Boolean = OFF) -> RigidBody:
        """This method creates a RigidBody object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].RigidBody
        
        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        refPointRegion
            A Region object specifying the reference point.
        bodyRegion
            None or a Region object specifying the elements constrained to the movement of the
            reference point. The default value is None.
        tieRegion
            None or a Region object specifying the nodes tied to the movement of the reference
            point. The default value is None.
        pinRegion
            None or a Region object specifying the nodes pinned to the movement of the reference
            point. The default value is None.
        surfaceRegion
            None or a Region object specifying the analytic surface constrained to the movement of
            the reference point. The default value is None.
        refPointAtCOM
            A Boolean specifying whether the analysis product should recompute the reference point
            position to be at the center of mass. The default value is OFF.
        isothermal
            A Boolean specifying whether the temperature degree of freedom should be constrained.
            The default value is OFF.

        Returns
        -------
            A RigidBody object.
        """
        self.constraints[name] = constraint = RigidBody(name, refPointRegion, bodyRegion, tieRegion, pinRegion,
                                                        surfaceRegion, refPointAtCOM, isothermal)
        return constraint

    def ShellSolidCoupling(self, name: str, shellEdge: Region, solidFace: Region,
                           positionToleranceMethod: SymbolicConstant = COMPUTED, positionTolerance: float = 0,
                           influenceDistanceMethod: SymbolicConstant = DEFAULT,
                           influenceDistance: float = 0) -> ShellSolidCoupling:
        """This method creates a ShellSolidCoupling object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].ShellSolidCoupling
        
        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        shellEdge
            A Region object specifying the name of the shell edge surface.
        solidFace
            A Region object specifying the name of the solid surface.
        positionToleranceMethod
            A SymbolicConstant specifying the method used to determine the position tolerance.
            Possible values are COMPUTED and SPECIFIED. The default value is COMPUTED.
        positionTolerance
            A Float specifying the position tolerance. The default value is 0.0.The
            *positionTolerance* argument applies only when
            *positionToleranceMethod*=SPECIFIED.Note:Abaqus will not constrain nodes on the solid
            face region outside the position tolerance.
        influenceDistanceMethod
            A SymbolicConstant specifying the method used to determine the influence distance.
            Possible values are DEFAULT and SPECIFIED. The default value is DEFAULT.
        influenceDistance
            A Float specifying the influence distance. The *influenceDistance* argument applies only
            when *influenceDistanceMethod*=SPECIFIED. The default value is 0.0.

        Returns
        -------
            A ShellSolidCoupling object.
        """
        self.constraints[name] = constraint = ShellSolidCoupling(name, shellEdge, solidFace, positionToleranceMethod,
                                                                 positionTolerance, influenceDistanceMethod,
                                                                 influenceDistance)
        return constraint

    def Tie(self, name: str, main: Region, secondary: Region, adjust: Boolean = ON,
            positionToleranceMethod: SymbolicConstant = COMPUTED, positionTolerance: float = 0,
            tieRotations: Boolean = ON, constraintRatioMethod: SymbolicConstant = DEFAULT,
            constraintRatio: float = 0, constraintEnforcement: SymbolicConstant = SOLVER_DEFAULT,
            thickness: Boolean = ON) -> Tie:
        """This method creates a Tie object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].Tie
        
        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        main
            A Region object specifying the name of the main surface.
        secondary
            A Region object specifying the name of the secondary surface.
        adjust
            A Boolean specifying whether initial positions of tied secondary nodes are adjusted to
            lie on the main surface. The default value is ON.
        positionToleranceMethod
            A SymbolicConstant specifying the method used to determine the position tolerance.
            Possible values are COMPUTED and SPECIFIED. The default value is COMPUTED.
        positionTolerance
            A Float specifying the position tolerance. The *positionTolerance* argument applies only
            when *positionToleranceMethod*=SPECIFIED. The default value is 0.0.
        tieRotations
            A Boolean specifying whether rotation degrees of freedom should be tied. The default
            value is ON.
        constraintRatioMethod
            A SymbolicConstant specifying the method used to determine the constraint ratio.
            Possible values are DEFAULT and SPECIFIED. The default value is DEFAULT.
        constraintRatio
            A Float specifying the fractional distance between the main reference surface and the
            secondary node at which the translational constraint should act. The *constraintRatio*
            argument applies only when *constraintRatioMethod*=SPECIFIED. The default value is 0.0.
        constraintEnforcement
            A SymbolicConstant specifying the discretization method. Possible values are
            SOLVER_DEFAULT, NODE_TO_SURFACE, and SURFACE_TO_SURFACE. The default value is
            SOLVER_DEFAULT.
        thickness
            A Boolean specifying whether shell element thickness is considered. The default value is
            ON.

        Returns
        -------
            A Tie object.
        """
        self.constraints[name] = constraint = Tie(name, main, secondary, adjust, positionToleranceMethod,
                                                  positionTolerance, tieRotations, constraintRatioMethod,
                                                  constraintRatio, constraintEnforcement, thickness)
        return constraint
