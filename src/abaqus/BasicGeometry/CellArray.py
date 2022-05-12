from abaqusConstants import *
from .Cell import Cell

from __init__ import *
from __future__ import annotations


class CellArray:
    from .FaceArray import FaceArray
    from .CellArray import CellArray
    """The CellArray is a sequence of Cell objects.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import part
        mdb.models[name].parts[name].allInternalSets[name].cells
        mdb.models[name].parts[name].allSets[name].cells
        mdb.models[name].parts[name].cells
        mdb.models[name].parts[name].sets[name].cells
        import assembly
        mdb.models[name].rootAssembly.allInstances[name].cells
        mdb.models[name].rootAssembly.allInstances[name].sets[name].cells
        mdb.models[name].rootAssembly.allInternalSets[name].cells
        mdb.models[name].rootAssembly.allSets[name].cells
        mdb.models[name].rootAssembly.instances[name].cells
        mdb.models[name].rootAssembly.instances[name].sets[name].cells
        mdb.models[name].rootAssembly.modelInstances[i].sets[name].cells
        mdb.models[name].rootAssembly.sets[name].cells

    """
    def __init__(self, cells: list[Cell]):
        """This method creates a CellArray object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            part.CellArray
        
        Parameters
        ----------
        cells
            A list of Cell objects. 

        Returns
        -------
            A CellArray object.
            
        """
        pass

    def findAt(self, coordinates: Tuple, printWarning: Boolean = True) -> Cell:
        """This method returns the object or objects in the CellArray located at the given
        coordinates. findAt initially uses the ACIS tolerance of 1E-6. As a result, findAt
        returns any entity that is at the arbitrary point specified or at a distance of less
        than 1E-6 from the arbitrary point. If nothing is found, findAt uses the tolerance for
        imprecise geometry (applicable only for imprecise geometric entities). The arbitrary
        point must not be shared by a second cell. If two cells intersect or coincide at the
        arbitrary point, findAt chooses the first cell that it encounters, and you should not
        rely on the return value being consistent.
        findAt will always try to find objects among all the cells in the part or assembly
        instance and will not restrict itself to a subset even if the CellArray represents such
        subset.
        
        Parameters
        ----------
        coordinates
            A sequence of Floats specifying the *X*-, *Y*-, and *Z*-coordinates of the object to 
            find.findAt returns either a Cell object or a sequence of Cell objects based on the type 
            of input. If *coordinates* is a sequence of Floats, findAt returns the Cell object at 
            that point. If *coordinates* is a sequence of sequence of Floats, findAt returns a 
            sequence of Cell objects at the given locations. The sequence of sequence of Floats must 
            be a sequence of sequence of point and normal data, not a sequence of point data. For 
            example,`cells1 = myCrackedBlockInstance.cells.findAt(                            ((5.5, 
            -8.3, 294.2),),                            ((12.1, -8.3, 287.8),),                       
                 ((14.4, -10.4, 285.5),),)` 
        printWarning
            A Boolean specifying whether a message is to be printed to the CLI if no entity is found 
            at the specified location. The default value is True. 

        Returns
        -------
            A Cell object.
            
        """
        pass

    def getExteriorFaces(self) -> FaceArray:
        """This method returns the cell faces on the exterior of the CellArray. That is, it returns
        the faces that are referenced by exactly one of the cells in the sequence.

        Returns
        -------
            A FaceArray object representing the faces on the exterior of the cells.
            
        """
        pass

    def getSequenceFromMask(self, mask: str) -> Union[Cell, CellArray]:
        """This method returns the object or objects in the CellArray identified using the
        specified *mask*. This command is generated when the JournalOptions are set to
        COMPRESSEDINDEX. When large number of objects are involved, this method is highly
        efficient.
        
        Parameters
        ----------
        mask
            A String specifying the object or objects. 

        Returns
        -------
            A Cell object or a sequence of Cell objects. 

        Raises
        ------
            - An exception occurs if the resulting sequence is empty. 
              Error: The mask results in an empty sequence 
            
        """
        pass

    def getMask(self) -> str:
        """This method returns a string specifying the object or objects.

        Returns
        -------
            A String specifying the object or objects.
            
        """
        pass

    def getByBoundingBox(self,
                         xMin: str = '',
                         yMin: str = '',
                         zMin: str = '',
                         xMax: str = '',
                         yMax: str = '',
                         zMax: str = '') -> CellArray:
        """This method returns an array of cell objects that lie within the specified bounding box.
        
        Parameters
        ----------
        xMin
            A float specifying the minimum *X*-boundary of the bounding box. 
        yMin
            A float specifying the minimum *Y*-boundary of the bounding box. 
        zMin
            A float specifying the minimum *Z*-boundary of the bounding box. 
        xMax
            A float specifying the maximum *X*-boundary of the bounding box. 
        yMax
            A float specifying the maximum *Y*-boundary of the bounding box. 
        zMax
            A float specifying the maximum *Z*-boundary of the bounding box. 

        Returns
        -------
            A CellArray object, which is a sequence of Cell objects.
            
        """
        pass

    def getByBoundingCylinder(self, center1: Tuple, center2: Tuple,
                              radius: str) -> CellArray:
        """This method returns an array of cell objects that lie within the specified bounding
        cylinder.
        
        Parameters
        ----------
        center1
            A Tuple of the *X*-, *Y*-, and *Z*-coordinates of the center of the first end of the 
            cylinder. 
        center2
            A Tuple of the *X*-, *Y*-, and *Z*-coordinates of the center of the second end of the 
            cylinder. 
        radius
            A float specifying the radius of the cylinder. 

        Returns
        -------
            A CellArray object, which is a sequence of Cell objects.
            
        """
        pass

    def getByBoundingSphere(self, center: Tuple, radius: str) -> CellArray:
        """This method returns an array of cell objects that lie within the specified bounding
        sphere.
        
        Parameters
        ----------
        center
            A Tuple of the *X*-, *Y*-, and *Z*-coordinates of the center of the sphere. 
        radius
            A float specifying the radius of the sphere. 

        Returns
        -------
            A CellArray object, which is a sequence of Cell objects.
            
        """
        pass

    def getBoundingBox(
            self
    ) -> Dict["low":COORDINATE_3D, "high":Tuple[float, float, float]]:
        """This method returns a dictionary of two tuples representing minimum and maximum boundary
        values of the bounding box of the minimum size containing the cell sequence.

        Returns
        -------
            A Dictionary object with the following items: 
            *low*: a Tuple of three floats representing the minimum *X*-, *Y*-, and *Z*-boundary 
            values of the bounding box. 
            *high*: a Tuple of three floats representing the maximum *X*-, *Y*-, and *Z*-boundary 
            values of the bounding box.
            
        """
        pass