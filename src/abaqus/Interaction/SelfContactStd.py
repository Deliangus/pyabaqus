from abaqusConstants import *
from .Interaction import Interaction
from ..Region.Region import Region


class SelfContactStd(Interaction):
    """The SelfContactStd object defines self-contact during an Abaqus/Standard analysis.
    The SelfContactStd object is derived from the Interaction object. 

    Attributes
    ----------
    contactTracking: SymbolicConstant
        A SymbolicConstant specifying the choice of contact tracking algorithm. The STATE
        tracking algorithm uses only normal projections and is specified by using ONE_CONFIG.
        The PATH tracking algorithm uses crossing and normal projections and is specified by
        using TWO_CONFIG. Possible values are ONE_CONFIG and TWO_CONFIG. The default value is
        TWO_CONFIG.This argument is valid only when **enforcement=SURFACE_TO_SURFACE**.
    supplementaryContact: SymbolicConstant
        A SymbolicConstant specifying the manner in which mid-face constraints are employed.
        Possible values are SELECTIVE, NEVER, and ALWAYS. The default value is SELECTIVE.This
        argument is valid only when **enforcement=NODE_TO_SURFACE**.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].interactions[name]

    """

    # A SymbolicConstant specifying the choice of contact tracking algorithm. The STATE 
    # tracking algorithm uses only normal projections and is specified by using ONE_CONFIG. 
    # The PATH tracking algorithm uses crossing and normal projections and is specified by 
    # using TWO_CONFIG. Possible values are ONE_CONFIG and TWO_CONFIG. The default value is 
    # TWO_CONFIG.This argument is valid only when *enforcement*=SURFACE_TO_SURFACE. 
    contactTracking: SymbolicConstant = TWO_CONFIG

    # A SymbolicConstant specifying the manner in which mid-face constraints are employed. 
    # Possible values are SELECTIVE, NEVER, and ALWAYS. The default value is SELECTIVE.This 
    # argument is valid only when *enforcement*=NODE_TO_SURFACE. 
    supplementaryContact: SymbolicConstant = SELECTIVE

    def __init__(self, name: str, createStepName: str, surface: Region, interactionProperty: str,
                 enforcement: SymbolicConstant = SURFACE_TO_SURFACE, thickness: Boolean = ON,
                 smooth: float = 0, contactControls: str = ''):
        """This method creates a SelfContactStd object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].SelfContactStd
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the SelfContactStd object is created. 
        surface
            A Region object specifying the surface where self-contact is defined. 
        interactionProperty
            A String specifying the name of the ContactProperty object associated with this 
            interaction. 
        enforcement
            A SymbolicConstant specifying the discretization method. Possible values are 
            NODE_TO_SURFACE and SURFACE_TO_SURFACE. The default value is SURFACE_TO_SURFACE. 
        thickness
            A Boolean specifying whether shell/membrane element thickness is considered. The default 
            value is ON.This argument in valid only when *enforcement*=SURFACE_TO_SURFACE. 
        smooth
            A Float specifying the degree of smoothing used for deformable or rigid main surfaces 
            involved when *enforcement*=NODE_TO_SURFACE. The value given must lie between 0.0 and 
            0.5. The default value is 0.2. 
        contactControls
            A String specifying the name of the ContactControl object associated with this 
            interaction. An empty string indicates that the default contact controls will be used. 
            The default value is an empty string. 

        Returns
        -------
            A SelfContactStd object.
        """
        super().__init__()
        pass

    def setValues(self, enforcement: SymbolicConstant = SURFACE_TO_SURFACE, thickness: Boolean = ON,
                  smooth: float = 0, contactControls: str = ''):
        """This method modifies the data for an existing SelfContactStd object in the step where it
        is created.
        
        Parameters
        ----------
        enforcement
            A SymbolicConstant specifying the discretization method. Possible values are 
            NODE_TO_SURFACE and SURFACE_TO_SURFACE. The default value is SURFACE_TO_SURFACE. 
        thickness
            A Boolean specifying whether shell/membrane element thickness is considered. The default 
            value is ON.This argument in valid only when *enforcement*=SURFACE_TO_SURFACE. 
        smooth
            A Float specifying the degree of smoothing used for deformable or rigid main surfaces 
            involved when *enforcement*=NODE_TO_SURFACE. The value given must lie between 0.0 and 
            0.5. The default value is 0.2. 
        contactControls
            A String specifying the name of the ContactControl object associated with this 
            interaction. An empty string indicates that the default contact controls will be used. 
            The default value is an empty string. 
        """
        pass

    def setValuesInStep(self, stepName: str, interactionProperty: str = '', contactControls: str = ''):
        """This method modifies the propagating data of an existing SelfContactStd object in the
        specified step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified. 
        interactionProperty
            A String specifying the name of the ContactProperty object associated with this 
            interaction. 
        contactControls
            A String specifying the name of the ContactControl object associated with this 
            interaction. An empty string indicates that the default contact controls will be used. 
            The default value is an empty string. 
        """
        pass
