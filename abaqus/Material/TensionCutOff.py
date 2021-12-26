from abaqusConstants import *

class TensionCutOff:

    """The TensionCutOff object specifies tension cutoff for different material models for 
    example the Mohr-Coulomb plasticity model. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].mohrCoulombPlasticity.tensionCutOff
        - import odbMaterial
        - session.odbs[name].materials[name].mohrCoulombPlasticity.tensionCutOff

    Table Data
    ----------
        - Tension cutoff stress.
        - The value of the corresponding tensile plastic strain.(The first tabular value entered must always be zero.)
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - TENSION CUTOFF

    """

    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a TensionCutOff object.

        Path
        ----
            - mdb.models[name].materials[name].mohrCoulombPlasticity.TensionCutOff
            - session.odbs[name].materials[name].mohrCoulombPlasticity.TensionCutOff

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A TensionCutOff object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the TensionCutOff object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
        """
        pass
