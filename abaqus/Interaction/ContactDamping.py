import typing

from abaqusConstants import *


class ContactDamping:

    """The ContactDamping object specifies damping for a contact interaction property. 

    Access
    ------
        - import interaction
        - mdb.models[name].interactionProperties[name].damping

    Table Data
    ----------
        If *definition*=DAMPING_COEFFICIENT and *clearanceDependence*=STEP, the table data specify the following:
        - Damping coefficient.
        If *definition*=DAMPING_COEFFICIENT and *clearanceDependence*=LINEAR or BILINEAR, the table data specify the following:
        - Damping coefficient.
        - Clearance.
        Two pairs must be given for *clearanceDependence*=LINEAR and three pairs for *clearanceDependence*=BILINEAR. The first pair must have *clearance*=0.0, and the last pair must have *coefficient*=0.0.
        If *definition*=CRITICAL_DAMPING_FRACTION, the table data specify the following:
        - Critical damping fraction.

    Corresponding analysis keywords
    -------------------------------
        - CONTACT DAMPING

    """

    # A SymbolicConstant specifying the method used to define the damping. Possible values are 
    # DAMPING_COEFFICIENT and CRITICAL_DAMPING_FRACTION. The default value is 
    # DAMPING_COEFFICIENT. 
    definition: SymbolicConstant = DAMPING_COEFFICIENT

    # The SymbolicConstant DEFAULT or a Float specifying the tangential damping coefficient 
    # divided by the normal damping coefficient. The default value is DEFAULT. 
    tangentFraction: typing.Union[SymbolicConstant,float] = DEFAULT

    # A SymbolicConstant specifying the variation of the damping coefficient or fraction with 
    # respect to clearance. Possible values are STEP, LINEAR, and BILINEAR. The default value 
    # is STEP.If *definition*=CRITICAL_DAMPING_FRACTION, the only possible value is STEP. 
    clearanceDependence: SymbolicConstant = STEP

    # A tuple of pairs of Floats specifying the damping properties. The items in the table 
    # data are described below. 
    table: float = None

    def Damping(self, definition: SymbolicConstant = DAMPING_COEFFICIENT, 
                tangentFraction: typing.Union[SymbolicConstant,float] = DEFAULT, 
                clearanceDependence: SymbolicConstant = STEP, table: tuple = ()):
        """This method creates a ContactDamping object.

        Path
        ----
            - mdb.models[name].interactionProperties[name].Damping

        Parameters
        ----------
        definition
            A SymbolicConstant specifying the method used to define the damping. Possible values are 
            DAMPING_COEFFICIENT and CRITICAL_DAMPING_FRACTION. The default value is 
            DAMPING_COEFFICIENT. 
        tangentFraction
            The SymbolicConstant DEFAULT or a Float specifying the tangential damping coefficient 
            divided by the normal damping coefficient. The default value is DEFAULT. 
        clearanceDependence
            A SymbolicConstant specifying the variation of the damping coefficient or fraction with 
            respect to clearance. Possible values are STEP, LINEAR, and BILINEAR. The default value 
            is STEP.If *definition*=CRITICAL_DAMPING_FRACTION, the only possible value is STEP. 
        table
            A sequence of pairs of Floats specifying the damping properties. The items in the table 
            data are described below. 

        Returns
        -------
            A ContactDamping object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self):
        """This method modifies the ContactDamping object.

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
