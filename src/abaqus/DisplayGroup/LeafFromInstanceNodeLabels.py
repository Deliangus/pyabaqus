from abaqusConstants import *
from .Leaf import Leaf


class LeafFromInstanceNodeLabels(Leaf):
    """The LeafFromInstanceNodeLabels object can be used whenever a Leaf object is expected as
    an argument. Leaf objects are used to specify the items in a display group. Leaf objects 
    are constructed as temporary objects, which are then used as arguments to DisplayGroup 
    commands. 
    The LeafFromInstanceNodeLabels object is derived from the Leaf object. 

    Attributes
    ----------
    leafType: SymbolicConstant
        A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
        DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import displayGroupMdbToolset

    """

    # A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF, 
    # DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES. 
    leafType: SymbolicConstant = None

    def __init__(self, nodeLabels: tuple):
        """This method creates a Leaf object from a sequence of Strings specifying the node labels.
        Leaf objects specify the items in a display group.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            LeafFromInstanceNodeLabels
        
        Parameters
        ----------
        nodeLabels
            A sequence of sequences specifying node labels. Each inner sequence consists of a 
            PartInstance object followed by a sequence of Strings specifying node labels. 

        Returns
        -------
            A LeafFromInstanceNodeLabels object.
        """
        super().__init__(DEFAULT_MODEL)
        pass
