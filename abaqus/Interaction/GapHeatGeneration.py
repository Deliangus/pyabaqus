

class GapHeatGeneration:

    """The GapHeatGeneration object specifies heat generation for a contact interaction 
    property. 

    Access
    ------
        - import interaction
        - mdb.models[name].interactionProperties[name].heatGeneration

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - GAP HEAT GENERATION

    """

    # A Float specifying the fraction of dissipated energy caused by friction or electric 
    # currents that is converted to heat. The default value is 1.0. 
    conversionFraction: float = 1

    # A Float specifying the fraction of converted heat distributed to the secondary surface. 
    # The default value is 0.5. 
    secondaryFraction: float = 0

    def HeatGeneration(self, conversionFraction: float = 1, secondaryFraction: float = 0):
        """This method creates a GapHeatGeneration object.

        Path
        ----
            - mdb.models[name].interactionProperties[name].HeatGeneration

        Parameters
        ----------
        conversionFraction
            A Float specifying the fraction of dissipated energy caused by friction or electric 
            currents that is converted to heat. The default value is 1.0. 
        secondaryFraction
            A Float specifying the fraction of converted heat distributed to the secondary surface. 
            The default value is 0.5. 

        Returns
        -------
            A GapHeatGeneration object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self):
        """This method modifies the GapHeatGeneration object.

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
