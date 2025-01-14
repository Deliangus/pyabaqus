from abaqusConstants import *
from .AcisFile import AcisFile
from ..Mdb.MdbBase import MdbBase


class AcisMdb(MdbBase):
    """The Mdb object is the high-level Abaqus model database. A model database stores models
    and analysis controls.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        mdb

    """

    @staticmethod
    def openAcis(fileName: str, scaleFromFile: Boolean = OFF):
        """This method creates an AcisFile object from a file containing ACIS-format geometry. This
        object is subsequently used by the PartFromGeometryFile method.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.openAcis
        
        Parameters
        ----------
        fileName
            A String specifying the path to the ACIS file to open.
        scaleFromFile
            A Boolean specifying whether to scale, rotate, and translate the part using the
            transform read from the ACIS file. The default value is OFF.

        Returns
        -------
            An AcisFile object.

        Raises
        ------
            - File is from a newer version of ACIS than the CAE kernel.
              Texterror: ACIS File version exceeds Kernel.
            - The data in the ACIS file are corrupted.
              Texterror: Failed to read ACIS file.
        """
        return AcisFile()

    @staticmethod
    def openCatia(fileName: str, topology: SymbolicConstant = None, convertUnits: SymbolicConstant = OFF,
                  combineBodies: Boolean = OFF):
        """This method creates an AcisFile object from a file containing V5-format geometry. This
        object is subsequently used by the PartFromGeometryFile method.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.openCatia
        
        Parameters
        ----------
        fileName
            A String specifying the path to the CATIA file to open.
        topology
            A SymbolicConstant specifying the topology of the data to be read from the file and of
            the part to be created. Possible values are SOLID , SHELL, and WIRE. If
            *topology*=SOLID, Abaqus/CAE attempts to attach cells to create a solid. If
            *topology*=SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid
            entity. The default value is SOLID .
        convertUnits
            A SymbolicConstant specifying whether the original units should be retained. Possible
            values are ON and OFF. The default value is OFF.
        combineBodies
            A Boolean specifying whether to combine the bodies in the CATPart file. If the bodies to
            be combined touch or overlap, invalid entities would result. For CATProduct files, this
            option will be ignored.

        Returns
        -------
            An AcisFile object.
        """
        return AcisFile()

    @staticmethod
    def openEnf(fileName: str, fileType: str, topology: SymbolicConstant = SOLID,
                convertUnits: Boolean = OFF):
        """This method creates an AcisFile object from a file containing Elysium Neutral
        File-format geometry that was created by CATIA V5, I-DEAS, or Pro/ENGINEER. This object
        is subsequently used by the PartFromGeometryFile method.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.openEnf
        
        Parameters
        ----------
        fileName
            A String specifying the path to the Elysium Neutral File that was created by I-DEAS,
            Pro/ENGINEER, or CATIA V5.
        fileType
            A String specifying the type of CAD system that created the file. Possible values are
            “ideas”, “proe”, or “catiav5” or a combination similar to “proe/ideas/catiav5” if the
            type is unknown.
        topology
            A SymbolicConstant specifying the topology of the data to be read from the file and of
            the part to be created. Possible values are SOLID , SHELL, and WIRE. If
            *topology*=SOLID, Abaqus/CAE attempts to attach cells to create a solid. If
            *topology*=SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid
            entity. The default value is SOLID.
        convertUnits
            A Boolean specifying if the dimensions of the part should be converted to millimeters.
            The default value is OFF.

        Returns
        -------
            An AcisFile object.
        """
        return AcisFile()

    @staticmethod
    def openIges(fileName: str, trimCurve: SymbolicConstant = DEFAULT,
                 scaleFromFile: SymbolicConstant = OFF, msbo: Boolean = False,
                 includedLayers: tuple = (), topology: SymbolicConstant = SOLID,
                 uniteWires: SymbolicConstant = ON):
        """This method creates an AcisFile object from a file containing IGES-format geometry. This
        object is subsequently used by the PartFromGeometryFile method.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.openIges
        
        Parameters
        ----------
        fileName
            A String specifying the path to the IGES file to open.
        trimCurve
            A SymbolicConstant specifying the method used to define the trim curves that bound
            parametric surfaces. Possible values are:DEFAULT, use either of the following as
            specified by the contents of the IGES file.PARAMETRIC_DATA, use the parameter space of
            the surface being trimmed.THREED_DATA, use real space—the coordinate system of the part
            along with an indication that the trim curve lies on the parametric surface.The default
            value is DEFAULT.
        scaleFromFile
            A SymbolicConstant specifying whether the imported geometry needs to be scaled using the
            units information available in the IGES file. Possible values are ON and OFF. The
            default value is OFF. When the argument is set to ON, the geometry is scaled to
            millimeters with respect to the unit system specified in the IGES file.
        msbo
            A Boolean specifying if the IGES file contains MSBO (Manifold Solid B-Rep Object)
            entities. The default value is False.
        includedLayers
            A sequence of Ints specifying the levels or layers of entities that will be translated
            from the IGES file to build the part. The default is to include all the layers.
        topology
            A SymbolicConstant specifying the topology of the data to be read from the file and of
            the part to be created. Possible values are SOLID , SHELL, and WIRE. If
            *topology*=SOLID, Abaqus/CAE attempts to attach cells to create a solid. If
            *topology*=SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid
            entity. The default value is SOLID.
        uniteWires
            A SymbolicConstant specifying whether the imported wires need to be united or not.
            Possible values are ON and OFF. The default value is ON. When importing a sketch, this
            value is set to OFF.

        Returns
        -------
            An AcisFile object.

        Raises
        ------
            - The data in the IGES file are corrupted.
              Texterror: Failed to read IGES file.
        """
        return AcisFile()

    @staticmethod
    def openParasolid(fileName: str, topology: SymbolicConstant = SOLID):
        """This method creates an AcisFile object from a file containing Parasolid-format geometry.
        This object is subsequently used by the PartFromGeometryFile method.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.openParasolid
        
        Parameters
        ----------
        fileName
            A String specifying the path to the Parasolid file to open.
        topology
            A SymbolicConstant specifying the topology of the data to be read from the file and of
            the part to be created. Possible values are SOLID , SHELL, and WIRE. If
            *topology*=SOLID, Abaqus/CAE attempts to attach cells to create a solid. If
            *topology*=SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid
            entity. The default value is SOLID.

        Returns
        -------
            An AcisFile object.
        """
        return AcisFile()

    @staticmethod
    def openStep(fileName: str, scale: float = 1):
        """This method creates an AcisFile object from a file containing STEP-format geometry. This
        object is subsequently used by the PartFromGeometryFile method.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.openStep
        
        Parameters
        ----------
        fileName
            A String specifying the path to the STEP file to open.
        scale
            A Float specifying the scaling factor to apply to the imported geometric entities. The
            default value is 1.0.

        Returns
        -------
            An AcisFile object.

        Raises
        ------
            - The data in the STEP file are corrupted.
              Texterror: Failed to read STEP file.
        """
        return AcisFile()

    @staticmethod
    def openVda(fileName: str):
        """This method creates an AcisFile object from a file containing VDA-FS-format geometry.
        This object is subsequently used by the PartFromGeometryFile method.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.openVda
        
        Parameters
        ----------
        fileName
            A String specifying the path to the VDA-FS file to open.

        Returns
        -------
            An AcisFile object.

        Raises
        ------
            - The data in the VDA-FS file are corrupted.
              Texterror: Failed to read VDA file.
        """
        return AcisFile()

    @staticmethod
    def openSolidworks(fileName: str, topology: SymbolicConstant = SOLID):
        """This method creates an AcisFile object from a file containing Solidworks format
        geometry. This object is subsequently used by the PartFromGeometryFile method.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                openSolidworks
        
        Parameters
        ----------
        fileName
            A String specifying the path to the Solidworks file to open.
        topology
            A SymbolicConstant specifying the topology of the data to be read from the file and of
            the part to be created. Possible values are SOLID, SHELL, and WIRE. If *topology*=SOLID,
            Abaqus/CAE attempts to attach cells to create a solid entity. If *topology*=SHELL,
            Abaqus/CAE builds the body as a shell entity, not as a solid entity. The default value
            is SOLID.

        Returns
        -------
            An AcisFile object.

        Raises
        ------
            - The data in the Solidworks file are corrupted.
              Texterror: Failed to read Solidworks file.
        """
        return AcisFile()
