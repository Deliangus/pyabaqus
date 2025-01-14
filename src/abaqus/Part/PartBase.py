import typing

from abaqusConstants import *
from .AcisFile import AcisFile
from .Feature import Feature
# from ..Assembly.PartInstance import PartInstance
from ..BasicGeometry.Cell import Cell
from ..BasicGeometry.CellArray import CellArray
from ..BasicGeometry.Edge import Edge
from ..BasicGeometry.EdgeArray import EdgeArray
from ..BasicGeometry.Face import Face
from ..BasicGeometry.FaceArray import FaceArray
from ..BasicGeometry.IgnoredEdgeArray import IgnoredEdgeArray
from ..BasicGeometry.IgnoredVertexArray import IgnoredVertexArray
from ..BasicGeometry.ReferencePoints import ReferencePoints
from ..BasicGeometry.VertexArray import VertexArray
from ..Datum.Datum import Datum
from ..EngineeringFeature.EngineeringFeature import EngineeringFeature
from ..Mesh.MeshEdge import MeshEdge
from ..Mesh.MeshEdgeArray import MeshEdgeArray
from ..Mesh.MeshElement import MeshElement
from ..Mesh.MeshElementArray import MeshElementArray
from ..Mesh.MeshFace import MeshFace
from ..Mesh.MeshFaceArray import MeshFaceArray
from ..Mesh.MeshNode import MeshNode
from ..Mesh.MeshNodeArray import MeshNodeArray
from ..Property.CompositeLayup import CompositeLayup
from ..Property.MaterialOrientationArray import MaterialOrientationArray
from ..Property.SectionAssignmentArray import SectionAssignmentArray
from ..Region.Set import Set
from ..Region.Skin import Skin
from ..Region.Stringer import Stringer
from ..Region.Surface import Surface
from ..Sketcher.ConstrainedSketch import ConstrainedSketch


# prevent circular imports
class PartInstance:
    pass


