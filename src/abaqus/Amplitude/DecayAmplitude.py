from abaqusConstants import *
from .Amplitude import Amplitude

from __init__ import *


class DecayAmplitude(Amplitude):
    """The DecayAmplitude object defines an amplitude curve using an exponential decay.
    The DecayAmplitude object is derived from the Amplitude object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import amplitude
        mdb.models[name].amplitudes[name]
        import odbAmplitude
        session.odbs[name].amplitudes[name]

    The corresponding analysis keywords are:
        - AMPLITUDE

    """
    def __init__(self,
                 name: str,
                 initial: float,
                 maximum: float,
                 start: float,
                 decayTime: float,
                 timeSpan: SymbolicConstant = STEP):
        """This method creates a DecayAmplitude object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].DecayAmplitude
            session.odbs[name].DecayAmplitude
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        initial
            A Float specifying the constant A0A0. 
        maximum
            A Float specifying the coefficient AA. 
        start
            A Float specifying the starting time t0t0. Possible values are non-negative numbers. 
        decayTime
            A Float specifying the decay time tdtd. Possible values are non-negative numbers. 
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP 
            and TOTAL. The default value is STEP. 

        Returns
        -------
            A DecayAmplitude object. 
            
        Raises
        ------
        InvalidNameError
        RangeError 
        """
        super().__init__()
        pass

    def setValues(self, timeSpan: SymbolicConstant = STEP):
        """This method modifies the DecayAmplitude object.
        
        Parameters
        ----------
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP 
            and TOTAL. The default value is STEP.

        Raises
        ------
        RangeError
        """
        pass
