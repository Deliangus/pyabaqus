from abaqusConstants import *
from .Leaf import Leaf


class LeafFromElementSets(Leaf):
    """The LeafFromElementSets object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects 
    are constructed as temporary objects, which are then used as arguments to DisplayGroup 
    commands. 
    The LeafFromElementSets object is derived from the Leaf object. 

    Notes
    -----
        This object can be accessed by:
        - import displayGroupOdbToolset

    """

    # A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF, 
    # DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES. 
    leafType: SymbolicConstant = None

    def __init__(self, elementSets: tuple):
        """This method creates a Leaf object from a sequence of element sets.

        Notes
        -----
            This function can be accessed by:
            - LeafFromElementSets

        Parameters
        ----------
        elementSets
            A sequence of Strings specifying element sets or a String specifying a single element 
            set. 

        Returns
        -------
            A LeafFromElementSets object. . 
        """
        super().__init__(DEFAULT_MODEL)
        pass
