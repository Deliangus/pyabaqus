from abaqusConstants import *

class PorousElastic:

    """The PorousElastic object specifies elastic material properties for porous materials. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].porousElastic
        - import odbMaterial
        - session.odbs[name].materials[name].porousElastic

    Table Data
    ----------
        If *shear*=G, the table data specify the following:
        - The logarithmic bulk modulus, κ. (Dimensionless.)
        - The shear modulus, G.
        - The elastic tensile limit, peltpte⁢l. (This value cannot be negative.)
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *shear*=POISSON, the table data specify the following:
        - The logarithmic bulk modulus, κ. (Dimensionless.)
        - The Poisson's ratio, ν.
        - The elastic tensile limit, peltpte⁢l. (This value cannot be negative.)
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - POROUS ELASTIC

    """

    def __init__(self, table: tuple, shear: SymbolicConstant = POISSON, temperatureDependency: Boolean = OFF, 
                 dependencies: int = 0):
        """This method creates a PorousElastic object.

        Path
        ----
            - mdb.models[name].materials[name].PorousElastic
            - session.odbs[name].materials[name].PorousElastic

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        shear
            A SymbolicConstant specifying the shear definition form. Possible values are G and 
            POISSON. The default value is POISSON. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A PorousElastic object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the PorousElastic object.

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
