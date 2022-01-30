from abaqusConstants import *
from abaqus.Material.Elastic.HyperElastic.ViscoElastic.CombinedTestData import CombinedTestData
from abaqus.Material.TestData.ShearTestData import ShearTestData
from abaqus.Material.Others.Mechanical.Viscosity.Trs import Trs
from abaqus.Material.TestData.VolumetricTestData import VolumetricTestData


class Viscoelastic:
    """The Viscoelastic object specifies dissipative behavior for use with elasticity.

    Notes
    -----
        This object can be accessed by:
        - import material
        - mdb.models[name].materials[name].viscoelastic
        - import odbMaterial
        - session.odbs[name].materials[name].viscoelastic

    Table Data
    ----------
        If *frequency*=FORMULA, the table data for *table* specify the following:
        - Real part of g∗1 (g∗(ω)=g∗1f−a).
        - Imaginary part of g∗1.
        - Value of a.
        - Real part of k∗1 (k∗(ω)=k∗1f−b). If the material is incompressible, this value is ignored.
        - Imaginary part of k1*. If the material is incompressible, this value is ignored.
        - Value of b. If the material is incompressible, this value is ignored.
        If *frequency*=TABULAR and *type*=ISOTROPIC and *preload*=NONE, or *time*=FREQUENCY_DATA the table data for *table* specify the following:
        - Real part of ω⁢g* (ωR(g∗)=Gℓ/G∞).
        - Imaginary part of ω⁢g* (ωI(g*)=1−Gs/G∞).
        - Real part of ω⁢k* (ωR(k∗)=Kℓ/K∞). If the material is incompressible, this value is ignored.
        - Imaginary part of ω⁢k* (ωI(k∗)=1−Ks/K∞). If the material is incompressible, this value is ignored.
        - Frequency f in cycles per time.
        If *frequency*=TABULAR and *type*=ISOTROPIC and *preload*=UNIAXIAL the table data for *table* specify the following:
        - Loss modulus.
        - Storage modulus.
        - Frequency.
        - Uniaxial strain.
        If *frequency*=TABULAR and *type*=TRACTION and *preload*=NONE the table data for *table* specify the following:
        - Normalized loss modulus.
        - Normalized shear modulus.
        - Frequency.
        If *frequency*=TABULAR and *type*=TRACTION and *preload*=UNIAXIAL or *preload*=UNIAXIAL_VOLUMETRIC the table data for *table* specify the following:
        - Loss modulus.
        - Storage modulus.
        - Frequency.
        - Closure.
        If *time*=PRONY or *frequency*=PRONY, the table data for *table* specify the following:
        - g¯1P, the modulus ratio in the first term in the Prony series expansion of the shear relaxation modulus.
        - k¯1P, the modulus ratio in the first term in the Prony series expansion of the bulk relaxation modulus.
        - τ1, the relaxation time for the first term in the Prony series expansion.
        If *frequency*=TABULAR and *type*=ISOTROPIC and *preload*=VOLUMETRIC or *preload*=UNIAXIAL_VOLUMETRIC the table data for *volumetricTable* specify the following:
        - Loss modulus.
        - Storage modulus.
        - Frequency.
        - Volume ratio.

    Corresponding analysis keywords
    -------------------------------
        - VISCOELASTIC

    """

    # A CombinedTestData object. 
    combinedTestData: CombinedTestData = CombinedTestData(((),))

    # A ShearTestData object. 
    shearTestData: ShearTestData = ShearTestData(((),))

    # A Trs object. 
    trs: Trs = Trs()

    # A VolumetricTestData object. 
    volumetricTestData: VolumetricTestData = VolumetricTestData(((),))

    def __init__(self, domain: SymbolicConstant, table: tuple, frequency: SymbolicConstant = FORMULA,
                 type: SymbolicConstant = ISOTROPIC, preload: SymbolicConstant = NONE,
                 time: SymbolicConstant = PRONY, errtol: float = 0, nmax: int = 13,
                 volumetricTable: tuple = ()):
        """This method creates a Viscoelastic object.

        Notes
        -----
            This function can be accessed by:
            - mdb.models[name].materials[name].Viscoelastic
            - session.odbs[name].materials[name].Viscoelastic

        Parameters
        ----------
        domain
            A SymbolicConstant specifying the domain definition. Possible values are:
            - FREQUENCY, specifying a frequency domain. This domain is only available for an Abaqus/Standard analysis.
            - TIME, specifying a time domain.
        table
            A sequence of sequences of Floats specifying the items described below. 
        frequency
            A SymbolicConstant specifying the frequency domain definition. This argument is required 
            only when *domain*=FREQUENCY. Possible values are FORMULA, TABULAR, PRONY, 
            CREEP_TEST_DATA, and RELAXATION_TEST_DATA. The default value is FORMULA. 
        type
            A SymbolicConstant specifying the type. This argument is required only when 
            *domain*=FREQUENCY and *frequency*=TABULAR. Possible values are ISOTROPIC and TRACTION. 
            The default value is ISOTROPIC. 
        preload
            A SymbolicConstant specifying the preload. This argument is required only when 
            *domain*=FREQUENCY and *frequency*=TABULAR. Possible values are NONE, UNIAXIAL, 
            VOLUMETRIC, and UNIAXIAL_VOLUMETRIC. The default value is NONE. 
        time
            A SymbolicConstant specifying the time domain definition. This argument is required only 
            when *domain*=TIME. Possible values are PRONY, CREEP_TEST_DATA, RELAXATION_TEST_DATA, 
            and FREQUENCY_DATA. The default value is PRONY. 
        errtol
            A Float specifying the allowable average root-mean-square error of the data points in 
            the least-squares fit. The Float values correspond to percentages; for example, 0.01 is 
            1%. The default value is 0.01.This argument is valid only when *time*=CREEP_TEST_DATA, 
            RELAXATION_TEST_DATA or FREQUENCY_DATA; or only when *frequency*=CREEP_TEST_DATA or 
            RELAXATION_TEST_DATA. 
        nmax
            An Int specifying the maximum number of terms NN in the Prony series. The maximum value 
            is 13. The default value is 13.This argument is valid only when *time*=CREEP_TEST_DATA, 
            RELAXATION_TEST_DATA or FREQUENCY_DATA; or only when *frequency*=CREEP_TEST_DATA or 
            RELAXATION_TEST_DATA. 
        volumetricTable
            A sequence of sequences of Floats specifying the items described below. The default 
            value is an empty sequence. 

        Returns
        -------
            A Viscoelastic object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the Viscoelastic object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Raises
        ------
            RangeError. 
        """
        pass
