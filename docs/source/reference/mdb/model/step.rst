====
Step
====

The Step commands described in this chapter are used to create and configure analysis steps. Step commands (output) describes the commands used to create and configure output requests and integrated output sections and the commands to configure diagnostic printing, monitoring, and restart. Step commands (miscellaneous) describes the commands used to configure controls, damping, and frequency tables.

.. toctree::
   :maxdepth: 1
   :caption: Objects in Step

   step/step_miscellaneous


Create steps
------------

.. automethod:: abaqus.Step.StepModel.StepModel.AnnealStep

.. automethod:: abaqus.Step.StepModel.StepModel.BuckleStep

.. automethod:: abaqus.Step.StepModel.StepModel.ComplexFrequencyStep

.. automethod:: abaqus.Step.StepModel.StepModel.CoupledTempDisplacementStep

.. automethod:: abaqus.Step.StepModel.StepModel.CoupledThermalElectricStep

.. automethod:: abaqus.Step.StepModel.StepModel.CoupledThermalElectricalStructuralStep

.. automethod:: abaqus.Step.StepModel.StepModel.DirectCyclicStep

.. automethod:: abaqus.Step.StepModel.StepModel.EmagTimeHarmonicStep

.. automethod:: abaqus.Step.StepModel.StepModel.ExplicitDynamicsStep

.. automethod:: abaqus.Step.StepModel.StepModel.FrequencyStep

.. automethod:: abaqus.Step.StepModel.StepModel.GeostaticStep

.. automethod:: abaqus.Step.StepModel.StepModel.HeatTransferStep

.. automethod:: abaqus.Step.StepModel.StepModel.ImplicitDynamicsStep

.. automethod:: abaqus.Step.StepModel.StepModel.MassDiffusionStep

.. automethod:: abaqus.Step.StepModel.StepModel.ModalDynamicsStep

.. automethod:: abaqus.Step.StepModel.StepModel.ModelFromInputFile

.. automethod:: abaqus.Step.StepModel.StepModel.ModelFromNastranFile

.. automethod:: abaqus.Step.StepModel.StepModel.ModelFromOdbFile

.. automethod:: abaqus.Step.StepModel.StepModel.RandomResponseStep

.. automethod:: abaqus.Step.StepModel.StepModel.ResponseSpectrumStep

.. automethod:: abaqus.Step.StepModel.StepModel.SoilsStep

.. automethod:: abaqus.Step.StepModel.StepModel.StaticLinearPerturbationStep

.. automethod:: abaqus.Step.StepModel.StepModel.StaticRiksStep

.. automethod:: abaqus.Step.StepModel.StepModel.StaticStep

.. automethod:: abaqus.Step.StepModel.StepModel.SteadyStateDirectStep

.. automethod:: abaqus.Step.StepModel.StepModel.SteadyStateModalStep

.. automethod:: abaqus.Step.StepModel.StepModel.SteadyStateSubspaceStep

.. automethod:: abaqus.Step.StepModel.StepModel.SubspaceDynamicsStep

.. automethod:: abaqus.Step.StepModel.StepModel.SubstructureGenerateStep

.. automethod:: abaqus.Step.StepModel.StepModel.TempDisplacementDynamicsStep

.. automethod:: abaqus.Step.StepModel.StepModel.ViscoStep

Object features
---------------

Step
~~~~

.. autoclass:: abaqus.Step.Step.Step
    :members:
    :inherited-members:

AnalysisStep
~~~~~~~~~~~~

.. autoclass:: abaqus.Step.AnalysisStep.AnalysisStep
    :members:

AnnealStep
~~~~~~~~~~

.. autoclass:: abaqus.Step.AnnealStep.AnnealStep
    :members:

BuckleStep
~~~~~~~~~~

.. autoclass:: abaqus.Step.BuckleStep.BuckleStep
    :members:

ComplexFrequencyStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.ComplexFrequencyStep.ComplexFrequencyStep
    :members:

CoupledTempDisplacementStep
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.CoupledTempDisplacementStep.CoupledTempDisplacementStep
    :members:

CoupledThermalElectricalStructuralStep
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.CoupledThermalElectricalStructuralStep.CoupledThermalElectricalStructuralStep
    :members:

CoupledThermalElectricStep
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.CoupledThermalElectricStep.CoupledThermalElectricStep
    :members:

DirectCyclicStep
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.DirectCyclicStep.DirectCyclicStep
    :members:

EmagTimeHarmonicStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.EmagTimeHarmonicStep.EmagTimeHarmonicStep
    :members:

ExplicitDynamicsStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.ExplicitDynamicsStep.ExplicitDynamicsStep
    :members:

FrequencyStep
~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.FrequencyStep.FrequencyStep
    :members:

GeostaticStep
~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.GeostaticStep.GeostaticStep
    :members:

HeatTransferStep
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.HeatTransferStep.HeatTransferStep
    :members:

ImplicitDynamicsStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.ImplicitDynamicsStep.ImplicitDynamicsStep
    :members:

InitialStep
~~~~~~~~~~~

.. autoclass:: abaqus.Step.InitialStep.InitialStep
    :members:

MassDiffusionStep
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.MassDiffusionStep.MassDiffusionStep
    :members:

ModalDynamicsStep
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.ModalDynamicsStep.ModalDynamicsStep
    :members:

RandomResponseStep
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.RandomResponseStep.RandomResponseStep
    :members:

ResponseSpectrumStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.ResponseSpectrumStep.ResponseSpectrumStep
    :members:

SoilsStep
~~~~~~~~~

.. autoclass:: abaqus.Step.SoilsStep.SoilsStep
    :members:

StaticLinearPerturbationStep
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.StaticLinearPerturbationStep.StaticLinearPerturbationStep
    :members:

StaticRiksStep
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.StaticRiksStep.StaticRiksStep
    :members:

StaticStep
~~~~~~~~~~

.. autoclass:: abaqus.Step.StaticStep.StaticStep
    :members:

SteadyStateDirectStep
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.SteadyStateDirectStep.SteadyStateDirectStep
    :members:

SteadyStateModalStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.SteadyStateModalStep.SteadyStateModalStep
    :members:

SteadyStateSubspaceStep
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.SteadyStateSubspaceStep.SteadyStateSubspaceStep
    :members:

SubspaceDynamicsStep
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.SubspaceDynamicsStep.SubspaceDynamicsStep
    :members:

SubstructureGenerateStep
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.SubstructureGenerateStep.SubstructureGenerateStep
    :members:

TempDisplacementDynamicsStep
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.TempDisplacementDynamicsStep.TempDisplacementDynamicsStep
    :members:

ViscoStep
~~~~~~~~~

.. autoclass:: abaqus.Step.ViscoStep.ViscoStep
    :members:
