class TimePoint:
    """The TimePoint object defines time points at which data are written to the output
    database or restart files. 

    Notes
    -----
        This object can be accessed by:
        - import step
        - mdb.models[name].timePoints[name]

    Corresponding analysis keywords
    -------------------------------
        - TIME POINTS

    """

    def __init__(self, name: str, points: tuple):
        """This method creates a TimePoint object.

        Notes
        -----
            This function can be accessed by:
            - mdb.models[name].TimePoint

        Parameters
        ----------
        name
            A String specifying the repository key. 
        points
            A sequence of sequences of Floats specifying time points at which data are written to 
            the output database or restart files. 

        Returns
        -------
            A TimePoint object.  and RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the TimePoint object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Raises
        ------
            RangeError. 
        """
        pass
