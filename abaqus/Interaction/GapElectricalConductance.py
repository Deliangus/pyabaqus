from abaqusConstants import *


class GapElectricalConductance:
    """The GapElectricalConductance object specifies electrical conductance for a contact
    interaction property. 

    Notes
    -----
        This object can be accessed by:
        - import interaction
        - mdb.models[name].interactionProperties[name].electricalConductance

    Table Data
    ----------
        The *clearanceDepTable* data specify the following:
        - Conductivity.
        - Clearance.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        The *pressureDepTable* data specify the following:
        - Conductivity.
        - Pressure.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - GAP ELECTRICAL CONDUCTANCE

    """

    def __init__(self, definition: SymbolicConstant = TABULAR, clearanceDependency: Boolean = ON,
                 pressureDependency: Boolean = OFF, temperatureDependencyC: Boolean = OFF,
                 dependenciesC: int = 0, clearanceDepTable: tuple = (),
                 temperatureDependencyP: Boolean = OFF, dependenciesP: int = 0,
                 pressureDepTable: tuple = ()):
        """This method creates a GapElectricalConductance object.

        Notes
        -----
            This function can be accessed by:
            - mdb.models[name].interactionProperties[name].GapElectricalConductance

        Parameters
        ----------
        definition
            A SymbolicConstant specifying how the electrical conductance is defined. Possible values 
            are TABULAR and USER_DEFINED. The default value is TABULAR. 
        clearanceDependency
            A Boolean specifying whether to use clearance-dependent data. The default value is ON. 
        pressureDependency
            A Boolean specifying whether to use pressure-dependent data. The default value is OFF. 
        temperatureDependencyC
            A Boolean specifying whether to use temperature-dependent data with clearance 
            dependency. The default value is OFF. 
        dependenciesC
            An Int specifying the number of field variables to use with clearance dependency. The 
            default value is 0. 
        clearanceDepTable
            A sequence of sequences of Floats specifying clearance dependency data. The items in the 
            table data are described below. 
        temperatureDependencyP
            A Boolean specifying whether to use temperature-dependent data with pressure dependency. 
            The default value is OFF. 
        dependenciesP
            An Int specifying the number of field variables to use with pressure dependency. The 
            default value is 0. 
        pressureDepTable
            A sequence of sequences of Floats specifying pressure dependency data. The items in the 
            table data are described below. 

        Returns
        -------
            A GapElectricalConductance object. . 
        """
        pass

    def setValues(self):
        """This method modifies the GapElectricalConductance object.

        Parameters
        ----------
        """
        pass
