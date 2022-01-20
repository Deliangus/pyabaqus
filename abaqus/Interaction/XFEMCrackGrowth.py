from abaqusConstants import *
from .Interaction import Interaction


class XFEMCrackGrowth(Interaction):
    """The XFEMCrackGrowth object defines the enrichment activation state for an XFEMCrack.
    The XFEMCrackGrowth object is derived from the Interaction object. 

    Access
    ------
        - import interaction
        - mdb.models[name].interactions[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - ENRICHMENT ACTIVATION

    """

    def __init__(self, name: str, createStepName: str, crackName: str, allowGrowth: Boolean = ON):
        """This method creates an XFEMCrackGrowth object.

        Path
        ----
            - mdb.models[name].XFEMCrackGrowth

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the XFEMCrackGrowth object is created. 
        crackName
            A String specifying the XFEMCrack object associated with this interaction. 
        allowGrowth
            A Boolean specifying whether the crack is allowed to grow (propagate) during this 
            analysis step. The default value is ON. 

        Returns
        -------
            A XFEMCrackGrowth object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def setValues(self, allowGrowth: Boolean = ON):
        """This method modifies the data for an existing XFEMCrackGrowth object in the step where
        it is created.

        Parameters
        ----------
        allowGrowth
            A Boolean specifying whether the crack is allowed to grow (propagate) during this 
            analysis step. The default value is ON. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValuesInStep(self, stepName: str, allowGrowth: Boolean = ON):
        """This method modifies the propagating data for an existing XFEMCrackGrowth object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified. 
        allowGrowth
            A Boolean specifying whether the crack is allowed to grow (propagate) during this 
            analysis step. The default value is ON. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
