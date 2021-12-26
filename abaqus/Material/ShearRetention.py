from abaqusConstants import *

class ShearRetention:

    """The ShearRetention object defines the reduction of the shear modulus associated with 
    crack surfaces in a Concrete model as a function of the tensile strain across the crack. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].concrete.shearRetention
        - import odbMaterial
        - session.odbs[name].materials[name].concrete.shearRetention

    Table Data
    ----------
        - ϱclose for dry concrete. The default value is 1.0.
        - εmax for dry concrete. The default value is a very large number (full shear retention).
        - ϱclose for wet concrete. The default value is 1.0.
        - εmax for wet concrete. The default value is a very large number (full shear retention).
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - SHEAR RETENTION

    """

    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a ShearRetention object.

        Path
        ----
            - mdb.models[name].materials[name].concrete.ShearRetention
            - session.odbs[name].materials[name].concrete.ShearRetention

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
            A ShearRetention object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the ShearRetention object.

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
