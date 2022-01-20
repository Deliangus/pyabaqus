from abaqusConstants import *


class Vertex:
    """Vertices are point regions of geometry.

    Access
    ------
        - import part
        - mdb.models[name].parts[name].allInternalSets[name].vertices[i]
        - mdb.models[name].parts[name].allSets[name].vertices[i]
        - mdb.models[name].parts[name].sets[name].vertices[i]
        - mdb.models[name].parts[name].vertices[i]
        - import assembly
        - mdb.models[name].rootAssembly.allInstances[name].sets[name].vertices[i]
        - mdb.models[name].rootAssembly.allInstances[name].vertices[i]
        - mdb.models[name].rootAssembly.allInternalSets[name].vertices[i]
        - mdb.models[name].rootAssembly.allSets[name].vertices[i]
        - mdb.models[name].rootAssembly.instances[name].sets[name].vertices[i]
        - mdb.models[name].rootAssembly.instances[name].vertices[i]
        - mdb.models[name].rootAssembly.modelInstances[i].sets[name].vertices[i]
        - mdb.models[name].rootAssembly.modelInstances[i].vertices[i]
        - mdb.models[name].rootAssembly.sets[name].vertices[i]
        - mdb.models[name].rootAssembly.vertices[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An Int specifying the index of the ConstrainedSketchVertex in the VertexArray.
    index: int = None

    # A Boolean specifying whether the vertex belongs to the reference representation of the 
    # Part or Instance. 
    isReferenceRep: Boolean = OFF

    # A tuple of Floats specifying the *X* -, *Y* -, and *Z* -coordinates of the vertex. 
    pointOn: float = None

    # A tuple of Floats specifying the name of the feature that created this vertex. 
    featureName: float = None

    # A tuple of Floats specifying the name of the part instance for this vertex (if 
    # applicable). 
    instanceName: float = None

    def getEdges(self):
        """This method returns a sequence consisting of the edge ids of the edges which share this
        vertex.

        Parameters
        ----------

        Returns
        -------
            A tuple of integers. 

        Exceptions
        ----------
            None. 
            !img 
        """
        pass

    def getNodes(self):
        """This method returns an array of node objects that are associated with the vertex.

        Parameters
        ----------

        Returns
        -------
            A MeshNodeArray object which is a sequence of MeshNode objects. 

        Exceptions
        ----------
            None. 
            !img 
        """
        pass

    def getElements(self):
        """This method returns an array of element objects that are associated with the vertex.

        Parameters
        ----------

        Returns
        -------
            A MeshElementArray object which is a sequence of MeshElement objects. 

        Exceptions
        ----------
            None. 
            !img 
        """
        pass
