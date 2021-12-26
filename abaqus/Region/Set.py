import typing

from abaqusConstants import *
from .Region import Region
from ..BasicGeometry.Cell import Cell
from ..BasicGeometry.CellArray import CellArray
from ..BasicGeometry.Edge import Edge
from ..BasicGeometry.EdgeArray import EdgeArray
from ..BasicGeometry.Face import Face
from ..BasicGeometry.FaceArray import FaceArray
from ..BasicGeometry.ReferencePoint import ReferencePoint
from ..BasicGeometry.ReferencePointArray import ReferencePointArray
from ..BasicGeometry.Vertex import Vertex
from ..BasicGeometry.VertexArray import VertexArray
from ..Mesh.MeshElement import MeshElement
from ..Mesh.MeshElementArray import MeshElementArray
from ..Mesh.MeshNode import MeshNode
from ..Mesh.MeshNodeArray import MeshNodeArray


class Set:

    """If a set spans more than one part instance, the members *vertices*, *edges*, *faces*, 
    *cells*, *elements*, or *nodes* return a sequence of all the queried 
    vertices/edges/faces/celss/elements/nodes respectively for each part instance contained 
    in the set. For example: 
    assembly=mdb.models['Transmission'].rootAssembly 
        clutchElements=assembly.instances['Clutch'].elements  
        clutchSet=clutchElements[16:18]+clutchElements[78:80]  
        housingElements=assembly.instances['Housing'].elements  
        housingSet=housingElements[45:48]  
        transmissionSet=assembly.Set(name='TransmissionSet', \ 
                                     elements=(clutchSet, housingSet)) 
        len(transmissionSet.elements)=7  
        
    transmissionSet.elements[0]=mdb.models['Transmission'].rootAssembly.instances['Clutch-1'].elements[16] 
     
        
    transmissionSet.elements[6]=mdb.models['Transmission'].rootAssembly.instances['housing-'].elements[47] 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].allInternalSets[name]
        - mdb.models[name].parts[name].allSets[name]
        - mdb.models[name].parts[name].sets[name]
        - import assembly
        - mdb.models[name].rootAssembly.allInstances[name].sets[name]
        - mdb.models[name].rootAssembly.allInternalSets[name]
        - mdb.models[name].rootAssembly.allSets[name]
        - mdb.models[name].rootAssembly.instances[name].sets[name]
        - mdb.models[name].rootAssembly.modelInstances[i].sets[name]
        - mdb.models[name].rootAssembly.sets[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A MeshElementArray object. 
    elements: MeshElementArray = None

    # A MeshNodeArray object. 
    nodes: MeshNodeArray = None

    # A VertexArray object. 
    vertices: VertexArray = None

    # An EdgeArray object. 
    edges: EdgeArray = None

    # A FaceArray object. 
    faces: FaceArray = None

    # A CellArray object. 
    cells: CellArray = None

    # A VertexArray object. 
    xVertices: VertexArray = None

    # An EdgeArray object. 
    xEdges: EdgeArray = None

    # A FaceArray object. 
    xFaces: FaceArray = None

    # A ReferencePointArray object. 
    referencePoints: ReferencePointArray = None

    @typing.overload
    def __init__(self, name: str, nodes: tuple[MeshNode] = None, elements: tuple[MeshElement] = None, 
                 region: Region = None, vertices: tuple[Vertex] = None, edges: tuple[Edge] = None, 
                 faces: tuple[Face] = None, cells: tuple[Cell] = None, xVertices: tuple[Vertex] = None, 
                 xEdges: tuple[Edge] = None, xFaces: tuple[Face] = None, 
                 referencePoints: tuple[ReferencePoint] = (), skinFaces: tuple = (), 
                 skinEdges: tuple = (), stringerEdges: tuple = ()):
        """This method creates a set from a sequence of objects in a model database.

        Path
        ----
            - mdb.models[*name*].parts[*name*].Set
            - mdb.models[*name*].rootAssembly.Set

        Parameters
        ----------
        name
            A String specifying the repository key. 
        nodes
            A sequence of MeshNode objects. The default value is None. 
        elements
            A sequence of MeshElement objects. The default value is None. 
        region
            A Region object specifying other objects to be included in the set. The default value is 
            None. 
        vertices
            A sequence of Vertex objects. The default value is None. 
        edges
            A sequence of Edge objects. The default value is None. 
        faces
            A sequence of Face objects. The default value is None. 
        cells
            A sequence of Cell objects. The default value is None. 
        xVertices
            A sequence of Vertex objects that excludes specific vertices from the set. The default 
            value is None. 
        xEdges
            A sequence of Edge objects that excludes specific edges from the set. The default value 
            is None. 
        xFaces
            A sequence of Face objects that excludes specific faces from the set. The default value 
            is None. 
        referencePoints
            A sequence of ReferencePoint objects. The default value is an empty sequence. 
        skinFaces
            A tuple of tuples specifying a skin name and the sequence of faces associated with this 
            skin. Valid only for geometric regions on 3D and 2D parts. 
        skinEdges
            A tuple of tuples specifying a skin name and the sequence of edges associated with this 
            skin. Valid only for geometric regions on Axisymmetric parts. 
        stringerEdges
            A tuple of tuples specifying a stringer name and the sequence of edges associated with 
            this stringer. Valid only for geometric regions on 3D and 2D parts. 

        Returns
        -------
            A Set object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass

    @typing.overload
    def __init__(self, name: str, objectToCopy: 'Set'):
        """This method copies a set from an existing set.

        Path
        ----
            - mdb.models[*name*].parts[*name*].Set
            - mdb.models[*name*].rootAssembly.Set

        Parameters
        ----------
        name
            A String specifying the name of the set. 
        objectToCopy
            A Set object to be copied. 

        Returns
        -------
            A Set object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass

    def __init__(self, *args, **kwargs):
        pass

    def SetByBoolean(self, name: str, sets: tuple[Set], operation: SymbolicConstant = UNION):
        """This method creates a set by performing a boolean operation on two or more input sets.

        Path
        ----
            - mdb.models[*name*].parts[*name*].SetByBoolean
            - mdb.models[*name*].rootAssembly.SetByBoolean

        Parameters
        ----------
        name
            A String specifying the repository key. 
        sets
            A sequence of Set objects. 
        operation
            A SymbolicConstant specifying the boolean operation to perform. Possible values are 
            UNION, INTERSECTION, and DIFFERENCE. The default value is UNION. Note that if DIFFERENCE 
            is specified, the order of the given input sets is important; All sets specified after 
            the first one are subtracted from the first one. 

        Returns
        -------
            A Set object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass

    def SetFromColor(self, name: str, color: tuple):
        """This method creates a set containing faces of the part marked with a specified color
        attribute. Third-party applications can assign color attributes to faces, and the color
        attribute can be imported into Abaqus from an ACIS file. You can use this method to
        create sets only on parts; however, you can access the sets from instances of the parts
        in the assembly.

        Path
        ----
            - mdb.models[*name*].parts[*name*].SetFromColor

        Parameters
        ----------
        name
            A String specifying the repository key. 
        color
            A sequence of three Ints specifying the RGB color. Values can range from 0 to 255. The 
            first integer is for red, the second for green, and the third for blue. For example, a 
            face colored in yellow is identified by:`color=(255,255,0)` 

        Returns
        -------
            A Set object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass

    def SetFromElementLabels(self, name: str, elementLabels: tuple):
        """This method creates a set from a sequence of element labels in a model database.

        Path
        ----
            - mdb.models[*name*].parts[*name*].SetFromElementLabels
            - mdb.models[*name*].rootAssembly.SetFromElementLabels

        Parameters
        ----------
        name
            A String specifying the repository key. 
        elementLabels
            A sequence of element labels. An element label is a sequence of Int element identifiers. 
            For example, for a part:`elementLabels=(2,3,5,7)`For an 
            assembly:`elementLabels=(('Instance-1', (2,3,5,7)),       ('Instance-2', (1,2,3)))` 

        Returns
        -------
            A Set object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass

    def SetFromNodeLabels(self, name: str, nodeLabels: tuple, unsorted: Boolean = False):
        """This method creates a set from a sequence of node labels in a model database.

        Path
        ----
            - mdb.models[*name*].parts[*name*].SetFromNodeLabels
            - mdb.models[*name*].rootAssembly.SetFromNodeLabels

        Parameters
        ----------
        name
            A String specifying the repository key. 
        nodeLabels
            A sequence of node labels. A node label is a sequence of Int node identifiers. For 
            example, for a part:`nodeLabels=(2,3,5,7)`For an assembly:`nodeLabels=(('Instance-1', 
            (2,3,5,7)), ('Instance-2', (1,2,3)))` 
        unsorted
            A Boolean specifying whether the created set is unsorted. The default value is False. 

        Returns
        -------
            A Set object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass

    def MapSetsFromOdb(self, odbPath: str, odbSets: str, partSets: str = '', method: str = OVERWRITE):
        """This method creates sets based on mapping sets from element centroid locations in an
        Odb.

        Path
        ----
            - mdb.models[*name*].parts[*name*].MapSetsFromOdb

        Parameters
        ----------
        odbPath
            A String specifying the path to the ODB containing the source sets. 
        odbSets
            A list of names of sets on the ODB to map. 
        partSets
            A list of names of sets to construct or use corresponding to the ODB sets. 
        method
            An enum to specify OVERWRITE, APPEND, INTERSECT, or REMOVE. The default is OVERWRITE. 

        Returns
        -------
            A Set object or a tuple of Set objects. 

        Exceptions
        ----------
            None. 
        """
        pass
