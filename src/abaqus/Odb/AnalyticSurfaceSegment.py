from abaqusConstants import *


class AnalyticSurfaceSegment:
    """An individual segment of the analytic surface.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import odbAccess
        session.odbs[name].parts[name].analyticSurface.segments[i]
        session.odbs[name].rootAssembly.instances[name].analyticSurface.segments[i]
        session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.analyticSurface.segments[i]

    """

    def __init__(self, type: SymbolicConstant, data: tuple):
        """This method creates an AnalyticSurfaceSegment object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            odbAccess.AnalyticSurfaceSegment
        
        Parameters
        ----------
        type
            A SymbolicConstant specifying the type of AnalyticSurfaceSegment. Possible values are 
            START, LINE, CIRCLE, and PARABOLA. 
        data
            A sequence of sequences of Floats specifying the coordinates of point/s representing the 
            segment of the AnalyticSurface object. If *type*=CIRCLE, the first row contains 
            coordinates of the end point and the second row contains coordinates of the center 
            point. If *type*=PARABOLA, the first row contains coordinates of the middle point and 
            the second row contains coordinates of the end point. If *type*=START or *type*=LINE, a 
            single row contains coordinates of the start/end point. 

        Returns
        -------
            An AnalyticSurfaceSegment object.
        """
        pass
