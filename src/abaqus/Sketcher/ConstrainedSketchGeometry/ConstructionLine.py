from .ConstrainedSketchGeometry import ConstrainedSketchGeometry

from __init__ import *
from __future__ import annotations


class ConstructionLine(ConstrainedSketchGeometry):
    def __init__(self, point1: Tuple[float], point2: Tuple[float]):
        """This method creates an oblique construction line that runs between two given points.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].sketches[name].ConstructionLine
        
        Parameters
        ----------
        point1
            A pair of Floats specifying the first endpoint. 
        point2
            A pair of Floats specifying the second endpoint. 

        Returns
        -------
            A ConstrainedSketchGeometry object (None if the line cannot be created).
            
        """
        pass