from abaqusConstants import *

class BrittleShear:

    """The BrittleShear object specifies the postcracking shear behavior of a material used in 
    a brittle cracking model. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].brittleCracking.brittleShear
        - import odbMaterial
        - session.odbs[name].materials[name].brittleCracking.brittleShear

    Table Data
    ----------
        If *type*=RETENTION_FACTOR the table data specify the following:
        - Shear retention factor.
        - Crack opening strain.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *type*=POWER_LAW the table data specify the following:
        - e.
        - p.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - BRITTLE SHEAR

    """

    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0, 
                 type: SymbolicConstant = RETENTION_FACTOR):
        """This method creates a BrittleShear object.

        Path
        ----
            - mdb.models[name].materials[name].brittleCracking.BrittleShear
            - session.odbs[name].materials[name].brittleCracking.BrittleShear

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 
        type
            A SymbolicConstant specifying the type of postcracking shear behavior. Possible values 
            are RETENTION_FACTOR and POWER_LAW. The default value is RETENTION_FACTOR. 

        Returns
        -------
            A BrittleShear object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the BrittleShear object.

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
