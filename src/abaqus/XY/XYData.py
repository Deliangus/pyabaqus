import typing

from abaqusConstants import *
from .QuantityType import QuantityType
from ..PathAndProbe.Path import Path


# prevent circular imports
class Odb:
    pass


class XYData:
    """The XYData object is used to store values and attributes associated with XYData type
    objects. 
    XYData objects can be created using the methods described below. The methods accessed 
    via the Session object cause the XYData object to be added to the session.xyData 
    repository. 
    Temporary XYData objects will be created if no name is supplied. Temporary XYData 
    objects will be added to the session.xyData repository but automatically deleted when 
    they are not used anymore. Temporary XYData objects are also created as a result of math 
    operations found in the abaqusMath module. 

    Attributes
    ----------
    sourceType: SymbolicConstant
        A SymbolicConstant specifying the source type of the :py:class:`~abaqus.XY.XYData.XYData` object. Possible values are
        FROM_ODB, FROM_KEYBOARD, FROM_ASCII_FILE, FROM_OPERATION, and FROM_USER_DEFINED.
    fileName: str
        A String specifying the source file name of the :py:class:`~abaqus.XY.XYData.XYData` object.
    description: str
        A String specifying the complete description of the :py:class:`~abaqus.XY.XYData.XYData` object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import visualization
        session.charts[name].axes1[i].axisData.curves[i].data
        session.charts[name].axes2[i].axisData.curves[i].data
        session.charts[name].curves[name].data
        session.curves[name].data
        session.defaultChartOptions.defaultAxis1Options.axisData.curves[i].data
        session.defaultChartOptions.defaultAxis2Options.axisData.curves[i].data
        import odbAccess
        session.odbs[name].userData.xyDataObjects[name]
        session.xyDataObjects[name]
        session.xyPlots[name].charts[name].axes1[i].axisData.curves[i].data
        session.xyPlots[name].charts[name].axes2[i].axisData.curves[i].data
        session.xyPlots[name].charts[name].curves[name].data
        session.xyPlots[name].curves[name].data

    """

    # A SymbolicConstant specifying the source type of the XYData object. Possible values are 
    # FROM_ODB, FROM_KEYBOARD, FROM_ASCII_FILE, FROM_OPERATION, and FROM_USER_DEFINED. 
    sourceType: SymbolicConstant = None

    # A String specifying the source file name of the XYData object. 
    fileName: str = ''

    # A String specifying the complete description of the XYData object. 
    description: str = ''

    @typing.overload
    def __init__(self, data: tuple, name: str = '', sourceDescription: str = '', contentDescription: str = '',
                 positionDescription: str = '', legendLabel: str = '', xValuesLabel: str = '',
                 yValuesLabel: str = '', axis1QuantityType: QuantityType = QuantityType(),
                 axis2QuantityType: QuantityType = QuantityType()):
        """This method creates an XYData object from a sequence of *X–Y* data pairs.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.XYData
            xyPlot.XYData
        
        Parameters
        ----------
        data
            A sequence of pairs of Floats specifying the *X–Y* data pairs. 
        name
            The repository key. If the name is not supplied while creating the XYData object using 
            xyPlot.XYData, a default name in the form _temp#_ is generated and the XYData object is 
            temporary. (This argument is required if the method is accessed from the session 
            object.) 
        sourceDescription
            A String specifying the source of the *X–Y* data (e.g., “Entered from keyboard”, “Taken 
            from ASCII file”, “Read from an ODB”, etc.). The default value is an empty string. 
        contentDescription
            A String specifying the content of the *X–Y* data (e.g., “field 1 vs. field 2”). The 
            default value is an empty string. 
        positionDescription
            A String specifying additional information about the *X–Y* data (e.g., “for whole 
            model”). The default value is an empty string. 
        legendLabel
            A String specifying the label to be used in the legend. The default value is the name of 
            the XYData object. 
        xValuesLabel
            A String specifying the label for the X-values. This value may be overridden if the 
            *X–Y* data are combined with other *X–Y* data. The default value is an empty string. 
        yValuesLabel
            A String specifying the label for the Y-values. This value may be overridden if the 
            *X–Y* data are combined with other *X–Y* data. The default value is an empty string. 
        axis1QuantityType
            A QuantityType object specifying the QuantityType object associated to the X -axis1- 
            values. 
        axis2QuantityType
            A QuantityType object specifying the QuantityType object associated to the Y -axis2- 
            values. 

        Returns
        -------
            An XYData object.
        """
        pass

    @typing.overload
    def __init__(self, objectToCopy: 'XYData'):
        """This method creates an XYData object by copying an existing XYData object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.XYData
            xyPlot.XYData
        
        Parameters
        ----------
        objectToCopy
            An XYData object to be copied. 

        Returns
        -------
            An XYData object.
        """
        pass

    def __init__(self, *args, **kwargs):
        pass

    def XYDataFromFile(self, fileName: str, name: str = '', sourceDescription: str = '',
                       contentDescription: str = '', positionDescription: str = '', legendLabel: str = '',
                       xValuesLabel: str = '', yValuesLabel: str = '',
                       axis1QuantityType: QuantityType = QuantityType(),
                       axis2QuantityType: QuantityType = QuantityType(), xField: int = 1, yField: int = 2,
                       skipFrequency: int = None):
        """This method creates an XYData object from data in an ASCII file.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.XYData
            xyPlot.XYData
        
        Parameters
        ----------
        fileName
            A String specifying the name of the file from which the *X–Y* data will be read. 
        name
            The repository key. If the name is not supplied, a default name in the form _temp#_ is 
            generated and the XYData object is temporary. 
        sourceDescription
            A String specifying the source of the *X–Y* data (e.g., “Entered from keyboard”, “Taken 
            from ASCII file”, “Read from an ODB”, etc.). The default value is an empty string. 
        contentDescription
            A String specifying the content of the *X–Y* data (e.g., “field 1 vs. field 2”). The 
            default value is an empty string. 
        positionDescription
            A String specifying additional information about the *X–Y* data (e.g., “for whole 
            model”). The default value is an empty string. 
        legendLabel
            A String specifying the label to be used in the legend. The default value is the name of 
            the XYData object. 
        xValuesLabel
            A String specifying the label for the X-values. This value may be overridden if the 
            *X–Y* data are combined with other *X–Y* data. The default value is an empty string. 
        yValuesLabel
            A String specifying the label for the Y-values. This value may be overridden if the 
            *X–Y* data are combined with other *X–Y* data. The default value is an empty string. 
        axis1QuantityType
            A QuantityType object specifying the QuantityType object associated to the X -axis1- 
            values. 
        axis2QuantityType
            A QuantityType object specifying the QuantityType object associated to the Y -axis2- 
            values. 
        xField
            An Int specifying the field from which the *X*-data will be read. Fields are delimited 
            by spaces, tabs, or commas. The default value is 1. 
        yField
            An Int specifying the field from which the *Y*-data will be read. Fields are delimited 
            by spaces, tabs, or commas. The default value is 2. 
        skipFrequency
            An Int specifying how often data rows will be skipped. A *skipFrequency* of 1 means skip 
            every other row. The first row is always read. Possible values are *skipFrequency* ≥≥ 0. 
            The default value is 0 (data are read from every row). 

        Returns
        -------
            An XYData object. 
            
        Raises
        ------
        InvalidNameError
        RangeError 
        """
        pass

    def XYDataFromHistory(self, odb: Odb, outputVariableName: str, steps: tuple, name: str = '',
                          sourceDescription: str = '', contentDescription: str = '',
                          positionDescription: str = '', legendLabel: str = '', skipFrequency: int = None,
                          numericForm: SymbolicConstant = REAL, complexAngle: float = 0, stepTuple: int = None):
        """This method creates an XYData object by reading history data from an Odb object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.XYData
            xyPlot.XYData
        
        Parameters
        ----------
        odb
            An Odb object specifying the output database from which data will be read. 
        outputVariableName
            A String specifying the output variable from which the *X–Y* data will be read. 
        steps
            A sequence of Strings specifying the names of the steps from which data will be 
            extracted. 
        name
            The repository key. If the name is not supplied, a default name in the form _temp#_ is 
            generated and the XYData object is temporary (this argument is required if the method is 
            accessed from the session object). 
        sourceDescription
            A String specifying the source of the *X–Y* data (for example, “Entered from keyboard”, 
            “Taken from ASCII file”, “Read from an ODB”, etc.). The default value is an empty 
            string. 
        contentDescription
            A String specifying the content of the *X–Y* data (for example, “field 1 vs. field 2”). 
            The default value is an empty string. 
        positionDescription
            A String specifying additional information about the *X–Y* data (for example, “for whole 
            model”). The default value is an empty string. 
        legendLabel
            A String specifying the label to be used in the legend. The default value is the name of 
            the XYData object. 
        skipFrequency
            An Int specifying how often data frames will be skipped. If *skipFrequency*=1, Abaqus 
            will skip every other frame. The first frame is always read. Possible values are 
            *skipFrequency* ≥≥ 0. The default value is 0 (data are read from every frame). 
        numericForm
            A SymbolicConstant specifying the numeric form in which to display results that contain 
            complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL, IMAGINARY, 
            and COMPLEX_VAL_AT_ANGLE. The default value is REAL. 
        complexAngle
            A Float specifying the angle (in degrees) at which to display results that contain 
            complex numbers when *numericForm*=COMPLEX_VAL_AT_ANGLE. The default value is 0. 
        stepTuple
            A tuple of Integers specifying the steps to include when extracting data. 

        Returns
        -------
            An XYData object. 
            
        Raises
        ------
        InvalidNameError
        RangeError 
        """
        pass

    def xyDataListFromField(self, odb: Odb, outputPosition: SymbolicConstant, variable: tuple[tuple],
                            elementSets: tuple = (), elementLabels: tuple = (), nodeSets: tuple = (),
                            nodeLabels: tuple = (), numericForm: SymbolicConstant = REAL, complexAngle: float = 0,
                            operator: SymbolicConstant = None) -> list['XYData']:
        """This method creates a list of XYData objects by reading field data from an Odb object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.XYData
            xyPlot.XYData
        
        Parameters
        ----------
        odb
            An Odb object specifying the output database from which data will be read. 
        outputPosition
            A SymbolicConstant specifying the position from which output will be read. Possible 
            values are ELEMENT_CENTROID, ELEMENT_NODAL, INTEGRATION_POINT, and NODAL. 
        variable
            A tuple of tuples containing the descriptions of variables for which to extract data 
            from the field. Each tuple specifies the following:Variable label: A String specifying 
            the variable; for example, 'U'.Variable output position: A SymbolicConstant specifying 
            the output position. Possible values are ELEMENT_CENTROID, ELEMENT_FACE, ELEMENT_NODAL, 
            GENERAL_PARTICLE, INTEGRATION_POINT, NODAL, WHOLE_ELEMENT, WHOLE_MODEL, 
            WHOLE_PART_INSTANCE, and WHOLE_REGION.Refinement: A tuple specifying the refinement. If 
            the refinement tuple is omitted, data are written for all components and invariants (if 
            applicable). This element is required if the location dictionary (the following element 
            in the tuple) is included. The refinement tuple contains the following:Type: A 
            SymbolicConstant specifying the type of refinement. Possible values are INVARIANT and 
            COMPONENT.Label: A String specifying the invariant or the component; for example, 
            'Mises' or 'S22'.Location: An optional Dictionary specifying the location. The 
            dictionary contains pairs of the following:A String specifying the category selection 
            label.A String specifying the section point label.For example,
            variable=('S',INTEGRATION_POINT, ((COMPONENT, 'S22' ), ), )
            variable=(('S',INTEGRATION_POINT, ((COMPONENT, 'S11' ), ), ), ('U',NODAL,((COMPONENT, 'U1'),)),)
            variable=(('S', INTEGRATION_POINT, ((INVARIANT, 'Mises' ), ),{'shell < STEEL > < 3 section points >':'SNEG, (fraction = -1.0)', }), )
                                          ` 
        elementSets
            A sequence of Strings specifying element sets or a String specifying a single element 
            set. 
        elementLabels
            A sequence of expressions specifying element labels per part instance in the model. Each 
            part instance element expression is a sequence of a String specifying the part instance 
            name and a sequence of element expressions; for example, 
            `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The element 
            expressions can be any of the following:An Int specifying a single element label; for 
            example, `1`.A String specifying a single element label; for example, `'7'`.A String 
            specifying a sequence of element labels; for example, `'3:5'` and `'3:15:3'`. 
        nodeSets
            A sequence of Strings specifying node sets or a String specifying a single node set. 
        nodeLabels
            A sequence of expressions specifying node labels per part instance in the model. Each 
            part instance node expression is a sequence of a String specifying the part instance 
            name and a sequence of node expressions; for example, 
            `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The node expressions 
            can be any of the following:An Int specifying a single node label; for example, `1`.A 
            String specifying a single node label; for example, `'7'`.A String specifying a sequence 
            of node labels; for example, `'3:5'` and `'3:15:3'`. 
        numericForm
            A SymbolicConstant specifying the numeric form in which to display results that contain 
            complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL, IMAGINARY, 
            and COMPLEX_VAL_AT_ANGLE. The default value is REAL. 
        complexAngle
            A Float specifying the angle (in degrees) at which to display results that contain 
            complex numbers when *numericForm*=COMPLEX_VAL_AT_ANGLE. The default value is 0. 
        operator
            A SymbolicConstant specifying the mathematical, trigonometric, logarithmic, exponential, 
            or other operations. Possible values are ADD, SUBTRACT, MULTIPLY, DIVIDE, POWER, 
            MINIMUM, MAXIMUM, AVERAGE, RANGE, SRSS, ABSOLUTE, UNARY_NEGATIVE, COSINE, 
            HYPERBOLIC_COSINE, INVERSE_COSINE, SINE, HYPERBOLIC_SINE, INVERSE_SINE, TANGENT, 
            HYPERBOLIC_TANGENT, INVERSE_TANGENT, EXPONENTIAL, NATURAL_LOG, LOG, SQUARE_ROOT, 
            NORMALIZE, DEG2RAD, RAD2DEG, SMOOTH, SWAP, AVERAGE_ALL, MAXIMUM_ENVELOPE, 
            MINIMUM_ENVELOPE, and RANGE_ALL. If no value is defined, no operation will be performed 
            on the data, and the data will be saved as is. 

        Returns
        -------
            A list of XYData objects. 
            
        Raises
        ------
        InvalidNameError
        RangeError 
        """
        pass

    def XYDataFromFreeBody(self, odb: Odb, force: Boolean = ON, moment: Boolean = OFF, heatFlowRate: Boolean = OFF,
                           resultant: Boolean = ON, comp1: Boolean = OFF, comp2: Boolean = OFF,
                           comp3: Boolean = OFF):
        """This method creates a list of XYData objects by computing free body data from an Odb
        object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.XYData
            xyPlot.XYData
        
        Parameters
        ----------
        odb
            An Odb object specifying the output database from which data will be read. 
        force
            A boolean indicating whether to compute the force. The default is ON. 
        moment
            A boolean indicating whether to compute the moment. The default is OFF. 
        heatFlowRate
            A boolean indicating whether to compute the heat flow rate resultant magnitude. It is 
            extracted only for viewcut based freebodies. The default is OFF. 
        resultant
            A boolean indicating whether to compute the resultant. It applies only to *force* and 
            *moment*. The default is ON. 
        comp1
            A boolean indicating whether to compute the first component. It applies only to *force* 
            and *moment*. The default is OFF. 
        comp2
            A boolean indicating whether to compute the second component. It applies only to *force* 
            and *moment*. The default is OFF. 
        comp3
            A boolean indicating whether to compute the third component. It applies only to *force* 
            and *moment*. The default is OFF. 

        Returns
        -------
            A list of XYData objects. 
            
        Raises
        ------
        InvalidNameError
        RangeError 
        """
        pass

    def XYDataFromShellThickness(self, odb: Odb, outputPosition: SymbolicConstant, variable: SymbolicConstant,
                                 elementSets: tuple = (), elementLabels: tuple = (), nodeSets: tuple = (),
                                 nodeLabels: tuple = (), numericForm: SymbolicConstant = REAL, complexAngle: float = 0):
        """This method creates a list of XYData objects by reading through the thickness field data
        from an Odb object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.XYData
            xyPlot.XYData
        
        Parameters
        ----------
        odb
            An Odb object specifying the output database from which data will be read. 
        outputPosition
            A SymbolicConstant specifying the position from which output will be read. Possible 
            values are ELEMENT_CENTROID, ELEMENT_NODAL, INTEGRATION_POINT, and NODAL. 
        variable
            A tuple of tuples containing the descriptions of variables for which to extract data 
            from the field. Each tuple specifies the following:Variable label: A String specifying 
            the variable; for example, 'U'.Variable output position: A SymbolicConstant specifying 
            the output position. Possible values are ELEMENT_CENTROID, ELEMENT_FACE, ELEMENT_NODAL, 
            GENERAL_PARTICLE, INTEGRATION_POINT, NODAL, WHOLE_ELEMENT, WHOLE_MODEL, 
            WHOLE_PART_INSTANCE, and WHOLE_REGION.Refinement: A tuple specifying the refinement. If 
            the refinement tuple is omitted, data are written for all components and invariants (if 
            applicable). This element is required if the location dictionary (the following element 
            in the tuple) is included. The refinement tuple contains the following:Type: A 
            SymbolicConstant specifying the type of refinement. Possible values are INVARIANT and 
            COMPONENT.Label: A String specifying the invariant or the component; for example, 
            'Mises' or 'S22'.Location: An optional Dictionary specifying the location. The 
            dictionary contains pairs of the following:A String specifying the category selection 
            label.A String specifying the section point label.For example,`variable= 
            ('S',INTEGRATION_POINT, ( (COMPONENT, 'S22' ), ), ) variable= (('S',INTEGRATION_POINT, 
            ((COMPONENT, 'S11' ), ), ),            ('U',NODAL,((COMPONENT, 'U1'),)),) variable= 
            (('S', INTEGRATION_POINT, ((INVARIANT, 'Mises' ), ),            {'shell < STEEL > < 3 
            section points >':'SNEG,                                    (fraction = -1.0)', }), )` 
        elementSets
            A sequence of Strings specifying element sets or a String specifying a single element 
            set. 
        elementLabels
            A sequence of expressions specifying element labels per part instance in the model. Each 
            part instance element expression is a sequence of a String specifying the part instance 
            name and a sequence of element expressions; for example, 
            `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The element 
            expressions can be any of the following:An Int specifying a single element label; for 
            example, `1`.A String specifying a single element label; for example, `'7'`.A String 
            specifying a sequence of element labels; for example, `'3:5'` and `'3:15:3'`. 
        nodeSets
            A sequence of Strings specifying node sets or a String specifying a single node set. 
        nodeLabels
            A sequence of expressions specifying node labels per part instance in the model. Each 
            part instance node expression is a sequence of a String specifying the part instance 
            name and a sequence of node expressions; for example, 
            `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The node expressions 
            can be any of the following:An Int specifying a single node label; for example, `1`.A 
            String specifying a single node label; for example, `'7'`.A String specifying a sequence 
            of node labels; for example, `'3:5'` and `'3:15:3'`. 
        numericForm
            A SymbolicConstant specifying the numeric form in which to display results that contain 
            complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL, IMAGINARY, 
            and COMPLEX_VAL_AT_ANGLE. The default value is REAL. 
        complexAngle
            A Float specifying the angle (in degrees) at which to display results that contain 
            complex numbers when *numericForm*=COMPLEX_VAL_AT_ANGLE. The default value is 0. 

        Returns
        -------
            A list of XYData objects. 
            
        Raises
        ------
        InvalidNameError
        RangeError 
        """
        pass

    def XYDataFromPath(self, path: Path, name: str, includeIntersections: Boolean, shape: SymbolicConstant,
                       pathStyle: SymbolicConstant, numIntervals: int, labelType: SymbolicConstant,
                       viewport: str = '', removeDuplicateXYPairs: Boolean = True,
                       includeAllElements: Boolean = False, step: int = None, frame: int = None,
                       variable: SymbolicConstant = None, deformedMag: float = None,
                       numericForm: SymbolicConstant = REAL, complexAngle: float = 0,
                       projectOntoMesh: Boolean = False, projectionTolerance: float = 0):
        """This method creates an XYData object from path information.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.XYData
            xyPlot.XYData
        
        Parameters
        ----------
        path
            A Path object to use in *X–Y* data generation. 
        name
            A String specifying the repository key:for *session* 'name' is required argument and for 
            *xyPlot* 'name' is optional argument. 
        includeIntersections
            A Boolean specifying whether to include *X–Y* data for the intersections between the 
            path and element faces or edges. The default value is False. 
        shape
            A SymbolicConstant specifying the model shape to use. Possible values are UNDEFORMED and 
            DEFORMED. 
        pathStyle
            A SymbolicConstant specifying the path style. Possible values are PATH_POINTS and 
            UNIFORM_SPACING. 
        numIntervals
            An Int specifying the number of uniform-spacing intervals. The default value is 10. 
        labelType
            A SymbolicConstant specifying the *X*-label type to use. Possible values are 
            NORM_DISTANCE, SEQ_ID, TRUE_DISTANCE, TRUE_DISTANCE_X, TRUE_DISTANCE_Y, TRUE_DISTANCE_Z, 
            X_COORDINATE, Y_COORDINATE and Z_COORDINATE. 
        viewport
            A String specifying the viewport name or an Int specifying the viewport id from which to 
            obtain values. The default is the current viewport. 
        removeDuplicateXYPairs
            A Boolean specifying whether to remove duplicate XY values from the final result. The 
            default value is True. 
        includeAllElements
            A Boolean specifying whether to include elements which do not lie in the direction of 
            the path. The default value is False. 
        step
            An Int identifying the step from which to obtain values. The default value is the 
            current step. 
        frame
            An Int identifying the frame from which to obtain values. The default value is the 
            current frame. 
        variable
            A tuple of tuples containing the descriptions of variables for which to extract data 
            along the path. The default value is the current variable. Each tuple specifies the 
            following:Variable label: A String specifying the variable; for example, 'U'.Variable 
            output position: A SymbolicConstant specifying the output position. Possible values are 
            ELEMENT_CENTROID, ELEMENT_FACE, ELEMENT_NODAL, GENERAL_PARTICLE, INTEGRATION_POINT, 
            NODAL, WHOLE_ELEMENT, WHOLE_MODEL, WHOLE_PART_INSTANCE, and WHOLE_REGION.Refinement: A 
            tuple specifying the refinement. If the refinement tuple is omitted, data are written 
            for all components and invariants (if applicable). This element is required if the 
            location dictionary (the following element in the tuple) is included. The refinement 
            tuple contains the following:Type: A SymbolicConstant specifying the type of refinement. 
            Possible values are INVARIANT and COMPONENT.Label: A String specifying the invariant or 
            the component; for example, 'Mises' or 'S22'.Location: An optional Dictionary specifying 
            the location. The dictionary contains pairs of the following:A String specifying the 
            category selection label.A String specifying the section point label.For 
            example,`variable= ('S',INTEGRATION_POINT, ( (COMPONENT, 'S22' ), ), ) variable= 
            (('S',INTEGRATION_POINT, ((COMPONENT, 'S11' ), ), ),            ('U',NODAL,((COMPONENT, 
            'U1'),)),) variable= (('S', INTEGRATION_POINT, ((INVARIANT, 'Mises' ), ),            
            {'shell < STEEL > < 3 section points >':'SNEG,                                    
            (fraction = -1.0)', }), )` 
        deformedMag
            A tuple of three Floats specifying the deformation magnitude in the *X-*, *Y-*, and 
            *Z-*planes. The default value is (1, 1, 1). 
        numericForm
            A SymbolicConstant specifying the numeric form in which to display results that contain 
            complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL, IMAGINARY, 
            and COMPLEX_VAL_AT_ANGLE. The default value is REAL. 
        complexAngle
            A Float specifying the angle (in degrees) at which to display results that contain 
            complex numbers when *numericForm*=COMPLEX_VAL_AT_ANGLE. The default value is 0. 
        projectOntoMesh
            A Boolean to specify whether to consider the data points that do not lie on or inside 
            the mesh. The default value is False. 
        projectionTolerance
            A Float specifying the tolerance value for the projected distance considered for the 
            data extraction when *projectOntoMesh*= True. The default value is 0. 

        Returns
        -------
            If *variable* specified has one fieldoutput: Returns an XYData object. 
            If *variable* specified has more than one fieldoutputs: Returns list of XYData objects. 

        Raises
        ------
            - If *path* is invalid: 
              ErrorPathNotFound: Path not found. 
            - If *viewport* is invalid: 
              ErrorCurrentVPNotFound: Current viewport not found. 
            - If *step* and/or *frame* are invalid: 
              ErrorInvalidUserStepAndFrame: The user step and frame specified have not been defined. 
            - If the *variable* argument is empty: 
              ErrorNoVarInPathExtract: No variable selection for XY data extraction from path. 
            - If the specified output variable is not available in the output database: 
              ErrorUnavailableSelectedVariable: The selected variable is not available for the 
            current frame. 
            - If the specified output variable cannot be used to obtain *X–Y* data: 
              ErrorUnusableVarInPathExtract: Specified variable cannot be used in XY data extraction 
            from path. 
            - If the SymbolicConstant specifying the refinement type is invalid: 
              ErrorUnsupportedRefinementType: Unsupported refinement type. 
            - If the label specifying the refinement invariant or component is invalid: 
              ErrorInvalidRefinementSpecification: Invalid refinement specification. 
            - If *deformedMag* does not contain three Floats: 
              ErrorDeformedMagTupleInPathExtract: Deformed magnification tuple must contain X, Y and 
            Z values. 
        """
        pass

    def save(self):
        """This method saves a temporary XYData. The name of the XYData is changed to "XYData-#".
        If the XYData is already saved, nothing is done.
        """
        pass

    def setValues(self, sourceDescription: str = '', contentDescription: str = '',
                  positionDescription: str = '', legendLabel: str = '', xValuesLabel: str = '',
                  yValuesLabel: str = '', axis1QuantityType: QuantityType = QuantityType(),
                  axis2QuantityType: QuantityType = QuantityType()):
        """This method modifies the XYData object.
        
        Parameters
        ----------
        sourceDescription
            A String specifying the source of the *X–Y* data (e.g., “Entered from keyboard”, “Taken 
            from ASCII file”, “Read from an ODB”, etc.). The default value is an empty string. 
        contentDescription
            A String specifying the content of the *X–Y* data (e.g., “field 1 vs. field 2”). The 
            default value is an empty string. 
        positionDescription
            A String specifying additional information about the *X–Y* data (e.g., “for whole 
            model”). The default value is an empty string. 
        legendLabel
            A String specifying the label to be used in the legend. The default value is the name of 
            the XYData object. 
        xValuesLabel
            A String specifying the label for the X-values. This value may be overridden if the 
            *X–Y* data are combined with other *X–Y* data. The default value is an empty string. 
        yValuesLabel
            A String specifying the label for the Y-values. This value may be overridden if the 
            *X–Y* data are combined with other *X–Y* data. The default value is an empty string. 
        axis1QuantityType
            A QuantityType object specifying the QuantityType object associated to the X -axis1- 
            values. 
        axis2QuantityType
            A QuantityType object specifying the QuantityType object associated to the Y -axis2- 
            values. 
        """
        pass
