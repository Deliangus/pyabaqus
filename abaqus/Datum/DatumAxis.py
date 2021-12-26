from .Datum import Datum

class DatumAxis(Datum):

    """The DatumAxis object has no direct constructor; it is created when a Feature object is 
    created. For example, the DatumAxisByCylFace method creates a Feature object that 
    creates a DatumAxis object. 
    The DatumAxis object is derived from the Datum object. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].datums[i]
        - import assembly
        - mdb.models[name].rootAssembly.allInstances[name].datums[i]
        - mdb.models[name].rootAssembly.datums[i]
        - mdb.models[name].rootAssembly.instances[name].datums[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A tuple of Floats specifying the *X*-, *Y*-, and *Z*-coordinates of a point located on 
    # the datum. 
    pointOn: float = None

    # A tuple of Floats specifying a sequence of three Floats specifying the direction of the 
    # axis. 
    direction: tuple = ()
