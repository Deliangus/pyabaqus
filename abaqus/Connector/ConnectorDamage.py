from abaqusConstants import *
from .ConnectorBehaviorOption import ConnectorBehaviorOption
from .ConnectorOptions import ConnectorOptions
from .ConnectorPotentialArray import ConnectorPotentialArray


class ConnectorDamage(ConnectorBehaviorOption):
    """The ConnectorDamage object defines damage behavior for one or more components of a
    connector's relative motion. 
    The ConnectorDamage object is derived from the ConnectorBehaviorOption object. 

    Notes
    -----
        This object can be accessed by:
        - import section
        - mdb.models[name].sections[name].behaviorOptions[i]
        - import odbSection
        - session.odbs[name].sections[name].behaviorOptions[i]

    Table Data
    ----------
        Table data for *initiationTable*:
        If *criterion*=FORCE, then each sequence of the table data specifies the following:
        - Lower (compression) limiting force or moment. Use -1.0E+36 to indicate an unspecified lower limit.
        - Upper (tension) limiting force or moment. Use 1.0E+36 to indicate an unspecified upper limit. At least one
          limit, lower or upper, must be specified.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *criterion*=MOTION, then each sequence of the table data specifies the following:
        - Lower (compression) limiting connector constitutive relative displacement or rotation. Use -1.0E+36 to
          indicate an unspecified lower limit.
        - Upper (tension) limiting connector constitutive relative displacement or rotation. Use 1.0E+36 to indicate an
          unspecified upper limit. At least one limit, lower or upper, must be specified.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *criterion*=PLASTIC_MOTION, then each sequence of the table data specifies the following:
        - Relative equivalent Plastic displacement/rotation at which damage will be initiated.
        - Mode-mix ratio (only if *coupling*=COUPLED).
        - Relative equivalent Plastic displacement/rotation rate.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        Table data for *evolutionTable*:
        If *evolutionType*=MOTION and *softening*=LINEAR, then each sequence of the table data specifies the following:
        - Post-initiation equivalent relative Plastic motion at ultimate failure if *criterion*=PLASTIC_MOTION.
          Otherwise, post-initiation constitutive relative motion (displacement/rotation) at ultimate failure.
        - Mode-mix ratio (only if *coupling*=COUPLED and *criterion*=PLASTIC_MOTION).
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *evolutionType*=MOTION and *softening*=EXPONENTIAL, then each sequence of the table data specifies the following:
        - Post-initiation equivalent relative Plastic motion at ultimate failure if *criterion*=PLASTIC_MOTION.
          Otherwise, post-initiation constitutive relative motion (displacement/rotation) at ultimate failure.
        - Exponential law parameter.
        - Mode-mix ratio (only if *coupling*=COUPLED and *criterion*=PLASTIC_MOTION).
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *evolutionType*=MOTION and *softening*=TABULAR, then each sequence of the table data specifies the following:
        - Damage variable (cannot be less than 0 or greater than 1).
        - Post-initiation equivalent relative Plastic motion if *criterion*=PLASTIC_MOTION. Otherwise, post-initiation
          constitutive relative motion (displacement/rotation).
        - Mode-mix ratio (only if *coupling*=COUPLED and *criterion*=PLASTIC_MOTION).
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *evolutionType*=ENERGY, then each sequence of the table data specifies the following:
        - Total energy dissipated by damage at ultimate failure.
        - Mode-mix ratio (only if *coupling*=COUPLED and *criterion*=PLASTIC_MOTION).
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - CONNECTOR DAMAGE INITIATION

    """

    # A ConnectorOptions object specifying the ConnectorOptions used to define tabular options 
    # for the damage initiation table. 
    initiationOptions: ConnectorOptions = ConnectorOptions()

    # A ConnectorOptions object specifying the ConnectorOptions used to define tabular options 
    # for the damage evolution table. 
    evolutionOptions: ConnectorOptions = ConnectorOptions()

    def __init__(self, coupling: SymbolicConstant = UNCOUPLED, criterion: SymbolicConstant = FORCE,
                 initiationTemperature: Boolean = OFF,
                 initiationPotentialOperator: SymbolicConstant = SUM,
                 initiationPotentialExponent: float = 2, initiationDependencies: int = 0,
                 evolution: Boolean = ON, evolutionType: SymbolicConstant = MOTION_TYPE,
                 softening: SymbolicConstant = LINEAR, useAffected: Boolean = OFF,
                 degradation: SymbolicConstant = MAXIMUM, evolutionTemperature: Boolean = OFF,
                 evolutionDependencies: int = 0, evolutionPotentialOperator: SymbolicConstant = SUM,
                 evolutionPotentialExponent: float = 2,
                 initiationPotentials: ConnectorPotentialArray = None,
                 evolutionPotentials: ConnectorPotentialArray = None,
                 initiationTable: tuple = (), evolutionTable: tuple = (), affectedComponents: tuple = (),
                 components: tuple = ()):
        """This method creates a connector damage behavior option for a ConnectorSection object.

        Path
        ----
            -           import connectorBehavior
            -           connectorBehavior.ConnectorDamage
            -           import odbConnectorBehavior
            -           odbConnectorBehavior.ConnectorDamage

        Parameters
        ----------
        coupling
            A SymbolicConstant specifying whether or not the behavior is coupled. Possible values 
            are UNCOUPLED and COUPLED. The default value is UNCOUPLED. 
        criterion
            A SymbolicConstant specifying the damage initiation criterion to be used. Possible 
            values are FORCE, MOTION, and PLASTIC_MOTION. The default value is FORCE. 
        initiationTemperature
            A Boolean specifying whether the initiation data depend on temperature. The default 
            value is OFF. 
        initiationPotentialOperator
            A SymbolicConstant specifying the contribution operator for the initiation potential 
            contributions. Possible values are SUM and MAXIMUM. The default value is SUM.This 
            argument is only if *coupling*=COUPLED and if *criterion*=FORCE or MOTION. 
        initiationPotentialExponent
            A Float specifying the number equal to the inverse of the overall exponent in the 
            initiation potential definition. The default value is 2.0.This argument is applicable 
            only if *coupling*=COUPLED, when *initiationPotentialOperator*=SUM, and when 
            *criterion*=FORCE or MOTION. 
        initiationDependencies
            An Int specifying the number of field variable dependencies for the initiation data. The 
            default value is 0. 
        evolution
            A Boolean specifying whether damage evolution data will be used. The default value is 
            ON. 
        evolutionType
            A SymbolicConstant specifying the type of damage evolution to be specified. Possible 
            values are MOTION_TYPE and ENERGY_TYPE. The default value is MOTION_TYPE.This argument 
            is applicable only if *evolution*=ON. 
        softening
            A SymbolicConstant specifying the damage evolution law to be specified. Possible values 
            are LINEAR, EXPONENTIAL, and TABULAR. The default value is LINEAR.This argument is 
            applicable only if *evolution*=ON and when *evolutionType*=MOTION_TYPE. 
        useAffected
            A Boolean specifying whether or not *affectedComponents* will be specified. If 
            *useAffected*=OFF, then only the components of relative motion specified by *components* 
            will undergo damage. The default value is OFF.This argument is applicable only if 
            *evolution*=ON. 
        degradation
            A SymbolicConstant specifying the contribution of each damage mechanism when more than 
            one damage mechanism is defined. Possible values are MAXIMUM and MULTIPLICATIVE. The 
            default value is MAXIMUM.This argument is applicable if *evolution*=ON. 
        evolutionTemperature
            A Boolean specifying whether the evolution data depend on temperature. The default value 
            is OFF.This argument is applicable only if *evolution*=ON. 
        evolutionDependencies
            An Int specifying the number of field variable dependencies for the evolution data. The 
            default value is 0.This argument is applicable only if *evolution*=ON. 
        evolutionPotentialOperator
            A SymbolicConstant specifying the contribution operator for the evolution potential 
            contributions. Possible values are SUM and MAXIMUM. The default value is SUM.This 
            argument is applicable only if *coupling*=COUPLED, when *evolution*=ON, when 
            *evolutionType*=MOTION_TYPE, and when *criterion*=FORCE or MOTION. 
        evolutionPotentialExponent
            A Float specifying the number equal to the inverse of the overall exponent in the 
            evolution potential definition. The default value is 2.0.This argument is applicable 
            only if *coupling*=COUPLED, when *evolution*=ON, when *evolutionPotentialOperator*=SUM, 
            when *evolutionType*=MOTION, and when *criterion*=FORCE or MOTION. 
        initiationPotentials
            A ConnectorPotentialArray object specifying one ConnectorPotential object for each 
            initiation potential contribution. This member can be specified only if 
            *coupling*=COUPLED and if *criterion*=FORCE or MOTION. 
        evolutionPotentials
            A ConnectorPotentialArray object specifying one ConnectorPotential object for each 
            evolution potential contribution). This member can be specified only if 
            *coupling*=COUPLED, if *evolution*=ON, if *evolutionType*=MOTION, and if 
            *criterion*=FORCE or MOTION. 
        initiationTable
            A sequence of sequences of Floats specifying the initiation properties. The default 
            value is an empty sequence.Items in the *initiationTable* data are described below. 
        evolutionTable
            A sequence of sequences of Floats specifying the evolution properties. The default value 
            is an empty sequence.Items in the *evolutionTable* data are described below. This 
            argument is only applicable if *evolution*=ON. 
        affectedComponents
            A sequence of Ints specifying the components of relative motion that will be damaged. 
            Possible values are 1 ≤≤ *components* ≤≤ 6. Only available components can be specified. 
            This argument is applicable only if *evolution*=ON and *useAffected*=ON. The default 
            value is an empty sequence. 
        components
            A sequence of Ints specifying the components of relative motion for which the behavior 
            is defined. Possible values are 1 ≤≤ *components* ≤≤ 6. Only available components can be 
            specified. This argument can be specified only if *coupling*=UNCOUPLED. The default 
            value is an empty sequence. 

        Returns
        -------
            A ConnectorDamage object. 

        Raises
        ------
            ValueError and TextError. 
        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the ConnectorDamage object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Raises
        ------
            ValueError. 
        """
        pass
