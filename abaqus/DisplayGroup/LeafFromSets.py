from abaqusConstants import *
from .Leaf import Leaf
from ..Region.Set import Set


class LeafFromSets(Leaf):

    """The LeafFromSets object can be used whenever a Leaf object is expected as an argument. 
    Leaf objects are used to specify the items in a display group. Leaf objects are 
    constructed as temporary objects, which are then used as arguments to DisplayGroup 
    commands. 
    The LeafFromSets object is derived from the Leaf object. 

    Access
    ------
        - import displayGroupMdbToolset

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF, 
    # DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES. 
    leafType: SymbolicConstant = None

    def __init__(self, sets: tuple[Set]):
        """This method creates a Leaf object from a sequence of Set objects.

        Path
        ----
            - LeafFromSets

        Parameters
        ----------
        sets
            A sequence of Set objects. 

        Returns
        -------
            A LeafFromSets object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass
