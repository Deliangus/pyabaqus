from .CommandRegister import CommandRegister


class RegisteredTuple(CommandRegister):
    """This class allows you to create a tuple that can be queried from the GUI and is capable
    of notifying the GUI when the contents of any of the tuple's members change. 
    The RegisteredTuple object is derived from the CommandRegister object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import customKernel

    """

    def __init__(self, tuple: tuple):
        """This method creates a RegisteredTuple object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            customKernel.RegisteredTuple
        
        Parameters
        ----------
        tuple
            A tuple of objects. These objects must be derived from the CommandRegister class. 

        Returns
        -------
            A RegisteredTuple object.
        """
        super().__init__()
        pass

    def Methods(self):
        """The RegisteredTuple object supports the same methods as a standard Python list object.
        """
        pass
