from abaqusConstants import *


class OptimizationProcess:
    """The OptimizationProcess object defines a process to perform an optimization of a model
    defined using an optimization task. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import job
        mdb.optimizationProcesses[name]

    """

    def __init__(self, name: str, model: str, task: str, prototypeJob: str, description: str = '',
                 maxDesignCycle: int = 15, dataSaveFrequency: str = OPT_DATASAVE_SPECIFY_CYCLE,
                 saveInitial: Boolean = True, saveFirst: Boolean = True, saveLast: Boolean = True,
                 saveEvery: int = None):
        """This method creates an OptimizationProcess object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.OptimizationProcess
            
        Parameters
        ----------
        name
            A String specifying name of the optimization process. 
        model
            A String specifying name of the model to be used for the optimization process. 
        task
            A String specifying name of the optimization task to be used for the optimization 
            process. 
        prototypeJob
            A String specifying name of the job to be used as the prototype for all analysis jobs 
            run by the optimization process. 
        description
            A String specifying a description of the optimization process. 
        maxDesignCycle
            An Int specifying the maximum number of allowed design cycles for the optimization 
            process. The default value is 15. 
        dataSaveFrequency
            An Enum specifying whether Abaqus should save every iteration file in the optimization 
            process or a selection of iteration files saved at a user-specified frequency. If you 
            set *dataSaveFrequency*=OPT_DATASAVE_EVERY_CYCLE, Abaqus saves every iteration file; if 
            you set *dataSaveFrequency*=OPT_DATASAVE_SPECIFY_CYCLE, Abaqus saves iteration files 
            according to the frequency defined by the *saveEvery* parameter. The default value is 
            OPT_DATASAVE_SPECIFY_CYCLE. 
        saveInitial
            A Boolean specifying whether the initial cycle should be saved when *dataSaveFrequency* 
            is OPT_DATASAVE_SPECIFY_CYCLE. The default value is True. 
        saveFirst
            A Boolean specifying whether the first cycle should be saved when *dataSaveFrequency* is 
            OPT_DATASAVE_SPECIFY_CYCLE. The default value is True. 
        saveLast
            A Boolean specifying whether the last cycle should be saved when *dataSaveFrequency* is 
            OPT_DATASAVE_SPECIFY_CYCLE. The default value is True. 
        saveEvery
            An Int specifying every nth cycle iterations to be saved when *dataSaveFrequency* is 
            OPT_DATASAVE_SPECIFY_CYCLE. Abaqus saves file iterations for every nth iteration after 
            iteration 1; if you set *saveEvery*=3, Abaqus saves file iterations for cycles 1, 4, 7, 
            and so on. The default value is None. 

        Returns
        -------
            An OptimizationProcess object. 

        Raises
        ------
            AbaqusException. 
        """
        pass

    def writeParAndInputFiles(self):
        """This method allows you to write par and input files for an optimization task.
        """
        pass

    def submit(self, validate: Boolean = False):
        """This method submits an optimization process.
        
        Parameters
        ----------
        validate
            A Boolean specifying whether Abaqus should perform the validation of the optimization 
            process only. The default value is False. 
        """
        pass

    def waitForCompletion(self):
        """This method interrupts the execution of the script until the end of all the analyses. If
        you call the waitForCompletion method and the *status* member is neither SUBMITTED nor
        RUNNING, Abaqus assumes the analysis has either completed or aborted and returns
        immediately.
        """
        pass

    def extract(self, outputFileName: str, designCycle: str, isoValue: str = 0, smoothCycles: str = 5,
                reductionPercent: str = 0, reductionAngle: str = '', targetVolume: str = 0,
                extractFormat: tuple = OPT_EXTRACT_SMOOTH_ABAQUS_INPUT_FILE, resultFiltering: str = OFF,
                instances: str = ''):
        """This method extracts a surface mesh from the optimized model.
        
        Parameters
        ----------
        outputFileName
            Name of the output file for the extracted surface mesh. 
        designCycle
            The design cycle number for which the surface mesh should be extracted. 
        isoValue
            Value used to determine the positions on the element edges where the new nodes are 
            created. Value between 0 and 1. The default value is 0.3. 
        smoothCycles
            Number of smoothing cycles; if set to 0, no smoothing is performed. The default value is 
            5. 
        reductionPercent
            Defines the percent of faces that should be removed during the data reduction. If set to 
            0, no data reduction occurs. If set to 100, the data reduction stops when no faces can 
            be removed (that is checked using reductionAngle parameter). Value between 0 and 100. 
            The default value is 0. 
        reductionAngle
            Defines the maximal angle between adjacent faces at a node such that the node may be 
            removed during the data reduction. Value in degrees between 0 and 90. The default value 
            is15. 
        targetVolume
            Defines the target volume that is to be achieved iteratively by varying the isovalue. 
            Value between 0 and 1. The default value is 0. 
        extractFormat
            A tuple for the types of format of the output. Possible values are 
            OPT_EXTRACT_SMOOTH_ABAQUS_INPUT_FILE, OPT_EXTRACT_SMOOTH_STL, OPT_EXTRACT_SMOOTH_IGES1, 
            OPT_EXTRACT_SMOOTH_IGES2, or OPT_EXTRACT_SMOOTH_IGES3. The default value is 
            OPT_EXTRACT_SMOOTH_ABAQUS_INPUT_FILE. 
        resultFiltering
            Possible string values are OFF or MODERATE or FULL. Defines if the element material 
            values are to be filtered (averaged locally) before the isocut, and to what extent. The 
            default value is OFF. 
        instances
            Defines a list of names of part instances to be used for surface extraction. One file 
            (according to extractFormat) is created for each part instance. If the argument is not 
            specified, no part instance is selected and surface is generated for the whole model. 
        """
        pass

    def setValues(self, description: str = '', maxDesignCycle: int = 15,
                  dataSaveFrequency: str = OPT_DATASAVE_SPECIFY_CYCLE, saveInitial: Boolean = True,
                  saveFirst: Boolean = True, saveLast: Boolean = True, saveEvery: int = None):
        """This method modifies the OptimizationProcess object.
        
        Parameters
        ----------
        description
            A String specifying a description of the optimization process. 
        maxDesignCycle
            An Int specifying the maximum number of allowed design cycles for the optimization 
            process. The default value is 15. 
        dataSaveFrequency
            An Enum specifying whether Abaqus should save every iteration file in the optimization 
            process or a selection of iteration files saved at a user-specified frequency. If you 
            set *dataSaveFrequency*=OPT_DATASAVE_EVERY_CYCLE, Abaqus saves every iteration file; if 
            you set *dataSaveFrequency*=OPT_DATASAVE_SPECIFY_CYCLE, Abaqus saves iteration files 
            according to the frequency defined by the *saveEvery* parameter. The default value is 
            OPT_DATASAVE_SPECIFY_CYCLE. 
        saveInitial
            A Boolean specifying whether the initial cycle should be saved when *dataSaveFrequency* 
            is OPT_DATASAVE_SPECIFY_CYCLE. The default value is True. 
        saveFirst
            A Boolean specifying whether the first cycle should be saved when *dataSaveFrequency* is 
            OPT_DATASAVE_SPECIFY_CYCLE. The default value is True. 
        saveLast
            A Boolean specifying whether the last cycle should be saved when *dataSaveFrequency* is 
            OPT_DATASAVE_SPECIFY_CYCLE. The default value is True. 
        saveEvery
            An Int specifying every nth cycle iterations to be saved when *dataSaveFrequency* is 
            OPT_DATASAVE_SPECIFY_CYCLE. Abaqus saves file iterations for every nth iteration after 
            iteration 1; if you set *saveEvery*=3, Abaqus saves file iterations for cycles 1, 4, 7, 
            and so on. The default value is None. 
        """
        pass
