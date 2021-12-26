from abaqusConstants import *
from ..BasicGeometry.CellArray import CellArray
from ..BasicGeometry.EdgeArray import EdgeArray
from ..BasicGeometry.FaceArray import FaceArray
from ..BasicGeometry.IgnoredEdgeArray import IgnoredEdgeArray
from ..BasicGeometry.IgnoredVertexArray import IgnoredVertexArray
from ..BasicGeometry.ReferencePoint import ReferencePoint
from ..BasicGeometry.VertexArray import VertexArray
from ..Datum.Datum import Datum
from ..Mesh.MeshEdge import MeshEdge
from ..Mesh.MeshEdgeArray import MeshEdgeArray
from ..Mesh.MeshElementArray import MeshElementArray
from ..Mesh.MeshFace import MeshFace
from ..Mesh.MeshFaceArray import MeshFaceArray
from ..Mesh.MeshNodeArray import MeshNodeArray
from ..Part.Part import Part
from ..Region.Set import Set
from ..Region.Skin import Skin
from ..Region.Stringer import Stringer
from ..Region.Surface import Surface
from ..UtilityAndView.Repository import Repository


class PartInstance:

    """A PartInstance object is an instance of a Part object. 

    Access
    ------
        - import assembly
        - mdb.models[name].rootAssembly.allInstances[name]
        - mdb.models[name].rootAssembly.instances[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the repository key. The name must be a valid Abaqus object name. 
    name: str = ''

    # A Boolean specifying whether the part instance is dependent or independent. If 
    # *dependent*=OFF, the part instance is independent. The default value is OFF. 
    dependent: Boolean = OFF

    # A Boolean specifying whether the part instance is excluded from the simulation. If 
    # *excludedFromSimulation*=ON, the part instance is excluded from the simulation. The 
    # default value is OFF. 
    excludedFromSimulation: Boolean = OFF

    # A Boolean specifying the validity of the geometry of the instance. The value is 
    # computed, but it can be set to ON to perform feature and mesh operations on an invalid 
    # instance. There is no guarantee that such operations will work if the instance was 
    # originally invalid. 
    geometryValidity: Boolean = OFF

    # A SymbolicConstant specifying the part type. Possible values are DEFORMABLE_BODY, 
    # EULERIAN, DISCRETE_RIGID_SURFACE, and ANALYTIC_RIGID_SURFACE. 
    analysisType: SymbolicConstant = None

    # An Int specifying the reference node number. This member is valid only if 
    # *analysisType*=DISCRETE_RIGID_SURFACE or ANALYTIC_RIGID_SURFACE. 
    referenceNode: int = None

    # A Part object specifying the instanced part. 
    part: Part = None

    # A repository of Set objects specifying the sets created on the part. For more 
    # information, see [Region 
    # commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all). 
    sets: Repository[str, Set] = None

    # A repository of Surface objects specifying the surfaces created on the part. For more 
    # information, see [Region 
    # commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all). 
    surfaces: Repository[str, Surface] = None

    # A repository of Skin objects specifying the skins created on the part. For more 
    # information, see [Region 
    # commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all). 
    skins: Repository[str, Skin] = None

    # A repository of Stringer objects specifying the stringers created on the part. For more 
    # information, see [Region 
    # commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all). 
    stringers: Repository[str, Stringer] = None

    # A VertexArray object. 
    vertices: VertexArray = None

    # An IgnoredVertexArray object. 
    ignoredVertices: IgnoredVertexArray = None

    # An EdgeArray object. 
    edges: EdgeArray = None

    # An IgnoredEdgeArray object. 
    ignoredEdges: IgnoredEdgeArray = None

    # A FaceArray object. 
    faces: FaceArray = None

    # A CellArray object. 
    cells: CellArray = None

    # A repository of Datum objects. 
    datums: Repository[str, Datum] = None

    # A MeshElementArray object. 
    elements: MeshElementArray = None

    # A MeshNodeArray object. 
    nodes: MeshNodeArray = None

    # A repository of MeshFace objects specifying all the element faces in the part instance. 
    # For a given element and a given face index within that element, the corresponding 
    # MeshFace object can be retrieved from the repository by using the key calculated as (i*8 
    # + j), where i and j are zero-based element and face indices, respectively. 
    elemFaces: Repository[str, MeshFace] = None

    # A MeshFaceArray object. 
    elementFaces: MeshFaceArray = None

    # A repository of MeshEdge objects specifying all the element edges in the part instance. 
    # For a given element and a given edge index on a given face within that element, the 
    # corresponding MeshEdge object can be retrieved from the repository by using the key 
    # calculated as (i*32 + j*4 + k), where i, j, and k are zero-based element, face, and edge 
    # indices, respectively. 
    elemEdges: Repository[str, MeshEdge] = None

    # A MeshEdgeArray object. 
    elementEdges: MeshEdgeArray = None

    # A repository of ReferencePoint objects. 
    referencePoints: Repository[str, ReferencePoint] = None

    # A String specifying the name of the part from which the instance was created. 
    partName: str = ''

    def Instance(self, name: str, part: Part, autoOffset: Boolean = OFF, dependent: Boolean = OFF):
        """This method creates a PartInstance object and puts it into the instances repository.

        Path
        ----
            - mdb.models[name].rootAssembly.Instance

        Parameters
        ----------
        name
            A String specifying the repository key. The name must be a valid Abaqus object name. 
        part
            A Part object to be instanced. If the part does not exist, no PartInstance object is 
            created. 
        autoOffset
            A Boolean specifying whether to apply an auto offset to the new part instance that will 
            offset it from existing part instances. The default value is OFF. 
        dependent
            A Boolean specifying whether the part instance is dependent or independent. If 
            *dependent*=OFF, the part instance is independent. The default value is OFF. 

        Returns
        -------
            A PartInstance object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def InstanceFromBooleanCut(self, name: str, instanceToBeCut: str, cuttingInstances: tuple[PartInstance], 
                               originalInstances: SymbolicConstant = SUPPRESS):
        """This method creates a PartInstance in the instances repository after subtracting or
        cutting the geometries of a group of part instances from that of a base part instance.

        Path
        ----
            - mdb.models[name].rootAssembly.InstanceFromBooleanCut

        Parameters
        ----------
        name
            A String specifying the repository key. The name must be a valid Abaqus object name. 
        instanceToBeCut
            A PartInstance specifying the base instance from which to cut other instances. 
        cuttingInstances
            A sequence of PartInstance objects specifying the instances with which to cut the base 
            instance. 
        originalInstances
            A SymbolicConstant specifying whether the original instances should be suppressed or 
            deleted after the merge operation. Possible values are SUPPRESS or DELETE. The default 
            value is SUPPRESS. 

        Returns
        -------
            A PartInstance object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def InstanceFromBooleanMerge(self, name: str, instances: tuple[PartInstance], keepIntersections: Boolean = False, 
                                 originalInstances: SymbolicConstant = SUPPRESS, domain: SymbolicConstant = GEOMETRY, 
                                 mergeNodes: SymbolicConstant = BOUNDARY_ONLY, nodeMergingTolerance: float = None, 
                                 removeDuplicateElements: Boolean = True):
        """This method creates a PartInstance in the instances repository after merging two or more
        part instances.

        Path
        ----
            - mdb.models[name].rootAssembly.InstanceFromBooleanMerge

        Parameters
        ----------
        name
            A String specifying the repository key. The name must be a valid Abaqus object name. 
        instances
            A sequence of PartInstance objects specifying the part instances to merge. 
        keepIntersections
            A Boolean specifying whether the boundary intersections of Abaqus native part instances 
            should be retained after the merge operation. The default value is False. 
        originalInstances
            A SymbolicConstant specifying whether the original instances should be suppressed or 
            deleted after the merge operation. Possible values are SUPPRESS or DELETE. The default 
            value is SUPPRESS. 
        domain
            A SymbolicConstant specifying whether geometry or mesh of the specified part instances 
            is to be merged. Possible values are GEOMETRY, MESH or BOTH. The default value is 
            GEOMETRY. 
        mergeNodes
            A SymbolicConstant specifying which nodes of the specified part instances should be 
            considered for merging. This argument is only applicable if *domain* is MESH. Possible 
            values are BOUNDARY_ONLY, ALL, or NONE. The default value is BOUNDARY_ONLY. 
        nodeMergingTolerance
            A Float specifying the maximum distance between nodes of the specified part instances 
            that will be merged and replaced with a single node in the new part. The location of the 
            new node is the average position of the deleted nodes. This argument is only applicable 
            if *domain* is MESH. The default value is 10–6. 
        removeDuplicateElements
            A Boolean specifying whether elements with the same connectivity in the new part will be 
            merged into a single element. This argument is only applicable if *domain* is MESH. The 
            default value is True. 

        Returns
        -------
            A PartInstance object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def LinearInstancePattern(self, instanceList: tuple, number1: int, spacing1: float, number2: int, spacing2: float, 
                              direction1: tuple = (), direction2: tuple = ()):
        """This method creates multiple PartInstance objects in a linear pattern and puts them into
        the instances repository.

        Path
        ----
            - mdb.models[name].rootAssembly.LinearInstancePattern

        Parameters
        ----------
        instanceList
            A sequence of Strings specifying the names of instances to pattern. 
        number1
            An Int specifying the total number of instances, including the original instances, that 
            appear along the first direction in the pattern. 
        spacing1
            A Float specifying the spacing between instances along the first direction in the 
            pattern. 
        number2
            An Int specifying the total number of instances, including the original instances, that 
            appear along the second direction in the pattern. 
        spacing2
            A Float specifying the spacing between instances along the second direction in the 
            pattern. 
        direction1
            A sequence of three Floats specifying a vector along the first direction. The default 
            value is (1.0, 0.0, 0.0). 
        direction2
            A sequence of three Floats specifying a vector along the second direction. The default 
            value is (0.0, 1.0, 0.0). 

        Returns
        -------
            A sequence of PartInstance objects. 

        Exceptions
        ----------
            None. 
        """
        pass

    def RadialInstancePattern(self, instanceList: tuple, number: int, totalAngle: float, point: tuple = (), 
                              axis: tuple = ()):
        """This method creates multiple PartInstance objects in a radial pattern and puts them into
        the instances repository.

        Path
        ----
            - mdb.models[name].rootAssembly.RadialInstancePattern

        Parameters
        ----------
        instanceList
            A sequence of Strings specifying the names of instances to pattern. 
        number
            An Int specifying the total number of instances, including the original instances, that 
            appear in the radial pattern. 
        totalAngle
            A Float specifying the total angle in degrees between the first and last instance in the 
            pattern. A positive angle corresponds to a counter-clockwise direction. The values 360° 
            and −360° represent a special case where the pattern makes a full circle. In this case, 
            because the copy would overlay the original, the copy is not placed at the last 
            position. Possible values are −360.0 ≤≤ *totalAngle* ≤≤ 360.0. 
        point
            A sequence of three Floats specifying the center of the radial pattern. The default 
            value is (0.0, 0.0, 0.0). 
        axis
            A sequence of three Floats specifying the central axis of the radial pattern. The 
            default value is (0.0, 0.0, 1.0). 

        Returns
        -------
            A sequence of PartInstance objects. 

        Exceptions
        ----------
            None. 
        """
        pass

    def checkGeometry(self, detailed: Boolean = OFF, level: int = None):
        """This method checks the validity of the geometry of the part instance and prints a count
        of all topological entities on the part instance (faces, edges, vertices, etc.).

        Parameters
        ----------
        detailed
            A Boolean specifying whether detailed output will be printed to the replay file. The 
            default value is OFF. 
        level
            An Int specifying which level of checking is performed. Values can range from 20 to 70, 
            with higher values reporting less and less important errors. The default value is 20, 
            which reports all critical errors. When the default value is used, the stored validity 
            status is updated to agree with the result of this check. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            - An exception is thrown if this is a dependent part instance and *level* was either not 
            specified or was set to 20, because the validity status cannot be updated for a 
            dependent part instance. In this case, this command should be called on the Part 
            instead. 
              The geometry of dependent part instances cannot be changed. 
        """
        pass

    def Contact(self, movableList: tuple, fixedList: tuple, direction: tuple, clearance: float, 
                isFaceEdges: Boolean = OFF):
        """This method translates an instance along the specified direction until it is in contact
        with a fixed instance.

        Parameters
        ----------
        movableList
            A sequence of Face or Edge objects on the part instance to be moved. 
        fixedList
            A sequence of Face or Edge objects on the part instance to remain fixed. 
        direction
            A sequence of three Floats specifying the direction of contact. 
        clearance
            A Float specifying the distance between the two faces along the direction of contact. 
        isFaceEdges
            A Boolean specifying how Abaqus calculates the contact. If *isFaceEdges* is OFF, contact 
            is computed from the movable face to the fixed face. If *isFaceEdges* is ON, contact is 
            computed using only the edges of the movable face and not its interior. The default 
            value is OFF. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def ConvertConstraints(self):
        """This method converts the position constraints of an instance to absolute positions. The
        method deletes the constraint features on the instance but preserves the position in
        space.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getPosition(self):
        """This method prints the sum of the translations and rotations applied to the PartInstance
        object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getRotation(self):
        """This method returns a tuple including the point of rotation, axis of rotation, and
        rotation angle (in degrees).

        Parameters
        ----------

        Returns
        -------
            A tuple including the point of rotation, axis of rotation, and rotation angle (in 
            degrees). 

        Exceptions
        ----------
            None. 
        """
        pass

    def getTranslation(self):
        """This method returns a tuple of three Floats representing translation in the *X*-, *Y*-,
        and *Z*-directions.

        Parameters
        ----------

        Returns
        -------
            A tuple of three Floats representing the translation. 

        Exceptions
        ----------
            None. 
        """
        pass

    def replace(self, instanceOf: Part, applyConstraints: Boolean = True):
        """This method replaces one instance with an instance of another part.

        Parameters
        ----------
        instanceOf
            A Part object specifying which Part will be instanced in place of the original Part. 
        applyConstraints
            A Boolean specifying whether to apply existing constraints on the new instance or to 
            position the new instance in the same place as the original instance. The default value 
            is True. A value of False indicates that constraints applies to the instance are deleted 
            will be deleted from the feature list. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def rotateAboutAxis(self, axisPoint: tuple, axisDirection: tuple, angle: float):
        """This method translates an instance by the specified amount.

        Parameters
        ----------
        axisPoint
            A sequence of three Floats specifying the *X*-, *Y*-, and *Z*-coordinates of a point on 
            the axis. 
        axisDirection
            A sequence of three Floats specifying the direction vector of the axis. 
        angle
            A Float specifying the rotation angle in degrees. Use the right-hand rule to determine 
            the direction. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def translate(self, vector: tuple):
        """This method translates an instance by the specified amount.

        Parameters
        ----------
        vector
            A sequence of three Floats specifying a translation vector. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def translateTo(self, movableList: tuple, fixedList: tuple, direction: tuple, clearance: float, 
                    vector: tuple = ()):
        """This method translates an instance along the specified direction until it is in contact
        with a fixed instance.

        Parameters
        ----------
        movableList
            A sequence of Face or Edge objects on the part instance to be moved. 
        fixedList
            A sequence of Face or Edge objects on the part instances to remain fixed. 
        direction
            A sequence of three Floats specifying the direction of contact. 
        clearance
            A Float specifying the distance between the two faces along the direction of contact. 
        vector
            A sequence of three Floats specifying a translation vector. If this argument is 
            specified, the movable instance will be translated by the specified amount without 
            solving for the actual contact. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            None. 
        """
        pass
