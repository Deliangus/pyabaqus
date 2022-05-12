from __init__ import *
from __future__ import annotations


class Datum:
    """The Datum object is the abstract base type for other Datum objects. The Datum object has
    no explicit constructor. The methods and members of the Datum object are common to all 
    objects derived from the Datum. 

    Notes
    -----
        This object can be accessed by:
        
        .. code-block:: python
            
            import part
            mdb.models[name].parts[name].datums[i]
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].datums[i]
            mdb.models[name].rootAssembly.datums[i]
            mdb.models[name].rootAssembly.instances[name].datums[i]
            mdb.models[name].rootAssembly.modelInstances[i].datums[i]

    """
    pass