import typing

from abaqusConstants import *
from ..BasicGeometry.EdgeArray import EdgeArray
from ..BasicGeometry.FaceArray import FaceArray
from ..Mesh.MeshElementArray import MeshElementArray
from ..Mesh.MeshNodeArray import MeshNodeArray


class Surface:

    """The Surface object stores surfaces selected from the assembly. A surface is comprised of 
    geometric or discrete entities but not both. An instance of a Surface object is 
    available from the *surface* member of the Assembly object. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].allInternalSurfaces[name]
        - mdb.models[name].parts[name].allSurfaces[name]
        - mdb.models[name].parts[name].surfaces[name]
        - import assembly
        - mdb.models[name].rootAssembly.allInstances[name].surfaces[name]
        - mdb.models[name].rootAssembly.allInternalSurfaces[name]
        - mdb.models[name].rootAssembly.allSurfaces[name]
        - mdb.models[name].rootAssembly.instances[name].surfaces[name]
        - mdb.models[name].rootAssembly.modelInstances[i].surfaces[name]
        - mdb.models[name].rootAssembly.surfaces[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An EdgeArray object. 
    edges: EdgeArray = None

    # A FaceArray object. 
    faces: FaceArray = None

    # A MeshElementArray object. 
    elements: MeshElementArray = None

    # A MeshNodeArray object. 
    nodes: MeshNodeArray = None

    # A tuple of SymbolicConstants specifying the sides; for example, (SIDE1, SIDE2). 
    sides: SymbolicConstant = None

    # A tuple of Ints specifying the instances. This member is not applicable for a Surface 
    # object on an output database. 
    instances: int = None

    @typing.overload
    def __init__(self, side1Faces: str, side2Faces: str, side12Faces: str, end1Edges: str, end2Edges: str, 
                 circumEdges: str, side1Edges: str, side2Edges: str, face1Elements: str, 
                 face2Elements: str, face3Elements: str, face4Elements: str, face5Elements: str, 
                 face6Elements: str, side1Elements: str, side2Elements: str, side12Elements: str, 
                 end1Elements: str, end2Elements: str, circumElements: str, name: str):
        """This method creates a surface from a sequence of objects in a model database. The
        surface will apply to the sides specified by the arguments.For example
        surface=mdb.models['Model-1'].parts['Part-1'].Surface(side1Faces=side1Faces,
        name='Surf-1')

        Path
        ----
            - mdb.models[*name*].parts[*name*].Surface
            - mdb.models[*name*].rootAssembly.Surface

        Parameters
        ----------
        side1Faces
        side2Faces
        side12Faces
            On three-dimensional wire edges, you can use the following arguments: 
        end1Edges
        end2Edges
        circumEdges
            On three-dimensional or two-dimensional or axisymmetric edges, you can use the following 
            arguments: 
        side1Edges
        side2Edges
            On two-dimensional or axisymmetric shell elements, you can use the following arguments: 
        face1Elements
        face2Elements
        face3Elements
        face4Elements
        face5Elements
        face6Elements
            On three-dimensional shell elements, you can use the following arguments: 
        side1Elements
        side2Elements
        side12Elements
            On three-dimensional wire elements, you can use the following arguments: 
        end1Elements
        end2Elements
        circumElements
            On two-dimensional or axisymmetric wire elements, you can use the following arguments: 
        name
            A String specifying the repository key. The default value is an empty string. 

        Returns
        -------
            A Surface object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass

    @typing.overload
    def __init__(self, name: str, objectToCopy: 'Surface'):
        """This method copies a surface from an existing surface.

        Path
        ----
            - mdb.models[*name*].parts[*name*].Surface
            - mdb.models[*name*].rootAssembly.Surface

        Parameters
        ----------
        name
            A String specifying the name of the surface. 
        objectToCopy
            A Surface object to be copied. 

        Returns
        -------
            A Surface object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass

    def __init__(self, *args, **kwargs):
        pass

    def SurfaceByBoolean(self, name: str, surfaces: tuple[Surface], operation: SymbolicConstant = UNION):
        """This method creates a surface by performing a boolean operation on two or more input
        surfaces.

        Path
        ----
            - mdb.models[*name*].parts[*name*].SurfaceByBoolean
            - mdb.models[*name*].rootAssembly.SurfaceByBoolean

        Parameters
        ----------
        name
            A String specifying the repository key. 
        surfaces
            A sequence of Surface objects. 
        operation
            A SymbolicConstant specifying the boolean operation to perform. Possible values are 
            UNION, INTERSECTION, andDIFFERENCE. The default value is UNION. Note that if DIFFERENCE 
            is specified, the order of the given input surfaces is important; All surfaces specified 
            after the first one are subtracted from the first one. 

        Returns
        -------
            A Surface object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass

    def SurfaceFromElsets(self, name: str, elementSetSeq: tuple):
        """This method creates a surface from a sequence of element sets in a model database.

        Path
        ----
            - mdb.models[*name*].rootAssembly.SurfaceFromElsets

        Parameters
        ----------
        name
            A String specifying the repository key. 
        elementSetSeq
            A sequence of element sets. For example,`elementSetSeq=((elset1, S1),(elset2, S2))`where 
            `elset1=mdb.models[name].rootAssembly.sets['Clutch']` and `S1` and `S2` indicate the 
            side of the element set. 

        Returns
        -------
            A Surface object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass
