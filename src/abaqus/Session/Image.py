class Image:
    """The Image object is used to store color values and attributes associated with a raster
    file. Upon creation, the Image object is added to the session.images repository. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        session.images[name]

    """

    def __init__(self, name: str, fileName: str):
        """This method creates an Image object from the contents of the specified file.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.Image
        
        Parameters
        ----------
        name
            A String specifying the repository name for the image. 
        fileName
            A String specifying the file from which the image is to be read. The file extension must 
            be specified and indicate the image format (.bmp, .gif, .jpg, .jpeg, .ico, .pcx, .png, 
            .rgb, .tga, .tif, or .xpm). 

        Returns
        -------
            An Image object. 

        Raises
        ------
            ValueError. 
            - If *fileName* does not exist or can not be read: 
              ValueError: Unable to open image file 
            - If *fileName* references an unsupported image file format: 
              ValueError: Unsupported image format 
            - If the contents of *fileName* are corrupt or can not be decoded: 
              ValueError: Unable to decode image file 
        """
        pass

    def ImageFromMovie(self, name: str, movieName: str, frame: int, time: float):
        """This method creates an Image object from a given frame of an existing Movie object.
        
        Parameters
        ----------
        name
            A String specifying the repository name for the image. 
        movieName
            A String specifying the name of the movie from which the image is to be extracted. The 
            movie must exist in the session.movies repository. 
        frame
            An Int specifying the movie frame number defining the image to be extracted. 
        time
            A Float specifying the time of the movie defining the image to be extracted. 

        Returns
        -------
            An Image object. 

        Raises
        ------
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
        """
        pass
