from .ConstrainedSketchConstraint import ConstrainedSketchConstraint
from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import ConstrainedSketchGeometry


class HorizontalConstraint(ConstrainedSketchConstraint):

    def __init__(self, entity: ConstrainedSketchGeometry):
        """This method creates a horizontal constraint. This constraint applies to a line and
        constrains it to be horizontal.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].sketches[name].HorizontalConstraint
        
        Parameters
        ----------
        entity
            A ConstrainedSketchGeometry object specifying the line to constrain. 

        Returns
        -------
            A ConstrainedSketchConstraint object.
            
        """
        pass
