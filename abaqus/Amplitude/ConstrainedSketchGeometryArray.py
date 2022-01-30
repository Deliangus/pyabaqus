from abaqusConstants import *


class ConstrainedSketchGeometryArray:
    """The ConstrainedSketchGeometryArray is a sequence of ConstrainedSketchGeometry objects.

    Notes
    -----
        This object can be accessed by:
        - import sketch
        - mdb.models[name].sketches[name].geometry[i]

    """

    def findAt(self, coordinates: tuple, printWarning: Boolean = True):
        """This method returns the ConstrainedSketchGeometry object located at the given
        coordinates.

        Parameters
        ----------
        coordinates
            A sequence of Floats specifying the *X*- and *Y*-coordinates of the object to find. 
        printWarning
            A Boolean specifying whether a message is to be printed to the CLI if no entity is found 
            at the specified location. The default value is True. 

        Returns
        -------
            A ConstrainedSketchGeometry object. . 
        """
        pass
