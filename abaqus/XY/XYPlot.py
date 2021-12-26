from abaqusConstants import *
from .Area import Area
from .Chart import Chart
from .Title import Title
from .XYCurve import XYCurve
from ..UtilityAndView.Repository import Repository


class XYPlot:

    """The XYPlot object is used to display Chart objects. 

    Access
    ------
        - import visualization
        - session.xyPlots[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An Area object specifying position, padding, background and borders of the XYPlot 
    # object. 
    area: Area = None

    # A Title object specifying the title of the XYPlot object. 
    title: Title = None

    # A repository of Chart objects. 
    charts: Repository[str, Chart] = None

    # A repository of XYCurve objects. 
    curves: Repository[str, XYCurve] = None

    # A tuple of Floats specifying a transformation matrix used to scale or pan along the axes 
    # of the active Chart object of this XYPlot. 
    transform: float = None

    def __init__(self, name: str):
        """This method creates an empty XYPlot object.

        Path
        ----
            - session.XYPlot

        Parameters
        ----------
        name
            A String specifying the name of the XYPlot object. 

        Returns
        -------
            An XYPlot object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass

    def autoColor(self, lines: Boolean = OFF, symbols: Boolean = OFF):
        """This method distributes the colors on all curves displayed in the XYPlot using the color
        palette defined by the xyColors AutoColors object.

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
        """This method distributes the symbols on all curves displayed in the XYPlot.

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
        """This method resets the transform of all the charts of the XYPlot object. It cancels any
        zoom or pan action.

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

    def next(self, drawImmediately: Boolean = False):
        """This method restores the *transform* member of the active Chart object to the next
        setting in the transform list. (There is a list of eight transforms stored for each
        chart.) If there is no next transform, no action is taken.

        Parameters
        ----------
        drawImmediately
            A Boolean specifying the viewport should refresh immediately after the command is 
            processed. This is typically only used when writing a script and it is desirable to show 
            intermediate results before the script completes. The default value is False. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def previous(self, drawImmediately: Boolean = False):
        """This method restores the *transform* member of the active Chart object to the previous
        setting in the transform list. (There is a list of eight transforms stored for each
        chart.) If there is no next transform, no action is taken.

        Parameters
        ----------
        drawImmediately
            A Boolean specifying the viewport should refresh immediately after the command is 
            processed. This is typically only used when writing a script and it is desirable to show 
            intermediate results before the script completes. The default value is False. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self, title: Title = None, transform: tuple = ()):
        """This method modifies the XYPlot object.

        Parameters
        ----------
        title
            A Title object specifying the title of the XYPlot object. 
        transform
            A sequence of Floats specifying a transformation matrix used to scale or pan along the 
            axes of the active Chart object of this XYPlot. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
