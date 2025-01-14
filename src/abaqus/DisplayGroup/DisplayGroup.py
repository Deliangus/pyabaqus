from abaqusConstants import *
from .Leaf import Leaf


class DisplayGroup:
    """DisplayGroup objects are used to select a subset of the entities displayed in the
    viewport. 

    Attributes
    ----------
    canUndo: Boolean
        A Boolean specifying whether Undo is possible or not.
    canRedo: Boolean
        A Boolean specifying whether Redo is possible or not.
    name: str
        A String specifying the repository key.
    module: SymbolicConstant
        A SymbolicConstant specifying the module in which the display group has been created.
        The possible values are PART, ASSEMBLY, PART_ASSEMBLY, ODB, and ALL.
    modelName: str
        A String specifying the name of the model to which the display group belongs when the
        module is part- or assembly-based.
    partName: str
        A String specifying the name of the part to which the display group belongs when the
        module is part-based.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        session.displayGroups[name]
        import assembly
        session.viewports[name].assemblyDisplay.displayGroup
        session.viewports[name].layers[name].assemblyDisplay.displayGroup
        import visualization
        session.viewports[name].layers[name].odbDisplay.displayGroup
        import part
        session.viewports[name].layers[name].partDisplay.displayGroup
        session.viewports[name].odbDisplay.displayGroup
        session.viewports[name].partDisplay.displayGroup

    """

    # A Boolean specifying whether Undo is possible or not. 
    canUndo: Boolean = OFF

    # A Boolean specifying whether Redo is possible or not. 
    canRedo: Boolean = OFF

    # A String specifying the repository key. 
    name: str = ''

    # A SymbolicConstant specifying the module in which the display group has been created. 
    # The possible values are PART, ASSEMBLY, PART_ASSEMBLY, ODB, and ALL. 
    module: SymbolicConstant = None

    # A String specifying the name of the model to which the display group belongs when the 
    # module is part- or assembly-based. 
    modelName: str = ''

    # A String specifying the name of the part to which the display group belongs when the 
    # module is part-based. 
    partName: str = ''

    def __init__(self, name: str, leaf: Leaf):
        """This method creates a DisplayGroup object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.DisplayGroup
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        leaf
            A Leaf object specifying the items in the display group. 

        Returns
        -------
            A DisplayGroup object.
        """
        pass

    def add(self, leaf: Leaf):
        """This method adds the specified items to the display group.
        
        Parameters
        ----------
        leaf
            A Leaf object specifying the items to add to the display group. 
        """
        pass

    def either(self, leaf: Leaf):
        """This method redefines the display group to be only those items that are not shared by
        the *leaf* argument and by the display group.
        
        Parameters
        ----------
        leaf
            A Leaf object specifying the items to be excluded from the display group. 
        """
        pass

    def intersect(self, leaf: Leaf):
        """This method redefines the display group to be only those items that are shared by the
        *leaf* argument and the display group.
        
        Parameters
        ----------
        leaf
            A Leaf object specifying the items to be included in the display group. 
        """
        pass

    def redoLast(self):
        """This method redoes the last undone operation on the display group.
        """
        pass

    def remove(self, leaf: Leaf):
        """This method removes the specified items from the display group.
        
        Parameters
        ----------
        leaf
            A Leaf object specifying the items to remove from the display group. 
        """
        pass

    def replace(self, leaf: Leaf):
        """This method replaces the contents of the display group with the specified items.
        
        Parameters
        ----------
        leaf
            A Leaf object specifying the items with which to replace the current display group 
            contents. 
        """
        pass

    def undoLast(self):
        """This method undoes the last operation performed on the display group.
        """
        pass
