from ..BasicGeometry.Edge import Edge
from ..BasicGeometry.EdgeArray import EdgeArray
from ..BasicGeometry.Face import Face
from ..BasicGeometry.FaceArray import FaceArray
from ..Mesh.MeshEdge import MeshEdge
from ..Mesh.MeshElementArray import MeshElementArray
from ..Mesh.MeshFace import MeshFace


class Skin:
    """The Skin object stores information on skin reinforcements created on entities.

    Attributes
    ----------
    elements: MeshElementArray
        A :py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` object.
    edges: EdgeArray
        An :py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` object.
    faces: FaceArray
        A :py:class:`~abaqus.BasicGeometry.FaceArray.FaceArray` object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import part
        mdb.models[name].parts[name].skins[name]
        import assembly
        mdb.models[name].rootAssembly.allInstances[name].skins[name]
        mdb.models[name].rootAssembly.instances[name].skins[name]
        mdb.models[name].rootAssembly.skins[name]

    """

    # A MeshElementArray object. 
    elements: MeshElementArray = MeshElementArray([])

    # An EdgeArray object. 
    edges: EdgeArray = EdgeArray([])

    # A FaceArray object. 
    faces: FaceArray = FaceArray([])

    def __init__(self, name: str, faces: tuple[Face] = (), edges: tuple[Edge] = (),
                 elementFaces: tuple[MeshFace] = (), elementEdges: tuple[MeshEdge] = ()):
        """This method creates a skin from a sequence of objects in a model database. At least one
        of the optional arguments needs to be specified.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].parts[*name*].Skin
        
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
        """
        pass

    def EditSkin(self, name: str = '', faces: tuple[Face] = (), edges: tuple[Edge] = (),
                 elementFaces: tuple[MeshFace] = (), elementEdges: tuple[MeshEdge] = ()):
        """This method modifies underlying entities of the selected skin. At least one of the
        optional arguments needs to be specified.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].parts[*name*].Skin
        
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
        """
        pass
