from abaqusConstants import *

class MeanFieldHomogenization:

    """The MeanFieldHomogenization object specifies the multiscale material definition. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].meanFieldHomogenization
        - import odbMaterial
        - session.odbs[name].materials[name].meanFieldHomogenization

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - MEAN FIELD HOMOGENIZATION

    """

    def __init__(self, angleSubdivision: int = None, formulation: SymbolicConstant = MT, 
                 isotropization: SymbolicConstant = ALLISO, uniformMatrixStrain: SymbolicConstant = NO):
        """This method creates a MeanFieldHomogenization object.

        Path
        ----
            - mdb.models[name].materials[name].MeanFieldHomogenization
            - session.odbs[name].materials[name].MeanFieldHomogenization

        Parameters
        ----------
        angleSubdivision
            An Int specifying the number of angle increments used for the discretization of the 
            orientation space. 
        formulation
            A SymbolicConstant specifying the type of homogenization model. Possible values are MT, 
            REUSS, VOIGT, INVERSED_MT, BALANCED, and UNSPECIFIED. The default value is MT. 
        isotropization
            A SymbolicConstant specifying the type of isotropization method. Possible values are 
            ALLISO, EISO, and PISO. The default value is ALLISO. 
        uniformMatrixStrain
            A SymbolicConstant specifying whether the average strain in the matrix is uniform across 
            all pseudo-grains. Possible values are NO and YES. The default value is NO. 

        Returns
        -------
            A MeanFieldHomogenization object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the MeanFieldHomogenization object.

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
