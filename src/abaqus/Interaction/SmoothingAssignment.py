from abaqusConstants import *

from __init__ import *
from __future__ import annotations


class SmoothingAssignment:
    """The SmoothingAssignment object stores the surface smoothing assignment definition for
    surfaces in ContactExp and ContactStd objects. The SmoothingAssignment object has no 
    constructor or members. 

    Notes
    -----
        This object can be accessed by:
        
        .. code-block:: python
            
            import interaction
            mdb.models[name].interactions[name].smoothingAssignments

    The corresponding analysis keywords are:
        - SURFACE PROPERTY ASSIGNMENT

    """
    def changeValuesInStep(self, stepName: str, index: int,
                           value: SymbolicConstant):
        """This method allows modification of surface smoothing assignments already defined on
        surfaces in a given step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the surface smoothing assignments are 
            to be modified. 
        index
            An Int specifying the position of the surface smoothing assignment whose value is to be 
            modified. 
        value
            A Tuple specifying the value of the surface smoothing assignments for the surface whose 
            index is referenced. Each Tuple contains one entry:A SymbolicConstant specifying the 
            surface smoothing value to be used for the surface. Possible values of the 
            SymbolicConstant are NONE, REVOLUTION, SPHERICAL, and TOROIDAL. 
        """
        pass

    def appendInStep(self, stepName: str, assignments: SymbolicConstant):
        """This method allows addition of surface smoothing assignments to new surfaces in a given
        step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which new surface smoothing assignments are 
            to be defined. 
        assignments
            A sequence of tuples specifying the surface smoothing assignments. Each Tuple contains 
            two entries: 
            - A region object specifying the surface to which the smoothing is assigned. 
            - A SymbolicConstant specifying the surface smoothing value to be used for the surface. 
            Possible values of the SymbolicConstant are NONE, REVOLUTION, SPHERICAL, and TOROIDAL. 
        """
        pass

    def delete(self, indices: Tuple):
        """The delete method allows you to delete existing surface smoothing assignments from
        ContactExp and ContactStd objects.
        
        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each surface smoothing assignment to delete. 
        """
        pass