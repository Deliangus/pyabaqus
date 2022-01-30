class DirectDampingByFrequencyComponent:
    """A DirectDampingByFrequencyComponent object is used to define direct damping over a range
    of frequencies. 

    Notes
    -----
        This object can be accessed by:
        - import step
        - mdb.models[name].steps[name].directDampingByFrequency.components[i]

    """

    # A Float specifying the frequency value in cycles/time. 
    frequency: float = None

    # A Float specifying the fraction of critical damping. 
    fraction: float = None
