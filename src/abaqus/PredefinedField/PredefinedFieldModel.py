from abaqusConstants import *
from .Field import Field
from .FluidCavityPressure import FluidCavityPressure
from .InitialState import InitialState
from .KinematicHardening import KinematicHardening
from .MaterialAssignment import MaterialAssignment
from .Stress import Stress
from .Temperature import Temperature
from .Velocity import Velocity
from ..Assembly.PartInstanceArray import PartInstanceArray
from ..Model.ModelBase import ModelBase
from ..Region.Region import Region


class PredefinedFieldModel(ModelBase, Field, FluidCavityPressure, InitialState, KinematicHardening, MaterialAssignment,
                           Stress, Temperature, Velocity):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        mdb.models[name]

    """

    def Field(self, name: str, createStepName: str, region: Region, outputVariable: str = '',
              fieldVariableNum: int = None, distributionType: SymbolicConstant = UNIFORM,
              crossSectionDistribution: SymbolicConstant = CONSTANT_THROUGH_THICKNESS,
              field: str = '', amplitude: str = UNSET, fileName: str = '',
              beginStep: SymbolicConstant = None, beginIncrement: SymbolicConstant = None,
              endStep: SymbolicConstant = None, endIncrement: SymbolicConstant = None,
              interpolate: SymbolicConstant = OFF, magnitudes: str = '') -> Field:
        """This method creates a Field object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].Field
        
        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the predefined field is created.
        region
            A Region object specifying the region to which the predefined field is applied. *Region*
            is ignored if the predefined field has a *distributionType* member available, and
            *distributionType*=FROM_FILE.
        outputVariable
            A String specifying the scalar nodal output variable that will be read from an output
            database and used to initialize a specified predefined field. This argument is a
            required argument if *distributionType*=FROM_FILE or
            *distributionType*=FROM_FILE_AND_USER_DEFINED.
        fieldVariableNum
            An Int specifying the field variable number.
        distributionType
            A SymbolicConstant specifying how the predefined field varies spatially. Possible values
            are UNIFORM, USER_DEFINED, FROM_FILE, FIELD, FROM_FILE_AND_USER_DEFINED, and
            DISCRETE_FIELD. The default value is UNIFORM.
        crossSectionDistribution
            A SymbolicConstant specifying how the predefined field is distributed over the
            cross-section of the region. Possible values are
            - CONSTANT_THROUGH_THICKNESS
            - GRADIENTS_THROUGH_SHELL_CS
            - GRADIENTS_THROUGH_BEAM_CS
            - POINTS_THROUGH_SECTION
            The default value is CONSTANT_THROUGH_THICKNESS.
        field
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with this predefined field. The *field* argument applies only when
            *distributionType*=FIELD or *distributionType*=DISCRETE_FIELD. The default value is an
            empty string.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the predefined field has no amplitude reference. The default
            value is UNSET.Note:*amplitude* should be given only if it is valid for the specified
            step.
        fileName
            A String specifying the name of the file from which the Field values are to be read when
            *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED.
        beginStep
            An Int specifying the first step from which Field values are to be read or the
            SymbolicConstant FIRST_STEP or LAST_STEP. This argument is valid only when
            *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        beginIncrement
            An Int specifying the first increment of the step set in *beginStep* or the
            SymbolicConstants STEP_START or STEP_END. This argument is valid only when
            *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        endStep
            An Int specifying the last step from which Field values are to be read or the
            SymbolicConstants FIRST_STEP and LAST_STEP. This argument is valid only when
            *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        endIncrement
            An Int specifying the last increment of the step set in *endStep* or the
            SymbolicConstants STEP_START and STEP_END. This argument is valid only when
            *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        interpolate
            A SymbolicConstant specifying whether to interpolate a field read from an output
            database or results file. Possible values are OFF, ON, or MIDSIDE_ONLY. The default
            value is OFF.
        magnitudes
            A Sequence of Doubles specifying the Field values when *distributionType*=UNIFORM or
            FIELD. The value of the *magnitudes* argument is a function of the
            *crossSectionDistribution* argument, as shown in the following list:
            - If *crossSectionDistribution*=CONSTANT_THROUGH_THICKNESS, *magnitudes* is a Double
            specifying the Field.
            - If *crossSectionDistribution*=GRADIENTS_THROUGH_SHELL_CS, *magnitudes* is a sequence
            of Doubles specifying the mean value and the gradient in the thickness direction.
            - If *crossSectionDistribution*=GRADIENTS_THROUGH_BEAM_CS, *magnitudes* is a sequence of
            Doubles specifying the mean value, the gradient in the N1 direction, and the gradient in
            the N2 direction.
            - If *crossSectionDistribution*=POINTS_THROUGH_SECTION, *magnitudes* is a sequence of
            Doubles specifying the Field at each point.

        Returns
        -------
            A Field object.
        """
        self.predefinedFields[name] = predefinedField = Field(name, createStepName, region, outputVariable,
                                                              fieldVariableNum, distributionType,
                                                              crossSectionDistribution, field, amplitude, fileName,
                                                              beginStep, beginIncrement, endStep, endIncrement,
                                                              interpolate, magnitudes)
        return predefinedField

    def FluidCavityPressure(self, name: str, fluidCavity: str, fluidPressure: float) -> FluidCavityPressure:
        """This method creates a FluidCavityPressure object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].FluidCavityPressure
        
        Parameters
        ----------
        name
            A String specifying the repository key.
        fluidCavity
            A String specifying the name of a Fluid Cavity Interaction.
        fluidPressure
            A Float specifying the initial fluid pressure.

        Returns
        -------
            A FluidCavityPressure object.
        """
        self.predefinedFields[name] = predefinedField = FluidCavityPressure(name, fluidCavity, fluidPressure)
        return predefinedField

    def InitialState(self, name: str, instances: PartInstanceArray, fileName: str,
                     endStep: SymbolicConstant = LAST_STEP, endIncrement: SymbolicConstant = STEP_END,
                     updateReferenceConfiguration: Boolean = OFF) -> InitialState:
        """This method creates an InitialState predefined field object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].InitialState
        
        Parameters
        ----------
        name
            A String specifying the repository key.
        instances
            A PartInstanceArray object specifying the instances to which the predefined field is
            applied.
        fileName
            A String specifying the name of the job that generated the initial state data.
        endStep
            The SymbolicConstant LAST_STEP or an Int specifying the step from which the initial
            state values are to be read or the SymbolicConstant LAST_STEP. The default value is
            LAST_STEP.
        endIncrement
            The SymbolicConstant STEP_END or an Int specifying the increment, interval or iteration
            of the step set in *endStep* or the SymbolicConstant STEP_END. The default value is
            STEP_END.
        updateReferenceConfiguration
            A Boolean specifying whether to update the reference configuration based on the import
            data. The default value is OFF.

        Returns
        -------
            An InitialState object.
        """
        self.predefinedFields[name] = predefinedField = InitialState(name, instances, fileName, endStep, endIncrement,
                                                                     updateReferenceConfiguration)
        return predefinedField

    def KinematicHardening(self, name: str, region: Region, numBackStress: int = 1, equivPlasticStrain: tuple = (),
                           backStress: tuple = (), sectPtNum: tuple = (),
                           definition: SymbolicConstant = KINEMATIC_HARDENING, rebarLayerNames: tuple = (),
                           distributionType: SymbolicConstant = MAGNITUDE) -> KinematicHardening:
        """This method creates a KinematicHardening object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].KinematicHardening
        
        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A Region object specifying the region to which the predefined field is applied.
        numBackStress
            An Int specifying the number of backstresses. The default value is 1.
        equivPlasticStrain
            A sequence of Floats specifying the initial equivalent Plastic strain.
        backStress
            A sequence of sequences of Floats specifying the initial backstress tensor for kinematic
            hardening models. The default value is an empty sequence.
        sectPtNum
            A sequence of Ints specifying section point numbers. This argument is valid only when
            *definition*=SECTION_PTS.
        definition
            A SymbolicConstant specifying different types of kinematic hardening. Possible values
            are KINEMATIC_HARDENING, CRUSHABLE_FOAM, REBAR, SECTION_PTS, and USER_DEFINED. The
            default value is KINEMATIC_HARDENING.
        rebarLayerNames
            A sequence of Strings specifying rebar layer names. This argument is valid only when
            *definition*=REBAR.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are MAGNITUDE
            and ANALYTICAL_FIELD. The default value is MAGNITUDE.

        Returns
        -------
            A KinematicHardening object.
        """
        self.predefinedFields[name] = predefinedField = KinematicHardening(name, region, numBackStress,
                                                                           equivPlasticStrain, backStress, sectPtNum,
                                                                           definition, rebarLayerNames,
                                                                           distributionType)
        return predefinedField

    def MaterialAssignment(self, name: str, instanceList: PartInstanceArray, useFields: Boolean = OFF,
                           assignmentList: tuple = (), fieldList: tuple = (),
                           colorList: tuple = ()) -> MaterialAssignment:
        """This method creates a MaterialAssignment predefined field object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].MaterialAssignment
        
        Parameters
        ----------
        name
            A String specifying the repository key.
        instanceList
            A PartInstanceArray object specifying the part instances to which the predefined field
            is applied. All instances must be assigned the same Eulerian section.
        useFields
            A Boolean specifying whether the volume fraction data will be uniform or defined by
            discrete fields. The default value is OFF.
        assignmentList
            A sequence of tuples specifying the uniform volume fractions to be assigned. This
            argument is valid only when *useFields*=FALSE. Each tuple contains two entries:A Region
            object.A tuple of Floats specifying the uniform volume fraction values. The length of
            the tuple must match the number of material instance names specified in the Eulerain
            section assigned to part instances specified by *instanceList*.
        fieldList
            A sequence of tuples specifying the discrete volume fractions to be assigned. This
            argument is valid only when *useFields*=TRUE. Each tuple contains two entries:A Region
            object.A tuple of Strings specifying Discrete Field names. The length of the tuple must
            match the number of material instance names specified in the Eulerain section assigned
            to part instances specified by *instanceList*.
        colorList
            A sequence of three Ints specifying colors used to display the material instance
            assignments. This is a sequence of R,G,B colors, where the values are represented by
            integers between 0 and 255. The default value is an empty sequence.

        Returns
        -------
            A MaterialAssignment object.
        """
        self.predefinedFields[name] = predefinedField = MaterialAssignment(name, instanceList, useFields,
                                                                           assignmentList, fieldList, colorList)
        return predefinedField

    def Stress(self, name: str, region: Region, distributionType: SymbolicConstant = UNIFORM,
               sigma11: float = None, sigma22: float = None, sigma33: float = None,
               sigma12: float = None, sigma13: float = None, sigma23: float = None) -> Stress:
        """This method creates a Stress predefined field object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].Stress
        
        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A Region object specifying the region to which the predefined field is applied. Region
            is ignored if the predefined field has *distributionType*=FROM_FILE.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM
            and FROM_FILE. The default value is UNIFORM.
        sigma11
            A Float specifying the first principal component of the stress.
        sigma22
            A Float specifying the second principal component of the stress.
        sigma33
            A Float specifying the third principal component of the stress.
        sigma12
            A Float specifying the first shear component of the stress.
        sigma13
            A Float specifying the second shear component of the stress.
        sigma23
            A Float specifying the third shear component of the stress.

        Returns
        -------
            A Stress object.
        """
        self.predefinedFields[name] = predefinedField = Stress(name, region, distributionType, sigma11, sigma22,
                                                               sigma33, sigma12, sigma13, sigma23)
        return predefinedField

    def Temperature(self, name: str, createStepName: str, region: Region,
                    distributionType: SymbolicConstant = UNIFORM,
                    crossSectionDistribution: SymbolicConstant = CONSTANT_THROUGH_THICKNESS,
                    field: str = '', amplitude: str = UNSET, fileName: str = '',
                    beginStep: SymbolicConstant = None, beginIncrement: SymbolicConstant = None,
                    endStep: SymbolicConstant = None, endIncrement: SymbolicConstant = None,
                    interpolate: SymbolicConstant = OFF, magnitudes: str = '',
                    absoluteExteriorTolerance: float = 0, exteriorTolerance: float = 0) -> Temperature:
        """This method creates a Temperature object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].Temperature
        
        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the predefined field is created.
        region
            A Region object specifying the region to which the predefined field is applied. *Region*
            is ignored if the predefined field has a *distributionType* member available, and
            *distributionType*=FROM_FILE .
        distributionType
            A SymbolicConstant specifying how the predefined field varies spatially. Possible values
            are UNIFORM, USER_DEFINED, FROM_FILE, FIELD, FROM_FILE_AND_USER_DEFINED, and
            DISCRETE_FIELD. The default value is UNIFORM.
        crossSectionDistribution
            A SymbolicConstant specifying how the predefined field is distributed over the cross
            section of the region. Possible values are
            - CONSTANT_THROUGH_THICKNESS
            - GRADIENTS_THROUGH_SHELL_CS
            - GRADIENTS_THROUGH_BEAM_CS
            - POINTS_THROUGH_SECTION
            The default value is CONSTANT_THROUGH_THICKNESS.
        field
            A String specifying the name of the AnalyticalField or DiscreteField object associated
            with this predefined field. The *field* argument applies only when
            *distributionType*=FIELD or *distributionType*=DISCRETE_FIELD. The default value is an
            empty string.
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
            UNSET should be used if the predefined field has no amplitude reference. The default
            value is UNSET.Note:*amplitude* should be given only if it is valid for the specified
            step.
        fileName
            A String specifying the name of the file from which the temperature values are to be
            read when *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED.
        beginStep
            An Int specifying the first step from which temperature values are to be read or the
            SymbolicConstant FIRST_STEP or LAST_STEP. This argument is valid only when
            *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        beginIncrement
            An Int specifying the first increment of the step set in *beginStep* or the
            SymbolicConstants STEP_START or STEP_END. This argument is valid only when
            *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        endStep
            An Int specifying the last step from which temperature values are to be read or the
            SymbolicConstants FIRST_STEP and LAST_STEP. This argument is valid only when
            *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        endIncrement
            An Int specifying the last increment of the step set in *endStep* or the
            SymbolicConstants STEP_START and STEP_END. This argument is valid only when
            *distributionType*=FROM_FILE or *distributionType*=FROM_FILE_AND_USER_DEFINED. The
            default value is None.
        interpolate
            A SymbolicConstant specifying whether to interpolate a field read from an output
            database or results file. Possible values are OFF, ON or MIDSIDE_ONLY. The default value
            is OFF.
        magnitudes
            A Sequence of Doubles specifying the temperature values when *distributionType*=UNIFORM
            or FIELD. The value of the *magnitudes* argument is a function of the
            *crossSectionDistribution* argument, as shown in the following list:
            - If *crossSectionDistribution*=CONSTANT_THROUGH_THICKNESS then *magnitudes* is a Double
            specifying the temperature.
            - If *crossSectionDistribution*=GRADIENTS_THROUGH_SHELL_CS then *magnitudes* is a
            sequence of Doubles specifying the mean value and the gradient in the thickness
            direction.
            - If *crossSectionDistribution*=GRADIENTS_THROUGH_BEAM_CS then *magnitudes* is a
            sequence of Doubles specifying the mean value, the gradient in the N1 direction, and the
            gradient in the N2 direction.
            - If *crossSectionDistribution*=POINTS_THROUGH_SECTION then *magnitudes* is a sequence
            of Doubles specifying the temperature at each point.
        absoluteExteriorTolerance
            A Float specifying the absolute value by which a driven node of the field can lie
            outside the region of the elements of the global model. The default value is 0.0. This
            argument cannot be used with *midside*.
        exteriorTolerance
            A Float specifying the fraction of the average element size in the global model by which
            a driven node of the field can lie outside the region of the elements of the global
            model. The default value is 0.0. This argument cannot be used with *midside*.

        Returns
        -------
            A Temperature object.
        """
        self.predefinedFields[name] = predefinedField = Temperature(name, createStepName, region, distributionType,
                                                                    crossSectionDistribution, field, amplitude,
                                                                    fileName, beginStep, beginIncrement, endStep,
                                                                    endIncrement, interpolate, magnitudes,
                                                                    absoluteExteriorTolerance, exteriorTolerance)
        return predefinedField

    def Velocity(self, name: str, region: Region, velocity1: float, velocity2: float, velocity3: float,
                 omega: float, axisBegin: tuple, axisEnd: tuple, field: str = '',
                 distributionType: SymbolicConstant = MAGNITUDE) -> Velocity:
        """This method creates a Velocity predefined field object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].Velocity
        
        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A Region object specifying the region to which the predefined field is applied.
        velocity1
            A Float specifying the first component of the velocity.
        velocity2
            A Float specifying the second component of the velocity.
        velocity3
            A Float specifying the third component of the velocity.
        omega
            A Float specifying the angular velocity.
        axisBegin
            A sequence of Floats specifying the *X-*, *Y-*, and *Z*- coordinates of the starting
            point of the axis about which *omega* is defined.
        axisEnd
            A sequence of Floats specifying the *X-*, *Y-*, and *Z*- coordinates of the end point of
            the axis about which *omega* is defined.
        field
            A String specifying the name of the AnalyticalField object associated with this
            predefined field. The *field* argument applies only when
            *distributionType*=FIELD_ANALYTICAL. The default value is an empty string.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are MAGNITUDE
            and FIELD_ANALYTICAL. The default value is MAGNITUDE.

        Returns
        -------
            A Velocity object.
        """
        self.predefinedFields[name] = predefinedField = Velocity(name, region, velocity1, velocity2, velocity3, omega,
                                                                 axisBegin, axisEnd, field, distributionType)
        return predefinedField
