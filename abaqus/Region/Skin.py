from ..BasicGeometry.Edge import Edge
from ..BasicGeometry.EdgeArray import EdgeArray
from ..BasicGeometry.Face import Face
from ..BasicGeometry.FaceArray import FaceArray
from ..Mesh.MeshEdge import MeshEdge
from ..Mesh.MeshElementArray import MeshElementArray
from ..Mesh.MeshFace import MeshFace

class Skin:

    """The Skin object stores information on skin reinforcements created on entities. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].skins[name]
        - import assembly
        - mdb.models[name].rootAssembly.allInstances[name].skins[name]
        - mdb.models[name].rootAssembly.instances[name].skins[name]
        - mdb.models[name].rootAssembly.skins[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A MeshElementArray object. 
    elements: MeshElementArray = None

    # An EdgeArray object. 
    edges: EdgeArray = None

    # A FaceArray object. 
    faces: FaceArray = None

    def __init__(self, name: str, faces: tuple[Face] = (), edges: tuple[Edge] = (), 
                 elementFaces: tuple[MeshFace] = (), elementEdges: tuple[MeshEdge] = ()):
        """This method creates a skin from a sequence of objects in a model database. At least one
        of the optional arguments needs to be specified.

        Path
        ----
            - mdb.models[*name*].parts[*name*].Skin

        Parameters
        ----------
        name
            A String specifying the repository key. The default value is an empty string. 
        faces
            A sequence of Face objects specifying the faces on which skins should be created. 
            Applicable to three and two dimensional parts. 
        edges
            A sequence of Edge objects specifying the edges on which skins should be created. 
            Applicable to axisymmetric parts. 
        elementFaces
            A sequence of MeshFace objects specifying the mesh faces on which skins should be 
            created. Applicable to three and two dimensional parts. 
        elementEdges
            A sequence of MeshEdge objects specifying the mesh edges on which skins should be 
            created. Applicable to axisymmetric parts. 

        Returns
        -------
            A Skin object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass

    def EditSkin(self, name: str, faces: tuple[Face] = (), edges: tuple[Edge] = (), 
                 elementFaces: tuple[MeshFace] = (), elementEdges: tuple[MeshEdge] = ()):
        """This method modifies underlying entities of the selected skin. At least one of the
        optional arguments needs to be specified.

        Path
        ----
            - mdb.models[*name*].parts[*name*].EditSkin

        Parameters
        ----------
        name
            A String specifying the repository key. The default value is an empty string. 
        faces
            A sequence of Face objects specifying the faces on which skins should be created. 
            Applicable to three and two dimensional parts. 
        edges
            A sequence of Edge objects specifying the edges on which skins should be created. 
            Applicable to axisymmetric parts. 
        elementFaces
            A sequence of MeshFace objects specifying the mesh faces on which skins should be 
            created. Applicable to three and two dimensional parts. 
        elementEdges
            A sequence of MeshEdge objects specifying the mesh edges on which skins should be 
            created. Applicable to axisymmetric parts. 

        Returns
        -------
            A Skin object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass
