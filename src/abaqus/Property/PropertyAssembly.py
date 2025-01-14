from abaqusConstants import *
from .SectionAssignment import SectionAssignment
from ..Assembly.AssemblyBase import AssemblyBase
from ..Region.Set import Set


class PropertyAssembly(AssemblyBase):
    """An Assembly object is a container for instances of parts. The Assembly object has no
    constructor command. Abaqus creates the *rootAssembly* member when a Model object is 
    created. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import assembly
        mdb.models[name].rootAssembly

    """

    def SectionAssignment(self, region: Set, sectionName: str, thicknessAssignment: SymbolicConstant = FROM_SECTION,
                          offset: float = 0, offsetType: SymbolicConstant = SINGLE_VALUE, offsetField: str = ''):
        """This method creates a SectionAssignment object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].parts[*name*].SectionAssignment
                mdb.models[name].rootAssembly.SectionAssignment
        
        Parameters
        ----------
        region
            A Set object specifying the region to which the section is assigned.
        sectionName
            A String specifying the name of the section.
        thicknessAssignment
            A SymbolicConstant specifying section thickness assignment method. Possible values are
            FROM_SECTION and FROM_GEOMETRY. The default value is FROM_SECTION.
        offset
            A Float specifying the offset of the shell section. The default value is 0.0.
        offsetType
            A SymbolicConstant specifying the method used to define the shell offset. If
            *offsetType* is set to OFFSET_FIELD the *offsetField* must have a value. Possible values
            are SINGLE_VALUE, MIDDLE_SURFACE, TOP_SURFACE, BOTTOM_SURFACE, FROM_GEOMETRY, and
            OFFSET_FIELD. The default value is SINGLE_VALUE.
        offsetField
            A String specifying the name of the field specifying the offset. The default value is
            "".

        Returns
        -------
            A SectionAssignment object.
        """
        sectionAssignment = SectionAssignment(region, sectionName, thicknessAssignment, offset, offsetType, offsetField)
        self.sectionAssignments.append(sectionAssignment)
        return sectionAssignment
