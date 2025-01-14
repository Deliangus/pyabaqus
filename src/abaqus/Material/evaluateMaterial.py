from abaqusConstants import *
from .Material import Material

""" This command evaluates the behavior of a hyperelastic material under standard test 
conditions. 

Notes
-----
    - from material import evaluateMaterial

"""


def evaluateMaterial(material: Material, simulationName: str, dataSource: SymbolicConstant = None,
                     strainEnergyPotentials: SymbolicConstant = None, marlowData: SymbolicConstant = None,
                     marlowDataType: SymbolicConstant = None, testDataTypes: SymbolicConstant = None,
                     uniaxialStrainRange: float = None, biaxialStrainRange: float = None,
                     planarStrainRange: float = None, volumeRatioRange: float = None,
                     simpleShearStrainRange: float = None, viscoDataSource: SymbolicConstant = None,
                     viscoTestDataTypes: SymbolicConstant = None, relaxationTime: float = None,
                     creepTime: float = None):
    """This method evaluates the behavior of a hyperelastic material under standard test
    conditions.

    Notes
    -----
        This function can be accessed by:
        
        .. code-block:: python
        
            evaluateMaterial

    Parameters
    ----------
    material
        A Material object. 
    simulationName
        A String specifying the name to be used for the material evaluation simulation. 
    dataSource
        A SymbolicConstant specifying whether test data or coefficients should be used for the 
        material definition in the unit element tests. Possible values are TEST_DATA or 
        COEFFICIENTS. 
    strainEnergyPotentials
        A sequence of SymbolicConstants specifying for which material models the material is to 
        be evaluated. Possible values are POLY_N1, POLY_N2, POLY_N3, POLY_N4, POLY_N5, POLY_N6, 
        OGDEN_N1, OGDEN_N2, OGDEN_N3, OGDEN_N4, OGDEN_N5, OGDEN_N6, REDUCED_POLY_N1, 
        REDUCED_POLY_N2, REDUCED_POLY_N3, REDUCED_POLY_N4, REDUCED_POLY_N5, REDUCED_POLY_N6, 
        ARRUDA_BOYCE, VAN_DER_WAALS, YEOH, MOONEY_RIVLIN, and NEO_HOOKE.Note:The options 
        POLY_N3, POLY_N4, POLY_N5, and POLY_N6 are valid only if the material was defined by 
        providing coefficients of the strain energy potential. 
    marlowData
        None or a sequence of SymbolicConstants specifying the types of test data to be included 
        in the material definition of the Marlow material that is being evaluated. Possible 
        values are UNIAXIAL, BIAXIAL, PLANAR, or VOLUMETRIC. The default value is None. 
    marlowDataType
        None or a SymbolicConstant specifying the input data type for the Marlow material model. 
        Possible values are TENSION, COMPRESSION, or BOTH. 
    testDataTypes
        A sequence of SymbolicConstants specifying the types of test data to be included in the 
        material definition of the material being evaluated. Possible values are UNIAXIAL, 
        BIAXIAL, PLANAR, and VOLUMETRIC. 
    uniaxialStrainRange
        A tuple of Floats specifying minimum and maximum nominal strains to be applied in the 
        uniaxial tension test. 
    biaxialStrainRange
        A tuple of Floats specifying the minimum and maximum nominal strains to be applied in 
        the biaxial tension test. 
    planarStrainRange
        A tuple of Floats specifying the minimum and maximum nominal strains to be applied in 
        the planar test. The planar test is equivalent to a pure shear test. 
    volumeRatioRange
        A tuple of Floats specifying the minimum and maximum compressive volume ratio. 
    simpleShearStrainRange
        A tuple of Floats specifying the minimum and maximum nominal strains to be applied in 
        the simple shear test. 
    viscoDataSource
        None or a SymbolicConstant specifying whether test data or coefficients should be used 
        for the viscoelastic material definition in the element tests. Possible values are 
        TEST_DATA or COEFFICIENTS. The default value is None. 
    viscoTestDataTypes
        None or a sequence of SymbolicConstants specifying the types of test data to be included 
        in the material definition of the viscoelastic material being evaluated. Possible values 
        are UNIAXIAL, BIAXIAL, PLANAR, or VOLUMETRIC. The default value is None. 
    relaxationTime
        None or a Float specifying the time period for the stress relaxation response mode. The 
        default value is None. 
    creepTime
        None or a Float specifying the time period for the creep response mode. The default 
        value is None. 

    Raises
    ------
        - If *dataSource*=TEST_DATA and *strainEnergyPotentials* contains POLY_N3, POLY_N4, 
        POLY_N5, or POLY_N6: 
          MaterialEvaluationError: POLY_N3, POLY_N4, POLY_N5, or POLY_N6not allowed for 
        *dataSource*=TEST_DATA. 
        - If the material evaluation failed: 
          MaterialEvaluationError: material evaluation failed, see*path to data file*. 
        - If the material type of the material to be evaluated is not hyperelastic: 
          MaterialEvaluationError: Material evaluation is currentlysupported only for 
        hyperelastic materials. 
    """
    pass
