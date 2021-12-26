from abaqusConstants import *

class FluidLeakoff:

    """The FluidLeakoff object specifies leak-off coefficients for pore pressure cohesive 
    elements. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].fluidLeakoff
        - import odbMaterial
        - session.odbs[name].materials[name].fluidLeakoff

    Table Data
    ----------
        The table data specify the following:
        - Fluid leak-off coefficient at top element surface.
        - Fluid leak-off coefficient at bottom element surface.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - FLUID LEAKOFF

    """

    def __init__(self, temperatureDependency: Boolean = OFF, dependencies: int = 0, 
                 type: SymbolicConstant = COEFFICIENTS, table: tuple = ()):
        """This method creates a FluidLeakoff object.

        Path
        ----
            - mdb.models[name].materials[name].FluidLeakoff
            - session.odbs[name].materials[name].FluidLeakoff

        Parameters
        ----------
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 
        type
            A SymbolicConstant specifying the type of fluid leak-off. Possible values are 
            COEFFICIENTS and USER. The default value is COEFFICIENTS. 
        table
            A sequence of sequences of Floats specifying the items described below. The default 
            value is an empty sequence. 

        Returns
        -------
            A FluidLeakoff object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self):
        """This method modifies the FluidLeakoff object.

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
