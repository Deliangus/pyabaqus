# SteadyStateDirectFrequency object

A SteadyStateDirectFrequency is an object used to define frequency over range of modes.

## Access

```
import step
mdb.models[name].steps[name].frequencyRange[i]
```

## Members

The SteadyStateDirectFrequency object has the following members:

- *lower*

  A Float specifying the lower limit of frequency range or a single frequency, in cycles/time.

- *upper*

  A Float specifying the upper limit of frequency range, in cycles/time.

- *nPoints*

  An Int specifying the number of points in the frequency range at which results should be given.

- *bias*

  A Float specifying the Bias parameter. When results are requested at four or more frequency points, Abaqus biases the results toward the ends of the intervals to obtain better resolution. The default value is 3.0.