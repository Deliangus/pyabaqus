# Image object

The Image object is used to store color values and attributes associated with a raster file. Upon creation, the Image object is added to the session.images repository.

## Access

```
session.images[name]
```

## Image(...)



This method creates an Image object from the contents of the specified file.



### Path

```
session.Image
```

### Required arguments

- *name*

  A String specifying the repository name for the image.

- *fileName*

  A String specifying the file from which the image is to be read. The file extension must be specified and indicate the image format (.bmp, .gif, .jpg, .jpeg, .ico, .pcx, .png, .rgb, .tga, .tif, or .xpm).

### Optional arguments

None.

### Return value

An Image object.

### Exceptions

ValueError.

- If *fileName* does not exist or can not be read:

  ValueError: Unable to open image file

- If *fileName* references an unsupported image file format:

  ValueError: Unsupported image format

- If the contents of *fileName* are corrupt or can not be decoded:

  ValueError: Unable to decode image file



## ImageFromMovie(...)



This method creates an Image object from a given frame of an existing [Movie](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-moviepyc.htm?ContextScope=all) object.



### Required arguments

- *name*

  A String specifying the repository name for the image.

- *movieName*

  A String specifying the name of the movie from which the image is to be extracted. The movie must exist in the session.movies repository.

- *frame*

  An Int specifying the movie frame number defining the image to be extracted.

- *time*

  A Float specifying the time of the movie defining the image to be extracted.

### Optional arguments

None.

### Return value

An Image object.

### Exceptions

ValueError.

TypeError.

- If *movieName* does not exist:

  ValueError: There is no movie object with this name: 'movieName'

- If *frame* references an non existing frame:

  ValueError: Could not load frame n from movie: 'movieName'

- If *time* references an non existing frame:

  ValueError: Could not load frame at time 't' from movie: 'movieName'

- If *time* and *frame* are given in the same command:

  TypeError: keyword error on time



## Members

The Image object has members with the same names and descriptions as the arguments to the [Image ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-imagepyc.htm?ContextScope=all#simaker-imageimagepyc)method.