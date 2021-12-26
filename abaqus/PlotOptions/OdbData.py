from abaqusConstants import *
from .CouplingConstraint import CouplingConstraint
from .HistoryVariable import HistoryVariable
from .MpcConstraint import MpcConstraint
from .OdbDataDatumCsys import OdbDataDatumCsys
from .OdbDataElementSet import OdbDataElementSet
from .OdbDataInstance import OdbDataInstance
from .OdbDataMaterial import OdbDataMaterial
from .OdbDataNodeSet import OdbDataNodeSet
from .OdbDataSection import OdbDataSection
from .OdbDataStep import OdbDataStep
from .OdbDataSurfaceSet import OdbDataSurfaceSet
from .OdbDiagnosticData import OdbDiagnosticData
from .RigidBodyConstraint import RigidBodyConstraint
from .TieConstraint import TieConstraint
from ..UtilityAndView.Repository import Repository


class OdbData:

    """The OdbData object stores non persistent values and attributes associated with an open 
    odb for the given session. The OdbData object has no constructor. Abaqus creates the 
    *odbData* repository when you import the Visualization module. Abaqus creates a OdbData 
    object when an odb is opened. 

    Access
    ------
        - import visualization
        - session.odbData[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A tuple specifying the active frames, or the SymbolicConstant ALL. Each item in the 
    # sequence is a tuple defining the stepName followed by a sequence of expressions 
    # specifying frame numbers. The expression can be any of the following: 
    # - An Int specifying a single frame number; for example, `1`. 
    # - A String specifying a single frame number ; for example, `'7'`. 
    # - A String specifying a sequence of frame numbers; for example, `'3:5'` and `'3:15:3'`. 
    # For these expressions a negative number will indicate reverse numbering: -1 is the last 
    # frame of the step, -2 is the one before the last frame. Frame numbering starts at 0. 
    activeFrames: SymbolicConstant = None

    # A tuple of (String, Float) tuples specifying the stepName and the stepPeriod. 
    # Alternatively, this member may take the value ODB_VALUES. 
    stepPeriods: float = None

    # A repository of HistoryVariable objects specifying the history request label. The 
    # repository is read-only. 
    historyVariables: Repository[str, HistoryVariable] = None

    # A repository of OdbDataStep objects specifying the list of steps. The repository is 
    # read-only. 
    steps: Repository[str, OdbDataStep] = None

    # A repository of OdbDataInstance objects specifying the list of instances. The repository 
    # is read-only. 
    instances: Repository[str, OdbDataInstance] = None

    # A repository of OdbDataMaterial objects specifying the list of materials. The repository 
    # is read-only. 
    materials: Repository[str, OdbDataMaterial] = None

    # A repository of OdbDataSection objects specifying the list of sections. The repository 
    # is read-only. 
    sections: Repository[str, OdbDataSection] = None

    # A repository of OdbDataElementSet objects specifying the list of element sets. The 
    # repository is read-only. 
    elementSets: Repository[str, OdbDataElementSet] = None

    # A repository of OdbDataNodeSet objects specifying the list of node sets. The repository 
    # is read-only. 
    nodeSets: Repository[str, OdbDataNodeSet] = None

    # A repository of OdbDataSurfaceSet objects specifying the list of surface sets. The 
    # repository is read-only. 
    surfaceSets: Repository[str, OdbDataSurfaceSet] = None

    # A repository of OdbDataDatumCsys objects specifying the list of coordinate systems 
    # defined in the model. The repository is read-only. 
    datumCsyses: Repository[str, OdbDataDatumCsys] = None

    # A repository of CouplingConstraint objects specifying the list of kinematic couplings. 
    # The repository is read-only. 
    kinematicCouplings: Repository[str, CouplingConstraint] = None

    # A repository of CouplingConstraint objects specifying the list of distributing 
    # couplings. The repository is read-only. 
    distributingCouplings: Repository[str, CouplingConstraint] = None

    # A repository of CouplingConstraint objects specifying the list of shellsolid couplings. 
    # The repository is read-only. 
    shellSolidCouplings: Repository[str, CouplingConstraint] = None

    # A repository of RigidBodyConstraint objects specifying the list of rigid body 
    # constraints. The repository is read-only. 
    rigidbodies: Repository[str, RigidBodyConstraint] = None

    # A repository of MpcConstraint objects specifying the list of multipoint constraints. The 
    # repository is read-only. 
    multiPointConstraints: Repository[str, MpcConstraint] = None

    # A repository of TieConstraint objects specifying the list of Tie constraints. The 
    # repository is read-only. 
    ties: Repository[str, TieConstraint] = None

    # An OdbDiagnosticData object. 
    diagnosticData: OdbDiagnosticData = None

    def setValues(self, activeFrames: SymbolicConstant = None, stepPeriods: tuple = ()):
        """This method modifies the OdbData object.

        Parameters
        ----------
        activeFrames
            A sequence specifying the active frames, or the SymbolicConstant ALL. Each item in the 
            sequence is a tuple defining the stepName followed by a sequence of expressions 
            specifying frame numbers. The expression can be any of the following:An Int specifying a 
            single frame number; for example, `1`.A String specifying a single frame number ; for 
            example, `'7'`.A String specifying a sequence of frame numbers; for example, `'3:5'` and 
            `'3:15:3'`.For these expressions a negative number will indicate reverse numbering: -1 
            is the last frame of the step, -2 is the one before the last frame. Frame numbering 
            starts at 0. 
        stepPeriods
            A sequence of (String, Float) sequences specifying the stepName and the stepPeriod. 
            Alternatively, this member may take the value ODB_VALUES. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
