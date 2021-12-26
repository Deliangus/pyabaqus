import typing

from abaqusConstants import *
from ..BasicGeometry.Cell import Cell
from ..BasicGeometry.Edge import Edge
from ..BasicGeometry.Face import Face
from ..Datum.Datum import Datum
from ..Datum.DatumPlane import DatumPlane
from ..Mesh.MeshFace import MeshFace
from ..Sketcher.ConstrainedSketch import ConstrainedSketch


class Feature:

    """Abaqus/CAE is a feature-based modeling system, and features are stored in the Feature 
    object. The user defines the parameters of the feature, and Abaqus/CAE modifies the 
    model based on the value of the parameters. This evaluation of the parameters is called 
    regeneration of the feature. Feature objects contain both the parameters and the 
    resulting model modification. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].features[name]
        - mdb.models[name].parts[name].featuresById[i]
        - import assembly
        - mdb.models[name].rootAssembly.features[name]
        - mdb.models[name].rootAssembly.featuresById[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the repository key. 
    name: str = ''

    # An Int specifying the ID of the feature. 
    id: int = None

    def AttachmentPoints(self, name: str, points: float, projectionMethod: SymbolicConstant = PROJECT_BY_PROXIMITY, 
                         projectOnFaces: tuple[Face] = (), projectOnElementFaces: tuple[MeshFace] = (), 
                         projectionDirStartPt: float = None, projectionDirEndPt: float = None, setName: str = ''):
        """This method creates an attachment points Feature. Attachment points may be created using
        datum points, vertices, reference points, attachment points, interesting points, orphan
        mesh nodes or coordinates. Optionally, the attachment points can be projected on
        geometric faces or element faces.

        Path
        ----
            - mdb.models[*name*].parts[*name*].AttachmentPoints
            - mdb.models[*name*].rootAssembly.AttachmentPoints

        Parameters
        ----------
        name
            A String specifying a unique Feature name. 
        points
            A tuple of points. Each point can be a Vertex, Datum point, Reference point, Attachment 
            point, orphan mesh Node, Interesting point object, or a tuple of Floats representing the 
            coordinates of a point. 
        projectionMethod
            A SymbolicConstant specifying the projection method. Possible values are 
            PROJECT_BY_PROXIMITY and PROJECT_BY_DIRECTION. The default value is 
            PROJECT_BY_PROXIMITY. 
        projectOnFaces
            A sequence of Face objects specifying the geometry faces onto which the points are to be 
            projected. 
        projectOnElementFaces
            A sequence of MeshFace objects specifying the orphan mesh element faces onto which the 
            points are to be projected. 
        projectionDirStartPt
            A point specifying the start point of the projection direction. The point can be a 
            Vertex, Datum point, Reference point, Attachment point, orphan mesh Node, Interesting 
            point object, or a tuple of Floats representing the coordinates of a point. 
        projectionDirEndPt
            A point specifying the end point of the projection direction. The point can be a Vertex, 
            Datum point, Reference point, Attachment point, orphan mesh Node, Interesting point 
            object, or a tuple of Floats representing the coordinates of a point. 
        setName
            A String specifying a unique set name. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def AttachmentPointsAlongDirection(self, name: str, startPoint: float, pointCreationMethod: SymbolicConstant, 
                                       endPoint: float = None, direction: str = '', spacing: str = '', 
                                       numPtsAlongDir: str = '', numPtsBetweenPts: str = '', createPtAtStartPt: Boolean = True, 
                                       createPtAtEndPt: Boolean = True, 
                                       projectionMethod: SymbolicConstant = PROJECT_BY_PROXIMITY, 
                                       projectOnFaces: tuple[Face] = (), projectOnElementFaces: tuple[MeshFace] = (), 
                                       projectionDirStartPt: float = None, projectionDirEndPt: float = None, 
                                       flipDirection: Boolean = OFF, setName: str = ''):
        """This method creates a Feature object by creating attachment points along a direction or
        between two points. A Datum point, a Vertex, a Reference point, an Attachment point, an
        Interesting point, or an orphan mesh Node can be specified as the start or end point.
        The direction can be specified using a straight edge or a datum axis.

        Path
        ----
            - mdb.models[*name*].parts[*name*].AttachmentPointsAlongDirection
            - mdb.models[*name*].rootAssembly.AttachmentPointsAlongDirection

        Parameters
        ----------
        name
            A String specifying a unique Feature name. 
        startPoint
            A point specifying the start point of the direction along which to create points. The 
            point can be a Vertex, Datum point, Reference point, Attachment point, orphan mesh Node, 
            Interesting point object, or a tuple of Floats representing the coordinates of a point. 
        pointCreationMethod
            A SymbolicConstant specifying the point creation method. Possible values are AUTO_FIT, 
            NUM_PTS_ALONG_DIR, and NUM_PTS_BETWEEN_PTS. 
        endPoint
            A point specifying the end point if creating points between two points. The point can be 
            a Vertex, Datum point, Reference point, Attachment point, orphan mesh Node, Interesting 
            point object, or a tuple of Floats representing the coordinates of a point. 
        direction
            The direction can be specified by a straight edge or a datum axis. 
        spacing
            A float specifying the spacing to be used between two points. 
        numPtsAlongDir
            An integer specifying the number of points to be created along the specified direction. 
        numPtsBetweenPts
            An integer specifying the number of points to be created between the start and end 
            points. 
        createPtAtStartPt
            A Boolean specifying whether to create an attachment point at the start point. The 
            default value is True. 
        createPtAtEndPt
            A Boolean specifying whether to create an attachment point at the end point. The default 
            value is True. 
        projectionMethod
            A SymbolicConstant specifying the projection method. Possible values are 
            PROJECT_BY_PROXIMITY and PROJECT_BY_DIRECTION. The default value is 
            PROJECT_BY_PROXIMITY. 
        projectOnFaces
            A sequence of Face objects specifying the geometry faces onto which the points are to be 
            projected. 
        projectOnElementFaces
            A sequence of MeshFace objects specifying the orphan mesh element faces onto which the 
            points are to be projected. 
        projectionDirStartPt
            A point specifying the start point of the projection direction. The point can be a 
            Vertex, Datum point, Reference point, Attachment point, orphan mesh Node, Interesting 
            point object, or a tuple of Floats representing the coordinates of a point. 
        projectionDirEndPt
            A point specifying the end point of the projection direction. The point can be a Vertex, 
            Datum point, Reference point, Attachment point, orphan mesh Node, Interesting point 
            object, or a tuple of Floats representing the coordinates of a point. 
        flipDirection
            A Boolean specifying if the direction along which the attachment points are created 
            should be reversed. This argument is valid only when 
            *pointCreationMethod*=NUM_PTS_ALONG_DIR. 
        setName
            A String specifying a unique set name. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def AttachmentPointsOffsetFromEdges(self, name: str, edges: tuple, startPoint: str = '', flipDirection: str = '', 
                                        pointCreationMethod: SymbolicConstant = None, numberOfPoints: str = '', 
                                        spacingBetweenPoints: str = '', offsetFromStartPoint: str = 0, 
                                        offsetFromEndPoint: str = 0, spacingMethod: SymbolicConstant = AUTO_FIT_PTS, 
                                        patterningMethod: SymbolicConstant = None, referenceFace: str = '', 
                                        startPointForPatternDirection: float = None, endPointForPatternDirection: float = None, 
                                        offsetFromEdges: str = '', numberOfRows: str = 1, spacingBetweenRows: str = '', 
                                        projectionMethod: SymbolicConstant = PROJECT_BY_PROXIMITY, 
                                        projectOnFaces: tuple[Face] = (), projectOnElementFaces: tuple[MeshFace] = (), 
                                        projectionDirStartPt: float = None, projectionDirEndPt: float = None, setName: str = ''):
        """This method creates a Feature object by creating attachment points along or offset from
        one or more connected edges.

        Path
        ----
            - mdb.models[*name*].parts[*name*].AttachmentPointsOffsetFromEdges
            - mdb.models[*name*].rootAssembly.AttachmentPointsOffsetFromEdges

        Parameters
        ----------
        name
            A String specifying a unique Feature name. 
        edges
            A sequence of connected Edge objects specifying the geometry edges from which to offset 
            the points. 
        startPoint
            A Vertex of the selected edges that specifies the point from which to create points. 
            This point can be one of the two end vertices of the connected edges. In case of edges 
            forming a closed loop and having multiple vertices, this point can be any one of the 
            vertices on the edges. 
        flipDirection
            This parameter is required to indicate the direction in which to create the points. This 
            parameter is required only in case of edges forming a closed loop. 
        pointCreationMethod
            A SymbolicConstant specifying the point creation method. Possible values are BY_NUMBER 
            or BY_SPACING. 
        numberOfPoints
            An integer specifying the number of points to be created along the selected edges. 
        spacingBetweenPoints
            A float specifying the spacing to be used between two points while creating the points 
            between the start and end points of the edges. 
        offsetFromStartPoint
            A float specifying the distance by which to offset the first point from the start vertex 
            of the edge chain. The default value is 0.0. 
        offsetFromEndPoint
            A float specifying the distance by which to offset the last point from the end vertex of 
            the edge chain. This parameter should be specified only if the point creation method is 
            BY_NUMBER. The default value is 0.0. 
        spacingMethod
            A SymbolicConstant specifying the spacing method. Possible values are AUTO_FIT_PTS or 
            SPECIFY_NUM_PTS. The default value is AUTO_FIT_PTS. 
        patterningMethod
            A SymbolicConstant specifying the method to pattern of points. Possible values are 
            PATTERN_ORTHOGONALLY or PATTERN_ALONG_DIRECTION. 
        referenceFace
            A geometry Face object adjacent to one of the edges from which to offset the points to 
            create a pattern of points when the PATTERN_ORTHOGONALLY method is chosen for 
            patterning. The face is used to identify the patterning direction. If the number of rows 
            is one and the initial offset is zero, the reference face may not be specified. 
        startPointForPatternDirection
            A point specifying the start point of the direction along which to create a pattern of 
            points when the PATTERN_ALONG_DIRECTION method is chosen for patterning. The point can 
            be a Vertex, Datum point, Reference point, Attachment point, orphan mesh Node, 
            Interesting point object, or a tuple of Floats representing the coordinates of a point. 
        endPointForPatternDirection
            A point specifying the end point of the direction along which to create a pattern of 
            points when the PATTERN_ALONG_DIRECTION method is chosen for patterning. The point can 
            be a Vertex, Datum point, Reference point, Attachment point, orphan mesh Node, 
            Interesting point object, or a tuple of Floats representing the coordinates of a point. 
        offsetFromEdges
            A float specifying the distance by which to offset the first row of points from the 
            edges. 
        numberOfRows
            An integer specifying the number of rows of points to be created for the pattern. The 
            default value is 1. 
        spacingBetweenRows
            A float specifying the spacing to be used between two rows while creating a pattern of 
            points. 
        projectionMethod
            A SymbolicConstant specifying the projection method. Possible values are 
            PROJECT_BY_PROXIMITY and PROJECT_BY_DIRECTION. The default value is 
            PROJECT_BY_PROXIMITY. 
        projectOnFaces
            A sequence of Face objects specifying the geometry faces onto which the points are to be 
            projected. 
        projectOnElementFaces
            A sequence of MeshFace objects specifying the orphan mesh element faces onto which the 
            points are to be projected. 
        projectionDirStartPt
            A point specifying the start point of the projection direction. The point can be a 
            Vertex, Datum point, Reference point, Attachment point, orphan mesh Node, Interesting 
            point object, or a tuple of Floats representing the coordinates of a point. 
        projectionDirEndPt
            A point specifying the end point of the projection direction. The point can be a Vertex, 
            Datum point, Reference point, Attachment point, orphan mesh Node, Interesting point 
            object, or a tuple of Floats representing the coordinates of a point. 
        setName
            A String specifying a unique set name. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def DatumAxisByCylFace(self, face: str):
        """This method creates a Feature object and a DatumAxis object along the axis of a cylinder
        or cone.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumAxisByCylFace
            - mdb.models[*name*].parts[*name*].DatumAxisByCylFace

        Parameters
        ----------
        face
            A cylindrical or conical Face object. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumAxisByNormalToPlane(self, plane: str, point: int):
        """This method creates a Feature object and a DatumAxis object normal to the specified
        plane and passing through the specified point.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumAxisByNormalToPlane
            - mdb.models[*name*].parts[*name*].DatumAxisByNormalToPlane

        Parameters
        ----------
        plane
            A planar Face, an ElementFace, or a Datum object representing a datum plane. 
        point
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumAxisByParToEdge(self, edge: str, point: int):
        """This method creates a Feature object and a DatumAxis object parallel to the specified
        edge and passing through the specified point.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumAxisByParToEdge
            - mdb.models[*name*].parts[*name*].DatumAxisByParToEdge

        Parameters
        ----------
        edge
            A straight Edge, an ElementEdge, or a Datum object representing a datum axis. 
        point
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumAxisByPrincipalAxis(self, principalAxis: SymbolicConstant):
        """This method creates a Feature object and a DatumAxis object along one of the three
        principal axes.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumAxisByPrincipalAxis
            - mdb.models[*name*].parts[*name*].DatumAxisByPrincipalAxis

        Parameters
        ----------
        principalAxis
            A SymbolicConstant specifying the principal axis. Possible values are XAXIS, YAXIS, and 
            ZAXIS. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    @typing.overload
    def DatumAxisByRotation(self, line: str, axis: str, angle: float):
        """This method creates a Feature object and a DatumAxis object in a three-dimensional model
        by rotating a line about the specified axis through the specified angle.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumAxisByRotation
            - mdb.models[*name*].parts[*name*].DatumAxisByRotation

        Parameters
        ----------
        line
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object 
            specifying the line to rotate. 
        axis
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object 
            specifying the axis about which to rotate the line. 
        angle
            A Float specifying the angle in degrees to rotate the line. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    @typing.overload
    def DatumAxisByRotation(self, line: str, point: int, angle: float):
        """This method creates a Feature object and a DatumAxis object in a two-dimensional model
        by rotating a line about the specified point through the specified angle.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumAxisByRotation
            - mdb.models[*name*].parts[*name*].DatumAxisByRotation

        Parameters
        ----------
        line
            A straight Edge, a Datum object representing a datum axis, or an ElementEdge object 
            specifying the line to rotate. 
        point
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point 
            specifying the point about which to rotate the line. 
        angle
            A Float specifying the angle in degrees to rotate the line. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumAxisByRotation(self, *args, **kwargs):
        pass

    def DatumAxisByThreePoint(self, point1: int, point2: int, point3: int):
        """This method creates a Feature object and a DatumAxis object normal to the circle
        described by three points and through its center.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumAxisByThreePoint
            - mdb.models[*name*].parts[*name*].DatumAxisByThreePoint

        Parameters
        ----------
        point1
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point 
            specifying the first point on the circle. 
        point2
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point 
            specifying the second point on the circle. 
        point3
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point 
            specifying the third point on the circle. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumAxisByThruEdge(self, edge: str):
        """This method creates a Feature object and a DatumAxis object along the specified edge.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumAxisByThruEdge
            - mdb.models[*name*].parts[*name*].DatumAxisByThruEdge

        Parameters
        ----------
        edge
            A straight Edge or an ElementEdge object. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumAxisByTwoPlane(self, plane1: str, plane2: str):
        """This method creates a Feature object and a DatumAxis object at the intersection of two
        planes.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumAxisByTwoPlane
            - mdb.models[*name*].parts[*name*].DatumAxisByTwoPlane

        Parameters
        ----------
        plane1
            A planar Face, an ElementFace, or a Datum object representing a datum plane. 
        plane2
            A planar Face, an ElementFace, or a Datum object representing a datum plane. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumAxisByTwoPoint(self, point1: int, point2: int):
        """This method creates a Feature object and a DatumAxis object along the line joining two
        points.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumAxisByTwoPoint
            - mdb.models[*name*].parts[*name*].DatumAxisByTwoPoint

        Parameters
        ----------
        point1
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point. 
        point2
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumCsysByDefault(self, coordSysType: SymbolicConstant, name: str = ''):
        """This method creates a Feature object and a DatumCsys object from the specified default
        coordinate system at the origin.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumCsysByDefault
            - mdb.models[*name*].parts[*name*].DatumCsysByDefault

        Parameters
        ----------
        coordSysType
            A SymbolicConstant specifying the default coordinate system to be used. Possible values 
            are CARTESIAN, CYLINDRICAL, and SPHERICAL. 
        name
            A String specifying the name of the DatumCsys. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumCsysByOffset(self, coordSysType: SymbolicConstant, datumCoordSys: Datum, vector: tuple, point: str, 
                          name: str = ''):
        """This method creates a Feature object and a DatumCsys object by offsetting the origin of
        an existing datum coordinate system to a specified point.

        Path
        ----
            - mdb.models[name].rootAssembly.DatumCsysByOffset
            - mdb.models[name].parts[name].DatumCsysByOffset

        Parameters
        ----------
        coordSysType
            A SymbolicConstant specifying the type of coordinate system. Possible values are 
            CARTESIAN, CYLINDRICAL, and SPHERICAL. 
        datumCoordSys
            A Datum object representing a datum coordinate system from which to offset. 
        vector
            A sequence of three Floats specifying the *X*-, *Y*-, and *Z*-offsets from 
            *datumCoordSys*. The arguments *vector* and *point* are mutually exclusive, and one of 
            them must be specified. 
        point
            A Vertex, InterestingPoint, DatumPoint object or a sequence of three Floats specifying 
            the *X*-, *Y*-, and *Z*-coordinates of a point in space. The point represents the origin 
            of the new datum coordinate system. The arguments *vector* and *point* are mutually 
            exclusive, and one of them must be specified. 
        name
            A String specifying the name of the DatumCsys. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumCsysByThreePoints(self, coordSysType: SymbolicConstant, origin: int, point1: int, point2: int, line1: str, 
                               line2: str, name: str = ''):
        """This method creates a Feature object and a DatumCsys object from three points.

        Path
        ----
            - mdb.models[name].parts[name].DatumCsysByThreePoints
            - mdb.models[name].rootAssembly.DatumCsysByThreePoints

        Parameters
        ----------
        coordSysType
            A SymbolicConstant specifying the type of coordinate system. Possible values are 
            CARTESIAN, CYLINDRICAL, and SPHERICAL. 
        origin
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point 
            specifying the origin of the coordinate system. 
        point1
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point 
            specifying a point on the *X*-axis or the rr-axis. The *point1* and *line1* arguments 
            are mutually exclusive. One of them must be specified. 
        point2
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point 
            specifying a point in the *X–Y* plane or the rr–θθ plane. The *point2* and *line2* 
            arguments are mutually exclusive. One of them must be specified. 
        line1
            An Edge, an Element Edge, or a Datum object representing a datum axis specifying the 
            *X*-axis or the rr-axis. The *point1* and *line1* arguments are mutually exclusive. One 
            of them must be specified. 
        line2
            An Edge, an Element Edge, or a Datum object representing a datum axis specifying a 
            vector in the *X–Y* plane or the rr–θθ plane. The *point2* and *line2* arguments are 
            mutually exclusive. One of them must be specified. 
        name
            A String specifying the name of the DatumCsys. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumCsysByTwoLines(self, coordSysType: SymbolicConstant, line1: str, line2: str, name: str = ''):
        """This method creates a Feature object and a DatumCsys object from two orthogonal lines.
        The origin of the new datum coordinate system is placed at the intersection of the two
        lines.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumCsysByTwoLines
            - mdb.models[*name*].parts[*name*].DatumCsysByTwoLines

        Parameters
        ----------
        coordSysType
            A SymbolicConstant specifying the type of coordinate system. Possible values are 
            CARTESIAN, CYLINDRICAL, and SPHERICAL. 
        line1
            A straight Edge, an ElementEdge, or a Datum object representing a datum axis specifying 
            the *X*-axis or the rr-axis. 
        line2
            A straight Edge, an ElementEdge, or a Datum object representing a datum axis specifying 
            a line in the *X–Y* plane or in the rr–θθ plane. 
        name
            A String specifying the name of the DatumCsys. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumPlaneByPrincipalPlane(self, principalPlane: SymbolicConstant, offset: float):
        """This method creates a Feature object and a DatumPlane object through the origin along
        one of the three principal planes.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumPlaneByPrincipalPlane
            - mdb.models[*name*].parts[*name*].DatumPlaneByPrincipalPlane

        Parameters
        ----------
        principalPlane
            A SymbolicConstant specifying the principal plane. Possible values are XYPLANE, YZPLANE, 
            and XZPLANE. 
        offset
            A Float specifying the offset from the plane. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    @typing.overload
    def DatumPlaneByOffset(self, plane: str, flip: SymbolicConstant, offset: float):
        """This method creates a Feature object and a DatumPlane object offset by a specified
        distance from an existing plane.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumPlaneByOffset
            - mdb.models[*name*].parts[*name*].DatumPlaneByOffset

        Parameters
        ----------
        plane
            A planar Face, an ElementFace, or a Datum object representing a datum plane. 
        flip
            A SymbolicConstant specifying whether the normal should be flipped. Possible values are 
            SIDE1 and SIDE2. 
        offset
            A Float specifying the offset from the plane. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    @typing.overload
    def DatumPlaneByOffset(self, plane: str, point: int):
        """This method creates a Feature object and a DatumPlane object offset from an existing
        plane and passing through the specified point.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumPlaneByOffset
            - mdb.models[*name*].parts[*name*].DatumPlaneByOffset

        Parameters
        ----------
        plane
            A planar Face, an ElementFace, or a Datum object representing a datum plane. 
        point
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumPlaneByOffset(self, *args, **kwargs):
        pass

    def DatumPlaneByRotation(self, plane: str, axis: str, angle: float):
        """This method creates a Feature object and a DatumPlane object by rotating a plane about
        the specified axis through the specified angle.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumPlaneByRotation
            - mdb.models[*name*].parts[*name*].DatumPlaneByRotation

        Parameters
        ----------
        plane
            A planar Face, an ElementFace, or a Datum object representing a datum plane. 
        axis
            A straight Edge, an ElementEdge, or a Datum object representing a datum axis. 
        angle
            A Float specifying the angle in degrees to rotate the plane. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumPlaneByThreePoints(self, point1: int, point2: int, point3: int):
        """This method creates a Feature object and a DatumPlane object defined by passing through
        three points.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumPlaneByThreePoints
            - mdb.models[*name*].parts[*name*].DatumPlaneByThreePoints

        Parameters
        ----------
        point1
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point. 
        point2
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point. 
        point3
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumPlaneByLinePoint(self, line: str, point: int):
        """This method creates a Feature object and a DatumPlane object that pass through the
        specified line and through the specified point that does not lie on the line.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumPlaneByLinePoint
            - mdb.models[*name*].parts[*name*].DatumPlaneByLinePoint

        Parameters
        ----------
        line
            A straight Edge, an ElementEdge, or a Datum object representing a datum axis. 
        point
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumPlaneByPointNormal(self, point: int, normal: str):
        """This method creates a Feature object and a DatumPlane object normal to the specified
        line and running through the specified point.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumPlaneByPointNormal
            - mdb.models[*name*].parts[*name*].DatumPlaneByPointNormal

        Parameters
        ----------
        point
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point. 
        normal
            A straight Edge, an ElementEdge, or a Datum object representing a datum axis. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumPlaneByTwoPoint(self, point1: int, point2: int):
        """This method creates a Feature object and a DatumPlane object midway between two points
        and normal to the line connecting the points.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumPlaneByTwoPoint
            - mdb.models[*name*].parts[*name*].DatumPlaneByTwoPoint

        Parameters
        ----------
        point1
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point. 
        point2
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumPointByCoordinate(self, coords: tuple):
        """This method creates a Feature object and a DatumPoint object at the point defined by the
        specified coordinates.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumPointByCoordinate
            - mdb.models[*name*].parts[*name*].DatumPointByCoordinate

        Parameters
        ----------
        coords
            A sequence of three Floats specifying the *X*-, *Y*-, and *Z*-coordinates of the datum 
            point. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def DatumPointByOffset(self, point: int, vector: tuple):
        """This method creates a Feature object and a DatumPoint object offset from an existing
        point by a vector.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumPointByOffset
            - mdb.models[*name*].parts[*name*].DatumPointByOffset

        Parameters
        ----------
        point
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point. 
        vector
            A sequence of three Floats specifying the *X*-, *Y*-, and *Z*-offsets from *point*. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def DatumPointByMidPoint(self, point1: int, point2: int):
        """This method creates a Feature object and a DatumPoint object midway between two points.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumPointByMidPoint
            - mdb.models[*name*].parts[*name*].DatumPointByMidPoint

        Parameters
        ----------
        point1
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point. 
        point2
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def DatumPointByOnFace(self, face: str, edge1: str, offset1: float, edge2: str, offset2: float):
        """This method creates a Feature object and a DatumPoint object on the specified face,
        offset from two edges.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumPointByOnFace
            - mdb.models[*name*].parts[*name*].DatumPointByOnFace

        Parameters
        ----------
        face
            A planar Face or a Datum object representing a datum plane. 
        edge1
            A straight Edge or a Datum object representing a datum axis. 
        offset1
            A Float specifying the offset from *edge1*. 
        edge2
            A straight Edge or a Datum object representing a datum axis. 
        offset2
            A Float specifying the offset from *edge2*. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumPointByEdgeParam(self, edge: Edge, parameter: float):
        """This method creates a Feature object and a DatumPoint object along an edge at a selected
        distance from one end of the edge.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumPointByEdgeParam
            - mdb.models[*name*].parts[*name*].DatumPointByEdgeParam

        Parameters
        ----------
        edge
            An Edge object. 
        parameter
            A Float specifying the distance along *edge* to the DatumPoint object. Possible values 
            are 0 << *parameter* << 1. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException and RangeError. 
        """
        pass

    def DatumPointByProjOnEdge(self, point: int, edge: str):
        """This method creates a Feature object and a DatumPoint object along an edge by projecting
        an existing point along the normal to the edge.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumPointByProjOnEdge
            - mdb.models[*name*].parts[*name*].DatumPointByProjOnEdge

        Parameters
        ----------
        point
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point. 
        edge
            An Edge, an ElementEdge or a Datum object representing a datum axis. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def DatumPointByProjOnFace(self, point: int, face: Face):
        """This method creates a Feature object and a DatumPoint object on a specified face by
        projecting an existing point onto the face.

        Path
        ----
            - mdb.models[*name*].rootAssembly.DatumPointByProjOnFace
            - mdb.models[*name*].parts[*name*].DatumPointByProjOnFace

        Parameters
        ----------
        point
            A Vertex, an InterestingPoint, a MeshNode, or a Datum object representing a datum point. 
        face
            A Face object or a Datum object representing a datum plane.Note:Any other types of 
            planes are not supported. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def MakeSketchTransform(self, sketchPlane: str, origin: tuple = (), sketchOrientation: SymbolicConstant = RIGHT, 
                            sketchPlaneSide: SymbolicConstant = SIDE1, sketchUpEdge: str = ''):
        """This method creates a Transform object. A Transform object is a 4x3 matrix of Floats
        that represents the transformation from sketch coordinates to part coordinates.

        Path
        ----
            - mdb.models[*name*].parts[*name*].MakeSketchTransform
            - mdb.models[*name*].rootAssembly.MakeSketchTransform

        Parameters
        ----------
        sketchPlane
            A Datum plane object or a planar Face object specifying the sketch plane. 
        origin
            A sequence of Floats specifying the *X*-, *Y*-, and *Z*-coordinates that will be used as 
            the origin of the sketch. The default value is computed as the centroid of the face. 
        sketchOrientation
            A SymbolicConstant specifying the orientation of *sketchUpEdge* on the sketch. Possible 
            values are RIGHT, LEFT, TOP, and BOTTOM. The default value is RIGHT. 
        sketchPlaneSide
            A SymbolicConstant specifying on which side of the *sketchPlane* the sketch is 
            positioned. Possible values are SIDE1 and SIDE2. The default value is SIDE1. 
        sketchUpEdge
            An Edge or DatumAxis object specifying the orientation of the sketch. If unspecified, 
            the sketch is assumed to be oriented with the *Y*-direction pointing up. 

        Returns
        -------
            A Transform object. A Transform is an object with one method that returns the transform 
            matrix. 

        Exceptions
        ----------
            - If the sketchUpEdge is parallel to the sketchPlane: 
              Up direction is parallel to plane normal 
        """
        pass

    def PartitionCellByDatumPlane(self, cells: tuple[Cell], datumPlane: DatumPlane):
        """This method partitions one or more cells using the given datum plane.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionCellByDatumPlane
            - mdb.models[*name*].rootAssembly.PartitionCellByDatumPlane

        Parameters
        ----------
        cells
            A sequence of Cell objects specifying the cells to partition. 
        datumPlane
            A DatumPlane object. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def PartitionCellByExtendFace(self, cells: tuple[Cell], extendFace: str):
        """This method partitions one or more cells by extending the underlying geometry of a given
        face to partition the target cells.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionCellByExtendFace
            - mdb.models[*name*].rootAssembly.PartitionCellByExtendFace

        Parameters
        ----------
        cells
            A sequence of Cell objects specifying the cells to partition. 
        extendFace
            A planar, cylindrical, conical, or spherical Face object. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def PartitionCellByExtrudeEdge(self, cells: tuple[Cell], edges: str, line: str, sense: SymbolicConstant):
        """This method partitions one or more cells by extruding selected edges in the given
        direction.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionCellByExtrudeEdge
            - mdb.models[*name*].rootAssembly.PartitionCellByExtrudeEdge

        Parameters
        ----------
        cells
            A sequence of Cell objects specifying the cells to partition. 
        edges
            The Edge objects to be extruded. The edges must be in the same plane. The edges must 
            form a continuous chain, without branches. The edges must belong to the same 
            PartInstance object. 
        line
            A straight Edge or DatumAxis object specifying the extrude direction. *line* must be 
            perpendicular to the plane formed by *edges*. 
        sense
            A SymbolicConstant specifying the direction of the extrusion. Possible values are 
            FORWARD and REVERSE. If *sense*=FORWARD, the extrusion is in the direction of *line*. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def PartitionCellByPatchNCorners(self, cell: Cell, cornerPoints: tuple):
        """This method partitions a cell using an N-sided cutting patch defined by the given corner
        points.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionCellByPatchNCorners
            - mdb.models[*name*].rootAssembly.PartitionCellByPatchNCorners

        Parameters
        ----------
        cell
            A Cell object specifying the cell to partition. 
        cornerPoints
            A sequence of Vertex, InterestingPoint, or DatumPoint objects. 3 ≤≤ len(*cornerPoints*) 
            ≤≤ 5. The corner points must not coincide. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def PartitionCellByPatchNEdges(self, cell: str, edges: tuple[Edge]):
        """This method partitions a cell using an N-sided cutting patch defined by the given edges.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionCellByPatchNEdges
            - mdb.models[*name*].rootAssembly.PartitionCellByPatchNEdges

        Parameters
        ----------
        cell
            A Cell specifying the cell to partition. 
        edges
            A sequence of Edge objects bounding the patch. The edges must form a closed loop. The 
            Edge objects must belong to the same PartInstance object as *cell*. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def PartitionCellByPlaneNormalToEdge(self, cells: tuple[Cell], edge: Edge, point: int):
        """This method partitions one or more cells using a plane normal to an edge at the given
        edge point.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionCellByPlaneNormalToEdge
            - mdb.models[*name*].rootAssembly.PartitionCellByPlaneNormalToEdge

        Parameters
        ----------
        cells
            A sequence of Cell objects specifying the cells to partition. 
        edge
            An Edge object specifying the normal to the plane. 
        point
            A Vertex, InterestingPoint, or DatumPoint object specifying a point on *edge*. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def PartitionCellByPlanePointNormal(self, cells: tuple[Cell], point: int, normal: str):
        """This method partitions one or more cells using a plane defined by a point and a normal
        direction.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionCellByPlanePointNormal
            - mdb.models[*name*].rootAssembly.PartitionCellByPlanePointNormal

        Parameters
        ----------
        cells
            A sequence of Cell objects specifying the cells to partition. 
        point
            A Vertex, InterestingPoint, or DatumPoint object specifying a point on the plane. 
        normal
            A straight Edge or DatumAxis object specifying the normal to the plane. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def PartitionCellByPlaneThreePoints(self, cells: tuple[Cell], point1: int, point2: int, point3: int):
        """This method partitions one or more cells using a plane defined by three points.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionCellByPlaneThreePoints
            - mdb.models[*name*].rootAssembly.PartitionCellByPlaneThreePoints

        Parameters
        ----------
        cells
            A sequence of Cell objects specifying the cells to partition. 
        point1
            A Vertex, InterestingPoint, or DatumPoint object specifying a point on the plane. 
        point2
            A Vertex, InterestingPoint, or DatumPoint object specifying a point on the plane. 
        point3
            A Vertex, InterestingPoint, or DatumPoint object specifying a point on the 
            plane.Note:*point1*, *point2*, and *point3* must not be colinear and must not coincide. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def PartitionCellBySweepEdge(self, cells: tuple[Cell], edges: tuple[Edge], sweepPath: Edge):
        """This method partitions one or more cells by sweeping selected edges along the given
        sweep path.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionCellBySweepEdge
            - mdb.models[*name*].rootAssembly.PartitionCellBySweepEdge

        Parameters
        ----------
        cells
            A sequence of Cell objects specifying the cells to partition. 
        edges
            A sequence of Edge objects to be swept. The edges must be in the same plane. The edges 
            must form a continuous chain without branches. The Edge objects must all belong to the 
            same PartInstance object. 
        sweepPath
            An Edge object specifying the sweep path. The start of *sweepPath* must be in the plane 
            and perpendicular to the plane formed by *edges*. The sweep path must be planar. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def PartitionEdgeByDatumPlane(self, edges: tuple[Edge], datumPlane: DatumPlane):
        """This method partitions an edge where it intersects with a datum plane.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionEdgeByDatumPlane
            - mdb.models[*name*].rootAssembly.PartitionEdgeByDatumPlane

        Parameters
        ----------
        edges
            A sequence of Edge objects specifying the edges to partition. 
        datumPlane
            A DatumPlane object specifying the location of the partition. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def PartitionEdgeByParam(self, edges: tuple[Edge], parameter: float):
        """This method partitions one or more edges at the given normalized edge parameter.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionEdgeByParam
            - mdb.models[*name*].rootAssembly.PartitionEdgeByParam

        Parameters
        ----------
        edges
            A sequence of Edge objects specifying the edges to partition. 
        parameter
            A Float specifying the normalized distance along *edge* at which to partition. Possible 
            values are 0.0 << *parameter* << 1.0. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def PartitionEdgeByPoint(self, edge: Edge, point: int):
        """This method partitions an edge at the given point.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionEdgeByPoint
            - mdb.models[*name*].rootAssembly.PartitionEdgeByPoint

        Parameters
        ----------
        edge
            An Edge object specifying the edge to partition. 
        point
            An InterestingPoint or DatumPoint object specifying a point on *edge*. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def PartitionFaceByAuto(self, face: Face):
        """This method automatically partitions a target face into simple regions that can be
        meshed using a structured meshing technique.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionFaceByAuto
            - mdb.models[*name*].rootAssembly.PartitionFaceByAuto

        Parameters
        ----------
        face
            A Face object specifying the face to partition. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def PartitionFaceByCurvedPathEdgeParams(self, face: Face, edge1: Edge, parameter1: float, edge2: Edge, parameter2: float):
        """This method partitions a face normal to two edges, using a curved path between the two
        given edge points defined by the normalized edge parameters.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionFaceByCurvedPathEdgeParams
            - mdb.models[*name*].rootAssembly.PartitionFaceByCurvedPathEdgeParams

        Parameters
        ----------
        face
            A Face object specifying the face to partition. 
        edge1
            An Edge object specifying the start of the partition. The edge must belong to *face*. 
        parameter1
            A Float specifying the distance along *edge1* at which to partition. Possible values are 
            0.0 ≤≤ *distance1* ≤≤ 1.0. 
        edge2
            An Edge object specifying the end of the partition. The edge must belong to *face*. 
        parameter2
            A Float specifying the distance along *edge2* at which to partition. Possible values are 
            0.0 ≤≤ *distance2* ≤≤ 1.0. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def PartitionFaceByCurvedPathEdgePoints(self, face: Face, edge1: Edge, point1: int, edge2: Edge, point2: int):
        """This method partitions a face normal to two edges, using a curved path between the two
        given edge points.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionFaceByCurvedPathEdgePoints
            - mdb.models[*name*].rootAssembly.PartitionFaceByCurvedPathEdgePoints

        Parameters
        ----------
        face
            A Face object specifying the face to partition. 
        edge1
            An Edge object specifying the start of the partition. The edge must belong to *face*. 
        point1
            A Vertex, InterestingPoint, or DatumPoint object specifying a point on *edge1*. 
        edge2
            An Edge object specifying the end of the partition. The edge must belong to *face*. 
        point2
            A Vertex, InterestingPoint, or DatumPoint object specifying a point on *edge2*. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def PartitionFaceByDatumPlane(self, faces: tuple[Face], datumPlane: DatumPlane):
        """This method partitions one or more faces using the given datum plane.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionFaceByDatumPlane
            - mdb.models[*name*].rootAssembly.PartitionFaceByDatumPlane

        Parameters
        ----------
        faces
            A sequence of Face objects specifying the faces to partition. 
        datumPlane
            A DatumPlane object specifying the location of the partition. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def PartitionFaceByExtendFace(self, faces: tuple[Face], extendFace: Face):
        """This method partitions one or more faces by extending the underlying geometry of another
        given face to partition the target faces.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionFaceByExtendFace
            - mdb.models[*name*].rootAssembly.PartitionFaceByExtendFace

        Parameters
        ----------
        faces
            A sequence of Face objects specifying the faces to partition. 
        extendFace
            A Face object that is to be extended to create the partition. The face to extend can be 
            a planar, cylindrical, conical, or spherical face. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def PartitionFaceByIntersectFace(self, faces: tuple[Face], cuttingFaces: tuple[Face]):
        """This method partitions one or more faces using the given cutting faces to partition the
        target faces.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionFaceByIntersectFace
            - mdb.models[*name*].rootAssembly.PartitionFaceByIntersectFace

        Parameters
        ----------
        faces
            A sequence of Face objects specifying the faces to partition. 
        cuttingFaces
            A sequence of Face objects that specify the cutting faces. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def PartitionFaceByProjectingEdges(self, faces: tuple[Face], edges: tuple[Edge], extendEdges: Boolean = False):
        """This method partitions one or more faces by projecting the given edges on the target
        faces.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionFaceByProjectingEdges
            - mdb.models[*name*].rootAssembly.PartitionFaceByProjectingEdges

        Parameters
        ----------
        faces
            A sequence of Face objects specifying the faces to partition. 
        edges
            A sequence of Edge objects specifying the edges that will be projected onto the target 
            faces. 
        extendEdges
            A boolean specifying whether to extend the given edges at their free ends in the tangent 
            direction before partitioning the target faces. The default value is False. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def PartitionFaceByShortestPath(self, faces: tuple[Face], point1: int, point2: int):
        """This method partitions one or more faces using a minimum distance path between the two
        given points.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionFaceByShortestPath
            - mdb.models[*name*].rootAssembly.PartitionFaceByShortestPath

        Parameters
        ----------
        faces
            A sequence of Face objects specifying the face to partition. 
        point1
            A Vertex, InterestingPoint, or DatumPoint object. 
        point2
            A Vertex, InterestingPoint, or DatumPoint object.Note:*point1* and *point2* must not 
            coincide, and they must both lie on the underlying surface geometry of at least one of 
            the target faces. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def PartitionFaceBySketch(self, faces: tuple[Face], sketch: ConstrainedSketch, sketchUpEdge: str = '', 
                              sketchOrientation: SymbolicConstant = RIGHT):
        """This method partitions one or more planar faces by sketching on them.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionFaceBySketch
            - mdb.models[*name*].rootAssembly.PartitionFaceBySketch

        Parameters
        ----------
        faces
            A sequence of Face objects specifying the faces to partition. 
        sketch
            A ConstrainedSketch object specifying the partition. 
        sketchUpEdge
            An Edge or DatumAxis object specifying the orientation of *sketch*. This edge or datum 
            axis must not be orthogonal to the plane defined by *faces*. If unspecified, *sketch* is 
            assumed to be oriented in with the *Y* direction pointing up. 
        sketchOrientation
            A SymbolicConstant specifying the orientation of *sketchUpEdge* on the sketch. Possible 
            values are RIGHT, LEFT, TOP, and BOTTOM. The default value is RIGHT. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def PartitionFaceBySketchDistance(self, faces: tuple[Face], sketchPlane: str, sketchPlaneSide: SymbolicConstant, 
                                      sketchUpEdge: Edge, sketch: ConstrainedSketch, distance: float, 
                                      sketchOrientation: SymbolicConstant = RIGHT):
        """This method partitions one or more faces by sketching on a sketch plane and then
        projecting the sketch toward the target faces through the given distance.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionFaceBySketchDistance
            - mdb.models[*name*].rootAssembly.PartitionFaceBySketchDistance

        Parameters
        ----------
        faces
            A sequence of Face objects specifying the faces to partition. 
        sketchPlane
            A planar Face or DatumPlane object. 
        sketchPlaneSide
            A SymbolicConstant specifying the side of the plane to be used for sketching. Possible 
            values are SIDE1 and SIDE2. 
        sketchUpEdge
            An Edge object specifying the orientation of *sketch*. This edge must not be orthogonal 
            to *sketchPlane*. 
        sketch
            A ConstrainedSketch object specifying the partition. 
        distance
            A Float specifying the projection distance. Possible values are *distance* >> 0.0. 
        sketchOrientation
            A SymbolicConstant specifying the orientation of *sketchUpEdge* on the sketch. Possible 
            values are RIGHT, LEFT, TOP, and BOTTOM. The default value is RIGHT. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def PartitionFaceBySketchRefPoint(self, faces: tuple[Face], sketchPlane: str, sketchUpEdge: Edge, sketch: ConstrainedSketch, 
                                      point: int, sketchOrientation: SymbolicConstant = RIGHT):
        """This method partitions one or more faces by sketching on a sketch plane and then
        projecting the sketch toward the target faces through a distance governed by the
        reference point.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionFaceBySketchRefPoint
            - mdb.models[*name*].rootAssembly.PartitionFaceBySketchRefPoint

        Parameters
        ----------
        faces
            A sequence of Face objects specifying the faces to partition. 
        sketchPlane
            A planar Face or DatumPlane object. 
        sketchUpEdge
            An Edge object or a DatumAxis object specifying the orientation of *sketch*. This edge 
            or datum axis must not be orthogonal to *sketchPlane*. 
        sketch
            A ConstrainedSketch object specifying the partition. 
        point
            A Vertex, InterestingPoint, or DatumPoint object specifying the distance to project 
            *sketch*. The point must not lie on *sketchPlane*. 
        sketchOrientation
            A SymbolicConstant specifying the orientation of *sketchUpEdge* on the sketch. Possible 
            values are RIGHT, LEFT, TOP, and BOTTOM. The default value is RIGHT. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def PartitionFaceBySketchThruAll(self, faces: tuple[Face], sketchPlane: str, sketchPlaneSide: SymbolicConstant, 
                                     sketchUpEdge: str, sketch: ConstrainedSketch, 
                                     sketchOrientation: SymbolicConstant = RIGHT):
        """This method partitions one or more faces by sketching on a sketch plane and then
        projecting toward the target faces through an infinite distance.

        Path
        ----
            - mdb.models[*name*].parts[*name*].PartitionFaceBySketchThruAll
            - mdb.models[*name*].rootAssembly.PartitionFaceBySketchThruAll

        Parameters
        ----------
        faces
            A sequence of Face objects specifying the faces to partition. 
        sketchPlane
            A planar Face or DatumPlane object. 
        sketchPlaneSide
            A SymbolicConstant specifying the extrude direction of the sketch. Possible values are 
            SIDE1 and SIDE2. 
        sketchUpEdge
            An Edge or a DatumAxis object specifying the orientation of *sketch*. This edge or datum 
            axis must not be orthogonal to *sketchPlane*. 
        sketch
            A ConstrainedSketch object specifying the partition. 
        sketchOrientation
            A SymbolicConstant specifying the orientation of *sketchUpEdge* on the sketch. Possible 
            values are RIGHT, LEFT, TOP, and BOTTOM. The default value is RIGHT. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def ReferencePoint(self, point: str, instanceName: str = ''):
        """This method creates a Feature object and a ReferencePoint object at the specified
        location.

        Path
        ----
            - mdb.models[*name*].rootAssembly.ReferencePoint
            - mdb.models[*name*].parts[name].ReferencePoint

        Parameters
        ----------
        point
            A Vertex, InterestingPoint, a MeshNode, or a Datum object specifying a reference point. 
            *point* can also be a sequence of three Floats representing the *X*-, *Y*-, and 
            *Z*-coordinates of the point. 
        instanceName
            Used internally by the input file writer. 

        Returns
        -------
            A Feature Object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def RemoveWireEdges(self, wireEdgeList: tuple[Edge]):
        """This method removes wire edges.

        Path
        ----
            - mdb.models[*name*].parts[*name*].RemoveWireEdges
            - mdb.models[*name*].rootAssembly.RemoveWireEdges

        Parameters
        ----------
        wireEdgeList
            A sequence of Edge objects specifying the edges to remove. Any specified edge that is 
            not a wire edge will not be removed. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def WirePolyLine(self, points: float, mergeType: SymbolicConstant = IMPRINT, meshable: Boolean = ON):
        """This method creates an additional Feature object by creating a series of wires joining
        points in pairs. When such a feature is created at the Part level, then each point can
        be either a datum point, a vertex, a reference point, an interesting point, an orphan
        mesh node, or the coordinates of a point. When such a feature is created at the Assembly
        level, then each point can only be a vertex, a reference point, or an orphan mesh node.

        Path
        ----
            - mdb.models[*name*].parts[*name*].WirePolyLine
            - mdb.models[*name*].rootAssembly.WirePolyLine

        Parameters
        ----------
        points
            A tuple of point pairs, each pair being itself represented by a tuple. For part level 
            features each point can be a Vertex, Datum point, Reference point, orphan mesh Node, or 
            InterestingPoint object specifying the points through which the polyline wire will pass. 
            Each point can also be a tuple of Floats representing the coordinates of a point. For 
            assembly level features each point can only be a Vertex, Reference point, or orphan mesh 
            Node specifying the points through which the polyline wire will pass (coordinates cannot 
            be specified). In any of the pairs, the first or second point can be NONE. In that case, 
            the point pair will create a zero-length wire, which is required for certain types of 
            connectors. You must specify at least one pair. 
        mergeType
            A SymbolicConstant specifying the merge behavior of the wire with existing geometry. If 
            *mergeType* is MERGE, Abaqus merges the wire into solid regions of the part if the wire 
            passes through them. If *mergeType* is IMPRINT, Abaqus imprints the wire on existing 
            geometry as edges. If *mergeType* is SEPARATE, Abaqus neither merges nor imprints the 
            spline wire with existing geometry. It creates the wire separately. The default value is 
            IMPRINT. 
        meshable
            A Boolean specifying whether the wire should be available for selection for meshing 
            operations. If *meshable*=OFF, the wire can be used for connector section assignment. 
            The default value is ON. 

        Returns
        -------
            A Feature object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def isSuppressed(self):
        """This method queries the suppressed state of the feature.

        Parameters
        ----------

        Returns
        -------
            A Boolean value of True if the feature is suppressed and False if it is not suppressed. 

        Exceptions
        ----------
            None. 
        """
        pass

    def restore(self):
        """This method restores the parameters of a feature to the value they had when the backup
        method was invoked on the part or assembly. Use the restore method after the backup
        method.

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

    def resume(self):
        """This method resumes suppressed features. Resuming a feature fully restores it to the
        part or assembly. You can resume the last feature you suppressed, all suppressed
        features, or just selected features. When you resume a child feature, Abaqus/CAE also
        resumes the parent features automatically.

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

    def setValues(self, parameter: float = None, parameter1: float = None, parameter2: float = None, 
                  sketch: ConstrainedSketch = None, distance: float = None):
        """This method modifies the Feature object.

        Parameters
        ----------
        parameter
            A Float specifying the normalized distance along *edge* at which to partition. Possible 
            values are 0.0 << *parameter* << 1.0. You use this argument to modify a partition 
            created with the created with the PartitionEdgeByParam method. 
        parameter1
            A Float specifying the distance along *edge1* at which to partition. Possible values are 
            0.0 ≤≤ *parameter1* ≤≤ 1.0. You use this argument to modify a partition object created 
            with the PartitionFaceByCurvedPathEdgeParam method. 
        parameter2
            A Float specifying the distance along *edge2* at which to partition. Possible values are 
            0.0 ≤≤ *parameter2* ≤≤ 1.0. You use this argument to modify a partition object created 
            with the PartitionFaceByCurvedPathEdgeParam method. 
        sketch
            A ConstrainedSketch object specifying the partition. You use this argument to modify a 
            partition object created with a sketch; for example, using the PartitionFaceBySketch 
            method. 
        distance
            A Float specifying the projection *distance*. Possible values are *distance* >> 0.0. You 
            use this argument to modify a partition object created with the 
            PartitionFaceBySketchDistance method. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def suppress(self):
        """This method suppresses features. Suppressing a feature is equivalent to temporarily
        removing the feature from the part or assembly. Suppressed features remain suppressed
        when you regenerate a part or assembly. You cannot suppress the base feature. In
        addition, if you suppress a parent feature, all of its child features are also
        suppressed automatically. Suppressed features can be restored with the resume command.

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
