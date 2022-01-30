from abaqusConstants import *
from .Amplitude import Amplitude


class ModulatedAmplitude(Amplitude):
    """The ModulatedAmplitude object defines a modulated amplitude curve.
    The ModulatedAmplitude object is derived from the Amplitude object. 

    Notes
    -----
        This object can be accessed by:
        - import amplitude
        - mdb.models[name].amplitudes[name]
        - import odbAmplitude
        - session.odbs[name].amplitudes[name]

    Corresponding analysis keywords
    -------------------------------
        - AMPLITUDE

    """

    def __init__(self, name: str, initial: float, magnitude: float, start: float, frequency1: float,
                 frequency2: float, timeSpan: SymbolicConstant = STEP):
        """This method creates a ModulatedAmplitude object.

        Path
        ----
            - mdb.models[name].ModulatedAmplitude
            - session.odbs[name].ModulatedAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key. 
        initial
            A Float specifying the constant A0A0. 
        magnitude
            A Float specifying the coefficient AA. 
        start
            A Float specifying the starting time t0t0. Possible values are non-negative numbers. 
        frequency1
            A Float specifying the circular frequency 1 (ω1ω1). Possible values are positive 
            numbers. 
        frequency2
            A Float specifying the circular frequency 2 (ω2ω2). Possible values are positive 
            numbers. 
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP 
            and TOTAL. The default value is STEP. 

        Returns
        -------
            A ModulatedAmplitude object.  and RangeError. 
        """
        super().__init__()
        pass

    def setValues(self, timeSpan: SymbolicConstant = STEP):
        """This method modifies the ModulatedAmplitude object.

        Parameters
        ----------
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP 
            and TOTAL. The default value is STEP.

        Raises
        ------
            RangeError. 
        """
        pass
