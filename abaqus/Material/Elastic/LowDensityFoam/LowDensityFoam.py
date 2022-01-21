from abaqusConstants import *
from abaqus.Material.TestData.UniaxialTestData import UniaxialTestData


class LowDensityFoam:
    """The LowDensityFoam object specifies properties for low-density foam.

    Access
    ------
        - import material
        - mdb.models[name].materials[name].lowDensityFoam
        - import odbMaterial
        - session.odbs[name].materials[name].lowDensityFoam

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - LOW DENSITY FOAM

    """

    # A UniaxialTestData object. 
    uniaxialTensionTestData: UniaxialTestData = UniaxialTestData(((),))

    # A UniaxialTestData object. 
    uniaxialCompressionTestData: UniaxialTestData = UniaxialTestData(((),))

    def __init__(self, elementRemoval: Boolean = OFF, maxAllowablePrincipalStress: float = None,
                 extrapolateStressStrainCurve: Boolean = OFF,
                 strainRateType: SymbolicConstant = VOLUMETRIC, mu0: float = None, mu1: float = 0,
                 alpha: float = 2):
        """This method creates a LowDensityFoam object.

        Path
        ----
            - mdb.models[name].materials[name].LowDensityFoam
            - session.odbs[name].materials[name].LowDensityFoam

        Parameters
        ----------
        elementRemoval
            A Boolean specifying whether elements are removed if exceeding maximum principal tensile 
            stress. This argument is valid only when *maxAllowablePrincipalStress* is defined. The 
            default value is OFF. 
        maxAllowablePrincipalStress
            None or a Float specifying the maximum allowable principal tensile stress. The default 
            value is None. 
        extrapolateStressStrainCurve
            A Boolean specifying whether the stress-strain curve is extrapolated if exceeding 
            maximum strain rate. The default value is OFF. 
        strainRateType
            A SymbolicConstant specifying strain rate measure used for constitutive calculations. 
            Possible values are PRINCIPAL and VOLUMETRIC. The default value is VOLUMETRIC. 
        mu0
            A Float specifying the relaxation coefficient μ0. The default value is 10–4. 
        mu1
            A Float specifying the relaxation coefficient μ1. The default value is 0.5×10–2. 
        alpha
            A Float specifying the relaxation coefficient α. The default value is 2.0. 

        Returns
        -------
            A LowDensityFoam object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the LowDensityFoam object.

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