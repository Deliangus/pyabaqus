import typing

from abaqusConstants import *
from .FieldOutput import FieldOutput
from .HistoryPoint import HistoryPoint
from .HistoryRegion import HistoryRegion
from .OdbFrameArray import OdbFrameArray
from .OdbLoadCase import OdbLoadCase


class OdbStepBase:
    """An output database contains the same steps of the model database that originated it.

    Attributes
    ----------
    number: int
        An Int specifying the step number.
    nlgeom: Boolean
        A Boolean specifying whether geometric nonlinearity can occur in this step.
    mass: float
        A Float specifying the current value of the mass of the model. This does not include the
        mass of the acoustic media if any present.
    acousticMass: float
        A Float specifying the current value of the mass of the acoustic media of the model.
    frames: OdbFrameArray
        An :py:class:`~abaqus.Odb.OdbFrameArray.OdbFrameArray` object.
    historyRegions: dict[str, HistoryRegion]
        A repository of :py:class:`~abaqus.Odb.HistoryRegion.HistoryRegion` objects.
    loadCases: dict[str, OdbLoadCase]
        A repository of :py:class:`~abaqus.Odb.OdbLoadCase.OdbLoadCase` objects.
    massCenter: float
        A tuple of Floats specifying the coordinates of the center of mass.
    inertiaAboutCenter: float
        A tuple of Floats specifying the moments and products of inertia about the center of
        mass. For 3-D models inertia quantities are written in the following order: I(XX),
        I(YY), I(ZZ), I(XY), I(XZ), and I(YZ). For 2-D models only I(ZZ) and I(XY) are
        outputted.
    inertiaAboutOrigin: float
        A tuple of Floats specifying the moments and products of inertia about the origin of the
        global coordinate system. For 3-D models inertia quantities are written in the following
        order: I(XX), I(YY), I(ZZ), I(XY), I(XZ), and I(YZ). For 2-D models only I(ZZ) and I(XY)
        are outputted.
    acousticMassCenter: float
        A tuple of Floats specifying the coordinates of the center of mass of the acoustic
        media.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import odbAccess
        session.odbs[name].steps[name]

    """

    # An Int specifying the step number. 
    number: int = None

    # A Boolean specifying whether geometric nonlinearity can occur in this step. 
    nlgeom: Boolean = OFF

    # A Float specifying the current value of the mass of the model. This does not include the 
    # mass of the acoustic media if any present. 
    mass: float = None

    # A Float specifying the current value of the mass of the acoustic media of the model. 
    acousticMass: float = None

    # An OdbFrameArray object. 
    frames: OdbFrameArray = OdbFrameArray()

    # A repository of HistoryRegion objects. 
    historyRegions: dict[str, HistoryRegion] = dict[str, HistoryRegion]()

    # A repository of OdbLoadCase objects. 
    loadCases: dict[str, OdbLoadCase] = dict[str, OdbLoadCase]()

    # A tuple of Floats specifying the coordinates of the center of mass. 
    massCenter: float = None

    # A tuple of Floats specifying the moments and products of inertia about the center of 
    # mass. For 3-D models inertia quantities are written in the following order: I(XX), 
    # I(YY), I(ZZ), I(XY), I(XZ), and I(YZ). For 2-D models only I(ZZ) and I(XY) are 
    # outputted. 
    inertiaAboutCenter: float = None

    # A tuple of Floats specifying the moments and products of inertia about the origin of the 
    # global coordinate system. For 3-D models inertia quantities are written in the following 
    # order: I(XX), I(YY), I(ZZ), I(XY), I(XZ), and I(YZ). For 2-D models only I(ZZ) and I(XY) 
    # are outputted. 
    inertiaAboutOrigin: float = None

    # A tuple of Floats specifying the coordinates of the center of mass of the acoustic 
    # media. 
    acousticMassCenter: float = None

    def __init__(self, name: str, description: str, domain: SymbolicConstant, timePeriod: float = 0,
                 previousStepName: str = '', procedure: str = '', totalTime: float = None):
        """This method creates an OdbStep object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.odbs[name].Step
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        description
            A String specifying the step description. 
        domain
            A SymbolicConstant specifying the domain of the step. Possible values are TIME, 
            FREQUENCY, ARC_LENGTH, and MODAL.The type of OdbFrame object that can be created for 
            this step is based on the value of the *domain* argument. 
        timePeriod
            A Float specifying the time period of the step. *timePeriod* is required if 
            *domain*=TIME; otherwise, this argument is not applicable. The default value is 0.0. 
        previousStepName
            A String specifying the preceding step. If *previousStepName* is the empty string, the 
            last step in the repository is used. If *previousStepName* is not the last step, this 
            will result in a change to the *previousStepName* member of the step that was in that 
            position. A special value 'Initial' refers to the internal initial model step and may be 
            used exclusively for inserting a new step at the first position before any other 
            existing steps. The default value is an empty string. 
        procedure
            A String specifying the step procedure. The default value is an empty string. The 
            following is the list of valid procedures: 
            ``` 
            *ANNEAL 
            *BUCKLE 
            *COMPLEX FREQUENCY 
            *COUPLED TEMPERATURE-DISPLACEMENT 
            *COUPLED TEMPERATURE-DISPLACEMENT, CETOL 
            *COUPLED TEMPERATURE-DISPLACEMENT, STEADY STATE 
            *COUPLED THERMAL-ELECTRICAL, STEADY STATE 
            *COUPLED THERMAL-ELECTRICAL 
            *COUPLED THERMAL-ELECTRICAL, DELTMX 
            *DYNAMIC 
            *DYNAMIC, DIRECT 
            *DYNAMIC, EXPLICIT 
            *DYNAMIC, SUBSPACE 
            *DYNAMIC TEMPERATURE-DISPLACEMENT, EXPLICT 
            *ELECTROMAGNETIC, HIGH FREQUENCY, TIME HARMONIC 
            *ELECTROMAGNETIC, LOW FREQUENCY, TIME DOMAIN 
            *ELECTROMAGNETIC, LOW FREQUENCY, TIME DOMAIN, DIRECT 
            *ELECTROMAGNETIC, LOW FREQUENCY, TIME HARMONIC 
            *FREQUENCY 
            *GEOSTATIC 
            *HEAT TRANSFER 
            *HEAT TRANSFER, DELTAMX=__ 
            *HEAT TRANSFER, STEADY STATE 
            *MAGNETOSTATIC 
            *MAGNETOSTATIC, DIRECT 
            *MASS DIFFUSION 
            *MASS DIFFUSION, DCMAX= 
            *MASS DIFFUSION, STEADY STATE 
            *MODAL DYNAMIC 
            *RANDOM RESPONSE 
            *RESPONSE SPECTRUM 
            *SOILS 
            *SOILS, CETOL/UTOL 
            *SOILS, CONSOLIDATION 
            *SOILS, CONSOLIDATION, CETOL/UTOL 
            *STATIC 
            *STATIC, DIRECT 
            *STATIC, RIKS 
            *STEADY STATE DYNAMICS 
            *STEADY STATE TRANSPORT 
            *STEADY STATE TRANSPORT, DIRECT 
            *STEP PERTURBATION, *STATIC 
            *SUBSTRUCTURE GENERATE 
            *USA ADDDED MASS GENERATION 
            *VISCO 
            ``` 
        totalTime
            A Float specifying the analysis time spend in all the steps previous to this step. The 
            default value is −1.0. 

        Returns
        -------
            An OdbStep object. 

        Raises
        ------
            - If *previousStepName* is invalid: 
              ValueError: previousStepName is invalid 
        """
        pass

    @typing.overload
    def getFrame(self, frameValue: str, match: SymbolicConstant = CLOSEST):
        """This method retrieves an OdbFrame object associated with a given frame value.
        
        Parameters
        ----------
        frameValue
            A Double specifying the value at which the frame is required. *frameValue* can be the 
            step time or frequency. 
        match
            A SymbolicConstant specifying which frame to return if there is no frame at the exact 
            frame value. Possible values are CLOSEST, BEFORE, AFTER, and EXACT. The default value is 
            CLOSEST.When *match*=CLOSEST, Abaqus returns the closest frame. If the frame value 
            requested is exactly halfway between two frames, Abaqus returns the frame after the 
            value.When *match*=EXACT, Abaqus raises an exception if the exact frame value does not 
            exist. 

        Returns
        -------
            An OdbFrame object. 

        Raises
        ------
            - If the OdbFrame object is not found: 
              OdbError: Frame not found. 
        """
        pass

    @typing.overload
    def getFrame(self, loadCase: OdbLoadCase):
        """This method retrieves an OdbFrame object associated with a given load case.
        
        Parameters
        ----------
        loadCase
            An OdbLoadCase object specifying a load case in the step. 

        Returns
        -------
            An OdbFrame object. 

        Raises
        ------
            - If the OdbFrame object is not found: 
              OdbError: Frame not found. 
        """
        pass

    @typing.overload
    def getFrame(self, loadCase: OdbLoadCase, frameValue: str, match: SymbolicConstant = CLOSEST):
        """This method retrieves an OdbFrame object associated with a given load case and frame
        value.
        
        Parameters
        ----------
        loadCase
            An OdbLoadCase object specifying a load case in the step. 
        frameValue
            A Double specifying the value at which the frame is required. *frameValue* can be the 
            step time or frequency. 
        match
            A SymbolicConstant specifying which frame to return if there is no frame at the exact 
            frame value. Possible values are CLOSEST, BEFORE, AFTER, and EXACT. The default value is 
            CLOSEST.When *match*=CLOSEST, Abaqus returns the closest frame. If the frame value 
            requested is exactly halfway between two frames, Abaqus returns the frame after the 
            value.When *match*=EXACT, Abaqus raises an exception if the exact frame value does not 
            exist. 

        Returns
        -------
            An OdbFrame object. 

        Raises
        ------
            - If the OdbFrame object is not found: 
              OdbError: Frame not found. 
        """
        pass

    def getFrame(self, *args, **kwargs):
        pass

    def getHistoryRegion(self, point: HistoryPoint, loadCase: OdbLoadCase = OdbLoadCase('loadCase')):
        """This method retrieves a HistoryRegion object associated with a HistoryPoint in the
        model.
        
        Parameters
        ----------
        point
            A HistoryPoint object specifying the point in the model. 
        loadCase
            An OdbLoadCase object specifying a load case in the step. 

        Returns
        -------
            A HistoryRegion object. 

        Raises
        ------
            - If a HistoryRegion object is not found: 
              OdbError: HistoryRegion not found. 
        """
        pass

    def setDefaultDeformedField(self, field: FieldOutput):
        """This method sets the default deformed field variable in a step.
        
        Parameters
        ----------
        field
            A FieldOutput object specifying the default deformed field variable for visualization. 
        """
        pass

    def setDefaultField(self, field: FieldOutput):
        """This method sets the default field variable in a step.
        
        Parameters
        ----------
        field
            A FieldOutput object specifying the default field variable for visualization. 
        """
        pass
