from abaqusConstants import *


class AreaStyle:
    """The AreaStyle object is used to define how areas are to be filled when drawing XY-plot
    objects. 
    AreaStyle objects are automatically created whenever an Area object is created. 
    AreaStyle objects can be created using the methods described below. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import visualization
        session.charts[name].area.style
        session.charts[name].gridArea.style
        session.charts[name].legend.area.style
        session.charts[name].tagAreaStyle
        session.defaultChartOptions.areaStyle
        session.defaultChartOptions.gridArea.style
        session.defaultChartOptions.legend.area.style
        session.defaultChartOptions.tagAreaStyle
        session.defaultPlot.area.style
        session.defaultPlot.title.area.style
        session.xyPlots[name].area.style
        session.xyPlots[name].charts[name].area.style
        session.xyPlots[name].charts[name].gridArea.style
        session.xyPlots[name].charts[name].legend.area.style
        session.xyPlots[name].charts[name].tagAreaStyle
        session.xyPlots[name].title.area.style

    """

    def __init__(self, color: str = '', fill: Boolean = ON, style: SymbolicConstant = SOLID):
        """This method creates an AreaStyle.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.AreaStyle
            xyPlot.AreaStyle
        
        Parameters
        ----------
        color
            A String specifying the color to be used when filling an area with this AreaStyle 
            object. The default value is "White". 
        fill
            A Boolean specifying whether to fill the area when using this AreaStyle. The default 
            value is ON. 
        style
            A SymbolicConstant specifying the area pattern style to be used when filling an area 
            using this AreaStyle. The default value is SOLID. 

        Returns
        -------
            An AreaStyle object. 

        Raises
        ------
            ColorError 
        """
        pass

    def setValues(self, color: str = '', fill: Boolean = ON, style: SymbolicConstant = SOLID):
        """This method modifies the AreaStyle object.
        
        Parameters
        ----------
        color
            A String specifying the color to be used when filling an area with this AreaStyle 
            object. The default value is "White". 
        fill
            A Boolean specifying whether to fill the area when using this AreaStyle. The default 
            value is ON. 
        style
            A SymbolicConstant specifying the area pattern style to be used when filling an area 
            using this AreaStyle. The default value is SOLID. 
        """
        pass
