from abaqusConstants import *
from .Area import Area
from .AreaStyle import AreaStyle
from .AxisArray import AxisArray
from .Legend import Legend
from .LineStyle import LineStyle
from .TextStyle import TextStyle
from .XYCurve import XYCurve
from ..UtilityAndView.Repository import Repository
from ..UtilityAndView.View import View


class Chart:

    """The Chart object is used to display XYCurve objects. A Chart object is automatically 
    created when creating an XYPlot object 

    Access
    ------
        - import visualization
        - session.charts[name]
        - session.xyPlots[name].charts[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the name of the Chart object. 
    name: str = ''

    # A Boolean specifying whether to use the QuantityType to associate curves with axes. The 
    # default value is ON. 
    useQuantityType: Boolean = ON

    # A Float specifying the aspect ratio of the grid area. A value of -1 specifies that the 
    # gridArea will take up all available space. The default value is −1. 
    aspectRatio: float = None

    # A repository of XYCurve objects specifying a repository of XYCurve objects to display in 
    # the Chart. 
    curves: Repository[str, XYCurve] = None

    # An AxisArray object specifying a read-only sequence of axis objects displayed as axes1 - 
    # the abscissa for a Cartesian chart. 
    axes1: AxisArray = None

    # An AxisArray object specifying a read-only sequence of axis objects displayed as axes2 - 
    # the ordinate for a Cartesian chart. 
    axes2: AxisArray = None

    # An Area object specifying position, padding, background and borders of the chart. 
    area: Area = None

    # An Area object specifying how to display the grid area. 
    gridArea: Area = None

    # A Legend object specifying the attributes for the legend of the chart. 
    legend: Legend = None

    # A LineStyle object specifying the line properties to be used when drawing major 
    # gridlines along axis 1. 
    majorAxis1GridStyle: LineStyle = None

    # A LineStyle object specifying the line properties to be used when drawing major 
    # gridlines along axis 2. 
    majorAxis2GridStyle: LineStyle = None

    # A LineStyle object specifying the line properties to be used when drawing minor 
    # gridlines along axis 1. 
    minorAxis1GridStyle: LineStyle = None

    # A LineStyle object specifying the line properties to be used when drawing minor 
    # gridlines along axis 2. 
    minorAxis2GridStyle: LineStyle = None

    # A TextStyle object specifying the text properties to be used when creating tags. 
    tagTextStyle: TextStyle = None

    # An AreaStyle object specifying the area properties to be used when creating tags. 
    tagAreaStyle: AreaStyle = None

    # A LineStyle object specifying the tag area border properties to be used when creating 
    # tags. 
    tagBorder: LineStyle = None

    # A tuple of Floats specifying a transformation matrix used to scale or pan along the axes 
    # of the Chart. 
    transform: float = None

    def autoColor(self, lines: Boolean = OFF, symbols: Boolean = OFF):
        """This method distributes the colors on all curves displayed in the chart using the color
        palette defined by the xyColors object.

        Parameters
        ----------
        lines
            A Boolean defining whether color distribution affects curve lines. 
        symbols
            A Boolean defining whether color distribution affects curve symbols. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def autoSymbol(self):
        """This method distributes the symbols on all curves displayed in the chart.

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

    def fitCurves(self):
        """This method resets the transform of the chart. It cancels any zoom or pan action.

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

    def getAxis1(self, curve: str, quantityType: str):
        """This method returns the Axis object used for displaying the Axis1 of the XYCurve
        specified by name or object or used for the given QuantityType object.

        Parameters
        ----------
        curve
            The name or the XYCurve object associated to the Axis object. 
        quantityType
            The QuantityType object associated to the Axis object. 

        Returns
        -------
            An Axis object. 

        Exceptions
        ----------
            If the given XYCurve is not used in the Chart. 
            XypError: Curve not found: 
            - If both arguments are specified. 
              TypeError: Specify curve or quantityType; too many arguments; expected 1, got 2. 
            - If the given QuantityType is not used in the Chart. 
              ValueError: QuantityType not found 
        """
        pass

    def getAxis2(self, curve: str, quantityType: str):
        """This method returns the Axis object used for displaying the Axis2 of the XYCurve
        specified by name or object or used for the given QuantityType object.

        Parameters
        ----------
        curve
            The name or the XYCurve object associated to the Axis object. 
        quantityType
            The QuantityType object associated to the Axis object. 

        Returns
        -------
            An Axis object. 

        Exceptions
        ----------
            If the given XYCurve is not used in the Chart. 
            XypError: Curve not found: 
            - If both arguments are specified. 
              TypeError: Specify curve or quantityType; too many arguments; expected 1, got 2. 
            - If the given QuantityType is not used in the Chart. 
              ValueError: QuantityType not found 
        """
        pass

    def moveAxisUp(self, axis: str):
        """This method moves the relative position of the given Axis object up in the axis sequence
        of the Chart.

        Parameters
        ----------
        axis
            The Axis object to be moved. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def moveAxisDown(self, axis: str):
        """This method moves the relative position of the given Axis object down in the axis
        sequence of the Chart.

        Parameters
        ----------
        axis
            The Axis object to be moved. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def removeCurve(self, curve: str):
        """This method removes the given XYCurve from the Chart.

        Parameters
        ----------
        curve
            The XYCurve name or the XYCurve object or a sequence of XYCurve names or XYCurve objects 
            to be removed from the Chart. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self, chart: 'Chart' = None, curvesToPlot: tuple[XYCurve] = (), aspectRatio: float = None, 
                  transform: tuple = (), view: View = None, useQuantityType: Boolean = ON):
        """This method modifies the Chart object.

        Parameters
        ----------
        chart
            A Chart object from which attributes are to be copied. 
        curvesToPlot
            A sequence of Strings specifying the names of the curves to plot. In addition to this 
            type, the argument can also be one of the following:A String specifying the name of the 
            curve to plot.An XYCurve object specifying the curve to plot.A sequence of XYCurve 
            objects specifying the curves to plot (as returned by the curveSet method). 
        aspectRatio
            A Float specifying the aspect ratio of the grid area. A value of -1 specifies that the 
            gridArea will take up all available space. The default value is −1. 
        transform
            A sequence of Floats specifying a transformation matrix used to scale or pan along the 
            axes of the Chart. 
        view
            A View object. 
        useQuantityType
            A Boolean specifying whether to use the QuantityType to associate curves with axes. The 
            default value is ON. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
        """
        pass
