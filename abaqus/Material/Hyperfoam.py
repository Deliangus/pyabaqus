from abaqusConstants import *
from .BiaxialTestData import BiaxialTestData
from .PlanarTestData import PlanarTestData
from .SimpleShearTestData import SimpleShearTestData
from .UniaxialTestData import UniaxialTestData
from .VolumetricTestData import VolumetricTestData


class Hyperfoam:

    """The Hyperfoam object specifies elastic properties for a hyperelastic foam. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].hyperfoam
        - import odbMaterial
        - session.odbs[name].materials[name].hyperfoam

    Table Data
    ----------
        The items in the table data specify the following for values of nn:
        - μi and αi for i from 1 to n.
        - νi.
        - Temperature, if the data depend on temperature. Temperature dependence is not allowed for 4 ≤n≤ 6 in an Abaqus/Explicit analysis.

    Corresponding analysis keywords
    -------------------------------
        - HYPERFOAM

    """

    # A BiaxialTestData object. 
    biaxialTestData: BiaxialTestData = None

    # A VolumetricTestData object. 
    volumetricTestData: VolumetricTestData = None

    # A PlanarTestData object. 
    planarTestData: PlanarTestData = None

    # A SimpleShearTestData object. 
    simpleShearTestData: SimpleShearTestData = None

    # A UniaxialTestData object. 
    uniaxialTestData: UniaxialTestData = None

    def __init__(self, testData: Boolean = OFF, poisson: float = None, n: int = 1, 
                 temperatureDependency: Boolean = OFF, moduli: SymbolicConstant = LONG_TERM, 
                 table: tuple = ()):
        """This method creates a Hyperfoam object.

        Path
        ----
            - mdb.models[name].materials[name].Hyperfoam
            - session.odbs[name].materials[name].Hyperfoam

        Parameters
        ----------
        testData
            A Boolean specifying whether test data are supplied. The default value is OFF. 
        poisson
            None or a Float specifying the effective Poisson's ratio, νν, of the material. This 
            argument is valid only when *testData*=ON. The default value is None. 
        n
            An Int specifying the order of the strain energy potential. Possible values are 1 ≤n≤≤n≤ 
            6. The default value is 1. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        moduli
            A SymbolicConstant specifying the time-dependence of the material constants. Possible 
            values are INSTANTANEOUS and LONG_TERM. The default value is LONG_TERM. 
        table
            A sequence of sequences of Floats specifying the items described below. This argument is 
            valid only when *testData*=OFF. The default value is an empty sequence. 

        Returns
        -------
            A Hyperfoam object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the Hyperfoam object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
        """
        pass
