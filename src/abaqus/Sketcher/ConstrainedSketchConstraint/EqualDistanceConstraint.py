from .ConstrainedSketchConstraint import ConstrainedSketchConstraint
from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import ConstrainedSketchGeometry
from ...BasicGeometry.Vertex import Vertex


class EqualDistanceConstraint(ConstrainedSketchConstraint):

    def __init__(self, entity1: str, entity2: ConstrainedSketchGeometry, midpoint: Vertex):
        """This method creates an equal distance constraint. This constraint can be applied between
        a midpoint ConstrainedSketchVertex object and any other two ConstrainedSketchVertex objects or between a midpoint ConstrainedSketchVertex
        object and two ConstrainedSketchGeometry objects that are lines. The equal distance
        constraint forces the midpoint vertex to remain at an equal distance from the two other
        vertices or lines.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].sketches[name].EqualDistanceConstraint
        
        Parameters
        ----------
        entity1
            AConstrainedSketchGeometry object specifying the first line or ConstrainedSketchVertex object.
        entity2
            A ConstrainedSketchGeometry object specifying the second line or ConstrainedSketchVertex object.
        midpoint
            A ConstrainedSketchVertex object specifying the vertex that will be positioned an equal distance from
            *entity1* and *entity2*. 

        Returns
        -------
            A ConstrainedSketchConstraint object.
            
        """
        pass
