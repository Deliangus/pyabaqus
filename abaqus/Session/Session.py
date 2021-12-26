from abaqusConstants import *
from .AutoColors import AutoColors
from .Color import Color
from .Drawing import Drawing
from .Image import Image
from .JournalOptions import JournalOptions
from .MemoryReductionOptions import MemoryReductionOptions
from .NetworkDatabaseConnector import NetworkDatabaseConnector
from ..Animation.AVIOptions import AVIOptions
from ..Animation.AnimationOptions import AnimationOptions
from ..Animation.ImageAnimation import ImageAnimation
from ..Animation.ImageAnimationOptions import ImageAnimationOptions
from ..Animation.Movie import Movie
from ..Animation.QuickTimeOptions import QuickTimeOptions
from ..Canvas.DrawingArea import DrawingArea
from ..Canvas.Viewport import Viewport
from ..CustomKernel.RepositorySupport import RepositorySupport
from ..DisplayGroup.DisplayGroup import DisplayGroup
from ..DisplayOptions.GraphicsInfo import GraphicsInfo
from ..DisplayOptions.GraphicsOptions import GraphicsOptions
from ..DisplayOptions.LightOptions import LightOptions
from ..DisplayOptions.ViewportAnnotationOptions import ViewportAnnotationOptions
from ..FieldReport.FieldReportOptions import FieldReportOptions
from ..FieldReport.FreeBodyReportOptions import FreeBodyReportOptions
from ..Job.Queue import Queue
from ..Mesh.MesherOptions import MesherOptions
from ..Odb.Odb import Odb
from ..Odb.ScratchOdb import ScratchOdb
from ..OdbDisplay.DefaultOdbDisplay import DefaultOdbDisplay
from ..OdbDisplay.ViewerOptions import ViewerOptions
from ..PathAndProbe.CurrentProbeValues import CurrentProbeValues
from ..PathAndProbe.FreeBody import FreeBody
from ..PathAndProbe.NodeQuery import NodeQuery
from ..PathAndProbe.Path import Path
from ..PathAndProbe.ProbeOptions import ProbeOptions
from ..PathAndProbe.ProbeReport import ProbeReport
from ..PathAndProbe.SelectedProbeValues import SelectedProbeValues
from ..PathAndProbe.Spectrum import Spectrum
from ..PathAndProbe.Stream import Stream
from ..PlotOptions.MdbData import MdbData
from ..PlotOptions.OdbData import OdbData
from ..PredefinedField.TiffOptions import TiffOptions
from ..Print.EpsOptions import EpsOptions
from ..Print.PageSetupOptions import PageSetupOptions
from ..Print.PngOptions import PngOptions
from ..Print.PrintOptions import PrintOptions
from ..Print.PsOptions import PsOptions
from ..Print.SvgOptions import SvgOptions
from ..Sketcher.ConstrainedSketcherOptions import ConstrainedSketcherOptions
from ..UtilityAndView.Repository import Repository
from ..UtilityAndView.View import View
from ..XY.Chart import Chart
from ..XY.DefaultChartOptions import DefaultChartOptions
from ..XY.DefaultPlot import DefaultPlot
from ..XY.XYCurve import XYCurve
from ..XY.XYData import XYData
from ..XY.XYPlot import XYPlot
from ..XY.XYReportOptions import XYReportOptions


