from abaqusConstants import *


class IgnoredVertexArray:
    """The IgnoredVertexArray is a sequence of IgnoredVertex objects. If the part is modified,
    then IgnoredVertexArray must be updated for that part. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].ignoredVertices
        - import assembly
        - mdb.models[name].rootAssembly.allInstances[name].ignoredVertices
        - mdb.models[name].rootAssembly.instances[name].ignoredVertices

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def findAt(self, coordinates: tuple, printWarning: Boolean = True):
        """This method returns the object or objects in the IgnoredVertexArray located at the given
        coordinates.
        findAt initially uses the ACIS tolerance of 1E-6. As a result, findAt returns any
        IgnoredVertex object that is at the arbitrary point specified or at a distance of less
        than 1E-6 from the arbitrary point. If nothing is found, findAt uses the tolerance for
        imprecise geometry (applicable only for imprecise geometric entities).
        findAt will always try to find objects among all the ignored vertices in the part or
        assembly instance and will not restrict itself to a subset even if the
        IgnoredVertexArray represents such subset.

        Parameters
        ----------
        coordinates
            A sequence of Floats specifying the *X*-, *Y*-, and *Z*-coordinates of the object to 
            find.findAt returns either a IgnoredVertex object or a sequence of IgnoredVertex objects 
            based on the type of input.If *coordinates* is a sequence of Floats, findAt returns the 
            IgnoredVertex object at that point.If you omit the *coordinates* keyword argument, 
            findAt accepts as arguments a sequence of sequence of floats in the following 
            format:`verts = v.findAt(((20.19686, -169.513997, 27.798593), ),                 
            ((19.657627, -167.295749, 27.056402), ),                 ((18.274129, -157.144741, 
            25.15218), ))` 
        printWarning
            A Boolean specifying whether a message is to be printed to the CLI if no entity is found 
            at the specified location. The default value is True. 

        Returns
        -------
            An IgnoredVertex object or a sequence of IgnoredVertex objects. 

        Exceptions
        ----------
            None. 
            !img 
        """
        pass

    def getSequenceFromMask(self, mask: str):
        """This method returns the object or objects in the IgnoredVertexArray identified using the
        specified *mask*. This command is generated when the JournalOptions are set to
        COMPRESSEDINDEX. When large number of objects are involved, this method is highly
        efficient.

        Parameters
        ----------
        mask
            A String specifying the object or objects. 

        Returns
        -------
            An IgnoredVertex object or a sequence of IgnoredVertex objects. 

        Exceptions
        ----------
            None. 
            !img 
        """
        pass

    def getMask(self):
        """This method returns a string specifying the object or objects.

        Parameters
        ----------

        Returns
        -------
            A String specifying the object or objects. 

        Exceptions
        ----------
            None. 
            !img 
        """
        pass

    def getClosest(self, coordinates: tuple, searchTolerance: str = ''):
        """This method returns a object or objects in the IgnoredVertexArray closest to the given
        set of points, where the given points need not lie on the vertices in the
        IgnoredVertexArray.

        Parameters
        ----------
        coordinates
            A sequence of a sequence of floats, where each sequence of floats describes the *X*-, 
            *Y*-, and *Z*-coordinates of a 
            point.`r=e.getClosest(coordinates=((20.0,20.0,10.0),(-1.0, -15.0, 15),))``r.keys()``[0, 
            1]``r[0]``(mdb.models['Model-1'].parts['Part-1'].ignoredVertices[3],                     
                        (15.7090625762939, 20.0, 10.0))` 
        searchTolerance
            A double specifying the distance within which the closest object must lie. The default 
            value is half of the parent part/instance size. 

        Returns
        -------
            This method returns a dictionary object. The key to the dictionary object is the 
            position of the input point in the tuple specified in the *coordinates* starting at 
            index 0. If a closest IgnoredVertex could be found then the value is a sequence 
            consisting of two objects. The first object in the sequence is a IgnoredVertex that is 
            close to the input point referred to by the key. The second object in the sequence, is a 
            sequence of floats which specify the *X*-, *Y*-, and *Z*-location of the IgnoredVertex. 
            See program listing above. 

        Exceptions
        ----------
            - An exception occurs if the resulting sequence is empty. 
              Error: The mask results in an empty sequence 
            !img 
        """
        pass
