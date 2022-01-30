from abaqusConstants import *
from .ContactProperty import ContactProperty


class FilmConditionProp(ContactProperty):
    """The FilmConditionProp object is an interaction property that defines a film coefficient
    as a function of temperature and field variables. 
    The FilmConditionProp object is derived from the InteractionProperty object. 

    Notes
    -----
        This object can be accessed by:
        - import interaction
        - mdb.models[name].interactionProperties[name]

    Corresponding analysis keywords
    -------------------------------
        - FILM PROPERTY

    """

    def __init__(self, name: str, temperatureDependency: Boolean = OFF, dependencies: int = 0,
                 property: tuple = ()):
        """This method creates a FilmConditionProp object.

        Notes
        -----
            This function can be accessed by:
            - mdb.models[name].FilmConditionProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 
        property
            A sequence of sequences of Floats specifying the following: 
            - The film coefficient, hh. 
            - Temperature, if the data depend on temperature. 
            - Value of the first field variable, if the data depend on field variables. 
            - Value of the second field variable. 
            - Etc. 

        Returns
        -------
            A FilmConditionProp object. . 
        """
        super().__init__(name)
        pass

    def setValues(self, temperatureDependency: Boolean = OFF, dependencies: int = 0, property: tuple = ()):
        """This method modifies the FilmConditionProp object.

        Parameters
        ----------
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 
        property
            A sequence of sequences of Floats specifying the following: 
            - The film coefficient, hh. 
            - Temperature, if the data depend on temperature. 
            - Value of the first field variable, if the data depend on field variables. 
            - Value of the second field variable. 
            - Etc. 
        """
        pass
