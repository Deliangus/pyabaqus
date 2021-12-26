from .Interaction import Interaction
from ..Region.Region import Region


class ElasticFoundation(Interaction):

    """The ElasticFoundation object defines a mechanical foundation. 
    The ElasticFoundation object is derived from the Interaction object. 

    Access
    ------
        - import interaction
        - mdb.models[name].interactions[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - FOUNDATION

    """

    def __init__(self, name: str, createStepName: str, surface: Region, stiffness: float):
        """This method creates an ElasticFoundation object.

        Path
        ----
            - mdb.models[name].ElasticFoundation

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the ElasticFoundation object is 
            created. *createStepName* must be set to 'Initial'. 
        surface
            A Region object specifying the surface to which the foundation applies. 
        stiffness
            A Float specifying the foundation stiffness per area (or per length for beams). 

        Returns
        -------
            An ElasticFoundation object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the data for an existing ElasticFoundation object in the step where
        it is created.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValuesInStep(self, stepName: str, stiffness: float = None):
        """This method modifies the propagating data of an existing ElasticFoundation object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified. 
        stiffness
            A Float specifying the foundation stiffness per area (or per length for beams). 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
