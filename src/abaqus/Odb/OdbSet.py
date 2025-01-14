from abaqusConstants import *
from .OdbMeshElement import OdbMeshElement
from .OdbMeshElementArray import OdbMeshElementArray
from .OdbMeshNode import OdbMeshNode
from .OdbMeshNodeArray import OdbMeshNodeArray


class OdbSet:
    """The set objects are used to identify regions of a model.

    Attributes
    ----------
    name: str
        A String specifying the name of the set and the repository key.
    instanceNames: tuple
        A tuple of Strings specifying the namespaces for the nodes, elements, and faces; None if
        the set is on a Part or an :py:class:`~abaqus.Odb.OdbInstance.OdbInstance` object.
    nodes: OdbMeshNodeArray
        An :py:class:`~abaqus.Odb.OdbMeshNodeArray.OdbMeshNodeArray` object specifying the nodes of an OdbSet. If a set spans more than
        one part instance, this member is a sequence of sequences for each part instance.
    elements: OdbMeshElementArray
        An :py:class:`~abaqus.Odb.OdbMeshElementArray.OdbMeshElementArray` object specifying the elements of an OdbSet. If a set spans more
        than one part instance, this member is a sequence of sequences for each part instance.
    faces: SymbolicConstant
        A tuple of SymbolicConstants specifying the element face. If a set spans more than one
        part instance, this member is a sequence of sequences for each part instance.
    instances: str
        A repository of an :py:class:`~abaqus.Odb.OdbInstance.OdbInstance` object.
    isInternal: Boolean
        A Boolean specifying whether the set is internal.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import odbAccess
        session.odbs[name].parts[name].elementSets[name]
        session.odbs[name].parts[name].nodeSets[name]
        session.odbs[name].parts[name].surfaces[name]
        session.odbs[name].rootAssembly.elementSets[name]
        session.odbs[name].rootAssembly.instances[name].elementSets[name]
        session.odbs[name].rootAssembly.instances[name].nodeSets[name]
        session.odbs[name].rootAssembly.instances[name].surfaces[name]
        session.odbs[name].rootAssembly.nodeSets[name]
        session.odbs[name].rootAssembly.surfaces[name]
        session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.elementSets[name]
        session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.nodeSets[name]
        session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.surfaces[name]

    """

    # A String specifying the name of the set and the repository key. 
    name: str = ''

    # A tuple of Strings specifying the namespaces for the nodes, elements, and faces; None if 
    # the set is on a Part or an OdbInstance object. 
    instanceNames: tuple = ()

    # An OdbMeshNodeArray object specifying the nodes of an OdbSet. If a set spans more than 
    # one part instance, this member is a sequence of sequences for each part instance. 
    nodes: OdbMeshNodeArray = OdbMeshNodeArray()

    # An OdbMeshElementArray object specifying the elements of an OdbSet. If a set spans more 
    # than one part instance, this member is a sequence of sequences for each part instance. 
    elements: OdbMeshElementArray = OdbMeshElementArray()

    # A tuple of SymbolicConstants specifying the element face. If a set spans more than one 
    # part instance, this member is a sequence of sequences for each part instance. 
    faces: SymbolicConstant = None

    # A repository of an OdbInstance object. 
    instances: str = ''

    # A Boolean specifying whether the set is internal. 
    isInternal: Boolean = OFF

    def __init__(self, name: str, nodes: tuple[OdbMeshNode]):
        """This method creates a node set from an array of OdbMeshNode objects (for part
        instance-level sets) or from a sequence of arrays of OdbMeshNode objects (for
        assembly-level sets).

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.odbs[*name*].parts[*name*].NodeSet
            session.odbs[*name*].rootAssembly.instances[*name*].NodeSet
            session.odbs[*name*].rootAssembly.NodeSet
        
        Parameters
        ----------
        name
            A String specifying the name of the set and the repository key. 
        nodes
            A sequence of OdbMeshNode objects. For example, for a part:`nodes=part1.nodes[1:5]`For 
            an assembly:`nodes=(instance1.nodes[6:7], instance2.nodes[1:5])` 

        Returns
        -------
            An OdbSet object.
        """
        pass

    def NodeSetFromNodeLabels(self, name: str, nodeLabels: tuple):
        """This method creates a node set from a sequence of node labels.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.odbs[*name*].parts[*name*].NodeSet
            session.odbs[*name*].rootAssembly.instances[*name*].NodeSet
            session.odbs[*name*].rootAssembly.NodeSet
        
        Parameters
        ----------
        name
            A String specifying the name of the set and the repository key. 
        nodeLabels
            A sequence of node labels. A node label is a sequence of Int node identifiers. For 
            example, for a part:`nodeLabels=(2,3,5,7)`For an assembly:`nodeLabels=(('Instance-1', 
            (2,3,5,7)), ('Instance-2', (1,2,3)))` 

        Returns
        -------
            An OdbSet object.
        """
        pass

    def ElementSet(self, name: str, elements: tuple[OdbMeshElement]):
        """This method creates an element set from an array of OdbMeshElement objects (for part
        instance-level sets) or from a sequence of arrays of OdbMeshElement objects (for
        assembly-level sets).

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.odbs[*name*].parts[*name*].NodeSet
            session.odbs[*name*].rootAssembly.instances[*name*].NodeSet
            session.odbs[*name*].rootAssembly.NodeSet
        
        Parameters
        ----------
        name
            A String specifying the name of the set and the repository key. 
        elements
            A sequence of OdbMeshElement objects. For example, for a 
            part:`elements=instance1.elements[1:5]`For an 
            assembly:`elements=(instance1.elements[1:5], instance2.elements[1:5])` 

        Returns
        -------
            An OdbSet object.
        """
        pass

    def ElementSetFromElementLabels(self, name: str, elementLabels: tuple):
        """This method creates an element set from a sequence of element labels.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.odbs[*name*].parts[*name*].NodeSet
            session.odbs[*name*].rootAssembly.instances[*name*].NodeSet
            session.odbs[*name*].rootAssembly.NodeSet
        
        Parameters
        ----------
        name
            A String specifying the name of the set and the repository key. 
        elementLabels
            A sequence of element labels. An element label is a sequence of Int element identifiers. 
            For example, for a part:`elementLabels=(2,3,5,7)`For an 
            assembly:`elementLabels=(('Instance-1', (2,3,5,7)), ('Instance-2', (1,2,3)))` 

        Returns
        -------
            An OdbSet object.
        """
        pass

    def MeshSurface(self, name: str, meshSurfaces: tuple):
        """This method creates a surface from the element and side identifiers for the assembly.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.odbs[*name*].parts[*name*].NodeSet
            session.odbs[*name*].rootAssembly.instances[*name*].NodeSet
            session.odbs[*name*].rootAssembly.NodeSet
        
        Parameters
        ----------
        name
            A String specifying the name of the set and the repository key. 
        meshSurfaces
            A sequence of sequences. Each sequence consists of an element sequence and a side 
            identifier. The possible side identifiers depend on the type of element, as described in 
            the following table: 
            | Sequence of elements             | Side identifiers                         | 
            | -------------------------------- | ---------------------------------------- | 
            | Solid elements                   | FACE1, FACE2, FACE3, FACE4, FACE5, FACE6 | 
            | Three-dimensional shell elements | SIDE1, SIDE2                             | 
            | Two-dimensional elements         | FACE1, FACE2, FACE3, FACE4               | 
            | Wire elements                    | END, END2                                | 
            For example: 
            ``` 
            side1Elements=instance1.elements[217:218] 
            side2Elements=instance2.elements[100:105] 
            assembly.MeshSurface(name='Surf-1'
            meshSurfaces=((side1Elems,SIDE1)
            (side2Elems,SIDE2))) 
            ``` 

        Returns
        -------
            An OdbSet object.
        """
        pass

    def MeshSurfaceFromElsets(self, name: str, elementSetSeq: tuple):
        """This method creates a mesh surface from a sequence of element sets.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.odbs[*name*].parts[*name*].NodeSet
            session.odbs[*name*].rootAssembly.instances[*name*].NodeSet
            session.odbs[*name*].rootAssembly.NodeSet
        
        Parameters
        ----------
        name
            A String specifying the name of the set and the repository key. 
        elementSetSeq
            A sequence of element sets. For 
            example,`elementSetSeq=((elset1,SIDE1),(elset2,SIDE2))`where 
            `elset1=session.odbs[name].rootAssembly.elementSets['Clutch'] `and `SIDE1` and `SIDE2` 
            indicate the side of the element set. 

        Returns
        -------
            An OdbSet object.
        """
        pass

    def MeshSurfaceFromLabels(self, name: str, surfaceLabels: tuple):
        """This method creates a mesh surface from a sequence of surface labels.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.odbs[*name*].parts[*name*].NodeSet
            session.odbs[*name*].rootAssembly.instances[*name*].NodeSet
            session.odbs[*name*].rootAssembly.NodeSet
        
        Parameters
        ----------
        name
            A String specifying the name of the set and the repository key. 
        surfaceLabels
            A sequence of surface labels. For example,`surfaceLabels=(('Instance-1', ((10, FACE1), 
            (11, FACE2))),  ('Instance-2', ((10, FACE3), (12, FACE4))))`where `10` is an element 
            number and `FACE1` indicates the side of the element. 

        Returns
        -------
            An OdbSet object.
        """
        pass
