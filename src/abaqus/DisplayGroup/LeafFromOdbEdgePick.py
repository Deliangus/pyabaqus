from abaqusConstants import *
from .Leaf import Leaf


class LeafFromOdbEdgePick(Leaf):
    """The LeafFromOdbEdgePick object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects 
    are constructed as temporary objects, which are then used as arguments to DisplayGroup 
    commands. 
    The LeafFromOdbEdgePick object is derived from the Leaf object. 

    Attributes
    ----------
    leafType: SymbolicConstant
        A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
        DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import displayGroupOdbToolset

    """

    # A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF, 
    # DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES. 
    leafType: SymbolicConstant = None

    def __init__(self, edgePick: tuple):
        """This method creates a Leaf object from a tuple containing machine readable, compact
        strings defining the edges picked for each part instance. Leaf objects specify the items
        in a display group.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            LeafFromOdbEdgePick
        
        Parameters
        ----------
        edgePick
            A sequence of tuples of the form [part name, entity count, machine readable pick 
            strings]. 

        Returns
        -------
            A LeafFromOdbEdgePick object.
        """
        super().__init__(DEFAULT_MODEL)
        pass
