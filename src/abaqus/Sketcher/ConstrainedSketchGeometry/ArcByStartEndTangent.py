from .ConstrainedSketchGeometry import ConstrainedSketchGeometry

from __init__ import *
from __future__ import annotations


class ArcByStartEndTangent(ConstrainedSketchGeometry):
    def __init__(self, point1: Tuple[float], point2: Tuple[float],
                 vector: Tuple):
        """This method constructs an arc using two vertices. The Arc object is added to the
        geometry repository of the ConstrainedSketch object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].sketches[name].ArcByStartEndTangent
        
        Parameters
        ----------
        point1
            A pair of Floats specifying the first endpoint of the arc. 
        point2
            A pair of Floats specifying the second endpoint of the arc. 
        vector
            A sequence of two Floats specifying the start direction for constructing the arc. 

        Returns
        -------
            A ConstrainedSketchGeometry object (None if the arc cannot be created).
            
        """
        pass