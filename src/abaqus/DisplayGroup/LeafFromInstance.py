from abaqusConstants import *
from .Leaf import Leaf
from ..Assembly.PartInstance import PartInstance


class LeafFromInstance(Leaf):
    """The LeafFromInstance object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects 
    are constructed as temporary objects, which are then used as arguments to DisplayGroup 
    commands. 
    The LeafFromInstance object is derived from the Leaf object. 

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

    def __init__(self, instances: PartInstance):
        """This method creates a Leaf object from a sequence of part instance objects.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            LeafFromInstance
        
        Parameters
        ----------
        instances
            A PartInstance object or a Sequence of PartInstance objects. 

        Returns
        -------
            A LeafFromInstance object. 

        Raises
        ------
            - If an invalid argument is passed to this method: 
              Cannot define empty leaf. 
        """
        super().__init__(DEFAULT_MODEL)
        pass
