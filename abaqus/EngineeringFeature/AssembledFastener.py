from ..Region.Region import Region
from .Fastener import Fastener
from abaqusConstants import *

class AssembledFastener(Fastener):

    """The AssembledFastener object defines an assembled fastener. 
    The AssembledFastener object is derived from the Fastener object. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].engineeringFeatures.fasteners[name]
        - import assembly
        - mdb.models[name].rootAssembly.engineeringFeatures.fasteners[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A Boolean specifying whether the fastener is suppressed or not. The default value is 
    # OFF. 
    suppressed: Boolean = OFF

    def __init__(self, name: str, region: Region, templateModel: str, controlSet: Region, 
                 templateSurfaces: tuple, assignedSurfaces: tuple, propertyPrefix: str, 
                 orientMethod: SymbolicConstant = NORMALS, localCsys: int = None, scriptName: str = ''):
        """This method creates an AssembledFastener object. Although the constructor is available
        both for parts and for the assembly, AssembledFastener objects are currently supported
        only under the assembly.

        Path
        ----
            - mdb.models[name].parts[name].engineeringFeatures.AssembledFastener
            - mdb.models[name].rootAssembly.engineeringFeatures.AssembledFastener

        Parameters
        ----------
        name
            A String specifying the repository key. 
        region
            A Region object specifying the region of attachment points to which assembled fasteners 
            are applied. 
        templateModel
            A String specifying the name of the template model. 
        controlSet
            A Region object specifying the template model control point set. The set must contain a 
            single node or vertex. 
        templateSurfaces
            A sequence of Strings specifying the names of the template model surfaces that are 
            referenced by tie or coupling constraints. 
        assignedSurfaces
            A sequence of Strings specifying the names of the main model surfaces that will be 
            substituted for the template model constraint surfaces. 
        propertyPrefix
            A String specifying the name of the property prefix string. This string will be 
            prepended to every property name as it is copied to the main model from the template 
            model. 
        orientMethod
            A SymbolicConstant specifying the method used to orient the virtual instances of the 
            template model at each attachment point. Possible values are NORMALS and CSYS. The 
            default value is NORMALS. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system. If *localCsys*=None, 
            the global coordinate system is used. When this member is queried, it returns an Int. 
            The default value is None.This argument applies only when *orientMethod*=CSYS. 
        scriptName
            A String specifying the name of the property generation script. The default value is an 
            empty string. 

        Returns
        -------
            An AssembledFastener object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def setValues(self, orientMethod: SymbolicConstant = NORMALS, localCsys: int = None, scriptName: str = ''):
        """This method modifies the AssembledFastener object.

        Parameters
        ----------
        orientMethod
            A SymbolicConstant specifying the method used to orient the virtual instances of the 
            template model at each attachment point. Possible values are NORMALS and CSYS. The 
            default value is NORMALS. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system. If *localCsys*=None, 
            the global coordinate system is used. When this member is queried, it returns an Int. 
            The default value is None.This argument applies only when *orientMethod*=CSYS. 
        scriptName
            A String specifying the name of the property generation script. The default value is an 
            empty string. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