class PartBase(Feature):
    """The Part object defines the physical attributes of a structure. Parts are instanced into
    the assembly and positioned before an analysis. 

    Attributes
    ----------
    geometryValidity: Boolean
        A Boolean specifying the validity of the geometry of the part. The value is computed,
        but it can be set to ON to perform feature and mesh operations on an invalid part. There
        is no guarantee that such operations will work if the part was originally invalid.
    isOutOfDate: int
        An Int specifying that feature parameters have been modified but that the part has not
        been regenerated. Possible values are 0 and 1.
    timeStamp: float
        A Float specifying when the part was last modified.
    vertices: VertexArray
        A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object specifying all the vertices in the part.
    ignoredVertices: IgnoredVertexArray
        An :py:class:`~abaqus.BasicGeometry.IgnoredVertexArray.IgnoredVertexArray` object specifying all the ignored
        vertices in the part.
    edges: EdgeArray
        An :py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` object specifying all the edges in the part.
    ignoredEdges: IgnoredEdgeArray
        An :py:class:`~abaqus.BasicGeometry.IgnoredEdgeArray.IgnoredEdgeArray` object specifying all the ignored edges
        in the part.
    faces: FaceArray
        A :py:class:`~abaqus.BasicGeometry.FaceArray.FaceArray` object specifying all the faces in the part.
    cells: CellArray
        A :py:class:`~abaqus.BasicGeometry.CellArray.CellArray` object specifying all the cells in the part.
    features: dict[str, Feature]
        A repository of :py:class:`~abaqus.Assembly.Feature.Feature` objects specifying all the features in the part.
    featuresById: dict[str, Feature]
        A repository of :py:class:`~abaqus.Feature.Feature.Feature` objects specifying all Feature objects in the part.
        The Feature
        objects in the featuresById repository are the same as the Feature objects in the 
        features' repository. However, the key to the objects in the featuresById repository is
        an integer specifying the *ID*, whereas the key to the objects in the features'
        repository is a string specifying the **name**.
        datums: list[Datum]
        A repository of :py:class:`~abaqus.Datum.Datum.Datum` objects specifying all the datums in the part.
    elements: MeshElementArray
        A :py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` object specifying all the elements in the part.
    elemFaces: dict[str, MeshFace]
        A repository of :py:class:`~abaqus.Mesh.MeshFace.MeshFace` objects specifying all the element faces in the part.
        For a
        given element and a given face index within that element, the corresponding
        :py:class:`~abaqus.Mesh.MeshFace.MeshFace`
        object can be retrieved from the repository by using the key calculated as (i*8 + j),
        where i and j are zero-based element and face indices, respectively.
    elementFaces: MeshFaceArray
        A :py:class:`~abaqus.Mesh.MeshFaceArray.MeshFaceArray` object specifying all the unique element faces in the
        part.
    nodes: MeshNodeArray
        A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object specifying all the nodes in the part.
    retainedNodes: MeshNodeArray
        A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object specifying all the retained nodes in the
        substructure part.
    sets: dict[str, Set]
        A repository of :py:class:`~abaqus.Region.Set.Set` objects specifying for more information, see
        :py:class:`~abaqus.Region.Set.Set`.
    allSets: dict[str, Set]
        A repository of :py:class:`~abaqus.Region.Set.Set` objects specifying the contents of the **all
        :py:class:`~abaqus.Region.Set.Set`s** repository is the
        same as the contents of the **sets** repository.
    allInternalSets: dict[str, Set]
        A repository of :py:class:`~abaqus.Region.Set.Set` objects specifying picked regions.
    surfaces: dict[str, Surface]
        A repository of :py:class:`~abaqus.Region.Surface.Surface` objects specifying for more information, see
        :py:class:`~abaqus.Region.Surface.Surface`.
    allSurfaces: dict[str, Surface]
        A repository of :py:class:`~abaqus.Region.Surface.Surface` objects specifying the contents of the
        **allSurfaces** repository
        is the same as the contents of the **surfaces** repository.
    allInternalSurfaces: dict[str, Surface]
        A repository of :py:class:`~abaqus.Region.Surface.Surface` objects specifying picked regions.
    skins: dict[str, Skin]
        A repository of :py:class:`~abaqus.Region.Skin.Skin` objects specifying the skins created on the part.
    stringers: dict[str, Stringer]
        A repository of :py:class:`~abaqus.Region.Stringer.Stringer` objects specifying the stringers created on the
        part.
    referencePoints: ReferencePoints
        A repository of :py:class:`~abaqus.BasicGeometry.ReferencePoint.ReferencePoint` objects.
    engineeringFeatures: EngineeringFeature
        An :py:class:`~abaqus.EngineeringFeature.EngineeringFeature.EngineeringFeature` object.
    sectionAssignments: SectionAssignmentArray
        A :py:class:`~abaqus.Property.SectionAssignmentArray.SectionAssignmentArray` object.
    materialOrientations: MaterialOrientationArray
        A :py:class:`~abaqus.Property.MaterialOrientationArray.MaterialOrientationArray` object.
    compositeLayups: dict[str, CompositeLayup]
        A repository of :py:class:`~abaqus.Property.CompositeLayup.CompositeLayup` objects.
    elemEdges: dict[str, MeshEdge]
        A repository of :py:class:`~abaqus.Mesh.:py:class:`~abaqus.Mesh.MeshEdge.MeshEdge`.
        :py:class:`~abaqus.Mesh.MeshEdge.MeshEdge`` objects specifying all the element edges in the part. For a
        given element and a given edge index on a given face within that element, the
        corresponding :py:class:`~abaqus.Mesh.:py:class:`~abaqus.Mesh.MeshEdge.MeshEdge`.
        :py:class:`~abaqus.Mesh.MeshEdge.MeshEdge`` object can be retrieved from the repository by using the key
        calculated as (i*32 + j*4 + k), where i, j, and k are zero-based element, face, and edge
        indices, respectively.
    elementEdges: MeshEdgeArray
        A :py:class:`~abaqus.Mesh.MeshEdgeArray.MeshEdgeArray` object specifying all the unique element edges in the
        part.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import part
        mdb.models[name].parts[name]

    """

    # A Boolean specifying the validity of the geometry of the part. The value is computed, 
    # but it can be set to ON to perform feature and mesh operations on an invalid part. There 
    # is no guarantee that such operations will work if the part was originally invalid. 
    geometryValidity: Boolean = OFF

    # An Int specifying that feature parameters have been modified but that the part has not 
    # been regenerated. Possible values are 0 and 1. 
    isOutOfDate: int = None

    # A Float specifying when the part was last modified. 
    timeStamp: float = None

    # A VertexArray object specifying all the vertices in the part. 
    vertices: VertexArray = VertexArray([])

    # An IgnoredVertexArray object specifying all the ignored vertices in the part. 
    ignoredVertices: IgnoredVertexArray = IgnoredVertexArray()

    # An EdgeArray object specifying all the edges in the part. 
    edges: EdgeArray = EdgeArray([])

    # An IgnoredEdgeArray object specifying all the ignored edges in the part. 
    ignoredEdges: IgnoredEdgeArray = IgnoredEdgeArray()

    # A FaceArray object specifying all the faces in the part. 
    faces: FaceArray = FaceArray([])

    # A CellArray object specifying all the cells in the part. 
    cells: CellArray = CellArray([])

    # A repository of Feature objects specifying all the features in the part. 
    features: dict[str, Feature] = dict[str, Feature]()

    # A repository of Feature objects specifying all Feature objects in the part. The Feature 
    # objects in the featuresById repository are the same as the Feature objects in the 
    # features' repository. However, the key to the objects in the featuresById repository is
    # an integer specifying the *ID*, whereas the key to the objects in the features 
    # repository is a string specifying the *name*. 
    featuresById: dict[str, Feature] = dict[str, Feature]()

    # A repository of Datum objects specifying all the datums in the part. 
    datums: list[Datum] = list[Datum]()

    # A MeshElementArray object specifying all the elements in the part. 
    elements: MeshElementArray = MeshElementArray([])

    # A repository of MeshFace objects specifying all the element faces in the part. For a 
    # given element and a given face index within that element, the corresponding MeshFace 
    # object can be retrieved from the repository by using the key calculated as (i*8 + j), 
    # where i and j are zero-based element and face indices, respectively. 
    elemFaces: dict[str, MeshFace] = dict[str, MeshFace]()

    # A MeshFaceArray object specifying all the unique element faces in the part. 
    elementFaces: MeshFaceArray = MeshFaceArray([])

    # A MeshNodeArray object specifying all the nodes in the part. 
    nodes: MeshNodeArray = MeshNodeArray([])

    # A MeshNodeArray object specifying all the retained nodes in the substructure part. 
    retainedNodes: MeshNodeArray = MeshNodeArray([])

    # A repository of Set objects specifying for more information, see Set. 
    sets: dict[str, Set] = dict[str, Set]()

    # A repository of Set objects specifying the contents of the *allSets* repository is the 
    # same as the contents of the *sets* repository. 
    allSets: dict[str, Set] = dict[str, Set]()

    # A repository of Set objects specifying picked regions. 
    allInternalSets: dict[str, Set] = dict[str, Set]()

    # A repository of Surface objects specifying for more information, see Surface. 
    surfaces: dict[str, Surface] = dict[str, Surface]()

    # A repository of Surface objects specifying the contents of the *allSurfaces* repository 
    # is the same as the contents of the *surfaces* repository. 
    allSurfaces: dict[str, Surface] = dict[str, Surface]()

    # A repository of Surface objects specifying picked regions. 
    allInternalSurfaces: dict[str, Surface] = dict[str, Surface]()

    # A repository of Skin objects specifying the skins created on the part. 
    skins: dict[str, Skin] = dict[str, Skin]()

    # A repository of Stringer objects specifying the stringers created on the part. 
    stringers: dict[str, Stringer] = dict[str, Stringer]()

    # A repository of ReferencePoint objects. 
    referencePoints: ReferencePoints = ReferencePoints()

    # An EngineeringFeature object. 
    engineeringFeatures: EngineeringFeature = EngineeringFeature()

    # A SectionAssignmentArray object. 
    sectionAssignments: SectionAssignmentArray = SectionAssignmentArray()

    # A MaterialOrientationArray object. 
    materialOrientations: MaterialOrientationArray = MaterialOrientationArray()

    # A repository of CompositeLayup objects. 
    compositeLayups: dict[str, CompositeLayup] = dict[str, CompositeLayup]()

    # A repository of MeshEdge objects specifying all the element edges in the part. For a 
    # given element and a given edge index on a given face within that element, the 
    # corresponding MeshEdge object can be retrieved from the repository by using the key 
    # calculated as (i*32 + j*4 + k), where i, j, and k are zero-based element, face, and edge 
    # indices, respectively. 
    elemEdges: dict[str, MeshEdge] = dict[str, MeshEdge]()

    # A MeshEdgeArray object specifying all the unique element edges in the part. 
    elementEdges: MeshEdgeArray = MeshEdgeArray([])

    @typing.overload
    def __init__(self, name: str, dimensionality: SymbolicConstant, type: SymbolicConstant,
                 twist: Boolean = OFF):
        """This method creates a Part object and places it in the parts repository.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Part
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        dimensionality
            A SymbolicConstant specifying the dimensionality of the part. Possible values are 
            THREE_D, TWO_D_PLANAR, and AXISYMMETRIC. 
        type
            A SymbolicConstant specifying the type of the part. Possible values are DEFORMABLE_BODY, 
            EULERIAN, DISCRETE_RIGID_SURFACE, and ANALYTIC_RIGID_SURFACE. 
        twist
            A Boolean specifying whether to include a twist DEGREE OF FREEDOM in the part (only 
            available when *dimensionality*=AXISYMMETRIC and *type*=DEFORMABLE_BODY). The default 
            value is OFF. 

        Returns
        -------
        part: Part
            A Part object
        """
        pass

    @typing.overload
    def __init__(self, name: str, objectToCopy: str, scale: float = 1, mirrorPlane: SymbolicConstant = NONE,
                 compressFeatureList: Boolean = OFF, separate: Boolean = OFF):
        """This method copies a Part object and places the copy in the parts repository.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Part
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        objectToCopy
            A Part Object to be copied. 
        scale
            A Float specifying the scaling factor to apply to the imported geometric entities during 
            copy. If a scale is specified, *compressFeatureList* will be set to ON, regardless of 
            whether it is specified in the command. The default value is 1. 
        mirrorPlane
            A SymbolicConstant specifying how the part is to be mirrored during copy. Possible 
            values are XYPLANE, XZPLANE, YZPLANE. If a mirror plane is specified, 
            *compressFeatureList* will be set to ON, regardless of whether it is specified in the 
            command. The default value is NONE. 
        compressFeatureList
            A Boolean specifying whether to compress the feature list when copying a Part object. 
            The default value is OFF. If *mirrorPlane* or *scale* is specified, this argument is 
            ignored.When you compress the feature, list the resulting part will have a single 
            feature. Any datums or sets in the original part will be lost. 
        separate
            A Boolean specifying whether to separate disconnected regions into parts. The default 
            value is OFF. 

        Returns
        -------
        part: Part
            A Part object
        """
        pass

    def __init__(self, *args, **kwargs):
        pass

    def PartFromBooleanCut(self, name: str, instanceToBeCut: str, cuttingInstances: tuple[PartInstance]):
        """This method creates a Part in the parts repository after subtracting or cutting the
        geometries of a group of part instances from that of a base part instance.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Part
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        instanceToBeCut
            A PartInstance specifying the base instance from which to cut other instances. 
        cuttingInstances
            A sequence of PartInstance objects specifying the instances with which to cut the base 
            instance. 

        Returns
        -------
        part: Part
            A Part object
        """
        pass

    def PartFromBooleanMerge(self, name: str, instances: tuple[PartInstance], keepIntersections: Boolean = False,
                             mergeNodes: SymbolicConstant = BOUNDARY_ONLY, nodeMergingTolerance: float = None,
                             removeDuplicateElements: Boolean = ON, domain: SymbolicConstant = GEOMETRY):
        """This method creates a Part in the parts repository after merging two or more part
        instances. The part instances can be either Abaqus native parts or orphan mesh parts,
        but they cannot be a combination of both.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Part
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        instances
            A sequence of PartInstance objects specifying the part instances to merge. 
        keepIntersections
            A Boolean specifying whether the boundary intersections of Abaqus native part instances 
            should be retained after the merge operation. The default value is False. 
        mergeNodes
            A SymbolicConstant specifying whether the nodes of orphan mesh part instances should be 
            retained after the merge operation. Possible values are BOUNDARY_ONLY, ALL, or NONE. The 
            default value is BOUNDARY_ONLY. 
        nodeMergingTolerance
            A Float specifying the maximum distance between nodes of orphan mesh part instances that 
            will be merged and replaced with a single new node. The location of the new node is the 
            average position of the deleted nodes. The default value is 10–6. 
        removeDuplicateElements
            A Boolean specifying whether elements with the same connectivity after the merge will 
            merged into a single element. The default value is ON. 
        domain
            A SymbolicConstant specifying whether the part instances being merged are geometric 
            instances or mesh instances. Possible values are GEOMETRY, MESH or BOTH. The default 
            value is GEOMETRY. 

        Returns
        -------
        part: Part
            A Part object
        """
        pass

    def PartFromExtrude2DMesh(self, name: str, part: 'PartBase', depth: float, elementSize: float):
        """This method creates a Part object by extruding an existing two-dimensional orphan mesh
        Part object in the positive *Z*-direction and places it in the parts repository.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Part
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        part
            A Part object specifying an existing two-dimensional orphan mesh Part object. 
        depth
            A Float specifying the total extrusion distance. 
        elementSize
            A Float specifying an approximate element length in the extruded direction. 

        Returns
        -------
        part: Part
            A Part object
            - If the specified part is not an orphan mesh part: 
              Cannot extrude a geometric part. 
            - If the specified part is not two-dimensional: 
              Cannot extrude a 3D part. 
            - If the specified part is a rigid body: 
              Cannot change dimension of a rigid body. 
        """
        pass

    def PartFromGeometryFile(self, name: str, geometryFile: AcisFile, dimensionality: SymbolicConstant,
                             type: SymbolicConstant, bodyNum: int = 1, combine: Boolean = False,
                             booleanSolids: Boolean = FALSE, retainBoundary: Boolean = FALSE,
                             usePartNameFromFile: Boolean = OFF, stitchTolerance: float = 1, twist: Boolean = OFF,
                             scale: float = 1, convertToAnalytical: int = 0, convertToPrecise: int = 0):
        """This method creates a Part object and places it in the parts repository.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Part
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        geometryFile
            An AcisFile object specifying a file containing geometry. 
        dimensionality
            A SymbolicConstant specifying the dimensionality of the part. Possible values are 
            THREE_D, TWO_D_PLANAR, and AXISYMMETRIC. 
        type
            A SymbolicConstant specifying the type of the part. Possible values are DEFORMABLE_BODY, 
            EULERIAN, DISCRETE_RIGID_SURFACE, and ANALYTIC_RIGID_SURFACE. 
        bodyNum
            An Int specifying the desired body to be selected from an ACIS object containing a list 
            of *N* ACIS bodies. Possible values are 1 ≤≤ *bodyNum* ≤≤ *N*. The default value is 1. 
        combine
            A Boolean specifying weather to create a single part by combining all the bodies in the 
            ACIS object. This argument is ignored if *bodyNum* is specified. The default value is 
            False. 
        booleanSolids
            A Boolean specifying whether the solids should be boolean while combining all the 
            bodies.The default value is FALSE. 
        retainBoundary
            A Boolean specifying whether the intersecting boundaries should be retained while 
            boolean the solids.The default value is FALSE. 
        usePartNameFromFile
            A Boolean specifying whether the part names specified in a STEP file should be used as 
            the names in the Abaqus model database. If this option is TRUE, the part names in the 
            STEP file will be used; if FALSE, each imported part will be named using the text of the 
            *name* argument followed by a number. This functionality is available only for import 
            from STEP files; for import from all other types of files this option should be FALSE. 
        stitchTolerance
            A Float indicating the maximum gap to be stitched. The value should be smaller than the 
            minimum feature size and bigger than the maximum gap expected to be stitched in the 
            model. Otherwise this command may remove small (sliver) edges that are smaller than the 
            tolerance. The default value is 1.0 
        twist
            A Boolean specifying whether to include a twist DEGREE OF FREEDOM in the part (only 
            available when *dimensionality*=AXISYMMETRIC and *type*=DEFORMABLE_BODY). The default 
            value is OFF. 
        scale
            A Float specifying the scaling factor to apply to the imported geometric entities. The 
            default value is 1.0. 
        convertToAnalytical
            An Int specifying whether to convert to analytical entities. Possible values are 0 or 1. 
            The default value is 0. If *convertToAnalytical*=1, all the numerical entities, such as 
            splines, are converted to analytical entities, such as arcs and lines, during the repair 
            phase of the command. 
        convertToPrecise
            An Int specifying whether to convert to precise geometry. Possible value are 0 or 1. The 
            default value is 0. If *convertToPrecise*=1, the application will attempt to re-evaluate 
            the tolerant entities to be more precise. 

        Returns
        -------
        part: Part
            A Part object
            - If the ACIS file is corrupt: 
              PartError: the file is corrupt 
            - If the dimensionality does not correspond to what is found in the ACIS file: 
              PartError: dimensionality does not match the contents of the file 
            - If the type does not correspond to what is found in the ACIS file: 
              PartError: type does not match the contents of the file 
        """
        pass

    def PartFromInstanceMesh(self, name: str, partInstances: tuple[PartInstance] = (), copyPartSets: Boolean = False,
                             copyAssemblySets: Boolean = False):
        """This method creates a Part object containing the mesh found in the supplied PartInstance
        objects and places the new Part object in the parts repository.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Part
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        partInstances
            A sequence of PartInstance objects to be used in the creation of the new mesh part. If 
            the *partInstances* argument is omitted, the new Part object contains the mesh of all 
            the part instances in the assembly. 
        copyPartSets
            A Boolean specifying whether to copy sets, surfaces, and attributes from the base part 
            or parts of the specified part instances to the new part. The default is False. 
        copyAssemblySets
            A Boolean specifying whether to copy assembly-level sets that reference entities of the 
            specified part instances to the new part. The default is False. 

        Returns
        -------
        part: Part
            A Part object
            - If the analysis type (deformable or rigid) is not consistent among the supplied part 
            instances: 
              The selected part instances do not have a consistent analysis type. 
            - If the assembly does not contain a mesh: 
              The current assembly does not contain a mesh for a mesh part. 
            - If the specified part instances do not contain a mesh: 
              The selected part instances do not have a mesh for a mesh part. 
        """
        pass

    def PartFromMesh(self, name: str, copySets: Boolean = False):
        """This method creates a Part object containing the mesh found in the part and places the
        new Part object in the parts repository.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Part
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        copySets
            A Boolean specifying whether to copy sets, surfaces, and attributes to the new part. The 
            default is False. 

        Returns
        -------
        part: Part
            A Part object
            - If the part does not contain a mesh: 
              The current part does not contain a mesh for a mesh part. 
        """
        pass

    def PartFromMeshMirror(self, name: str, part: 'PartBase', point1: tuple, point2: tuple):
        """This method creates a Part object by mirroring an existing orphan mesh Part object about
        a specified plane and places it in the parts repository. The result is a union of the
        original and the mirrored copy. Contrast the PartFromMeshMirror method with the
        *mirrorPlane* argument of the Part copy constructor. The *mirrorPlane* argument creates
        only the second half of the part but does not unite the two halves.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Part
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        part
            A Part object specifying an existing orphan mesh part. 
        point1
            A sequence of three Floats specifying a point on the mirror plane. This point is the 
            local origin in the local system of the plane. 
        point2
            A sequence of three Floats specifying a point in the direction of the normal to the 
            mirror plane. This point must not be coincident with *point1*. 

        Returns
        -------
        part: Part
            A Part object
            - If the specified part is not an orphan mesh part: 
              Cannot mirror a geometric part. 
            - If the specified part is a rigid body: 
              Cannot mirror a rigid body. 
            - If *point1* and *point2* are coincident: 
              Mirror plane director has zero length. 
            - If the specified part is two-dimensional and the plane is not parallel to the 
            *Z*-axis: 
              Mirror plane must be parallel to Z axis for 2D parts 
        """
        pass

    def PartFromNodesAndElements(self, name: str, dimensionality: SymbolicConstant, type: SymbolicConstant,
                                 nodes: tuple,
                                 elements: tuple, twist: Boolean = OFF):
        """This method creates a Part object from nodes and elements and places it in the parts
        repository.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Part
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        dimensionality
            A SymbolicConstant specifying the dimensionality of the part. Possible values are 
            THREE_D, TWO_D_PLANAR, and AXISYMMETRIC. 
        type
            A SymbolicConstant specifying the type of the part. Possible values are DEFORMABLE_BODY, 
            EULERIAN, DISCRETE_RIGID_SURFACE, and ANALYTIC_RIGID_SURFACE. 
        nodes
            A sequence of (*nodeLabels*, *nodeCoords*) specifying the nodes of the mesh. 
            *nodeLabels* is a sequence of Ints specifying the node labels, and *nodeCoords* is a 
            sequence of sequences of three Floats specifying the nodal coordinates. 
        elements
            A sequence of sequences of(*meshType*, *elementLabels*, *elementConns*) specifying the 
            elements of the mesh. *meshType* is a String specifying the element type. 
            *elementlabels* is a sequence of Ints specifying the element labels. *elementConns* is a 
            sequence of sequences of node labels specifying the element connectivity. 
        twist
            A boolean specifying whether the part is defined with twist. This option has meaning 
            only when *dimensionality*=AXISYMMETRIC. Possible values are ON and OFF. The default 
            value is OFF. 

        Returns
        -------
        part: Part
            A Part object
        """
        pass

    def PartFromOdb(self, name: str, odb: str, fileName: str = '', instance: str = '', elementSet: str = '',
                    shape: SymbolicConstant = UNDEFORMED, step: int = None, frame: int = None,
                    twist: Boolean = OFF):
        """This method creates an orphan mesh Part object by reading an output database. The new
        part is placed in the parts repository.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Part
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        odb
            An output database object. 
        fileName
            A String specifying the name of the output database file from which to create the part. 
            The default value is an empty string. 
        instance
            A String specifying the part instance in the output database from which to create the 
            part. If no instance name is specified, Abaqus creates an orphan mesh part from the 
            first part instance in the output database. 
        elementSet
            A String specifying an element set defined on the output database. Only elements from 
            this set will be imported. The default is to import all element sets. 
        shape
            A SymbolicConstant specifying the configuration state. Possible values are UNDEFORMED 
            and DEFORMED. The default value is UNDEFORMED. 
        step
            An Int specifying the step number for reading deformed coordinates. 0≤step≤N−10≤step≤N-1 
            where NN is the number of available steps. The default value is the last available step. 
            You should specify the *step* argument only when *shape*=DEFORMED. 
        frame
            An Int specifying the frame number for reading deformed coordinates. 
            0≤frame≤N−10≤frame≤N-1 where NN is the number of available frames. The default value is 
            the last available frame. You should specify the *frame* argument only when 
            *shape*=DEFORMED. 
        twist
            A Boolean specifying whether to include a twist DEGREE OF FREEDOM in the part (only 
            available when *dimensionality*=AXISYMMETRIC and *type*=DEFORMABLE_BODY). The default 
            value is OFF. 

        Returns
        -------
        part: Part
            A Part object
            - If the output database contains elements of more than one dimensionality or type: 
              File contains both axisymmetric and nonaxisymmetric elements.File contains both 2D and 
            3D elements.File contains both rigid and deformable elements. 
            - If more than one part is found on the output database: 
              PartError: importing of more than one part is not currently supported 
            - If the output database does not contain any valid results for the specified step: 
              Error. File does not contain any valid frames. 
            - If the specified step and frame do not contain any displacements: 
              Error. Specified frame does not contain nodal displacements. 
            - If the specified element set is not found on the output database: 
              Error. Specified element set is not defined in the ODB. 
            - If the step number is invalid: 
              OdiError: Invalid step index: i. Available step indices: 0 - j. 
            - If the frame number is invalid: 
              OdiError: Invalid frame index: i. Available frame indices: 0 - j. 
        """
        pass

    def PartFromSection3DMeshByPlane(self, name: str, part: 'PartBase', point1: float, point2: float, point3: tuple):
        """This method creates a Part object by cutting an existing three-dimensional orphan mesh
        Part object by a plane and places it in the parts repository. This method is valid only
        for orphan mesh parts composed of 8-node brick elements.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Part
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        part
            A Part object specifying an existing three-dimensional orphan mesh part. 
        point1
            A Sequence of three Floats specifying a point on the cutting plane. This point is the 
            local origin in the local system of the plane. 
        point2
            A Sequence of three Floats specifying a point in the direction of the normal to the 
            cutting plane. This point must not be coincident with *point1*. 
        point3
            A sequence of three Floats specifying the direction of the local 1-axis in the local 
            system of the plane. This point must not project onto *point1*. 

        Returns
        -------
        part: Part
            A Part object
            - If the specified part is not an orphan mesh part: 
              Cannot reduce dimension of a geometric part. 
            - If the specified part is not three-dimensional: 
              Cannot reduce dimension of a 2D part. 
            - If the specified part is a rigid body: 
              Cannot change dimension of a rigid body. 
            - If *point1* and *point2* are coincident: 
              Cutting plane director has zero length. 
            - If *point3* projects onto *point1*: 
              Local axis point projects to origin. 
            - If no elements are cut by the specified plane: 
              Cannot reduce part dimension. 
        """
        pass

    def PartFromSubstructure(self, name: str, substructureFile: str, odbFile: str):
        """This method creates a substructure Part object by reading a substructure sim file and
        places it in the parts repository.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Part
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        substructureFile
            A substructure sim file. 
        odbFile
            The output database file corresponding to the substructure sim file. 

        Returns
        -------
        part: Part
            A Part object
            - If the specified part is not a substructure: 
              File specified does not contain a substructure. 
            - If the specified part already exists: 
              A part with the same name already exists. 
            - If the substructure cannot be imported: 
              The output database is missing nodes and elements.Nested substructures are not 
            supported.The substructure sim file was generated using a version that is different from 
            the current version. 
        """
        pass

    def Part2DGeomFrom2DMesh(self, name: str, part: 'PartBase', featureAngle: float, splineCurvatureLimit: float = 90,
                             twist: Boolean = OFF):
        """This method creates a geometric Part object from the outline of an existing
        two-dimensional orphan mesh Part object and places it in the parts repository. If the
        Part2DGeomFrom2DMesh method cannot create a valid two-dimensional shell section from the
        two-dimensional mesh, the method fails and creates an empty geometry part with a failed
        base shell feature.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Part
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        part
            A Part object specifying an existing two-dimensional orphan mesh Part object. 
        featureAngle
            A Float specifying the angle (in degrees) between line segments that triggers a break in 
            the geometry. 
        splineCurvatureLimit
            A Float specifying the traversal angle in degrees of the spline that triggers a break in 
            the geometry. The default value is 90. 
        twist
            A Boolean specifying whether to include a twist DEGREE OF FREEDOM in the part (only 
            available when *dimensionality*=AXISYMMETRIC and *type*=DEFORMABLE_BODY). The default 
            value is OFF. 

        Returns
        -------
        part: Part
            A Part object
            If the specified part is not an orphan mesh part: 
              Specified part must be an orphan mesh. 
            If the Part2DGeomFrom2DMesh method cannot create a valid two-dimensional shell section from the two-dimensional mesh: 
              Planar shell feature failed 
            If the specified part is not two-dimensional: 
              Cannot create a geometry from a 3D part. 
            If the specified part is a rigid body: 
              Cannot create a geometry from a rigid body. 
        """
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the Part object.

        Raises
        ------
        RangeError
        """
        pass

    def addGeomToSketch(self, sketch: ConstrainedSketch):
        """This method converts a part into a sketch by projecting all of the edges of the part
        onto the X-Y plane of the sketch. You can use addGeomToSketch with a part of any
        modeling space.
        
        Parameters
        ----------
        sketch
            A ConstrainedSketch object. 
        """
        pass

    def assignThickness(self, faces: tuple[Face], thickness: float = None, topFaces: tuple[Face] = (),
                        bottomFaces: tuple[Face] = ()):
        """This method assigns thickness data to shell faces. The thickness can be used while
        assigning shell and membrane sections to faces.
        
        Parameters
        ----------
        faces
            A sequence of Face objects specifying the regions where thickness will be applied. 
        thickness
            A Float specifying the thickness along the given *faces* . Either *thickness*, 
            *topFaces*, or *bottomFaces* must be specified. 
        topFaces
            A sequence of Face objects whose distance to *faces* argument is used to calculate the 
            thickness along the *faces*. The combination of *topFaces* and *bottomFaces* determines 
            the thickness and the offset of the elements. If *bottomFaces* is not specified then the 
            thickness is twice the distance to the *topFaces*. This argument will be ignored if 
            *thickness* is specified. Either *thickness*, *topFaces*, or *bottomFaces* must be 
            specified. 
        bottomFaces
            A sequence of Face objects whose distance to *faces* is used to calculate the thickness 
            along the *faces*. The combination of *topFaces* and *bottomFaces* determines the 
            thickness and the offset of the elements. If *topFaces* is not specified then the 
            thickness is twice the distance to the *bottomFaces*. This argument will be ignored if 
            *thickness* is specified. Either *thickness*, *topFaces*, or *bottomFaces* must be 
            specified. 
        """
        pass

    def backup(self):
        """This method makes a backup copy of the features in the part. Use the restore method to
        retrieve the part's features from the backup.
        """
        pass

    def checkGeometry(self, detailed: Boolean = OFF, reportFacetErrors: Boolean = OFF, level: int = None):
        """This method checks the validity of the geometry of the part and prints a count of all
        topological entities on the part (faces, edges, vertices, etc.).
        
        Parameters
        ----------
        detailed
            A Boolean specifying whether detailed output will be printed to the replay file. The 
            default value is OFF. 
        reportFacetErrors
            A Boolean specifying whether faces are checked for proper facetting. The default value 
            is OFF. 
        level
            An Int specifying which level of checking is performed. Values can range from 20 to 70, 
            with higher values reporting less and less important errors. The default value is 20, 
            which reports all critical errors. When the default value is used, the stored validity 
            status is updated to agree with the result of this check. 
        """
        pass

    def clearGeometryCache(self):
        """This method clears the geometry cache. Clearing the geometry cache reduces the amount of
        memory being used to cache part features.
        """
        pass

    def deleteAllFeatures(self):
        """This method deletes all the features in the part.
        """
        pass

    def deleteFeatures(self, featureNames: tuple):
        """This method deletes the given features.
        
        Parameters
        ----------
        featureNames
            A sequence of Strings specifying the feature names that will be deleted from the part. 
        """
        pass

    def getAngle(self, plane1: str, plane2: str, line1: str, line2: str, commonVertex: str = ''):
        """This method returns the angle between the specified entities.
        
        Parameters
        ----------
        plane1
            A Face, MeshFace, or a Datum object specifying the first plane. The Datum object must 
            represent a datum plane. The *plane1* and *line1* arguments are mutually exclusive. One 
            of them must be specified. 
        plane2
            A Face, MeshFace, or a Datum object specifying the second plane. The Datum object must 
            represent a datum plane. The *plane2* and *line2* arguments are mutually exclusive. One 
            of them must be specified. 
        line1
            An Edge, MeshEdge, or a Datum object specifying the first curve. The Datum object must 
            represent a datum axis. The *plane1* and *line1* arguments are mutually exclusive. One 
            of them must be specified. 
        line2
            An Edge, MeshEdge, or a Datum object specifying the second curve. The Datum object must 
            represent a datum axis. The *plane2* and *line2* arguments are mutually exclusive. One 
            of them must be specified. 
        commonVertex
            If the two selected Edge objects have more than one vertex in common, this ConstrainedSketchVertex object
            specifies the vertex at which to evaluate the angle. 

        Returns
        -------
        angle: float
            A Float specifying the angle between the specified entities. If you provide a plane as 
            an argument, Abaqus/CAE computes the angle using the normal to the plane.
        """
        pass

    def getArea(self, faces: tuple[Face], relativeAccuracy: float = 0):
        """This method returns the total surface area of a given face or group of faces.
        
        Parameters
        ----------
        faces
            A sequence of Face objects whose area the method will calculate. 
        relativeAccuracy
            A Float specifying that the area computation should stop when the specified relative 
            accuracy has been achieved. The default value is 0.000001 (0.0001%). 

        Returns
        -------
        area: float
            A Float specifying the sum of the calculated areas of the given faces.
        """
        pass

    def getAssociatedCADPaths(self):
        """This method returns the paths to the associated CAD part and root file. These are only
        available if the part was imported from one of the supported CAD softwares using the
        Associative Import capability. The root file can be the assembly file or the part file,
        depending on what which one was imported.

        Returns
        -------`
        paths: tuple
            A sequence containing the path to the associated CAD part and assembly file
        """
        pass

    def getCADParameters(self):
        """This method returns the names and values of the CAD parameters associated with the part.
        These are only available if the part was imported from one of the supported CAD
        softwares using the Associative Import capability, and if the parameter names defined in
        that CAD software are prefixed with the string ABQ.

        Returns
        -------
        paras: dict
            A dictionary object representing a map of the name of the parameter and its associated 
            value.
        """
        pass

    def getCentroid(self, faces: tuple[Face], cells: tuple[Face], relativeAccuracy: float = 0):
        """Depending on the arguments provided, this method returns the following:
            - The location of the centroid of a given face or group of faces.
            - The location of the centroid of a given cell or group of cells.
        faces
            A sequence of Face objects whose centroid the method will calculate. The arguments 
            *faces* and *cells* are mutually exclusive. 
        cells
            A sequence of Face objects whose centroid the method will calculate. The arguments 
            *faces* and *cells* are mutually exclusive. 
        relativeAccuracy
            A Float specifying that the centroid computation should stop when the specified relative 
            accuracy has been achieved. The default value is 0.000001 (0.0001%). 

        Returns
        -------
        centroid: tuple[float]
            A sequence of Floats specifying the *X*-, *Y*-, and *Z*-coordinates of the centroid.
        """
        pass

    def getCoordinates(self, entity: str):
        """This method returns the coordinates of specified point.
        
        Parameters
        ----------
        entity
            A ConstrainedSketchVertex, Datum point, MeshNode, or ReferencePoint specifying the entity to query.

        Returns
        -------
            A tuple of 3 Floats representing the coordinates of the specified point.
        """
        pass

    def getCurvature(self, edges: tuple[Edge], samplePoints: int = 100):
        """This method returns the maximum curvature of a given edge or group of edges. For an arc,
        the curvature is constant over the entire edge, and equal to the inverse of the radius.
        For a straight line, the curvature is constant and equal to 0. For a spline edge, the
        curvature varies over a range, and this methods computes the maximum.
        
        Parameters
        ----------
        edges
            A sequence of Edge objects whose curvature the method will calculate. 
        samplePoints
            An Int specifying the number of points along each edge at which the curvature will be 
            computed. The higher the number of sample points, the better the accuracy of the 
            computation. The default value is 100. 

        Returns
        -------
        curvature: float
            A Float specifying the maximum curvature.
        """
        pass

    def getDistance(self, entity1: str, entity2: str):
        """Depending on the arguments provided, this method returns one of the following:
            - The distance between two points.
            - The minimum distance between a point and an edge.
            - The minimum distance between two edges.
        
        Parameters
        ----------
        entity1
            A ConstrainedSketchVertex, Datum point, MeshNode, or Edge specifying the first entity from which to
            measure. 
        entity2
            A ConstrainedSketchVertex, Datum point, MeshNode, or Edge specifying the second entity to which to
            measure. 

        Returns
        -------
        distance: float
            A Float specifying the distance between *entity1* and *entity2*.
        """
        pass

    def getLength(self, edges: tuple[Edge]):
        """This method returns the length of a given edge or group of edges.
        
        Parameters
        ----------
        edges
            A sequence of Edge objects whose total length the method will calculate. 

        Returns
        -------
        length: float
            A Float specifying the total length
        """
        pass

    def getPerimeter(self, faces: tuple[Face]):
        """This method returns the total perimeter of a given face or group of faces. All faces
        need to be on the same part. If the specified faces have shared edges, these edges are
        excluded from the computation, thus providing the length of the outer perimeter of the
        specified faces.
        
        Parameters
        ----------
        faces
            A sequence of Face objects whose perimeter the method will calculate. 

        Returns
        -------
        perimeter: float
            A Float specifying the perimeter
        """
        pass

    def getVolume(self, cells: tuple[Cell], relativeAccuracy: float = 0):
        """This method returns the volume area of a given cell or group of cells.
        
        Parameters
        ----------
        cells
            A sequence of Cell objects whose volume the method will calculate. 
        relativeAccuracy
            A Float specifying the relative accuracy of the computation. The default value is 
            0.000001 (0.0001%). 

        Returns
        -------
        volume: float
            A Float specifying the sum of the areas of the given faces
        """
        pass

    def getMassProperties(self, regions: str = '', relativeAccuracy: SymbolicConstant = LOW, useMesh: Boolean = False,
                          specifyDensity: Boolean = False, density: str = '', specifyThickness: Boolean = False,
                          thickness: str = '', miAboutCenterOfMass: Boolean = True, miAboutPoint: tuple = ()):
        """This method returns the mass properties of a part or region. Only beams, trusses,
        shells, solids, point, nonstructural mass, and rotary inertia elements are supported.
        
        Parameters
        ----------
        regions
            A MeshElementArray, CellArray, FaceArray, or EdgeArray specifying the regions whose mass 
            properties are to be queried. The whole part is queried by default. 
        relativeAccuracy
            A SymbolicConstant specifying the relative accuracy for geometry computation. Possible 
            values are LOW, MEDIUM and HIGH. The default value is LOW. 
        useMesh
            A Boolean specifying whether the mesh should be used in the computation if the geometry 
            is meshed. The default value is False. 
        specifyDensity
            A Boolean specifying whether a user-specified density should be used in regions with 
            density errors such as undefined material density. The default value is False. 
        density
            A double value specifying the user-specified density value to be used in regions with 
            density errors. The user-specified density should be greater than 0. 
        specifyThickness
            A Boolean specifying whether a user-specified thickness should be used in regions with 
            thickness errors such as undefined thickness. The default value is False. 
        thickness
            A double value specifying the user-specified thickness value to be used in regions with 
            thickness errors. The user-specified thickness should be greater than 0. 
        miAboutCenterOfMass
            A Boolean specifying if the moments of inertia should be evaluated about the center of 
            mass. The default value is True. 
        miAboutPoint
            A tuple of three floats specifying the coordinates of the point about which to evaluate 
            the moment of inertia. By default if the moments of inertia are not being evaluated 
            about the center of mass, they will be evaluated about the origin. 

        Returns
        -------
        properties: dict
            A Dictionary object with the following items: 
            *area*: None or a Float specifying the sum of the area of the specified faces. The area 
            is computed only for one side for shells. 
            *areaCentroid*: None or a tuple of three Floats representing the coordinates of the area 
            centroid. 
            *volume*: None or a Float specifying the volume of the specified regions. 
            *volumeCentroid*: None or a tuple of three Floats representing the coordinates of the 
            volume centroid. 
            *massFromMassPerUnitSurfaceArea*: None or a Float specifying the mass due to mass per 
            unit surface area. 
            *mass*: None or a Float specifying the mass of the specified regions. It is the total 
            mass and includes mass from quantities such as mass per unit surface area. 
            *centerOfMass*: None or a tuple of three Floats representing the coordinates of the 
            center of mass. 
            *momentOfInertia*: None or a tuple of six Floats representing the moments of inertia 
            about the center of mass or about the point specified. 
            *warnings*: A tuple of SymbolicConstants representing the problems encountered while 
            computing the mass properties. Possible SymbolicConstants are: 
            UNSUPPORTED_ENTITIES: Some unsupported entities exist in the specified region. The mass 
            properties are computed only for beams, trusses, shells, solids, point and 
            non-structural mass elements and rotary inertia elements. The mass properties are not 
            computed for axisymmetric elements, springs, connectors, gaskets or any other elements. 
            MISSING_THICKNESS: For some regions, the section definitions are missing thickness 
            values. 
            ZERO_THICKNESS: For some regions, the section definitions have a zero thickness value. 
            VARIABLE_THICKNESS: The nodal thickness or field thickness specified for some regions 
            has been ignored. 
            NON_APPLICABLE_THICKNESS: For some regions, the thickness value is not applicable to the 
            corresponding sections specified on the regions. 
            MISSING_DENSITY: For some regions, the section definitions are missing material density 
            values. 
            MISSING_MATERIAL_DEFINITION: For some regions, the material definition is missing. 
            ZERO_DENSITY: For some regions, the section definitions have a zero material density 
            value. 
            UNSUPPORTED_DENSITY: For some regions, either a negative material density or a 
            temperature dependent density has been specified, or the material value is missing for 
            one or more plies in the composite section. 
            SHELL_OFFSETS: For shells, this method does not account for any offsets specified. 
            MISSING_SECTION_DEFINITION: For some regions, the section definition is missing. 
            UNSUPPORTED_SECTION_DEFINITION: The section definition provided for some regions is not 
            supported. 
            REINFORCEMENTS: This method does not account for any reinforcements specified on the 
            model. 
            SMEARED_PROPERTIES: For regions with composite section assignments, the density is 
            smeared across the thickness. The volume centroid and center of mass computations for a 
            composite shell use a lumped mass approach where the volume and mass is assumed to be 
            lumped in the plane of the shell. As a result of these approximations the volume 
            centroid, center of mass and moments of inertia may be slightly inaccurate for regions 
            with composite section assignments. 
            UNSUPPORTED_NON_STRUCTURAL_MASS_ENTITIES: This method does not account for any 
            non-structural mass on wires. 
            INCORRECT_MOMENT_OF_INERTIA: For geometry regions with non-structural mass per volume, 
            the non-structural mass is assumed to be a point mass at the centroid of the regions. 
            Thus, the moments of inertia may be inaccurate as the distribution of the non-structural 
            mass is not accounted for. Use the mesh for accurately computing the moments of inertia. 
            MISSING_BEAM_ORIENTATIONS: For some regions with beam section assignments, the beam 
            section orientations are missing. 
            UNSUPPORTED_BEAM_PROFILES: This method supports the Box, Pipe, Circular, Rectangular, 
            Hexagonal, Trapezoidal, I, L, T, Arbitrary, and Tapered beam profiles. Any other beam 
            profile is not supported. 
            TAPERED_BEAM_MI: Moment of inertia calculations for tapered beams are not accurate. 
            SUBSTRUCTURE_INCORRECT_PROPERTIES: The user assigned density and thickness is not 
            considered for substructures. 
            UNSUPPORTED_NON_STRUCTURAL_MASS_PROPORTIONAL: Non-structural mass with Mass Proportional 
            distribution is not supported. Results are computed using Volume Proportional 
            distribution.
        """
        pass

    def getFeatureFaces(self, name: str):
        """This method returns a sequence of Face objects that are created by the given feature.
        
        Parameters
        ----------
        name
            A string specifying the feature name. 

        Returns
        -------
        faces: tuple[Face]
            Sequence of Face objects. 

        Raises
        ------
            - An exception occurs if a feature with the given name does not exist. 
              Error : Incorrect feature name. 
        """
        pass

    def getFeatureEdges(self, name: str):
        """This method returns a sequence of Edge objects that are created by the given feature.
        
        Parameters
        ----------
        name
            A string specifying the feature name. 

        Returns
        -------
        edges: tuple[Edge]
            Sequence of Edge objects. 

        Raises
        ------
            - An exception occurs if a feature with the given name does not exist. 
              Error : Incorrect feature name. 
        """
        pass

    def getFeatureCells(self, name: str):
        """This method returns a sequence of Cell objects that are created by the given feature.
        
        Parameters
        ----------
        name
            A string specifying the feature name. 

        Returns
        -------
        cells: tuple[Cell]
            Sequence of Cell objects. 

        Raises
        ------
            - An exception occurs if a feature with the given name does not exist. 
              Error : Incorrect feature name. 
        """
        pass

    def getFeatureVertices(self, name: str):
        """This method returns a sequence of ConstrainedSketchVertex objects that are created by the given feature.
        
        Parameters
        ----------
        name
            A string specifying the feature name. 

        Returns
        -------
        vertices: tuple[ConstrainedSketchVertex]
            Sequence of ConstrainedSketchVertex objects.

        Raises
        ------
            - An exception occurs if a feature with the given name does not exist. 
              Error : Incorrect feature name. 
        """
        pass

    def isAlignedWithSketch(self):
        """This method checks if the normal of an analytical rigid surface part is aligned with
        that of its sketch.

        Returns
        -------
            A Boolean value of True if the part is aligned with the sketch and False if it is not 
            aligned. 

        Raises
        ------
            - If the part is not an analytical rigid part: 
              AbaqusException: Can only be used with analytical rigid parts. 
        """
        pass

    def printAssignedSections(self):
        """This method prints information on each section that has been assigned to a region of the
        part.
        """
        pass

    def projectEdgesOntoSketch(self, sketch: str, edges: tuple, constrainToBackground: Boolean = True):
        """This method projects the selected edges of a part onto the specified ConstrainedSketch
        object. The edges appear as sketch geometry after projection. If the plane of projection
        is not parallel to the specified edge, the resultant sketch geometry may be of a
        different type. For example, a circular edge can be projected as an ellipse or a line
        depending on the angle of the plane of projection. By default, the projected edge will
        be constrained to the background geometry. You can remove this constraint by setting
        *constrainToBackground* to False.
        
        Parameters
        ----------
        sketch
            The ConstrainedSketch object on which the edges are projected. 
        edges
            A sequence of candidate edges to be projected onto the sketch. 
        constrainToBackground
            A Boolean that determines whether the projected edges need to constrained to the 
            background geometry. The default is True. 
        """
        pass

    def projectReferencesOntoSketch(self, sketch: str, filter: SymbolicConstant = ALL_EDGES,
                                    upToFeature: Feature = Feature(),
                                    edges: tuple = (), vertices: tuple = ()):
        """This method projects the vertices of specified edges, and datum points from the part
        onto the specified ConstrainedSketch object. The vertices and datum points appear on the
        sketch as reference geometry.
        
        Parameters
        ----------
        sketch
            The ConstrainedSketch object on which the edges, vertices, and datum points are 
            projected. 
        filter
            A SymbolicConstant specifying how to limit the amount of projection. Possible values are 
            ALL_EDGES and COPLANAR_EDGES. If *filter*=COPLANAR_EDGES, edges that are coplanar to the 
            sketching plane are the only candidates for projection. The default value is ALL_EDGES. 
        upToFeature
            A Feature object specifying a marker in the feature-based history of the part. 
            Abaqus/CAE projects onto the sketch only the part entities that were created before the 
            feature specified by this marker. By default, part entities in features created before 
            the sketch you are editing are candidates for projection. 
        edges
            A sequence of candidate edges whose vertices need to be projected onto the sketch. By 
            default, all edges specified by the *filter* argument are candidates for projection. 
        vertices
            A sequence of candidate vertices to be projected onto the sketch. By default, all 
            vertices are candidates for projection. 
        """
        pass

    def queryAttributes(self, printResults: Boolean = OFF):
        """This method prints the following information about a part:
            - the name, modeling space, and analysis type; and
            - whether twist is included (only available when the modeling space is axisymmetric and
        the analysis type is deformable); and
            - the number of vertices, edges, faces and cells if applicable.
        
        Parameters
        ----------
        printResults
            A Boolean which specifies whether the above information is to be printed. The default 
            value is True 

        Returns
        -------
        attributes: dict
            A Dictionary object with string keys and integer values which returns the above 
            information with the keys being numVertices, numEdges, numFaces, numCells, 
            numWiredEdges, numShellFaces and numSolidFaces.
        """
        pass

    def queryCachedStates(self):
        """This method displays the position of geometric states relative to the sequence of
        features in the part cache. The output is displayed in the message area.
        """
        pass

    def queryGeometry(self, relativeAccuracy: float = 0, printResults: Boolean = True):
        """This method prints the following information about a part:
            - the name, modeling space, and analysis type;
            - whether twist is included (only available when the modeling space is axisymmetric and
        the analysis type is deformable);
            - a 3D point representing the minimum of the part's bounding box;
            - a 3D point representing the maximum of the part's bounding box;
            - a 3D point representing the part's centroid (only on 3D solid parts); and
            - the volume (only on 3D solid parts).
        
        Parameters
        ----------
        relativeAccuracy
            A Float specifying that the property computations should stop when the specified 
            relative accuracy has been achieved. The default value is 0.000001 (0.0001%). 
        printResults
            A Boolean which specifies whether the above information is to be printed. The default 
            value is True. 

        Returns
        -------
        geometry: dict
            A Dictionary object with string keys, which returns the above information with the keys 
            being name, space, type, volume, centroid, category and boundingBox.
        """
        pass

    def queryRegionsMissingSections(self):
        """This method returns all regions in the part that do not have a section assignment but
        require one for analysis.

        Returns
        -------
        region: Region
            A Region object, or None
        """
        pass

    def queryDisjointPlyRegions(self):
        """This method provides a list of all composite plys in the current part which have
        disjoint regions.
        """
        pass

    def regenerate(self):
        """This method regenerates a part. When you modify features, it may be convenient to
        postpone regeneration until you make all your changes, since regeneration can be time
        consuming.
        """
        pass

    def regenerationWarnings(self):
        """This method prints any regeneration warnings associated with the features.
        """
        pass

    def removeInvalidGeometry(self):
        """Removes all invalid entities from the part, leaving a valid part. This is not recorded
        as a feature in the feature list, therefore it should be used on parts that have a
        single feature (such as an imported part).
        Note:This may remove valid entities that are connected to invalid ones. You can identify
        invalid entities using the query toolset before using this command.
        """
        pass

    def restore(self):
        """This method restores the parameters of all features in the assembly to the value they
        had before a failed regeneration. Use the restore method after a failed regeneration,
        followed by a regenerate command.
        """
        pass

    def resumeAllFeatures(self):
        """This method resumes all the suppressed features in the part.
        """
        pass

    def resumeFeatures(self, featureNames: tuple):
        """This method resumes the specified suppressed features in the part.
        
        Parameters
        ----------
        featureNames
            A tuple of names of features which are to be resumed. 
        """
        pass

    def resumeLastSetFeatures(self):
        """This method resumes the last set of features to be suppressed in the part.
        """
        pass

    def saveGeometryCache(self):
        """This method caches the current geometry. Caching the current geometry improves
        regeneration performance.
        """
        pass

    def setAssociatedCADPaths(self, partFile: str = '', rootFile: str = ''):
        """This method sets the paths to the associated CAD part and root file. This method is only
        available if the part was imported from one of the supported CAD softwares using the
        Associative Import capability. The root file can be the assembly file or the part file,
        depending on the one that was imported. This method can be used to specify the new paths
        when the CAD data is moved to a different directory.
        
        Parameters
        ----------
        partFile
            A String specifying the name of the associated CAD part file. 
        rootFile
            A String specifying the name of the root associated CAD file. This can be the same as 
            the part file or can be the assembly file, depending on the one that was imported. 
        """
        pass

    def suppressFeatures(self, featureNames: tuple):
        """This method suppresses the given features.
        
        Parameters
        ----------
        featureNames
            A tuple of names of features which are to be suppressed in the part. 
        """
        pass

    def writeAcisFile(self, fileName: str, version: float = None):
        """This method exports the geometry of the part to a named file in ACIS format.
        
        Parameters
        ----------
        fileName
            A String specifying the name of the file to which to write. 
        version
            A Float specifying the ACIS version. For example, the Float 12.0 corresponds to ACIS 
            Version 12.0. The default value is the current version of ACIS.

        Raises
        ------
            - If the part is an orphan mesh part: 
              Cannot export orphan mesh parts to ACIS. 
        """
        pass

    def writeCADParameters(self, paramFile: str, modifiedParams: tuple = (), updatePaths: str = ''):
        """This method writes the parameters that were imported from the CAD system to a parameter
        file.
        
        Parameters
        ----------
        paramFile
            A String specifying the parameter file name. 
        modifiedParams
            A tuple of tuples each containing the part name, the parameter name, and the modified 
            parameter value. Default is an empty tuple. 
        updatePaths
            A Bool specifying whether to update the path of the CAD model file specified in the 
            *parameterFile* to the current directory, if the CAD model is present in the current 
            directory. 
        """
        pass

    def writeIgesFile(self, fileName: str, flavor: SymbolicConstant):
        """This method exports the geometry of the part to a named file in IGES format.
        
        Parameters
        ----------
        fileName
            A String specifying the name of the file to which to write. 
        flavor
            A SymbolicConstant specifying a particular flavor of IGES. Possible values are STANDARD, 
            AUTOCAD, SOLIDWORKS, JAMA, and MSBO.

        Raises
        ------
            - If the part is an orphan mesh part: 
              Cannot export orphan mesh parts to IGES. 
        """
        pass

    def writeStepFile(self, fileName: str):
        """This method exports the geometry of the part to a named file in STEP format.
        
        Parameters
        ----------
        fileName
            A String specifying the name of the file to which to write.

        Raises
        ------
            - If the part contains no geometry: 
              Parterror: Cannot export orphan mesh parts to STEP. 
        """
        pass

    def writeVdaFile(self, fileName: str):
        """This method exports the geometry of the part to a named file in VDA-FS format.
        
        Parameters
        ----------
        fileName
            A String specifying the name of the file to which to write.

        Raises
        ------
            - If the part is an orphan mesh part: 
              Cannot export orphan mesh parts to VDA-FS. 
        """
        pass

    def copyMeshPattern(self, elements: tuple[MeshElement] = (), faces: tuple[Face] = (),
                        elemFaces: tuple[MeshFace] = (), targetFace: MeshFace = MeshFace(),
                        nodes: tuple[MeshNode] = (), coordinates: tuple = ()):
        """This method copies a mesh pattern from a source region consisting of a set of shell
        elements or element faces onto a target face, mapping nodes and elements in a one-one
        correspondence between source and target.
        
        Parameters
        ----------
        elements
            A sequence of MeshElement objects or a Set object containing elements and specifying the 
            source region. 
        faces
            A sequence of Face objects that have associated with shell elements or element faces and 
            specifying the source region. 
        elemFaces
            A sequence of MeshFace objects specifying the source region. 
        targetFace
            A MeshFace object specifying the target region. 
        nodes
            A sequence of MeshNode objects or a Set object containing nodes on the boundary of 
            source region which are to be positioned to the boundary of target face. 
        coordinates
            A sequence of three-dimensional coordinate tuples specifying the coordinates for each of 
            the given nodes. When specified, the number of coordinate tuples must match the number 
            of given nodes, and be ordered to correspond to the given nodes in *ascending order* 
            according to index. These coordinates are positions of the nodes of a mesh that will be 
            the target face corresponding to nodes provided. 
        """
        pass

    def smoothNodes(self, nodes: tuple[MeshNode]):
        """This method smooths the given nodes of a native mesh, moving them locally to a more
        optimal location that improves the quality of the mesh
        
        Parameters
        ----------
        nodes
            A sequence of MeshNode objects or a Set object containing nodes. 
        """
        pass

    def Lock(self):
        """This method locks the part. Locking the part prevents any further changes to the part
        that can trigger regeneration of the part.
        """
        pass

    def Unlock(self):
        """This method unlocks the part. Unlocking the part allows it to be regenerated after any
        modifications to the part.
        """
        pass

    def LockForUpgrade(self):
        """This method locks the part for upgrade. Locking the part prevents any further changes to
        the part that can trigger regeneration of the part. When the part is unlocked, all the
        parts are upgraded and regenrated.
        """
        pass
