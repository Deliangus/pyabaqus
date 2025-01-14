from abaqusConstants import *
from .JobData import JobData
from .OdbAssembly import OdbAssembly
from .OdbPart import OdbPart
from .OdbStep import OdbStep
from .SectionCategory import SectionCategory
from .SectorDefinition import SectorDefinition
from .UserData import UserData
from ..Amplitude.Amplitude import Amplitude
from ..BeamSectionProfile.Profile import Profile
from ..CustomKernel.RepositorySupport import RepositorySupport
from ..Filter.Filter import Filter
from ..Material.Material import Material
from ..Section.Section import Section


class OdbBase:
    """The Odb object is the in-memory representation of an output database (ODB) file.

    Attributes
    ----------
    isReadOnly: Boolean
        A Boolean specifying whether the output database was opened with read-only access.
    amplitudes: dict[str, Amplitude]
        A repository of :py:class:`~abaqus.Amplitude.Amplitude.Amplitude` objects.
    filters: dict[str, Filter]
        A repository of :py:class:`~abaqus.Filter.Filter.Filter` objects.
    rootAssembly: OdbAssembly
        An :py:class:`~abaqus.Odb.OdbAssembly.OdbAssembly` object.
    jobData: JobData
        A :py:class:`~abaqus.Odb.JobData.JobData` object.
    parts: dict[str, OdbPart]
        A repository of :py:class:`~abaqus.Odb.OdbPart.OdbPart` objects.
    materials: dict[str, Material]
        A repository of :py:class:`~abaqus.Material.Material.Material` objects.
    steps: dict[str, OdbStep]
        A repository of :py:class:`~abaqus.Odb.OdbStep.OdbStep` objects.
    sections: dict[str, Section]
        A repository of :py:class:`~abaqus.Section.Section.Section` objects.
    sectionCategories: dict[str, SectionCategory]
        A repository of :py:class:`~abaqus.Odb.SectionCategory.SectionCategory` objects.
    sectorDefinition: SectorDefinition
        A :py:class:`~abaqus.Odb.SectorDefinition.SectorDefinition` object.
    userData: UserData
        A :py:class:`~abaqus.Odb.UserData.UserData` object.
    customData: RepositorySupport
        A :py:class:`~abaqus.CustomKernel.RepositorySupport.RepositorySupport` object.
    profiles: dict[str, Profile]
        A repository of :py:class:`~abaqus.BeamSectionProfile.Profile.Profile` objects.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import odbAccess
        session.odbs[name]

    """

    # A Boolean specifying whether the output database was opened with read-only access. 
    isReadOnly: Boolean = OFF

    # A repository of Amplitude objects. 
    amplitudes: dict[str, Amplitude] = dict[str, Amplitude]()

    # A repository of Filter objects. 
    filters: dict[str, Filter] = dict[str, Filter]()

    # An OdbAssembly object. 
    rootAssembly: OdbAssembly = OdbAssembly()

    # A JobData object. 
    jobData: JobData = JobData()

    # A repository of OdbPart objects. 
    parts: dict[str, OdbPart] = dict[str, OdbPart]()

    # A repository of Material objects. 
    materials: dict[str, Material] = dict[str, Material]()

    # A repository of OdbStep objects. 
    steps: dict[str, OdbStep] = dict[str, OdbStep]()

    # A repository of Section objects. 
    sections: dict[str, Section] = dict[str, Section]()

    # A repository of SectionCategory objects. 
    sectionCategories: dict[str, SectionCategory] = dict[str, SectionCategory]()

    # A SectorDefinition object. 
    sectorDefinition: SectorDefinition = SectorDefinition()

    # A UserData object. 
    userData: UserData = UserData()

    # A RepositorySupport object. 
    customData: RepositorySupport = RepositorySupport()

    # A repository of Profile objects. 
    profiles: dict[str, Profile] = dict[str, Profile]()

    def __init__(self, name: str, analysisTitle: str = '', description: str = '', path: str = ''):
        """This method creates a new Odb object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.Odb
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        analysisTitle
            A String specifying the title of the output database. The default value is an empty 
            string. 
        description
            A String specifying the description of the output database. The default value is an 
            empty string. 
        path
            A String specifying the path to the file where the new output database (.odb ) file will 
            be written. The default value is an empty string. 

        Returns
        -------
            An Odb object.
        """
        pass

    def close(self):
        """This method closes an output database.
        """
        pass

    def getFrame(self, frameValue: str, match: SymbolicConstant = CLOSEST):
        """This method returns the frame at the specified time, frequency, or mode. It will not
        interpolate values between frames. The method is not applicable to an Odb object
        containing steps with different domains or to an Odb object containing a step with load
        case specific data.
        
        Parameters
        ----------
        frameValue
            A Double specifying the value at which the frame is required. *frameValue* can be the 
            total time or frequency. 
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
            - If the exact frame is not found: 
              OdbError: Frame not found. 
        """
        pass

    def save(self):
        """This method saves output to an output database (.odb ) file.

        Raises
        ------
            - OdbError 
              Database save failed. The database was opened as read-only. Modification of data is 
            not permitted. 
        """
        pass

    def update(self):
        """This method is used to update an Odb object in memory while an Abaqus analysis writes
        data to the associated output database. update checks if additional steps have been
        written to the output database since it was opened or last updated. If additional steps
        have been written to the output database, update adds them to the Odb object.

        Returns
        -------
            A Boolean specifying whether additional steps or frames were added to the Odb object.
        """
        pass
