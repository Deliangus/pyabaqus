from abaqusConstants import *
from .Load import Load
from ..Region.Region import Region


class SubmodelSB(Load):
    """The SubmodelSB object stores the data for a submodel surface based load.
    The SubmodelSB object is derived from the Load object. 

    Attributes
    ----------
    name: str
        A String specifying the load repository key.
    absoluteExteriorTolerance: float
        None or a Float specifying the absolute value by which a driven node of the submodel can
        lie outside the region of the elements of the global model. The default value is None.
    exteriorTolerance: float
        None or a Float specifying the fraction of the average element size in the global model
        by which a driven node of the submodel can lie outside the region of the elements of the
        global model. The default value is 0.05.
    globalDrivingRegion: str
        A String specifying the element set in the global model that will be searched for
        elements whose responses will be used to drive the submodel. An empty string indicates
        that the entire global model will be searched. The default value is an empty string.
    region: Region
        A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the load is applied.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import load
        mdb.models[name].loads[name]

    """

    # A String specifying the load repository key. 
    name: str = ''

    # None or a Float specifying the absolute value by which a driven node of the submodel can 
    # lie outside the region of the elements of the global model. The default value is None. 
    absoluteExteriorTolerance: float = None

    # None or a Float specifying the fraction of the average element size in the global model 
    # by which a driven node of the submodel can lie outside the region of the elements of the 
    # global model. The default value is 0.05. 
    exteriorTolerance: float = 0

    # A String specifying the element set in the global model that will be searched for 
    # elements whose responses will be used to drive the submodel. An empty string indicates 
    # that the entire global model will be searched. The default value is an empty string. 
    globalDrivingRegion: str = ''

    # A Region object specifying the region to which the load is applied. 
    region: Region = Region()

    def __init__(self, name: str, createStepName: str, region: Region, globalStep: str,
                 globalDrivingRegion: str = '', absoluteExteriorTolerance: float = None,
                 exteriorTolerance: float = 0, globalIncrement: int = 0):
        """This method creates a SubmodelSB object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].SubmodelSB
        
        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            A Region object specifying the region to which the load is applied. 
        globalStep
            A String specifying the step in the global model from which Abaqus reads the values of 
            the variables that will drive the submodel analysis. The String indicates the position 
            of the step in the sequence of analysis steps. For example, *globalStep*='1' indicates 
            the first step. 
        globalDrivingRegion
            A String specifying the element set in the global model that will be searched for 
            elements whose responses will be used to drive the submodel. An empty string indicates 
            that the entire global model will be searched. The default value is an empty string. 
        absoluteExteriorTolerance
            None or a Float specifying the absolute value by which a driven node of the submodel can 
            lie outside the region of the elements of the global model. The default value is None. 
        exteriorTolerance
            None or a Float specifying the fraction of the average element size in the global model 
            by which a driven node of the submodel can lie outside the region of the elements of the 
            global model. The default value is 0.05. 
        globalIncrement
            An Int specifying the increment number in the global model step from which the solution 
            will be used to specify the values of the driven variables. If *globalIncrement*=0, the 
            solution from the last increment will be used. The *globalIncrement* argument is 
            applicable only for linear perturbation steps. The default value is 0. 

        Returns
        -------
            A SubmodelSB object.
        """
        super().__init__()
        pass

    def setValues(self, globalDrivingRegion: str = '', absoluteExteriorTolerance: float = None,
                  exteriorTolerance: float = 0, globalIncrement: int = 0):
        """This method modifies the data for an existing SubmodelSB object in the step where it is
        created.
        
        Parameters
        ----------
        globalDrivingRegion
            A String specifying the element set in the global model that will be searched for 
            elements whose responses will be used to drive the submodel. An empty string indicates 
            that the entire global model will be searched. The default value is an empty string. 
        absoluteExteriorTolerance
            None or a Float specifying the absolute value by which a driven node of the submodel can 
            lie outside the region of the elements of the global model. The default value is None. 
        exteriorTolerance
            None or a Float specifying the fraction of the average element size in the global model 
            by which a driven node of the submodel can lie outside the region of the elements of the 
            global model. The default value is 0.05. 
        globalIncrement
            An Int specifying the increment number in the global model step from which the solution 
            will be used to specify the values of the driven variables. If *globalIncrement*=0, the 
            solution from the last increment will be used. The *globalIncrement* argument is 
            applicable only for linear perturbation steps. The default value is 0. 
        """
        pass

    def setValuesInStep(self, stepName: str, fixed: Boolean = ON, globalStep: str = '', globalIncrement: int = 0):
        """This method modifies the propagating data for an existing SubmodelSB object in the
        specified step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified. 
        fixed
            A Boolean specifying whether the load should remain fixed at the current values at the 
            start of the step. The default value is ON. 
        globalStep
            A String specifying the step in the global model from which Abaqus reads the values of 
            the variables that will drive the submodel analysis. The String indicates the position 
            of the step in the sequence of analysis steps. For example, *globalStep*='1' indicates 
            the first step. The *globalStep* argument is applicable only if *fixed*=OFF. 
        globalIncrement
            An Int specifying the increment number in the global model step at which the solution 
            will be used to specify the values of the driven variables. If *globalIncrement*=0, the 
            solution from the last increment will be used. The *globalIncrement* argument is 
            applicable only for linear perturbation steps and if *fixed*=OFF. The default value is 
            0. 
        """
        pass
