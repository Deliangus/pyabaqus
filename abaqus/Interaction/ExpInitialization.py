from abaqusConstants import *
from .ContactInitialization import ContactInitialization


class ExpInitialization(ContactInitialization):
    """The ExpInitialization object is used in conjunction with ContactExp in Abaqus/Explicit
    analyses to specify contact initialization data. 
    The ExpInitialization object is derived from the ContactInitialization object. 

    Notes
    -----
        This object can be accessed by:
        - import interaction
        - mdb.models[name].contactInitializations[name]

    Corresponding analysis keywords
    -------------------------------
        - CONTACT INITIALIZATION DATA

    """

    def __init__(self, name: str, overclosureType: SymbolicConstant = ADJUST,
                 interferenceDistance: float = None, clearanceDistance: float = None,
                 openingTolerance: float = None, overclosureTolerance: float = None,
                 adjustNodalCoords: Boolean = True, secondaryNodesetName: str = None,
                 stepFraction: float = 1):
        """This method creates an ExpInitialization object.

        Path
        ----
            - mdb.models[name].ExpInitialization

        Parameters
        ----------
        name
            A String specifying the contact initialization repository key. 
        overclosureType
            A SymbolicConstant specifying the type of overclosure to be defined. Possible values are 
            ADJUST, INTERFERENCE, and CLEARANCE. The default value is ADJUST. 
        interferenceDistance
            None or a Float specifying the interference distance. This argument is valid only when 
            *overclosureType*=INTERFERENCE. The default value is None. 
        clearanceDistance
            None or a Float specifying the initial clearance distance. This argument is valid only 
            when *overclosureType*=CLEARANCE and must be specified in that case. The default value 
            is None. 
        openingTolerance
            None or a Float specifying the distance tolerance within which initial openings will 
            undergo strain-free adjustments. This argument is not valid when 
            *overclosureType*=INTERFERENCE unless a value has been specified for 
            *interferenceDistance*. The default value is None. 
        overclosureTolerance
            None or a Float specifying the distance tolerance within which initial overclosures will 
            undergo strain-free adjustments. The default value is None. 
        adjustNodalCoords
            A Boolean specifying whether to resolve clearances/overclosures by adjusting the nodal 
            coordinates without creating strain in the model. *adjustNodalCoords*=True can be used 
            only for clearances/overclosures defined in the first step of an analysis. The default 
            value is True. 
        secondaryNodesetName
            A String specifying the name of the node set containing the secondary nodes to be 
            included in the initial clearance specification. This argument is not valid when 
            *overclosureType*=INTERFERENCE and if *openingTolerance* or *overclosureTolerance* is 
            specified. The default value is None. 
        stepFraction
            A Float specifying the fraction of the step time (between 0.0 and 1.0) in which the 
            interference fit has to be solved. The default value is 1.0. This argument is valid only 
            when *overclosureType*=INTERFERENCE. 

        Returns
        -------
            An ExpInitialization object. 

        Raises
        ------
            RangeError. 
        """
        super().__init__()
        pass

    def setValues(self, overclosureType: SymbolicConstant = ADJUST, interferenceDistance: float = None,
                  clearanceDistance: float = None, openingTolerance: float = None,
                  overclosureTolerance: float = None, adjustNodalCoords: Boolean = True,
                  secondaryNodesetName: str = None, stepFraction: float = 1):
        """This method modifies the ExpInitialization object.

        Parameters
        ----------
        overclosureType
            A SymbolicConstant specifying the type of overclosure to be defined. Possible values are 
            ADJUST, INTERFERENCE, and CLEARANCE. The default value is ADJUST. 
        interferenceDistance
            None or a Float specifying the interference distance. This argument is valid only when 
            *overclosureType*=INTERFERENCE. The default value is None. 
        clearanceDistance
            None or a Float specifying the initial clearance distance. This argument is valid only 
            when *overclosureType*=CLEARANCE and must be specified in that case. The default value 
            is None. 
        openingTolerance
            None or a Float specifying the distance tolerance within which initial openings will 
            undergo strain-free adjustments. This argument is not valid when 
            *overclosureType*=INTERFERENCE unless a value has been specified for 
            *interferenceDistance*. The default value is None. 
        overclosureTolerance
            None or a Float specifying the distance tolerance within which initial overclosures will 
            undergo strain-free adjustments. The default value is None. 
        adjustNodalCoords
            A Boolean specifying whether to resolve clearances/overclosures by adjusting the nodal 
            coordinates without creating strain in the model. *adjustNodalCoords*=True can be used 
            only for clearances/overclosures defined in the first step of an analysis. The default 
            value is True. 
        secondaryNodesetName
            A String specifying the name of the node set containing the secondary nodes to be 
            included in the initial clearance specification. This argument is not valid when 
            *overclosureType*=INTERFERENCE and if *openingTolerance* or *overclosureTolerance* is 
            specified. The default value is None. 
        stepFraction
            A Float specifying the fraction of the step time (between 0.0 and 1.0) in which the 
            interference fit has to be solved. The default value is 1.0. This argument is valid only 
            when *overclosureType*=INTERFERENCE.

        Raises
        ------
            RangeError. 
        """
        pass
