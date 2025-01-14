from abaqusConstants import *
from .ConstrainedSketchDimension import ConstrainedSketchDimension
from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import ConstrainedSketchGeometry


class RadialDimension(ConstrainedSketchDimension):

    def __init__(self, curve: ConstrainedSketchGeometry, textPoint: tuple[float], value: float = None,
                 reference: Boolean = OFF, majorRadius: float = None, minorRadius: float = None):
        """This method constructs a ConstrainedSketchDimension object on a circular or elliptical
        arc. A radial dimension indicates the radius of an arc or circle or the major or minor
        radius of an ellipse.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].sketches[name].RadialDimension
        
        Parameters
        ----------
        curve
            A ConstrainedSketchGeometry object specifying the circular or elliptical arc. 
        textPoint
            A pair of Floats specifying the location of the dimension text. 
        value
            A Float specifying the radius of the arc, circle or ellipse. 
        reference
            A Boolean specifying whether the created dimension enforces the above value or if it 
            simply measures the angle between two lines. 
        majorRadius
            A Float specifying the major Radius if *curve* is an ellipse. This is mutually exclusive 
            with *value* and *minorRadius*. 
        minorRadius
            A Float specifying the minor Radius if *curve* is an ellipse. This is mutually exclusive 
            with *value* and *majorRadius*. 

        Returns
        -------
            A ConstrainedSketchDimension object (None if the dimension cannot be created).
            
        """
        pass
