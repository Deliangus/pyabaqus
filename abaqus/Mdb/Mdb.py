from abaqus.Job.ModelJob import ModelJob
from abaqusConstants import *
from .MdbBase import MdbBase
from ..Job.JobMdb import JobMdb
from ..Model.Model import Model
from ..Part.AcisMdb import AcisMdb


class Mdb(AcisMdb, JobMdb):

    def Model(self, name: str, description: str = '', stefanBoltzmann: float = None,
              absoluteZero: float = None, waveFormulation: SymbolicConstant = NOT_SET,
              modelType: SymbolicConstant = STANDARD_EXPLICIT, universalGas: float = None,
              copyConstraints: Boolean = ON, copyConnectors: Boolean = ON,
              copyInteractions: Boolean = ON) -> Model:
        """This method creates a Model object.

        Path
        ----
            - mdb.Model

        Parameters
        ----------
        name
            A String specifying the repository key.
        description
            A String specifying the purpose and contents of the Model object. The default value is
            an empty string.
        stefanBoltzmann
            None or a Float specifying the Stefan-Boltzmann constant. The default value is None.
        absoluteZero
            None or a Float specifying the absolute zero constant. The default value is None.
        waveFormulation
            A SymbolicConstant specifying the type of incident wave formulation to be used in
            acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value
            is NOT_SET.
        modelType
            A SymbolicConstant specifying the analysis model type. Possible values are
            STANDARD_EXPLICIT and ELECTROMAGNETIC. The default is STANDARD_EXPLICIT.
        universalGas
            None or a Float specifying the universal gas constant. The default value is None.
        copyConstraints
            A boolean specifying whether to copy the constraints created in the model to the model
            that instances this model. The default value is ON.
        copyConnectors
            A boolean specifying whether to copy the connectors created in the model to the model
            that instances this model. The default value is ON.
        copyInteractions
            A boolean specifying whether to copy the interactions created in the model to the model
            that instances this model. The default value is ON.

        Returns
        -------
        model: Model
            A Model object
        """
        self.models[name] = model = Model(name, description, stefanBoltzmann, absoluteZero, waveFormulation, modelType,
                                          universalGas, copyConstraints, copyConnectors, copyInteractions)
        return model
    
