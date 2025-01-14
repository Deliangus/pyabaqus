from abaqusConstants import *


class TextStyle:
    """The TextStyle object is used to store the text properties to be used for drawing XY-plot
    text objects. 
    TextStyle objects are automatically created when creating a chart or can be created with 
    methods described below. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import visualization
        session.charts[name].axes1[i].labelStyle
        session.charts[name].axes1[i].titleStyle
        session.charts[name].axes2[i].labelStyle
        session.charts[name].axes2[i].titleStyle
        session.charts[name].legend.textStyle
        session.charts[name].legend.titleStyle
        session.charts[name].tagTextStyle
        session.defaultChartOptions.defaultAxis1Options.labelStyle
        session.defaultChartOptions.defaultAxis1Options.titleStyle
        session.defaultChartOptions.defaultAxis2Options.labelStyle
        session.defaultChartOptions.defaultAxis2Options.titleStyle
        session.defaultChartOptions.legend.textStyle
        session.defaultChartOptions.legend.titleStyle
        session.defaultChartOptions.tagTextStyle
        session.defaultPlot.title.titleStyle
        session.xyPlots[name].charts[name].axes1[i].labelStyle
        session.xyPlots[name].charts[name].axes1[i].titleStyle
        session.xyPlots[name].charts[name].axes2[i].labelStyle
        session.xyPlots[name].charts[name].axes2[i].titleStyle
        session.xyPlots[name].charts[name].legend.textStyle
        session.xyPlots[name].charts[name].legend.titleStyle
        session.xyPlots[name].charts[name].tagTextStyle
        session.xyPlots[name].title.titleStyle

    """

    def __init__(self, color: str = '', show: Boolean = ON, font: str = '', rotationAngle: float = 0):
        """This method creates a TextStyle.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.TextStyle
            xyPlot.TextStyle
        
        Parameters
        ----------
        color
            A String specifying the color to be used when drawing text with this TextStyle object. 
            The default value is "White". 
        show
            A Boolean specifying whether to draw the text when using this TextStyle object. The 
            default value is ON. 
        font
            A String specifying the name of the font to be used when drawing text with this 
            TextStyle object. The default value is "-*-verdana-medium-r-normal-*-*-120-*-*-p-*-*-*". 
        rotationAngle
            A Float specifying the angle in degrees used for displaying the text. The default value 
            is 0.0. 

        Returns
        -------
            A TextStyle object. 

        Raises
        ------
            ColorError 
        """
        pass

    def setValues(self, color: str = '', show: Boolean = ON, font: str = '', rotationAngle: float = 0):
        """This method modifies the TextStyle object.
        
        Parameters
        ----------
        color
            A String specifying the color to be used when drawing text with this TextStyle object. 
            The default value is "White". 
        show
            A Boolean specifying whether to draw the text when using this TextStyle object. The 
            default value is ON. 
        font
            A String specifying the name of the font to be used when drawing text with this 
            TextStyle object. The default value is "-*-verdana-medium-r-normal-*-*-120-*-*-p-*-*-*". 
        rotationAngle
            A Float specifying the angle in degrees used for displaying the text. The default value 
            is 0.0. 
        """
        pass
