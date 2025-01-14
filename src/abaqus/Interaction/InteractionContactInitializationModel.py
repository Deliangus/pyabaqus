from abaqusConstants import *
from .ExpInitialization import ExpInitialization
from .StdInitialization import StdInitialization
from ..Model.ModelBase import ModelBase


class InteractionContactInitializationModel(ModelBase):

    def ExpInitialization(self, name: str, overclosureType: SymbolicConstant = ADJUST,
                          interferenceDistance: float = None, clearanceDistance: float = None,
                          openingTolerance: float = None, overclosureTolerance: float = None,
                          adjustNodalCoords: Boolean = True, secondaryNodesetName: str = None,
                          stepFraction: float = 1) -> ExpInitialization:
        """This method creates an ExpInitialization object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].ExpInitialization
        
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
        self.contactInitializations[name] = contactInitialization = ExpInitialization(name, overclosureType,
                                                                                      interferenceDistance,
                                                                                      clearanceDistance,
                                                                                      openingTolerance,
                                                                                      overclosureTolerance,
                                                                                      adjustNodalCoords,
                                                                                      secondaryNodesetName,
                                                                                      stepFraction)
        return contactInitialization

    def StdInitialization(self, name: str, overclosureType: SymbolicConstant = ADJUST,
                          interferenceDistance: float = None, clearanceDistance: float = None,
                          openingTolerance: float = None, overclosureTolerance: float = None) -> StdInitialization:
        """This method creates a StdInitialization object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].StdInitialization
        
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
            when *overclosureType*=CLEARANCE, and must be specified in that case. The default value
            is None.
        openingTolerance
            None or a Float specifying the distance tolerance within which initial openings will
            undergo strain-free adjustments. This argument is not valid when
            *overclosureType*=INTERFERENCE unless a value has been specified for
            *interferenceDistance*. The default value is None.
        overclosureTolerance
            None or a Float specifying the distance tolerance within which initial overclosures will
            undergo strain-free adjustments.. The default value is None.

        Returns
        -------
            A StdInitialization object.

        Raises
        ------
            RangeError.
        """
        self.contactInitializations[name] = contactInitialization = StdInitialization(name, overclosureType,
                                                                                      interferenceDistance,
                                                                                      clearanceDistance,
                                                                                      openingTolerance,
                                                                                      overclosureTolerance)
        return contactInitialization
