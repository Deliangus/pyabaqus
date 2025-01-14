from abaqusConstants import *
from .AnalyticSurface import AnalyticSurface
from .OdbMeshNode import OdbMeshNode
from .OdbSet import OdbSet


class OdbRigidBody:
    """The Rigid body object is used to bind a set of elements and/or a set of nodes and/or an
    analytical surface with a reference node. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import odbAccess
        session.odbs[name].parts[name].rigidBodies[i]
        session.odbs[name].rootAssembly.instances[name].rigidBodies[i]
        session.odbs[name].rootAssembly.rigidBodies[i]
        session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.rigidBodies[i]

    """

    def __init__(self, referenceNode: OdbSet, position: SymbolicConstant = INPUT, isothermal: Boolean = ON,
                 elements: OdbSet = OdbSet('set', tuple[OdbMeshNode]()),
                 tieNodes: OdbSet = OdbSet('set', tuple[OdbMeshNode]()),
                 pinNodes: OdbSet = OdbSet('set', tuple[OdbMeshNode]()),
                 analyticSurface: AnalyticSurface = AnalyticSurface()):
        """This method creates a OdbRigidBody object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.odbs[*name*].rootAssembly.instances[*name*].RigidBody
            session.odbs[*name*].rootAssembly.RigidBody
        
        Parameters
        ----------
        referenceNode
            An OdbSet object specifying the reference node set associated with the rigid body. 
        position
            A SymbolicConstant specifying the specific location of the OdbRigidBody reference node 
            relative to the rest of the rigid body. Possible values are INPUT and CENTER_OF_MASS. 
            The default value is INPUT. 
        isothermal
            A Boolean specifying specify whether the OdbRigidBody can have temperature gradients or 
            be isothermal. This is used only for fully coupled thermal-stress analysis The default 
            value is ON. 
        elements
            An OdbSet object specifying the element set whose motion is governed by the motion of 
            rigid body reference node. 
        tieNodes
            An OdbSet object specifying the node set which have both translational and rotational 
            degrees of freedom associated with the rigid body. 
        pinNodes
            An OdbSet object specifying the node set which have only translational degrees of 
            freedom associated with the rigid body. 
        analyticSurface
            An AnalyticSurface object specifying the analytic surface whose motion is governed by 
            the motion of rigid body reference node. 

        Returns
        -------
            An OdbRigidBody object.
        """
        pass
