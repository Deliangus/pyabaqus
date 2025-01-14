import typing

from abaqusConstants import *
from .Path import Path
from .Spectrum import Spectrum
from .Stream import Stream
from ..Session.SessionBase import SessionBase


class PathSession(SessionBase):

    def Path(self, name: str, type: SymbolicConstant, expression: tuple,
             circleDefinition: SymbolicConstant, numSegments: int, startAngle: float,
             endAngle: float, radius: typing.Union[SymbolicConstant, float], radialAngle: float,
             startRadius: typing.Union[SymbolicConstant, float],
             endRadius: typing.Union[SymbolicConstant, float]) -> Path:
        """This method creates a Path object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                session.Path
        
        Parameters
        ----------
        name
            A String specifying the repository key.
        type
            A SymbolicConstant specifying the type of path being created. Possible values are
            NODE_LIST, POINT_LIST, EDGE_LIST, CIRCUMFERENTIAL, and RADIAL.
        expression
            A sequence specifying the nodes or points that make up the path. The definition of the
            path expression depends on the *type* argument.
            - If *type*=NODE_LIST, *expression* must be a sequence of sequences. Each inner sequence
            contains two items, the first item is a String specifying the name of a part instance,
            and the second item can be either a sequence of Ints or a sequence of Strings, each
            specifying a range of Ints.
            - If *type*=POINT_LIST, *expression* must be a sequence of tuples of three Floats,
            specifying the coordinates of each point.
            - If *type*=EDGE_LIST, *expression* must be a sequence of sequences. Each inner sequence
            contains two items, the first item is a String specifying the name of the part instance,
            and the second item is a sequence of tuples of four Ints that uniquely identify an
            element edge. The four Ints are:
            1. The element label.
            2. The element face index (one-based).
            3. The face edge index (one-based).
            4. The edge direction. A positive number specifies that the edge direction runs from the
            edge start node to the edge end node. A negative number specifies the opposite.
            - When *type*=CIRCUMFERENTIAL or RADIAL, *expression* must be a sequence of three tuples
            of three Floats, specifying the coordinates of the points used to define a coordinate
            system.
        circleDefinition
            A SymbolicConstant specifying the method in which the circle is being defined. This
            argument is valid only when *type*=CIRCUMFERENTIAL or RADIAL. Possible values are
            ORIGIN_AXIS and POINT_ARC.When the value is ORIGIN_AXIS, the first two points in
            *expression* are points on the rotational axis and the third point lies on the x-axis.
            When the value is POINT_ARC, the three points in *expression* are points lying on the
            arc of the circle.
        numSegments
            An Int specifying the number of equal segments in the path. This argument is valid only
            when *type*=CIRCUMFERENTIAL or RADIAL.
        startAngle
            A Float specifying the start angle of the circumferential path. This argument is valid
            only when *type*=CIRCUMFERENTIAL.
        endAngle
            A Float specifying the end angle of the circumferential path. This argument is valid
            only when *type*=CIRCUMFERENTIAL.
        radius
            The SymbolicConstant CIRCLE_RADIUS or a Float specifying the radius of the
            circumferential path. This argument is valid only when *type*=CIRCUMFERENTIAL.
        radialAngle
            A Float specifying the angle between the radial path and the *X*-axis of the specified
            coordinate system. This argument is valid only when *type*=RADIAL.
        startRadius
            The SymbolicConstant CIRCLE_RADIUS or a Float specifying the start radius of the radial
            path. This argument is valid only when *type*=RADIAL.
        endRadius
            The SymbolicConstant CIRCLE_RADIUS or a Float specifying the end radius of the radial
            path. This argument is valid only when *type*=RADIAL.

        Returns
        -------
            A Path object.

        Raises
        ------
            ModelError, ErrorUnsupportedNodeData, ErrorUnsupportedPointData, ErrorIncorrectPathData,
            KeyError, ErrorEmptyPathName, ErrorPathNotFound, and ErrorNoOdbPathDisplay.
            ValueError: When *type*=CIRCUMFERENTIAL or RADIAL, the three points specified in
            *expression* are collinear.
        """
        self.paths[name] = path = Path(name, type, expression, circleDefinition, numSegments, startAngle, endAngle,
                                       radius, radialAngle, startRadius, endRadius)
        return path

    def Spectrum(self, name: str, colors: tuple) -> Spectrum:
        """This method creates a Spectrum object and places it in the spectrums repository.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                session.Spectrum
        
        Parameters
        ----------
        name
            A string name for the spectrum.
        colors
            A sequence of strings indicating the colors of the spectrum.

        Returns
        -------
            A Spectrum object.
        """
        self.spectrums[name] = spectrum = Spectrum(name, colors)
        return spectrum

    def Stream(self, name: str, numPointsOnRake: str, pointA: tuple = (), pointB: tuple = (), path: str = '') -> Stream:
        """This method creates aStream object and places it in the streams repository.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                session.Stream
        
        Parameters
        ----------
        name
            A string name for the stream.
        numPointsOnRake
            An integer specifying the number of points along the rake.
        pointA
            A tuple of 3 floats specifying the starting point of the rake. Alternatively, a string
            representation of the node selected in the viewport.
        pointB
            A tuple of 3 floats specifying the end point of the rake. Alternatively, a string
            representation of the node selected in the viewport.
        path
            APath object that specifies the rake.

        Returns
        -------
            A Stream object.
        """
        self.streams[name] = stream = Stream(name, numPointsOnRake, pointA, pointB, path)
        return stream
