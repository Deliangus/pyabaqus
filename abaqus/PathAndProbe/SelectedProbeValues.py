from abaqusConstants import *

class SelectedProbeValues:

    """The SelectedProbeValues object has no constructor. The SelectedProbeValues object is 
    created when you import the Visualization module. 

    Access
    ------
        - import visualization
        - session.selectedProbeValues

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An Int specifying the length of the *values* member. 
    length: int = None

    # A Boolean specifying whether any probe values have been selected (as is necessary prior 
    # to writing to a file). 
    fieldOutputAvailable: Boolean = OFF

    # A tuple of tuples of Floats specifying the selected probe values. 
    values: float = None

    # A tuple of Floats specifying the last sequence of the *values* member. 
    lastValues: tuple = ()
