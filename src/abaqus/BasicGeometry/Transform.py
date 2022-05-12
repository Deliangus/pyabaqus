from __init__ import *
from __future__ import annotations


class Transform:
    """The MakeSketchTransform method creates a Transform object. The Transform object has no
    direct constructor. A Transform object is a 4×3 matrix of Floats that represents the 
    transformation from sketch coordinates to assembly coordinates or to part coordinates. 

    Notes
    -----
        This object can be accessed by:
        
        .. code-block:: python
            
            import part
            import assembly

    """
    def matrix(self):
        """This method returns the transformation matrix as a Tuple of 12 Floats.

        Returns
        -------
            A Tuple of 12 Floats.
            
        """
        pass
