from abaqusConstants import *


class View:
    """The Session and Viewport View objects store view settings for custom (both predefined
    and user-defined) views. The paradigm used to define a view is based on a camera 
    analogy. Similar to taking a photograph with a camera, features such as camera position, 
    view direction, orientation, depth of field, and projection are specified to transform 
    three-dimensional views to the screen. 
    The Layer View objects store a transformation matrix used to position the contents of 
    the Layer within a viewport. 

    Attributes
    ----------
    displayedObjectScreenWidth: float
        A Float specifying the width in viewport millimeters of the bounding rectangle around
        the viewport contents. This value does not include annotations or symbols and it is not
        clipped to the size of the viewport window.
    displayedObjectScreenHeight: float
        A Float specifying the height in viewport millimeters of the bounding rectangle around
        the viewport contents. This value does not include annotations or symbols and it is not
        clipped to the size of the viewport window.
    layerTransform: float
        A tuple of Floats specifying a transformation matrix used to position the contents of
        the Layer within a viewport.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        session.viewports[name].layers[name].view
        session.viewports[name].view
        session.views[name]

    """

    # A Float specifying the width in viewport millimeters of the bounding rectangle around 
    # the viewport contents. This value does not include annotations or symbols and it is not 
    # clipped to the size of the viewport window. 
    displayedObjectScreenWidth: float = None

    # A Float specifying the height in viewport millimeters of the bounding rectangle around 
    # the viewport contents. This value does not include annotations or symbols and it is not 
    # clipped to the size of the viewport window. 
    displayedObjectScreenHeight: float = None

    # A tuple of Floats specifying a transformation matrix used to position the contents of 
    # the Layer within a viewport. 
    layerTransform: float = None

    def __init__(self, name: str, nearPlane: float, farPlane: float, width: float, height: float,
                 projection: SymbolicConstant, cameraPosition: tuple, cameraUpVector: tuple,
                 cameraTarget: tuple, viewOffsetX: float, viewOffsetY: float, autoFit: Boolean,
                 movieMode: Boolean = OFF):
        """This method creates a View object.
        Note:All dimensions and coordinates are specified in the model coordinate system.
        Note:This method cannot be used to create a View for a Layer object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.View
        
        Parameters
        ----------
        name
            A String specifying the name of the view (also used as the repository key). Possible 
            values are 'Front', 'Back', 'Top', 'Bottom', 'Left', `Right', 'Iso', 'User-1', 'User-2', 
            'User-3', and 'User-4'. The object member associated with this argument is a 
            SymbolicConstant. Possible values of the *name* member are:FRONT, BACK, TOP, BOTTOM, 
            LEFT, RIGHT, ISO, USER1, USER2, USER3, and USER4. 
        nearPlane
            A Float specifying the distance from the camera to the near clipping plane. Possible 
            values are *nearPlane* >> 0.0. 
        farPlane
            A Float specifying the distance from the camera to the far clipping plane when 
            *farPlaneMode* =SPECIFY. Possible values are *farPlane* >> *nearPlane*. 
        width
            A Float specifying the width of the front clipping plane. Possible values are *width* >> 
            0.0. 
        height
            A Float specifying the height of the front clipping plane. Possible values are *height* 
            >> 0.0. 
        projection
            A SymbolicConstant specifying the projection mode. Possible values are PERSPECTIVE and 
            PARALLEL. 
        cameraPosition
            A sequence of three Floats specifying the camera position. 
        cameraUpVector
            A sequence of three Floats specifying the camera's up vector (the screen's positive 
            *Y*-axis). The initial value is (0, 0, 0). 
        cameraTarget
            A sequence of three Floats specifying the center of the scene. 
        viewOffsetX
            A Float specifying the amount to pan the model in the screen *X*-direction as a fraction 
            of the viewport width. A positive value pans the model to the right. A negative value 
            pans the model to the left.The*viewOffsetX* and *viewOffsetY* arguments allow you to pan 
            the view without changing the position of the camera or the target (*cameraPosition* and 
            *cameraTarget* arguments to the View method). The resulting change in the view allows 
            you to pan a perspective display without producing an apparent rotation of the model. 
        viewOffsetY
            A Float specifying the amount to pan the model in the screen *Y*-direction as a fraction 
            of the viewport height. A positive value pans the model upward. A negative value pans 
            the model downward. 
        autoFit
            A Boolean specifying whether the view is auto-fit when applied. 
        movieMode
            A Boolean specifying whether or not the camera is in movie mode. The default value is 
            OFF. 

        Returns
        -------
            A View object. 

        Raises
        ------
        RangeError
        """
        pass

    def fitView(self, drawImmediately: Boolean = False):
        """This method scales the displayable object (such as a part, the assembly, or an *X–Y*
        plot) to fit the viewport.
        
        Parameters
        ----------
        drawImmediately
            A Boolean specifying the viewport should refresh immediately after the command is 
            processed. This is typically only used when writing a script and it is desirable to show 
            intermediate results before the script completes. The default value is False. 
        """
        pass

    def next(self, drawImmediately: Boolean = False):
        """This method restores the view in the viewport to the next view setting in the list.
        (There is a list of eight views stored for each viewport.) If there is no next view, no
        action is taken.
        Note:This method is not available for a Layer View.
        
        Parameters
        ----------
        drawImmediately
            A Boolean specifying the viewport should refresh immediately after the command is 
            processed. This is typically only used when writing a script and it is desirable to show 
            intermediate results before the script completes. The default value is False. 
        """
        pass

    def pan(self, xFraction: float = 0, yFraction: float = 0, asMovie: Boolean = OFF,
            drawImmediately: Boolean = False):
        """This method pans the view in the viewport using absolute, not relative, mode.
        
        Parameters
        ----------
        xFraction
            A Float specifying the amount to pan the model in the screen *X*-direction as a fraction 
            of the viewport width. A positive value pans the model to the right. A negative value 
            pans the model to the left. The default value is 0.0. 
        yFraction
            A Float specifying the amount to pan the model in the screen *Y*-direction as a fraction 
            of the viewport height. A positive value pans the model upward. A negative value pans 
            the model downward. The default value is 0.0. 
        asMovie
            A Boolean specifying the alternate mode of the pan view manipulation should be used. The 
            default value is OFF. This argument is ignored for a Layer View. 
        drawImmediately
            A Boolean specifying the viewport should refresh immediately after the command is 
            processed. This argument is typically used only when writing a script and it is 
            desirable to show intermediate results before the script completes. The default value is 
            False. 
        """
        pass

    def previous(self, drawImmediately: Boolean = False):
        """This method restores the view in the viewport to the previous view setting in the list.
        (There is a list of eight views stored for each viewport.) If there is no previous view,
        no action is taken.
        Note:This method is not available for a Layer View.
        
        Parameters
        ----------
        drawImmediately
            A Boolean specifying the viewport should refresh immediately after the command is 
            processed. This argument is typically used only when writing a script and it is 
            desirable to show intermediate results before the script completes. The default value is 
            False. 
        """
        pass

    def rotate(self, xAngle: float = 0, yAngle: float = 0, zAngle: float = 0, mode: SymbolicConstant = MODEL,
               asMovie: Boolean = OFF, drawImmediately: Boolean = False):
        """This method rotates the view in the viewport. If a center of rotation has been
        previously specified and *asMovie* is OFF then this method will honor that rotation
        center.
        
        Parameters
        ----------
        xAngle
            A Float specifying the degrees to rotate about the *X*-axis. The default value is 0.0. 
        yAngle
            A Float specifying the degrees to rotate about the *Y*-axis. The default value is 0.0. 
        zAngle
            A Float specifying the degrees to rotate about the*Z*-axis. The default value is 0.0. 
        mode
            A SymbolicConstant specifying the rotation mode. Possible values are:TOTAL : Set the 
            view to (0, 0, 1), then rotate about the screen's axes (an absolute rotation).SCREEN : 
            Rotate incrementally about the screen's axes (a relative rotation).MODEL : Rotate 
            incrementally about the model's axes (a relative rotation).The default value is MODEL. 
        asMovie
            A Boolean specifying the alternate mode of the rotate view manipulation should be used. 
            The default value is OFF. 
        drawImmediately
            A Boolean specifying the viewport should refresh immediately after the command is 
            processed. This argument is typically used only when writing a script and it is 
            desirable to show intermediate results before the script completes. The default value is 
            False. 
        """
        pass

    def setLayerTransform(self, layerTransform: tuple = (), options: 'View' = None, drawImmediately: Boolean = False):
        """This method modifies the transformation used to position a Layer.
        Note:This method is not available for Session and Viewport Views.
        
        Parameters
        ----------
        layerTransform
            A sequence of 16 Floats specifying the transformation matrix. 
        options
            A View object from which the view settings are to be copied. If the *layerTransform* 
            argument is also supplied to setLayerTransform, it will override the values in the View 
            object specified by *view*. 
        drawImmediately
            A Boolean specifying the viewport should refresh immediately after the command is 
            processed. This argument is typically used only when writing a script and it is 
            desirable to show intermediate results before the script completes. The default value is 
            False. 
        """
        pass

    def setProjection(self, projection: SymbolicConstant, drawImmediately: Boolean = False):
        """This method modifies the appearance of three-dimensional models in the viewport.
        Choosing PERSPECTIVE makes a model appear more realistic by decreasing the apparent size
        of features that are farther away from the viewing point.
        Note:This method is not available for a Layer View.
        
        Parameters
        ----------
        projection
            A SymbolicConstant specifying the projection mode. Possible values are PERSPECTIVE and 
            PARALLEL. 
        drawImmediately
            A Boolean specifying the viewport should refresh immediately after the command is 
            processed. This argument is typically used only when writing a script and it is 
            desirable to show intermediate results before the script completes. The default value is 
            False.

        Raises
        ------
        RangeError
        """
        pass

    def setRotationCenter(self, rotationCenter: tuple):
        """This method sets the center of rotation to the specified location.
        
        Parameters
        ----------
        rotationCenter
            A sequence of a String and an Int specifying a part instance name and a node label or a 
            sequence of 3 Floats specifying a point.

        Raises
        ------
            TypeError: rotationCenter cannot be set using a part instance and node label unless the 
            displayed object is an ODB 
        """
        pass

    def setValues(self, movieMode: Boolean = OFF):
        """This method modifies the View object.
        Note:This method is not available for a Layer View.
        
        Parameters
        ----------
        movieMode
            A Boolean specifying whether or not the camera is in movie mode. The default value is 
            OFF.

        Raises
        ------
        RangeError
        """
        pass

    def setViewpoint(self, viewVector: tuple, cameraUpVector: tuple = (), drawImmediately: Boolean = False):
        """This method sets the camera's position in the viewport.
        Note:This method is not available for a Layer View.
        
        Parameters
        ----------
        viewVector
            A sequence of three Floats specifying the viewing vector (from the camera to the origin 
            of the model). 
        cameraUpVector
            A sequence of three Floats specifying the camera's up vector (the screen's positive 
            *Y*-axis). The initial value is (0, 0, 0). 
        drawImmediately
            A Boolean specifying the viewport should refresh immediately after the command is 
            processed. This argument is typically used only when writing a script and it is 
            desirable to show intermediate results before the script completes. The default value is 
            False. 
        """
        pass

    def zoom(self, zoomFactor: float, mode: SymbolicConstant = ABSOLUTE, asMovie: Boolean = OFF,
             drawImmediately: Boolean = False):
        """This method magnifies the view in the viewport.
        
        Parameters
        ----------
        zoomFactor
            A Float specifying the amount to zoom. Possible values are 0.000001 ≤≤ *zoomFactor* ≤≤ 
            1000000. A *zoomFactor* less than one reduces the image. A *zoomFactor* greater than one 
            enlarges the image. 
        mode
            A SymbolicConstant specifying the way the zoom is executed. Possible values are:ABSOLUTE 
            : Execute fitView, then zoom.RELATIVE : Zoom from the current camera settings.The 
            default value is ABSOLUTE. 
        asMovie
            A Boolean specifying the alternate mode of the zoom view manipulation should be used. 
            The default value is OFF. This argument is ignored for a Layer View. 
        drawImmediately
            A Boolean specifying the viewport should refresh immediately after the command is 
            processed. This argument is typically used only when writing a script and it is 
            desirable to show intermediate results before the script completes. The default value is 
            False.

        Raises
        ------
        RangeError
        """
        pass

    def zoomRectangle(self, point1: tuple[float], point2: tuple[float], drawImmediately: Boolean = False):
        """This method fills the viewport with the graphics located within the given rectangle.
        
        Parameters
        ----------
        point1
            A pair of Floats specifying the*X*- and *Y*-coordinates of one corner of the rectangle 
            in fractions of the viewport width and height. 
        point2
            A pair of Floats specifying the*X*- and *Y*-coordinates of the other corner of the 
            rectangle in fractions of the viewport width and height. 
        drawImmediately
            A Boolean specifying the viewport should refresh immediately after the command is 
            processed. This argument is typically used only when writing a script and it is 
            desirable to show intermediate results before the script completes. The default value is 
            False. 
        """
        pass
