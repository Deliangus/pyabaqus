

class IgnoredEdge:

    """An IgnoredEdge object is a one-dimensional region of geometry that has been abstracted 
    away by a virtual topology feature. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].ignoredEdges[i]
        - import assembly
        - mdb.models[name].rootAssembly.allInstances[name].ignoredEdges[i]
        - mdb.models[name].rootAssembly.instances[name].ignoredEdges[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An Int specifying the index of the IgnoredEdge in the IgnoredEdgeArray. 
    index: int = None

    # A tuple of Floats specifying the *X*-, *Y*-, and *Z*-coordinates of a point located on 
    # the edge. 
    pointOn: float = None

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

    def getRadius(self):
        """This method returns the radius of a circular IgnoredEdge object.

        Parameters
        ----------

        Returns
        -------
            A Float specifying the radius. 

        Exceptions
        ----------
            The given IgnoredEdge object is not circular. 
            !img 
        """
        pass

    def getCurvature(self, parameter: float, point: tuple):
        """This method returns curvature information at a location on the IgnoredEdge object.

        Parameters
        ----------
        parameter
            A Float specifying the normalized parameter location on the IgnoredEdge where the 
            curvature is to be computed. This argument is mutually exclusive with the argument 
            *point*. 
        point
            A tuple of *X*-, *Y*-, and *Z*-coordinates of a point at which the curvature is to be 
            computed. If *point* does not lie on the IgnoredEdge an attempt is made to project it 
            onto the IgnoredEdge and use the projected point. 

        Returns
        -------
            A dictionary with keys 'evaluationPoint', 'curvature', 'radius', 'tangent'. Where 
            'evaluationPoint' specifies the location at which the curvature was computed. 
            'curvature' specifies the curvature vector at that location. 'radius' is the Radius of 
            curvature and 'tangent' specifies the tangent to the IgnoredEdge at that location. 

        Exceptions
        ----------
            The given IgnoredEdge is straight. 
            !img 
        """
        pass
