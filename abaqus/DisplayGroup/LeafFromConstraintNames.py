from abaqusConstants import *
from .Leaf import Leaf


class LeafFromConstraintNames(Leaf):

    """The LeafFromConstraintNames object can be used whenever a Leaf object is expected as an 
    argument. 
    A Leaf object is used used to specify the items in a display group. Leaf objects are 
    constructed as temporary objects that are used as arguments to DisplayGroup 
    (DisplayGroup object) commands. 
    The LeafFromConstraintNames object is derived from the Leaf object. 

    Access
    ------
        - import displayGroupOdbToolset

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A SymbolicConstant specifying the leaf type. Possible values are TIE, 
    # SHELL_TO_SOLID_COUPLING, DISTRIBUTING_COUPLING, KINEMATIC_COUPLING, RIGID_BODY, and MPC. 
    leafType: SymbolicConstant = None

    def __init__(self, name: tuple, type: SymbolicConstant):
        """This method creates a Leaf object from a sequence of constraint objects. Leaf objects
        specify the items in a display group.

        Path
        ----
            - LeafFromConstraintNames

        Parameters
        ----------
        name
            A sequence of tuples of name objects. 
        type
            A SymbolicConstant specifying the Leaf type. Possible values are TIE, 
            SHELL_TO_SOLID_COUPLING, DISTRIBUTING_COUPLING, KINEMATIC_COUPLING, RIGID_BODY, and MPC. 

        Returns
        -------
            A LeafFromConstraintNames object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass
