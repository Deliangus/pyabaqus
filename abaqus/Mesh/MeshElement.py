from abaqusConstants import *
from .MeshNode import MeshNode


class MeshElement:
    """The MeshElement object refers to an element of a native mesh or an orphan mesh. A
    MeshElement object can be accessed via a part or part instance using an index that 
    refers to the internal numbering of the element repository. The index does not refer to 
    the element label. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].allInternalSets[name].elements[i]
        - mdb.models[name].parts[name].allInternalSurfaces[name].elements[i]
        - mdb.models[name].parts[name].allSets[name].elements[i]
        - mdb.models[name].parts[name].allSurfaces[name].elements[i]
        - mdb.models[name].parts[name].elements[i]
        - mdb.models[name].parts[name].sets[name].elements[i]
        - mdb.models[name].parts[name].surfaces[name].elements[i]
        - import assembly
        - mdb.models[name].rootAssembly.allInstances[name].elements[i]
        - mdb.models[name].rootAssembly.allInstances[name].sets[name].elements[i]
        - mdb.models[name].rootAssembly.allInstances[name].surfaces[name].elements[i]
        - mdb.models[name].rootAssembly.allInternalSets[name].elements[i]
        - mdb.models[name].rootAssembly.allInternalSurfaces[name].elements[i]
        - mdb.models[name].rootAssembly.allSets[name].elements[i]
        - mdb.models[name].rootAssembly.allSurfaces[name].elements[i]
        - mdb.models[name].rootAssembly.elements[i]
        - mdb.models[name].rootAssembly.instances[name].elements[i]
        - mdb.models[name].rootAssembly.instances[name].sets[name].elements[i]
        - mdb.models[name].rootAssembly.instances[name].surfaces[name].elements[i]
        - mdb.models[name].rootAssembly.modelInstances[i].elements[i]
        - mdb.models[name].rootAssembly.modelInstances[i].sets[name].elements[i]
        - mdb.models[name].rootAssembly.modelInstances[i].surfaces[name].elements[i]
        - mdb.models[name].rootAssembly.sets[name].elements[i]
        - mdb.models[name].rootAssembly.surfaces[name].elements[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An Int specifying the element label. 
    label: int = None

    # A SymbolicConstant specifying the Abaqus element code. 
    type: SymbolicConstant = None

    # A String specifying the name of the part instance that owns this element. 
    instanceName: str = ''

    # A tuple of Ints specifying the internal node indices that define the nodal connectivity. 
    # It is important to note the difference with OdbMeshElement object of ODB where the 
    # connectivity is node labels instead of node indices. 
    connectivity: int = None

    def Element(self, nodes: tuple[MeshNode], elemShape: SymbolicConstant, label: int = None):
        """This method creates an element on an orphan mesh part from a sequence of nodes.

        Path
        ----
            - mdb.models[*name*].parts[*name*].Element

        Parameters
        ----------
        nodes
            A sequence of MeshNode objects. 
        elemShape
            A SymbolicConstant specifying the shape of the new element. Possible values are LINE2, 
            LINE3, TRI3, TRI6, QUAD4, QUAD8, TET4, TET10, WEDGE6, WEDGE15, HEX8, and HEX20. 
        label
            An Int specifying the element label. 

        Returns
        -------
            A MeshElement object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getNodes(self):
        """This method returns a tuple of node objects of the element.

        Parameters
        ----------

        Returns
        -------
            A tuple of MeshNode objects. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getElemEdges(self):
        """This method returns a tuple of unique element edge objects on the element.

        Parameters
        ----------

        Returns
        -------
            A tuple of MeshEdge objects. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getElemFaces(self):
        """This method returns a tuple of unique element face objects on the element.

        Parameters
        ----------

        Returns
        -------
            A tuple of MeshFace objects. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getAdjacentElements(self):
        """This method returns an array of element objects adjacent to the mesh element.

        Parameters
        ----------

        Returns
        -------
            A MeshElementArray object which is a sequence of MeshElement objects. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getElementsByFeatureEdge(self, angle: str):
        """This method returns an array of mesh element objects that are obtained by recursively
        finding adjacent elements along a feature edge with a face angle of less than or equal
        to the specified angle.

        Parameters
        ----------
        angle
            A float specifying the value of the face angle in degrees. 

        Returns
        -------
            A MeshElementArray object, which is a sequence of MeshElement objects. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self, label: int = None):
        """This method modifies the MeshElement object.

        Parameters
        ----------
        label
            An Int specifying the element label. This member may only be edited if the element 
            belongs to an orphan mesh part. The specified label must be non-negative and must not be 
            in use by any other element of the same part. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
