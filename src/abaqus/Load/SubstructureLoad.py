from abaqusConstants import *
from .Load import Load
from ..Region.Region import Region


class SubstructureLoad(Load):
    """The SubstructureLoad object defines a substructure load.
    The SubstructureLoad object is derived from the Load object. 

    Attributes
    ----------
    name: str
        A String specifying the load repository key.
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

    # A Region object specifying the region to which the load is applied. 
    region: Region = Region()

    def __init__(self, name: str, createStepName: str, region: Region, loadCaseNames: str, magnitude: float,
                 amplitude: str = UNSET):
        """This method creates a SubstructureLoad object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].SubstructureLoad
        
        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the substructure load is created. 
        region
            A Region object specifying the region to which the load is applied. 
        loadCaseNames
            A list of names of the load cases that should be activated by this substructure load. 
        magnitude
            A Float specifying the multiplier for the load case magnitude. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A SubstructureLoad object.
        """
        super().__init__()
        pass

    def setValues(self, amplitude: str = UNSET):
        """This method modifies the data for an existing SubstructureLoad object in the step where
        it is created.
        
        Parameters
        ----------
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        """
        pass

    def setValuesInStep(self, stepName: str, loadCaseNames: str = '', magnitude: float = None, amplitude: str = ''):
        """This method modifies the propagating data for an existing SubstructureLoad object in the
        specified step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified. 
        loadCaseNames
            A list of names of the load cases that should be activated by this substructure load. 
        magnitude
            A Float specifying the multiplier for the load case magnitude. 
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible 
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the 
            amplitude is propagated from the previous analysis step. FREED should be used if the 
            load has no amplitude reference. You should provide the *amplitude* argument only if it 
            is valid for the specified step. 
        """
        pass
