from __init__ import *


class HeatGeneration:
    """The HeatGeneration object includes volumetric heat generation in heat transfer analyses.

    Notes
    -----
        This object can be accessed by:
        
        .. code-block:: python
            
            import material
            mdb.models[name].materials[name].heatGeneration
            import odbMaterial
            session.odbs[name].materials[name].heatGeneration

    The corresponding analysis keywords are:
        - HEAT GENERATION

    """
    def __init__(self):
        """This method creates a HeatGeneration object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].materials[name].HeatGeneration
                session.odbs[name].materials[name].HeatGeneration

        Returns
        -------
            A HeatGeneration object.
        """
        pass
