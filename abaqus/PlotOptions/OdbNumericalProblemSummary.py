from abaqusConstants import *

class OdbNumericalProblemSummary:

    """The OdbNumericalProblemSummary object stores the numerical problem summary of a job. 

    Access
    ------
        - import visualization
        - session.odbData[name].diagnosticData.numericalProblemSummary

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A boolean specifying whether negative eigenvalues converged during the analysis. This 
    # attribute is read-only. 
    convergedNegativeEigenValues: Boolean = OFF

    # A boolean specifying whether numerical singularities converged during the analysis. This 
    # attribute is read-only. 
    convergedNumericalSingularities: Boolean = OFF

    # A boolean specifying whether pivot points converged during the analysis. This attribute 
    # is read-only. 
    convergedZeroPivots: Boolean = OFF

    # An int specifying the number of zero pivots. This attribute is read-only. 
    numberOfZeroPivots: str = ''

    # An int specifying the number of numerical singularities. This attribute is read-only. 
    numberOfNumericalSingularities: str = ''

    # An int specifying the number of negative eigenvalues. This attribute is read-only. 
    numberOfNegativeEigenValues: str = ''
