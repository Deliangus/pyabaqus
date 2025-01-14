from abaqusConstants import *
from .Leaf import Leaf


class LeafFromModelElemLabels(Leaf):
    """The LeafFromModelElemLabels object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects 
    are constructed as temporary objects, which are then used as arguments to DisplayGroup 
    commands. 
    The LeafFromModelElemLabels object is derived from the Leaf object. 

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

    def __init__(self, elementLabels: tuple):
        """This method creates a Leaf object from a sequence of element labels spanning several
        part instances.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            LeafFromModelElemLabels
        
        Parameters
        ----------
        elementLabels
            A sequence of Strings specifying expressions that denote element labels per part 
            instance in the model. Each part instance element expression is a sequence of a String 
            specifying the part instance name and a sequence of element expressions; for example, 
            `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The element 
            expressions can be any of the following:An Int specifying a single element label; for 
            example, `1`.A String specifying a single element label; for example, `'7'`.A String 
            specifying a sequence of element labels; for example, `'3:5'` and `'3:15:3'`. 

        Returns
        -------
            A LeafFromModelElemLabels object.
        """
        super().__init__(DEFAULT_MODEL)
        pass
