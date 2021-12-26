from ..DisplayOptions.AssemblyDisplayOptions import AssemblyDisplayOptions
from ..DisplayOptions.PartDisplayOptions import PartDisplayOptions
from ..OdbDisplay.OdbDisplay import OdbDisplay
from ..UtilityAndView.View import View

class Layer:

    """Objects can be superimposed by displaying them in different layers of a viewport. 

    Access
    ------
        - session.viewports[name].layers[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A Displayable object specifying the object to be displayed. The Displayable type is an 
    # abstract generalization. The concrete possible types are Part, Assembly, 
    # ConstrainedSketch, Odb, or XYPlot. 
    displayedObject: Displayable = None

    # A View object specifying the object that controls viewing of the layer. 
    view: View = None

    # An OdbDisplay object specifying the display options for the Odb object. 
    odbDisplay: OdbDisplay = None

    # A PartDisplayOptions object specifying the display options for the Part object. 
    partDisplay: PartDisplayOptions = None

    # An AssemblyDisplayOptions object specifying the display options for the Assembly object. 
    assemblyDisplay: AssemblyDisplayOptions = None

    def __init__(self, name: str, copyViewName: str = ''):
        """This method creates a Layer object in the Layer repository.

        Path
        ----
            - session.viewports[name].Layer

        Parameters
        ----------
        name
            A String specifying the repository key. 
        copyViewName
            A String specifying the name of the layer to copy. 

        Returns
        -------
            A Layer object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def moveBefore(self, name: str):
        """This method moves the layer object before another object in the layer repository.

        Parameters
        ----------
        name
            A String specifying the name of the other Layer object. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def moveAfter(self, name: str):
        """This method moves the layer object after another object in the layer repository.

        Parameters
        ----------
        name
            A String specifying the name of the other Layer object. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
