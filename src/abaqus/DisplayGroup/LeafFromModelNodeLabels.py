from abaqusConstants import *
from .Leaf import Leaf


class LeafFromModelNodeLabels(Leaf):
    """The LeafFromModelNodeLabels object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects 
    are constructed as temporary objects, which are then used as arguments to DisplayGroup 
    commands. 
    The LeafFromModelNodeLabels object is derived from the Leaf object. 

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

    def __init__(self, nodeLabels: tuple):
        """This method creates a Leaf object from a sequence of node labels spanning several part
        instances.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            LeafFromModelNodeLabels
        
        Parameters
        ----------
        nodeLabels
            A sequence of Strings specifying expressions that denote node labels per part instance 
            in the model. Each part instance node expression is a sequence of a String specifying 
            the part instance name and a sequence of node expressions; for example, 
            `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The node expressions 
            can be any of the following:An Int specifying a single node label; for example, `1`.A 
            String specifying a single node label; for example, `'7'`.A String specifying a sequence 
            of node labels; for example, `'3:5'` and `'3:15:3'`. 

        Returns
        -------
            A LeafFromModelNodeLabels object.
        """
        super().__init__(DEFAULT_MODEL)
        pass
