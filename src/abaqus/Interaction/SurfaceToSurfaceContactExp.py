import typing

from abaqusConstants import *
from .Interaction import Interaction
from ..Datum.DatumAxis import DatumAxis
from ..Region.Region import Region


class SurfaceToSurfaceContactExp(Interaction):
    """The SurfaceToSurfaceContactExp object defines surface-to-surface contact during an
    Abaqus/Explicit analysis. 
    The SurfaceToSurfaceContactExp object is derived from the Interaction object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].interactions[name]

    """

    def __init__(self, name: str, createStepName: str, main: Region, secondary: Region,
                 sliding: SymbolicConstant, interactionProperty: str,
                 mechanicalConstraint: SymbolicConstant = KINEMATIC,
                 weightingFactorType: SymbolicConstant = DEFAULT, weightingFactor: float = 0,
                 contactControls: str = '',
                 initialClearance: typing.Union[SymbolicConstant, float] = OMIT,
                 halfThreadAngle: str = None, pitch: str = None,
                 majorBoltDiameter: typing.Union[SymbolicConstant, float] = COMPUTED,
                 meanBoltDiameter: typing.Union[SymbolicConstant, float] = COMPUTED,
                 datumAxis: DatumAxis = DatumAxis(), useReverseDatumAxis: Boolean = OFF,
                 clearanceRegion: Region = Region()):
        """This method creates a SurfaceToSurfaceContactExp object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].SurfaceToSurfaceContactExp
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the SurfaceToSurfaceContactExp object 
            is created. 
        main
            A Region object specifying the main surface. 
        secondary
            A Region object specifying the secondary surface. 
        sliding
            A SymbolicConstant specifying the contact formulation. Possible values are FINITE and 
            SMALL. 
        interactionProperty
            A String specifying the name of the ContactProperty object associated with this 
            interaction. 
        mechanicalConstraint
            A SymbolicConstant specifying the mechanical constraint formulation. Possible values are 
            KINEMATIC and PENALTY. The default value is KINEMATIC. 
        weightingFactorType
            A SymbolicConstant specifying the weighting for node-to-face contact. Possible values 
            are DEFAULT and SPECIFIED. The default value is DEFAULT. 
        weightingFactor
            A Float specifying the weighting factor for the contact surfaces when 
            *weightingFactorType*=SPECIFIED. The default value is 0.0. 
        contactControls
            A String specifying the name of the ContactControl object associated with this 
            interaction. An empty string indicates that the default contact controls will be used. 
            The default value is an empty string. 
        initialClearance
            A SymbolicConstant or a Float specifying the initial clearance at regions of contact. 
            Possible values are OMIT and COMPUTED. The default value is OMIT. 
        halfThreadAngle
            None or a sequence of Floats specifying the half thread angle used for bolt clearance. 
            The default value is None. 
        pitch
            None or a sequence of Floats specifying the pitch used for bolt clearance. The default 
            value is None. 
        majorBoltDiameter
            The SymbolicConstant COMPUTED or a Float specifying the major diameter of the bolt used 
            for bolt clearance. The default value is COMPUTED. 
        meanBoltDiameter
            The SymbolicConstant COMPUTED or a Float specifying the mean diameter of the bolt used 
            for bolt clearance. The default value is COMPUTED. 
        datumAxis
            A DatumAxis object specifying the orientation of the bolt hole when specifying bolt 
            clearance. 
        useReverseDatumAxis
            A Boolean specifying whether to reverse the bolt clearance direction given by the datum 
            axis. The default value is OFF. 
        clearanceRegion
            A Region object specifying the contact region for which clearance is specified. 

        Returns
        -------
            A SurfaceToSurfaceContactExp object.
        """
        super().__init__()
        pass

    def swapSurfaces(self):
        """This method switches the main and secondary surfaces of a surface-to-surface contact
        pair. This command is valid only during the step in which the interaction is created.
        """
        pass

    def setValues(self, mechanicalConstraint: SymbolicConstant = KINEMATIC,
                  weightingFactorType: SymbolicConstant = DEFAULT, weightingFactor: float = 0,
                  contactControls: str = '',
                  initialClearance: typing.Union[SymbolicConstant, float] = OMIT,
                  halfThreadAngle: str = None, pitch: str = None,
                  majorBoltDiameter: typing.Union[SymbolicConstant, float] = COMPUTED,
                  meanBoltDiameter: typing.Union[SymbolicConstant, float] = COMPUTED,
                  datumAxis: DatumAxis = DatumAxis(), useReverseDatumAxis: Boolean = OFF,
                  clearanceRegion: Region = Region()):
        """This method modifies the data for an existing SurfaceToSurfaceContactExp object in the
        step where it is created.
        
        Parameters
        ----------
        mechanicalConstraint
            A SymbolicConstant specifying the mechanical constraint formulation. Possible values are 
            KINEMATIC and PENALTY. The default value is KINEMATIC. 
        weightingFactorType
            A SymbolicConstant specifying the weighting for node-to-face contact. Possible values 
            are DEFAULT and SPECIFIED. The default value is DEFAULT. 
        weightingFactor
            A Float specifying the weighting factor for the contact surfaces when 
            *weightingFactorType*=SPECIFIED. The default value is 0.0. 
        contactControls
            A String specifying the name of the ContactControl object associated with this 
            interaction. An empty string indicates that the default contact controls will be used. 
            The default value is an empty string. 
        initialClearance
            A SymbolicConstant or a Float specifying the initial clearance at regions of contact. 
            Possible values are OMIT and COMPUTED. The default value is OMIT. 
        halfThreadAngle
            None or a sequence of Floats specifying the half thread angle used for bolt clearance. 
            The default value is None. 
        pitch
            None or a sequence of Floats specifying the pitch used for bolt clearance. The default 
            value is None. 
        majorBoltDiameter
            The SymbolicConstant COMPUTED or a Float specifying the major diameter of the bolt used 
            for bolt clearance. The default value is COMPUTED. 
        meanBoltDiameter
            The SymbolicConstant COMPUTED or a Float specifying the mean diameter of the bolt used 
            for bolt clearance. The default value is COMPUTED. 
        datumAxis
            A DatumAxis object specifying the orientation of the bolt hole when specifying bolt 
            clearance. 
        useReverseDatumAxis
            A Boolean specifying whether to reverse the bolt clearance direction given by the datum 
            axis. The default value is OFF. 
        clearanceRegion
            A Region object specifying the contact region for which clearance is specified. 
        """
        pass

    def setValuesInStep(self, stepName: str, interactionProperty: str = '', contactControls: str = ''):
        """This method modifies the propagating data for an existing SurfaceToSurfaceContactExp
        object in the specified step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is modified. 
        interactionProperty
            A String specifying the name of the ContactProperty object associated with this 
            interaction. 
        contactControls
            A String specifying the name of the ContactControl object associated with this 
            interaction. An empty string indicates that the default contact controls will be used. 
            The default value is an empty string. 
        """
        pass
