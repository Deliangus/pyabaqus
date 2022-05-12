from .ConstrainedSketchGeometry import ConstrainedSketchGeometry

from __init__ import *
from __future__ import annotations


class CircleByCenterPerimeter(ConstrainedSketchGeometry):
    def __init__(self, center: Tuple[float], point1: Tuple[float]):
        """This method constructs a circle using a center point and a point on the perimeter. The
        circle is added to the geometry repository of the ConstrainedSketch object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].sketches[name].CircleByCenterPerimeter
        
        Parameters
        ----------
        center
            A pair of Floats specifying the center point of the circle. 
        point1
            A pair of Floats specifying a point on the perimeter of the circle. 

        Returns
        -------
            A ConstrainedSketchGeometry object (None if the circle cannot be created).
            
        """
        pass