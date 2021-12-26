# SubstructureGenerateModes object

A SubstructureGenerateModes object is used to define the modes to be used in a modal dynamic analysis.

## Access

```
import step
mdb.models[name].steps[name].modeRange[i]
```

## Members

The SubstructureGenerateModes object has the following members:

- *start*

  An Int specifying the mode number of the lowest mode of a range.

- *end*

  An Int specifying the mode number of the highest mode of a range.

- *increment*

  An Int specifying the increment used to define the intermediate mode numbers beginning from the lowest mode to the highest mode.