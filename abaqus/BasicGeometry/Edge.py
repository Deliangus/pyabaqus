from abaqusConstants import *

class Edge:

    """Edges are one-dimensional regions of geometry. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].allInternalSets[name].edges[i]
        - mdb.models[name].parts[name].allInternalSurfaces[name].edges[i]
        - mdb.models[name].parts[name].allSets[name].edges[i]
        - mdb.models[name].parts[name].allSurfaces[name].edges[i]
        - mdb.models[name].parts[name].edges[i]
        - mdb.models[name].parts[name].sets[name].edges[i]
        - mdb.models[name].parts[name].surfaces[name].edges[i]
        - import assembly
        - mdb.models[name].rootAssembly.allInstances[name].edges[i]
        - mdb.models[name].rootAssembly.allInstances[name].sets[name].edges[i]
        - mdb.models[name].rootAssembly.allInstances[name].surfaces[name].edges[i]
        - mdb.models[name].rootAssembly.allInternalSets[name].edges[i]
        - mdb.models[name].rootAssembly.allInternalSurfaces[name].edges[i]
        - mdb.models[name].rootAssembly.allSets[name].edges[i]
        - mdb.models[name].rootAssembly.allSurfaces[name].edges[i]
        - mdb.models[name].rootAssembly.edges[i]
        - mdb.models[name].rootAssembly.instances[name].edges[i]
        - mdb.models[name].rootAssembly.instances[name].sets[name].edges[i]
        - mdb.models[name].rootAssembly.instances[name].surfaces[name].edges[i]
        - mdb.models[name].rootAssembly.modelInstances[i].edges[i]
        - mdb.models[name].rootAssembly.modelInstances[i].sets[name].edges[i]
        - mdb.models[name].rootAssembly.modelInstances[i].surfaces[name].edges[i]
        - mdb.models[name].rootAssembly.sets[name].edges[i]
        - mdb.models[name].rootAssembly.surfaces[name].edges[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An Int specifying the index of the edge in the EdgeArray. 
    index: int = None

    # A Boolean specifying whether the edge belongs to the reference representation of the 
    # Part or Instance. 
    isReferenceRep: Boolean = OFF

    # A tuple of Floats specifying the *X*-, *Y*-, and *Z*-coordinates of a point located on 
    # the edge. 
    pointOn: float = None

    # A tuple of Floats specifying the name of the feature that created this edge. 
    featureName: float = None

    # A tuple of Floats specifying the name of the part instance for this edge (if 
    # applicable). 
    instanceName: float = None

    def isTangentFlipped(self):
        """This method determines whether the tangent to the edge is flipped from its default
        direction by the use of the flipTangent method on a Part object.

        Parameters
        ----------

        Returns
        -------
            A Boolean value of True if the tangent is flipped and False if not. 

        Exceptions
        ----------
            None. 
            !img 
        """
        pass

    def getCurvature(self, parameter: float, point: tuple):
        """This method returns curvature information at a location on the edge.

        Parameters
        ----------
        parameter
            A Float specifying the normalized parameter location on the edge where the curvature is 
            to be computed. This argument is mutually exclusive with the argument *point*. 
        point
            A tuple of *X*-, *Y*-, and *Z*-coordinates of a point at which the curvature is to be 
            computed. If *point* does not lie on the edge an attempt is made to project it onto the 
            edge and use the projected point. 

        Returns
        -------
            A dictionary with keys 'evaluationPoint', 'curvature', 'radius', and 'tangent', where 
            'evaluationPoint' specifies the location at which the curvature was computed; 
            'curvature' specifies the curvature vector at that location; 'radius' is the radius of 
            curvature; and 'tangent' specifies the tangent to the edge at that location. 

        Exceptions
        ----------
            The given edge is straight. 
            !img 
        """
        pass

    def getFaces(self):
        """This method returns a sequence consisting of the face ids of the faces which share this
        edge.

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

    def getAdjacentEdges(self):
        """This method returns an array of Edge objects that share at least one vertex of the edge.

        Parameters
        ----------

        Returns
        -------
            An EdgeArray object, which is a sequence of Edge objects. 

        Exceptions
        ----------
            None. 
            !img 
        """
        pass

    def getEdgesByEdgeAngle(self, angle: str):
        """This method returns an array of Edge objects that are obtained by recursively finding
        adjacent edges that are at an angle of less than or equal to the specified face angle.

        Parameters
        ----------
        angle
            A float specifying the value of the face angle in degrees. 

        Returns
        -------
            An EdgeArray object, which is a sequence of Edgeobjects. 

        Exceptions
        ----------
            None. 
            !img 
        """
        pass

    def getNodes(self):
        """This method returns an array of node objects that are associated with the edge.

        Parameters
        ----------

        Returns
        -------
            A MeshNodeArray object, which is a sequence of MeshNode objects. 

        Exceptions
        ----------
            None. 
            !img 
        """
        pass

    def getElements(self):
        """This method returns an array of element objects that are associated with the edge.

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

    def getRadius(self):
        """This method returns the radius of circular edges.

        Parameters
        ----------

        Returns
        -------
            A Float specifying the radius. 

        Exceptions
        ----------
            The given edges is not circular. 
            !img 
        """
        pass

    def getSize(self, printResults: str = True):
        """This method returns a Float indicating the length of the edge.

        Parameters
        ----------
        printResults
            A Bool specifying whether verbose output is printed. The default is True. 

        Returns
        -------
            A Float. 

        Exceptions
        ----------
            None. 
            !img 
        """
        pass

    def getVertices(self):
        """This method returns a sequence of indices of the vertices that bound this edge. The
        first index refers to the vertex where the normalized curve parameter = 0.0, and the
        second index refers to the vertex where the normalized curve parameter = 1.0. If the
        edge is a closed curve, only one vertex index is returned.

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
