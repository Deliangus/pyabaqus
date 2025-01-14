class Stream:
    """TheStream object defines a set of streamlines in fluid mechanics.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import visualization
        session.streams[name]

    """

    def __init__(self, name: str, numPointsOnRake: str, pointA: tuple = (), pointB: tuple = (), path: str = ''):
        """This method creates aStream object and places it in the streams repository.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.Stream
        
        Parameters
        ----------
        name
            A string name for the stream. 
        numPointsOnRake
            An integer specifying the number of points along the rake. 
        pointA
            A tuple of 3 floats specifying the starting point of the rake. Alternatively, a string 
            representation of the node selected in the viewport. 
        pointB
            A tuple of 3 floats specifying the end point of the rake. Alternatively, a string 
            representation of the node selected in the viewport. 
        path
            APath object that specifies the rake. 

        Returns
        -------
            A Stream object.
        """
        pass
