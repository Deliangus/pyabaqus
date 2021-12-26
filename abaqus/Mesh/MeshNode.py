from ..Datum.DatumCsys import DatumCsys

class MeshNode:

    """The MeshNode object refers to a node of a native mesh or an orphan mesh. A MeshNode 
    object can be accessed via a part or part instance using an index that refers to the 
    internal numbering of the node repository. The index does not refer to the node label. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].allInternalSets[name].nodes[i]
        - mdb.models[name].parts[name].allInternalSurfaces[name].nodes[i]
        - mdb.models[name].parts[name].allSets[name].nodes[i]
        - mdb.models[name].parts[name].allSurfaces[name].nodes[i]
        - mdb.models[name].parts[name].nodes[i]
        - mdb.models[name].parts[name].retainedNodes[i]
        - mdb.models[name].parts[name].sets[name].nodes[i]
        - mdb.models[name].parts[name].surfaces[name].nodes[i]
        - import assembly
        - mdb.models[name].rootAssembly.allInstances[name].nodes[i]
        - mdb.models[name].rootAssembly.allInstances[name].sets[name].nodes[i]
        - mdb.models[name].rootAssembly.allInstances[name].surfaces[name].nodes[i]
        - mdb.models[name].rootAssembly.allInternalSets[name].nodes[i]
        - mdb.models[name].rootAssembly.allInternalSurfaces[name].nodes[i]
        - mdb.models[name].rootAssembly.allSets[name].nodes[i]
        - mdb.models[name].rootAssembly.allSurfaces[name].nodes[i]
        - mdb.models[name].rootAssembly.instances[name].nodes[i]
        - mdb.models[name].rootAssembly.instances[name].sets[name].nodes[i]
        - mdb.models[name].rootAssembly.instances[name].surfaces[name].nodes[i]
        - mdb.models[name].rootAssembly.modelInstances[i].nodes[i]
        - mdb.models[name].rootAssembly.modelInstances[i].sets[name].nodes[i]
        - mdb.models[name].rootAssembly.modelInstances[i].surfaces[name].nodes[i]
        - mdb.models[name].rootAssembly.nodes[i]
        - mdb.models[name].rootAssembly.sets[name].nodes[i]
        - mdb.models[name].rootAssembly.surfaces[name].nodes[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An Int specifying the node label. 
    label: int = None

    # A String specifying the name of the part instance that owns this node. 
    instanceName: str = ''

    # A tuple of three Floats specifying the coordinates of the new node. 
    coordinates: float = None

    def Node(self, coordinates: tuple, localCsys: DatumCsys = None, label: int = None):
        """This method creates a node on an orphan mesh part.

        Path
        ----
            - mdb.models[*name*].parts[*name*].Node

        Parameters
        ----------
        coordinates
            A sequence of three Floats specifying the coordinates of the new node. 
        localCsys
            A DatumCsys object specifying the local coordinate system. If unspecified, the global 
            coordinate system will be used. 
        label
            An Int specifying the node label. 

        Returns
        -------
            A MeshNode object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getElemEdges(self):
        """This method returns a tuple of element edge objects that share the node.

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
        """This method returns a tuple of element face objects that share the node.

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

    def getElements(self):
        """This method returns a tuple of element objects that share the node.

        Parameters
        ----------

        Returns
        -------
            A tuple of MeshElement objects. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getNodesByFeatureEdge(self, angle: str):
        """This method returns an array of mesh node objects that are obtained by recursively
        finding adjacent nodes along a feature edge that are at an angle of less than or equal
        to the specified face angle.

        Parameters
        ----------
        angle
            A float specifying the value of the face angle in degrees. 

        Returns
        -------
            A MeshNodeArray object, which is a sequence of MeshNode objects. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self, label: int = None):
        """This method modifies the MeshNode object.

        Parameters
        ----------
        label
            An Int specifying the node label. This member may only be edited if the node belongs to 
            an orphan mesh part. The specified label must be non-negative and must not be in use by 
            any other node of the same part. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
