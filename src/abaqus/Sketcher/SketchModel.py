from .ConstrainedSketch import ConstrainedSketch
from ..Model.ModelBase import ModelBase


class SketchModel(ModelBase):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        mdb.models[name]

    """

    def ConstrainedSketch(self, name: str, sheetSize: float, gridSpacing: float = None, 
                          transform: tuple = ()) -> ConstrainedSketch:
        """This method creates a ConstrainedSketch object. If the sketch cannot be created, the
        method returns None.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].ConstrainedSketch
        
        Parameters
        ----------
        name
            A String specifying the repository key.
        sheetSize
            A Float specifying the sheet size.
        gridSpacing
            A Float specifying the spacing between gridlines. Possible values are Floats >> 0. The
            default value is approximately 2 percent of *sheetSize*.
        transform
            A sequence of sequences of Floats specifying the three-dimensional orientation of the
            sketch. The sequence is a 3 × 4 transformation matrix specifying the axis of rotation
            and the translation vector. Possible values are any Floats.The default value for the
            axis of rotation is the identity matrix`(1.0, 0.0, 0.0),  (0.0, 1.0, 0.0),  (0.0, 0.0,
            1.0)`The default value for the translation vector is`(0.0, 0.0, 0.0)`The default values
            position the sketch on the *X–Y* plane centered at the origin.

        Returns
        -------
        sketch: ConstrainedSketch
            A ConstrainedSketch object.
        """
        self.sketches[name] = sketch = ConstrainedSketch(name, sheetSize, gridSpacing, transform)
        return sketch
