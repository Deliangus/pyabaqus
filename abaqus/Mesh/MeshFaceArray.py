

class MeshFaceArray:

    """The MeshFaceArray is a sequence of MeshFace objects. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].elementFaces
        - import assembly
        - mdb.models[name].rootAssembly.allInstances[name].elementFaces
        - mdb.models[name].rootAssembly.instances[name].elementFaces

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def __init__(self, elemFaces: str):
        """This method creates a MeshFaceArray object.

        Path
        ----
            - mesh.MeshFaceArray

        Parameters
        ----------
        elemFaces
            A list of MeshFace objects. 

        Returns
        -------
            A MeshFaceArray object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getSequenceFromMask(self, mask: str):
        """This method returns the objects in the MeshFaceArray identified using the specified
        *mask*. When large number of objects are involved, this method is highly efficient.

        Parameters
        ----------
        mask
            A String specifying the object or objects. 

        Returns
        -------
            A MeshFaceArray object. 

        Exceptions
        ----------
            - An exception occurs if the resulting sequence is empty. 
              Error: The mask results in an empty sequence 
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
        """
        pass
