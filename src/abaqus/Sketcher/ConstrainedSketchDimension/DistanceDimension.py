from abaqusConstants import *
from .ConstrainedSketchDimension import ConstrainedSketchDimension
from ..ConstrainedSketchVertex.ConstrainedSketchVertex import ConstrainedSketchVertex


class DistanceDimension(ConstrainedSketchDimension):

    def __init__(self, entity1: ConstrainedSketchVertex, entity2: ConstrainedSketchVertex,
                 textPoint: tuple[float], value: float = None, reference: Boolean = OFF):
        """This method constructs a ConstrainedSketchDimension object between two
        ConstrainedSketchGeometry, or aConstrainedSketchVertex and ConstrainedSketchGeometry
        object. A distance dimension specifies the shortest distance between two entities.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].sketches[name].DistanceDimension
        
        Parameters
        ----------
        entity1
            A ConstrainedSketchVertex object or ConstrainedSketchGeometry object. 
        entity2
            A ConstrainedSketchVertex object or ConstrainedSketchGeometry object. 
        textPoint
            A pair of Floats specifying the location of the dimension text. 
        value
            A Float specifying the angle between the two lines. 
        reference
            A Boolean specifying whether the created dimension enforces the above value or if it 
            simply measures the angle between two lines. 

        Returns
        -------
            A ConstrainedSketchDimension object (None if the dimension cannot be created).
            
        """
        pass
