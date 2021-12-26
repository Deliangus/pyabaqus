from abaqusConstants import *

class CrushableFoamHardening:

    """The CrushableFoamHardening object specifies hardening for the crushable foam plasticity 
    model. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].crushableFoam.crushableFoamHardening
        - import odbMaterial
        - session.odbs[name].materials[name].crushableFoam.crushableFoamHardening

    Table Data
    ----------
        - The yield stress in uniaxial compression, σcσc.
        - The absolute value of the corresponding plastic strain.(The first tabular value entered must always be zero.)
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - CRUSHABLE FOAM HARDENING

    """

    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a CrushableFoamHardening object.

        Path
        ----
            - mdb.models[name].materials[name].crushableFoam.CrushableFoamHardening
            - session.odbs[name].materials[name].crushableFoam\
            - .CrushableFoamHardening

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
            A CrushableFoamHardening object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the CrushableFoamHardening object.

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
