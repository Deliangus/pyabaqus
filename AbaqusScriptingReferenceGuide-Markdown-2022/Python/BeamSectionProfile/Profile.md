# Profile object

The Profile object defines the geometrical properties of a beam cross-section. Profile is an abstract base type.

## Access

```
import section
mdb.models[name].profiles[name]
import odbSection
session.odbs[name].profiles[name]
```

## beamProfilesFromOdb(...)



This method creates Profile objects by reading an output database. The new profiles are placed in the profiles repository.



### Path

mdb.models[*name*].beamProfilesFromOdb

### Required arguments

- *fileName*

  A String specifying the name of the output database file (including the .odb extension) to be read. The String can also be the full path to the output database file if it is located in another directory.

### Optional arguments

None.

### Return value

A list of Profile objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The Profile object has the following member:

- *name*

  A String specifying the repository key.