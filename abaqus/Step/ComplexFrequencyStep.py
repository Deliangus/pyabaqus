from abaqusConstants import *
from .AnalysisStep import AnalysisStep
from ..Adaptivity.AdaptiveMeshConstraintState import AdaptiveMeshConstraintState
from ..Adaptivity.AdaptiveMeshDomain import AdaptiveMeshDomain
from ..BoundaryCondition.BoundaryConditionState import BoundaryConditionState
from ..LoadAndLoadCase.LoadCase import LoadCase
from ..LoadAndLoadCase.LoadState import LoadState
from ..PredefinedField.PredefinedFieldState import PredefinedFieldState
from ..StepMiscellaneous.Control import Control
from ..StepMiscellaneous.SolverControl import SolverControl
from ..StepOutput.DiagnosticPrint import DiagnosticPrint
from ..StepOutput.FieldOutputRequestState import FieldOutputRequestState
from ..StepOutput.HistoryOutputRequestState import HistoryOutputRequestState
from ..StepOutput.Monitor import Monitor
from ..StepOutput.Restart import Restart
from ..UtilityAndView.Repository import Repository


class ComplexFrequencyStep(AnalysisStep):

    """The ComplexFrequencyStep object is used to perform eigenvalue extraction to calculate 
    the complex eigenvalues and corresponding complex mode shapes of a system. 
    The ComplexFrequencyStep object is derived from the AnalysisStep object. 

    Access
    ------
        - import step
        - mdb.models[name].steps[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - COMPLEX FREQUENCY
        - STEP

    """

    # A String specifying the repository key. 
    name: str = ''

    # The SymbolicConstant ALL or an Int specifying the number of complex eigenmodes to be 
    # calculated or a SymbolicConstant ALL. The default value is ALL. 
    numEigen: SymbolicConstant = ALL

    # None or a Float specifying the shift point in cycles per time. The default value is 
    # None. 
    shift: float = None

    # A Boolean specifying whether to add to the damping matrix contributions due to friction 
    # effects. The default value is OFF. 
    frictionDamping: Boolean = OFF

    # A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
    # UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
    matrixStorage: SymbolicConstant = SOLVER_DEFAULT

    # None or a Float specifying the minimum frequency of interest in cycles per time. The 
    # default value is None. 
    minEigen: float = None

    # None or a Float specifying the maximum frequency of interest in cycles per time. The 
    # default value is None. 
    maxEigen: float = None

    # None or a Float specifying the frequency at which to evaluate frequency-dependent 
    # properties for viscoelasticity, springs, and dashpots during the eigenvalue extraction. 
    # If the value is None, the analysis product will evaluate the stiffness associated with 
    # frequency-dependent springs and dashpots at zero frequency and will not consider the 
    # stiffness contributions from frequency-domain viscoelasticity in the step. The default 
    # value is None. 
    propertyEvaluationFrequency: float = None

    # A String specifying the name of the previous step. The new step appears after this step 
    # in the list of analysis steps. 
    previous: str = ''

    # A String specifying a description of the new step. The default value is an empty string. 
    description: str = ''

    # A SymbolicConstant specifying whether the step has an explicit procedure type 
    # (*procedureType*=ANNEAL, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT). 
    explicit: SymbolicConstant = None

    # A Boolean specifying whether the step has a perturbation procedure type. 
    perturbation: Boolean = OFF

    # A Boolean specifying whether the step has a mechanical procedure type. 
    nonmechanical: Boolean = OFF

    # A SymbolicConstant specifying the Abaqus procedure. Possible values are: 
    # - ANNEAL 
    # - BUCKLE 
    # - COMPLEX_FREQUENCY 
    # - COUPLED_TEMP_DISPLACEMENT 
    # - COUPLED_THERMAL_ELECTRIC 
    # - DIRECT_CYCLIC 
    # - DYNAMIC_IMPLICIT 
    # - DYNAMIC_EXPLICIT 
    # - DYNAMIC_SUBSPACE 
    # - DYNAMIC_TEMP_DISPLACEMENT 
    # - COUPLED_THERMAL_ELECTRICAL_STRUCTURAL 
    # - FREQUENCY 
    # - GEOSTATIC 
    # - HEAT_TRANSFER 
    # - MASS_DIFFUSION 
    # - MODAL_DYNAMICS 
    # - RANDOM_RESPONSE 
    # - RESPONSE_SPECTRUM 
    # - SOILS 
    # - STATIC_GENERAL 
    # - STATIC_LINEAR_PERTURBATION 
    # - STATIC_RIKS 
    # - STEADY_STATE_DIRECT 
    # - STEADY_STATE_MODAL 
    # - STEADY_STATE_SUBSPACE 
    # - VISCO 
    procedureType: SymbolicConstant = None

    # A Boolean specifying whether the step is suppressed or not. The default value is OFF. 
    suppressed: Boolean = OFF

    # A repository of FieldOutputRequestState objects. 
    fieldOutputRequestState: Repository[str, FieldOutputRequestState] = None

    # A repository of HistoryOutputRequestState objects. 
    historyOutputRequestState: Repository[str, HistoryOutputRequestState] = None

    # A DiagnosticPrint object. 
    diagnosticPrint: DiagnosticPrint = None

    # A Monitor object. 
    monitor: Monitor = None

    # A Restart object. 
    restart: Restart = None

    # A repository of AdaptiveMeshConstraintState objects. 
    adaptiveMeshConstraintStates: Repository[str, AdaptiveMeshConstraintState] = None

    # A repository of AdaptiveMeshDomain objects. 
    adaptiveMeshDomains: Repository[str, AdaptiveMeshDomain] = None

    # A Control object. 
    control: Control = None

    # A SolverControl object. 
    solverControl: SolverControl = None

    # A repository of BoundaryConditionState objects. 
    boundaryConditionStates: Repository[str, BoundaryConditionState] = None

    # A repository of InteractionState objects. 
    interactionStates: int = None

    # A repository of LoadState objects. 
    loadStates: Repository[str, LoadState] = None

    # A repository of LoadCase objects. 
    loadCases: Repository[str, LoadCase] = None

    # A repository of PredefinedFieldState objects. 
    predefinedFieldStates: Repository[str, PredefinedFieldState] = None

    def __init__(self, name: str, previous: str, numEigen: SymbolicConstant = ALL, description: str = '', 
                 shift: float = None, frictionDamping: Boolean = OFF, 
                 matrixStorage: SymbolicConstant = SOLVER_DEFAULT, maintainAttributes: Boolean = False, 
                 minEigen: float = None, maxEigen: float = None, 
                 propertyEvaluationFrequency: float = None):
        """This method creates a ComplexFrequencyStep object.

        Path
        ----
            - mdb.models[name].ComplexFrequencyStep

        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        numEigen
            The SymbolicConstant ALL or an Int specifying the number of complex eigenmodes to be 
            calculated or a SymbolicConstant ALL. The default value is ALL. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        shift
            None or a Float specifying the shift point in cycles per time. The default value is 
            None. 
        frictionDamping
            A Boolean specifying whether to add to the damping matrix contributions due to friction 
            effects. The default value is OFF. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        minEigen
            None or a Float specifying the minimum frequency of interest in cycles per time. The 
            default value is None. 
        maxEigen
            None or a Float specifying the maximum frequency of interest in cycles per time. The 
            default value is None. 
        propertyEvaluationFrequency
            None or a Float specifying the frequency at which to evaluate frequency-dependent 
            properties for viscoelasticity, springs, and dashpots during the eigenvalue extraction. 
            If the value is None, the analysis product will evaluate the stiffness associated with 
            frequency-dependent springs and dashpots at zero frequency and will not consider the 
            stiffness contributions from frequency-domain viscoelasticity in the step. The default 
            value is None. 

        Returns
        -------
            A ComplexFrequencyStep object. 

        Exceptions
        ----------
            RangeError. 
        """
        super().__init__()
        pass

    def setValues(self, numEigen: SymbolicConstant = ALL, description: str = '', shift: float = None, 
                  frictionDamping: Boolean = OFF, matrixStorage: SymbolicConstant = SOLVER_DEFAULT, 
                  minEigen: float = None, maxEigen: float = None, 
                  propertyEvaluationFrequency: float = None):
        """This method modifies the ComplexFrequencyStep object.

        Parameters
        ----------
        numEigen
            The SymbolicConstant ALL or an Int specifying the number of complex eigenmodes to be 
            calculated or a SymbolicConstant ALL. The default value is ALL. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        shift
            None or a Float specifying the shift point in cycles per time. The default value is 
            None. 
        frictionDamping
            A Boolean specifying whether to add to the damping matrix contributions due to friction 
            effects. The default value is OFF. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        minEigen
            None or a Float specifying the minimum frequency of interest in cycles per time. The 
            default value is None. 
        maxEigen
            None or a Float specifying the maximum frequency of interest in cycles per time. The 
            default value is None. 
        propertyEvaluationFrequency
            None or a Float specifying the frequency at which to evaluate frequency-dependent 
            properties for viscoelasticity, springs, and dashpots during the eigenvalue extraction. 
            If the value is None, the analysis product will evaluate the stiffness associated with 
            frequency-dependent springs and dashpots at zero frequency and will not consider the 
            stiffness contributions from frequency-domain viscoelasticity in the step. The default 
            value is None. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
        """
        pass
