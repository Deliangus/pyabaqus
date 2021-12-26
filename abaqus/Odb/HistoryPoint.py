import typing

from abaqusConstants import *
from .OdbAssembly import OdbAssembly
from .OdbInstance import OdbInstance
from .OdbMeshElement import OdbMeshElement
from .OdbMeshNode import OdbMeshNode
from .OdbSet import OdbSet
from .SectionPoint import SectionPoint


class HistoryPoint:

    """The HistoryPoint object specifies the point at which history data will be collected. The 
    HistoryPoint object is a temporary object used as an argument to the HistoryRegion 
    method. 

    Access
    ------
        - import odbAccess
        - session.odbs[name].steps[name].historyRegions[name].point

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An Int specifying the integration point. This argument is used to define a history 
    # output position of INTEGRATION_POINT or ELEMENT_FACE_INTEGRATION_POINT. The default 
    # value is 0. 
    ipNumber: int = 0

    # A SymbolicConstant specifying the element face. This argument is used to define a 
    # history output position of ELEMENT_FACE or ELEMENT_FACE_INTEGRATION_POINT. Possible 
    # values are: 
    # - FACE_UNKOWN, specifying this value indicates that no value has been specified. 
    # - FACE1, specifying this value indicates that element face 1 has been specified. 
    # - FACE2, specifying this value indicates that element face 2 has been specified. 
    # - FACE3, specifying this value indicates that element face 3 has been specified. 
    # - FACE4, specifying this value indicates that element face 4 has been specified. 
    # - FACE5, specifying this value indicates that element face 5 has been specified. 
    # - FACE6, specifying this value indicates that element face 6 has been specified. 
    # - SIDE1, specifying this value indicates that element side 1 has been specified. 
    # - SIDE2, specifying this value indicates element side 2 has been specified. 
    # - END1, specifying this value indicates that element end 1 has been specified. 
    # - END2, specifying this value indicates that element end 2 has been specified. 
    # - END3, specifying this value indicates that element end 3 has been specified. 
    # The default value is FACE_UNKNOWN. 
    face: SymbolicConstant = FACE_UNKNOWN

    # A SymbolicConstant specifying the result position of the history point. Possible values 
    # are: 
    # - NODAL, specifying the values calculated at the nodes. 
    # - ELEMENT_NODAL, specifying the values obtained by extrapolating results calculated at 
    # the integration points. 
    # - INTEGRATION_POINT, specifying the values calculated at the integration points. 
    # - ELEMENT_FACE, specifying the results obtained for surface variables such as cavity 
    # radiation that are defined for the surface facets of an element. 
    # - ELEMENT_FACE_INTEGRATION_POINT, specifying the results obtained for surface variables 
    # such as cavity radiation that are defined for the surface facets of an element when the 
    # surface facets have integration points. 
    # - WHOLE_ELEMENT, specifying the results obtained for whole element variables. 
    # - WHOLE_REGION, specifying the results for an entire region of the model. 
    # - WHOLE_PART_INSTANCE, specifying the results for an entire part instance of the model. 
    # - WHOLE_MODEL, specifying the results for the entire model. 
    position: SymbolicConstant = None

    # An OdbMeshElement object specifying the element for which the data are to be collected. 
    element: OdbMeshElement = None

    # A SectionPoint object. 
    sectionPoint: SectionPoint = None

    # An OdbSet object specifying the region for which the data are to be collected. 
    region: OdbSet = None

    # An OdbAssembly object specifying the assembly for which the data are to be collected. 
    assembly: OdbAssembly = None

    # An OdbInstance object specifying the instance for which the data are to be collected. 
    instance: OdbInstance = None

    @typing.overload
    def __init__(self, node: OdbMeshNode):
        """This method creates a HistoryPoint object for a node.

        Path
        ----
            - odbAccess.HistoryPoint

        Parameters
        ----------
        node
            An OdbMeshNode object specifying the node for which the data are to be collected. 

        Returns
        -------
            A HistoryPoint object. 

        Exceptions
        ----------
            None. 
        """
        pass

    @typing.overload
    def __init__(self, element: OdbMeshElement, ipNumber: int = 0, sectionPoint: SectionPoint = None, 
                 face: SymbolicConstant = FACE_UNKNOWN, node: OdbMeshNode = None):
        """This method creates a HistoryPoint object for an element.

        Path
        ----
            - odbAccess.HistoryPoint

        Parameters
        ----------
        element
            An OdbMeshElement object specifying the element for which the data are to be collected. 
        ipNumber
            An Int specifying the integration point. This argument is used to define a history 
            output position of INTEGRATION_POINT or ELEMENT_FACE_INTEGRATION_POINT. The default 
            value is 0. 
        sectionPoint
            A SectionPoint object. 
        face
            A SymbolicConstant specifying the element face. This argument is used to define a 
            history output position of ELEMENT_FACE or ELEMENT_FACE_INTEGRATION_POINT. Possible 
            values are: 
            - FACE_UNKOWN, specifying this value indicates that no value has been specified. 
            - FACE1, specifying this value indicates that element face 1 has been specified. 
            - FACE2, specifying this value indicates that element face 2 has been specified. 
            - FACE3, specifying this value indicates that element face 3 has been specified. 
            - FACE4, specifying this value indicates that element face 4 has been specified. 
            - FACE5, specifying this value indicates that element face 5 has been specified. 
            - FACE6, specifying this value indicates that element face 6 has been specified. 
            - SIDE1, specifying this value indicates that element side 1 has been specified. 
            - SIDE2, specifying this value indicates element side 2 has been specified. 
            - END1, specifying this value indicates that element end 1 has been specified. 
            - END2, specifying this value indicates that element end 2 has been specified. 
            - END3, specifying this value indicates that element end 3 has been specified. 
            The default value is FACE_UNKNOWN. 
        node
            An OdbMeshNode object specifying the node for which the data are to be collected. 

        Returns
        -------
            A HistoryPoint object. 

        Exceptions
        ----------
            None. 
        """
        pass

    @typing.overload
    def __init__(self, region: OdbSet):
        """This method creates a HistoryPoint object for a region.

        Path
        ----
            - odbAccess.HistoryPoint

        Parameters
        ----------
        region
            An OdbSet object specifying the region for which the data are to be collected. 

        Returns
        -------
            A HistoryPoint object. 

        Exceptions
        ----------
            None. 
        """
        pass

    @typing.overload
    def __init__(self, assembly: OdbAssembly):
        """This method creates a HistoryPoint object for the OdbAssembly object.

        Path
        ----
            - odbAccess.HistoryPoint

        Parameters
        ----------
        assembly
            An OdbAssembly object specifying the assembly for which the data are to be collected. 

        Returns
        -------
            A HistoryPoint object. 

        Exceptions
        ----------
            None. 
        """
        pass

    @typing.overload
    def __init__(self, instance: OdbInstance):
        """This method creates a HistoryPoint object for the OdbInstance object.

        Path
        ----
            - odbAccess.HistoryPoint

        Parameters
        ----------
        instance
            An OdbInstance object specifying the instance for which the data are to be collected. 

        Returns
        -------
            A HistoryPoint object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def __init__(self, *args, **kwargs):
        pass
