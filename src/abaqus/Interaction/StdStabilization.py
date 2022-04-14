from abaqusConstants import *
from .ContactStabilization import ContactStabilization

from __init__ import *


class StdStabilization(ContactStabilization):
    """The StdStabilization object is used in conjunction with ContactStd in Abaqus/Standard
    analyses to specify contact stabilization. 
    The StdStabilization object is derived from the ContactStabilization object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].contactStabilizations[name]

    The corresponding analysis keywords are:
        - CONTACT STABILIZATION

    """
    def __init__(self,
                 name: str,
                 zeroDistance: float = None,
                 reductionFactor: float = 0,
                 scaleFactor: float = 1,
                 tangentialFactor: float = 0,
                 amplitude: str = '',
                 reset: Boolean = OFF):
        """This method creates a StdStabilization object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].StdStabilization
        
        Parameters
        ----------
        name
            A String specifying the contact stabilization repository key. 
        zeroDistance
            None or a Float specifying the clearance distance at which the stabilization becomes 
            zero. The default value is None. 
        reductionFactor
            A Float specifying the factor by which the analysis will reduce the contact 
            stabilization coefficient per increment. The default value is 0.1. 
        scaleFactor
            A Float specifying the factor by which the analysis will scale the contact stabilization 
            coefficient. The default value is 1.0. 
        tangentialFactor
            A Float specifying the factor that scales the contact stabilization coefficient in the 
            tangential direction. The default value is 0.0. 
        amplitude
            A String specifying the name of the Amplitude object that defines a time-dependent scale 
            factor for contact stabilization over the step. The default value is an empty string. 
        reset
            A Boolean specifying whether to cancel carryover effects from contact stabilization 
            specifications involving nondefault amplitudes that appeared in previous steps. The 
            default value is OFF. 

        Returns
        -------
            A StdStabilization object. 

        Raises
        ------
        RangeError
        """
        super().__init__()
        pass

    def setValues(self,
                  zeroDistance: float = None,
                  reductionFactor: float = 0,
                  scaleFactor: float = 1,
                  tangentialFactor: float = 0,
                  amplitude: str = '',
                  reset: Boolean = OFF):
        """This method modifies the StdStabilization object.
        
        Parameters
        ----------
        zeroDistance
            None or a Float specifying the clearance distance at which the stabilization becomes 
            zero. The default value is None. 
        reductionFactor
            A Float specifying the factor by which the analysis will reduce the contact 
            stabilization coefficient per increment. The default value is 0.1. 
        scaleFactor
            A Float specifying the factor by which the analysis will scale the contact stabilization 
            coefficient. The default value is 1.0. 
        tangentialFactor
            A Float specifying the factor that scales the contact stabilization coefficient in the 
            tangential direction. The default value is 0.0. 
        amplitude
            A String specifying the name of the Amplitude object that defines a time-dependent scale 
            factor for contact stabilization over the step. The default value is an empty string. 
        reset
            A Boolean specifying whether to cancel carryover effects from contact stabilization 
            specifications involving nondefault amplitudes that appeared in previous steps. The 
            default value is OFF.

        Raises
        ------
        RangeError
        """
        pass
