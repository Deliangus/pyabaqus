from abaqusConstants import *

class CohesiveBehavior:

    """The CohesiveBAccess 
    import interaction 
    mdb.models[name].interactionProperties[name].cohesiveBehavior 

    Access
    ------

    Table Data
    ----------
        If *coupling*=UNCOUPLED, the table data specify the following:
        - Stiffness coefficient in the normal direction, KnnKn⁢n.
        - Stiffness coefficient in the first shear direction, KssKs⁢s.
        - Stiffness coefficient in the second shear direction, KttKt⁢t.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *coupling*=COUPLED, the table data specify the following:
        - Stiffness coefficient in the normal direction, KnnKn⁢n.
        - Stiffness coefficient in the first shear direction, KssKs⁢s.
        - Stiffness coefficient in the second shear direction, KttKt⁢t.
        - Coupled stiffness coefficient, KnsKn⁢s.
        - Coupled stiffness coefficient, KntKn⁢t.
        - Coupled stiffness coefficient, KstKs⁢t.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - COHESIVE BEHAVIOR

    """

    def __init__(self, repeatedContacts: Boolean = OFF, eligibility: SymbolicConstant = ALL_NODES, 
                 defaultPenalties: Boolean = ON, coupling: SymbolicConstant = UNCOUPLED, 
                 temperatureDependency: Boolean = OFF, dependencies: int = 0, table: tuple = ()):
        """This method creates a CohesiveBehavior object.

        Path
        ----
            - mdb.models[name].interactionProperties[name].CohesiveBehavior

        Parameters
        ----------
        repeatedContacts
            A Boolean specifying whether to enforce cohesive behavior for recurrent contacts at 
            nodes on the secondary surface subsequent to ultimate failure. The default value is OFF. 
        eligibility
            A SymbolicConstant specifying the eligible secondary nodes. Possible values are 
            ALL_NODES, INITIAL_NODES, and SPECIFIED. The default value is ALL_NODES. 
        defaultPenalties
            A Boolean specifying whether to use the default contact penalties. The default value is 
            ON. 
        coupling
            A SymbolicConstant specifying whether the traction-separation coefficients are coupled 
            or uncoupled. This argument is valid only for *defaultPenalties*=OFF. Possible values 
            are UNCOUPLED and COUPLED. The default value is UNCOUPLED. 
        temperatureDependency
            A Boolean specifying whether the coefficient data depend on temperature. This argument 
            is valid only for *defaultPenalties*=OFF. The default value is OFF. 
        dependencies
            An Int specifying the number of field variables. This argument is valid only for 
            *defaultPenalties*=OFF. The default value is 0. 
        table
            A sequence of sequences of Floats specifying the traction-separation coefficients. The 
            items in the table data are described below. This argument is valid only for 
            *defaultPenalties*=OFF. 

        Returns
        -------
            A CohesiveBehavior object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self):
        """This method modifies the CohesiveBehavior object.

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
