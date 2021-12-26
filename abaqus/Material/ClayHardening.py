from abaqusConstants import *

class ClayHardening:

    """The ClayHardening object specifies hardening for the clay plasticity model. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].clayPlasticity.clayHardening
        - import odbMaterial
        - session.odbs[name].materials[name].clayPlasticity.clayHardening

    Table Data
    ----------
        - The hydrostatic pressure stress at yield, pc.
        - The absolute value of the corresponding volumetric plastic strain.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - CLAY HARDENING

    """

    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a ClayHardening object.

        Path
        ----
            - mdb.models[name].materials[name].clayPlasticity.ClayHardening
            - session.odbs[name].materials[name].clayPlasticity.ClayHardening

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
            A ClayHardening object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the ClayHardening object.

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