class Session:

    """The Session object has no constructor. Abaqus creates the *session* member when a 
    session is started. 

    Access
    ------
        - session

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A Boolean specifying whether an Abaqus interactive session is running. 
    attachedToGui: Boolean = OFF

    # A Boolean specifying whether Abaqus is executing a replay file. 
    replayInProgress: Boolean = OFF

    # A Float specifying the memory usage value for the Abaqus/CAE kernel process in 
    # megabytes. 
    kernelMemoryFootprint: float = None

    # A Float specifying the maximum value for the memory usage for the Abaqus/CAE kernel 
    # process in megabytes. 
    kernelMemoryMaxFootprint: float = None

    # A Float specifying the limit for the memory use for the Abaqus/CAE kernel process in 
    # megabytes. 
    kernelMemoryLimit: float = None

    # A repository of Color objects. 
    colors: Repository[str, Color] = None

    # A JournalOptions object specifying how to record selection of geometry in the journal 
    # and replay files. 
    journalOptions: JournalOptions = None

    # A MemoryReductionOptions object specifying options for running in reduced memory mode. 
    memoryReductionOptions: MemoryReductionOptions = None

    # A NodeQuery object specifying nodes and their coordinates in a path. 
    nodeQuery: NodeQuery = None

    # A ConstrainedSketcherOptions object specifying common options for all sketches. 
    sketcherOptions: ConstrainedSketcherOptions = None

    # A ViewerOptions object. 
    viewerOptions: ViewerOptions = None

    # An AnimationOptions object. 
    animationOptions: AnimationOptions = None

    # An AVIOptions object. 
    aviOptions: AVIOptions = None

    # An ImageAnimationOptions object. 
    imageAnimationOptions: ImageAnimationOptions = None

    # An ImageAnimation object. 
    imageAnimation: ImageAnimation = None

    # A QuickTimeOptions object. 
    quickTimeOptions: QuickTimeOptions = None

    # A repository of Viewport objects. 
    viewports: Repository[str, Viewport] = None

    # A RepositorySupport object. 
    customData: RepositorySupport = None

    # A FieldReportOptions object. 
    defaultFieldReportOptions: FieldReportOptions = None

    # A FreeBodyReportOptions object. 
    defaultFreeBodyReportOptions: FreeBodyReportOptions = None

    # A FieldReportOptions object. 
    fieldReportOptions: FieldReportOptions = None

    # A FreeBodyReportOptions object. 
    freeBodyReportOptions: FreeBodyReportOptions = None

    # A repository of Odb objects. 
    odbs: Repository[str, Odb] = None

    # A repository of ScratchOdb objects. 
    scratchOdbs: Repository[str, ScratchOdb] = None

    # A DefaultOdbDisplay object. 
    defaultOdbDisplay: DefaultOdbDisplay = None

    # A DefaultPlot object. 
    defaultPlot: DefaultPlot = None

    # A DefaultChartOptions object. 
    defaultChartOptions: DefaultChartOptions = None

    # A repository of OdbData objects. 
    odbData: Repository[str, OdbData] = None

    # A repository of MdbData objects. 
    mdbData: Repository[str, MdbData] = None

    # A repository of Path objects. 
    paths: Repository[str, Path] = None

    # A repository of FreeBody objects. 
    freeBodies: Repository[str, FreeBody] = None

    # A repository of Stream objects. 
    streams: Repository[str, Stream] = None

    # A repository of Spectrum objects. 
    spectrums: Repository[str, Spectrum] = None

    # A CurrentProbeValues object. 
    currentProbeValues: CurrentProbeValues = None

    # A ProbeOptions object. 
    defaultProbeOptions: ProbeOptions = None

    # A ProbeOptions object. 
    probeOptions: ProbeOptions = None

    # A ProbeReport object. 
    probeReport: ProbeReport = None

    # A ProbeReport object. 
    defaultProbeReport: ProbeReport = None

    # A SelectedProbeValues object. 
    selectedProbeValues: SelectedProbeValues = None

    # A PrintOptions object. 
    printOptions: PrintOptions = None

    # An EpsOptions object. 
    epsOptions: EpsOptions = None

    # A PageSetupOptions object. 
    pageSetupOptions: PageSetupOptions = None

    # A PngOptions object. 
    pngOptions: PngOptions = None

    # A PsOptions object. 
    psOptions: PsOptions = None

    # A SvgOptions object. 
    svgOptions: SvgOptions = None

    # A TiffOptions object. 
    tiffOptions: TiffOptions = None

    # An AutoColors object specifying the color palette to be used for color coding. 
    autoColors: AutoColors = None

    # An AutoColors object specifying the color palette to be used forXYCurve objects. 
    xyColors: AutoColors = None

    # A repository of XYData objects. 
    xyDataObjects: Repository[str, XYData] = None

    # A repository of XYCurve objects. 
    curves: Repository[str, XYCurve] = None

    # A repository of XYPlot objects. 
    xyPlots: Repository[str, XYPlot] = None

    # A repository of Chart objects. 
    charts: Repository[str, Chart] = None

    # An XYReportOptions object. 
    defaultXYReportOptions: XYReportOptions = None

    # An XYReportOptions object. 
    xyReportOptions: XYReportOptions = None

    # A repository of View objects. 
    views: Repository[str, View] = None

    # A repository of NetworkDatabaseConnector objects. 
    networkDatabaseConnectors: Repository[str, NetworkDatabaseConnector] = None

    # A repository of DisplayGroup objects. 
    displayGroups: Repository[str, DisplayGroup] = None

    # A GraphicsInfo object. 
    graphicsInfo: GraphicsInfo = None

    # A GraphicsOptions object. 
    defaultGraphicsOptions: GraphicsOptions = None

    # A GraphicsOptions object. 
    graphicsOptions: GraphicsOptions = None

    # A ViewportAnnotationOptions object. 
    defaultViewportAnnotationOptions: ViewportAnnotationOptions = None

    # A repository of Queue objects. 
    queues: Repository[str, Queue] = None

    # A String specifying the name of the current viewport. 
    currentViewportName: str = ''

    # A Dictionary object specifying the viewports and their associated models. The Dictionary 
    # key specifies the viewport name. The Dictionary value is a Dictionary specifying the 
    # model name. 
    sessionState: dict = {}

    # A repository of Image objects. 
    images: Repository[str, Image] = None

    # A repository of Movie objects. 
    movies: Repository[str, Movie] = None

    # A LightOptions object. 
    defaultLightOptions: LightOptions = None

    # A DrawingArea object. 
    drawingArea: DrawingArea = None

    # A MesherOptions object specifying how to control default settings in the Mesh module. 
    defaultMesherOptions: MesherOptions = None

    # A repository of Drawing objects. 
    drawings: Repository[str, Drawing] = None

    def setValues(self, kernelMemoryLimit: float = None):
        """This method modifies the Session object.

        Parameters
        ----------
        kernelMemoryLimit
            A Float specifying the memory limit value for the Abaqus/CAE kernel process in 
            megabytes. If the limit is exceeded, Abaqus/CAE displays an error message.The default 
            memory limit value for Windows 32-bit systems if not set is 1800 MB. Increasing the 
            memory limit is not recommended unless you are using a Windows 32-bit system with the 
            boot option /3GB /userva=SizeInMBytes to extend the amount of memory available for 
            Abaqus/CAE. In this case the limit can be changed to 2800 MB.If the kernel memory size 
            reaches the **abq_ker_memory** value or the virtual memory limit of the machine, the 
            following message will be displayed:`Operation did not complete due to a memory 
            allocation failure.`For optimal performance, the memory limit should be set to a value 
            less than the physical amount of memory on the machine.The minimum setting allowed is 
            256 MB. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def enableCADConnection(self, CADName: str, portNum: int = None):
        """This method enables the Abaqus/CAE listening port for the specified *CAD* system.

        Parameters
        ----------
        CADName
            A String specifying the CAD system. Available options are Pro/ENGINEER, CATIA V5, CATIA 
            V6, NX and SolidWorks. 
        portNum
            An Integer specifying the port number to be used by the CAD system to communicate with 
            Abaqus/CAE. If unspecified, attempts will be made to identify an open port. The default 
            ports used are as follow:Pro/E : 49178CATIA V5 : 49179SolidWorks : 49180NX : 49181CATIA 
            V6 : 49182 

        Returns
        -------
            The connection port number used for the CAD connection. 

        Exceptions
        ----------
            None. 
        """
        pass

    def isCADConnectionEnabled(self):
        """This method checks the status of CAD Connection.

        Parameters
        ----------

        Returns
        -------
            A Boolean value of True if the CAD connection enabled and False if the CAD connection 
            disabled. 

        Exceptions
        ----------
            None. 
        """
        pass

    def disableCADConnection(self, CADName: str):
        """This method disables an associative import CAD connection that was enabled.

        Parameters
        ----------
        CADName
            A String specifying the CAD system for which associative import will be disabled. 
            Available options are Pro/ENGINEER, CATIA V5, and CATIA V6, NX and SolidWorks. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def enableParameterUpdate(self, CADName: str, CADVersion: str, CADPort: int = None):
        """This method enables parameter updates for ProE and NX by establishing a connection with
        the listening port previously setup by the CAD application.

        Parameters
        ----------
        CADName
            A String specifying the CAD system for which parameter update will be enabled. Available 
            options are Pro/ENGINEER and NX. 
        CADVersion
            A String specifying the CAD system version. Allowable options take the form of the 
            specific CAD system plus a version string. Examples for Pro/ENGINEER are "Wildfire5" and 
            "Creo4." An NX example is "NX11." 
        CADPort
            An Integer specifying the port number to be used by Abaqus/CAE to communicate with the 
            CAD system. If unspecified, attempts will be made to identify an open port. This port 
            number is not the same as the *portNum* used by the associative import interface. The 
            default CAD listening ports are as follow:ProE : 3344NX : 3344 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setCADPortNumber(self, CADName: str, Port: str):
        """This method enables parameter updates for CATIA V5 and CATIA V6 by establishing a
        connection with the listening port previously setup by the CAD application. This port
        number is used to send the parameter information to the CAD system.

        Parameters
        ----------
        CADName
            A String specifying the CAD system for which the port number will be saved. The 
            available options are 'CATIA V5' and ' CATIA V6'. 
        Port
            An integer specifying the port number to be used by Abaqus/CAE to send the modified 
            parameters to the CAD system. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def updateCADParameters(self, modelName: str, CADName: str, parameterFile: str, CADPartFile: str, 
                            CADPartName: str = ''):
        """This method updates the parameters for the specified model using the specified parameter
        file.

        Parameters
        ----------
        modelName
            A String specifying the model name to update. 
        CADName
            A String specifying the CAD system for which Abaqus updates the parameters. The 
            available options are 'Pro/ENGINEER', 'CATIA V5' and 'CATIA V6'. 
        parameterFile
            A parameter file containing the parameters that were exposed in the CAD system using the 
            'ABQ_' prefix. 
        CADPartFile
            A file name specifying the CAD part file for which parameter update is triggered.For 
            *CADName*='CATIA V5' or 'CATIA V6', you can specify either products or parts using this 
            argument. If you specify a product, Abaqus updates all of the parts associated with that 
            product.For *CADName*='Pro/ENGINEER', this argument is optional, and you can specify 
            update for parts only. However, a single file can be associated with multiple parts in 
            the case of family tables. In this case, Abaqus updates all listed parts. 
        CADPartName
            An String specifying the part name to update. This part name should match the part name 
            in the originating CAD system.If you specify neither *CADPartFile* nor *CADPartName* 
            during an update in which you specified *CADName*='Pro/ENGINEER', Abaqus updates all of 
            the parts in the specified file. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def disableParameterUpdate(self, CADName: str):
        """This method disables an associative CAD connection using parameters.

        Parameters
        ----------
        CADName
            A String specifying the CAD system for which the parameter update will be disabled. 
            Available option is Pro/ENGINEER. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def printToFile(self, fileName: str, format: SymbolicConstant = PNG, canvasObjects: tuple[canvas] = (), 
                    compression: Boolean = OFF):
        """This method prints canvas objects to a file using the attributes stored in the
        PrintOptions object and the appropriate format options object.

        Parameters
        ----------
        fileName
            A String specifying the file to which the image is to be written. If no file extension 
            is supplied, an extension is added based on the selected image format (.ps, .eps, .png, 
            .tif, .svg, or .svgz). 
        format
            A SymbolicConstant specifying the image format. Possible values are PNG, SVG, TIFF, PS, 
            and EPS. The default value is PNG. 
        canvasObjects
            A sequence of canvas objects (viewports, text strings, or arrows) to print. The default 
            is to print all canvas objects. 
        compression
            A Boolean specifying the format for an SVG file. It is only valid to use this argument 
            when *format* is SVG. Possible values are False (Uncompressed) and True (Compressed). 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def printToPrinter(self, printCommand: str = '', numCopies: int = 1, canvasObjects: tuple[canvas] = ()):
        """This method prints canvas objects to a Windows printer or to a PostScript printer. The
        attributes used for printing to a Windows printer are stored in the PrintOptions object
        and the PageSetupOptions object; the attributes used for printing to a PostScript
        printer are stored in the PrintOptions object and the PsOptions object.

        Parameters
        ----------
        printCommand
            A String specifying the operating system command or printer name to issue for printing 
            to the printer. The default value is “lpr” or the value specified by the printOptions 
            method. If you create a script to print directly to a Windows printer, the 
            *printCommand* must take the following 
            form:`session.printToPrinter.setValues(printCommand='PRINTER[                            
                 number of characters in name                                 ]:                     
                        printername                                 PROPERTIES[                      
                       number of characters in properties                                 ]:         
                                    document properties                                 ')           
                               `The `PROPERTIES` is a list of characters that represents the 
            printing preferences for the selected Windows printer. The properties are not required 
            in a script; the printed output will use the current settings for the selected printer. 
            You can use `'PRINTER[7]: DEFAULT'` to specify the default Windows printer. 
        numCopies
            An Int specifying the number of copies to print. Possible values are 1 ≤≤ *numCopies* ≤≤ 
            100. The default value is 1. 
        canvasObjects
            A sequence of canvas objects (viewports, text strings, or arrows) to print. The default 
            is to print all canvas objects. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            - If *printCommand* is invalid: 
              SystemError: invalid print command 
            - If the print command fails: 
              SystemError: print command failed 
            - If *numCopies* is out of range: 
              RangeError: numCopies must be in the range 1 <= value <= 100 
            - If *compression* is specified when *format* is not SVG : 
              TypeError: keyword error on compression 
        """
        pass

    def saveOptions(self, directory: SymbolicConstant):
        """This method saves your customized display settings.

        Parameters
        ----------
        directory
            A SymbolicConstant specifying the directory in which Abaqus saves the file that will be 
            used to restore your customized settings (abaqus_2021.gpr). Possible values are HOME and 
            CURRENT. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def writeVrmlFile(self, fileName: str, format: Boolean = OFF, canvasObjects: tuple[canvas] = ()):
        """This method exports the current viewport objects to a file.

        Parameters
        ----------
        fileName
            A String specifying the file to which the graphics data is to be written. If no file 
            extension is supplied, an extension is added based on the selected format (.wrl, .wrz). 
        format
            A Boolean specifying the format. Possible values are False (Uncompressed) and True 
            (Compressed). 
        canvasObjects
            A sequence of canvas objects (viewports, text strings, or arrows) to export. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def write3DXMLFile(self, fileName: str, format: Boolean = OFF, canvasObjects: tuple[canvas] = ()):
        """This method exports the current viewport objects to a file.

        Parameters
        ----------
        fileName
            A String specifying the file to which the graphics data is to be written. If no file 
            extension is supplied, (.3dxml) will be added. 
        format
            A Boolean specifying the format. Possible values are False (Uncompressed) and True 
            (Compressed). 
        canvasObjects
            A sequence of canvas objects to export. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def writeOBJFile(self, fileName: str, canvasObjects: tuple[canvas] = ()):
        """This method exports the current viewport objects to a file.

        Parameters
        ----------
        fileName
            A String specifying the file to which the graphics data is to be written. If no file 
            extension is supplied, (.obj) will be added. 
        canvasObjects
            A sequence of canvas objects to export. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
