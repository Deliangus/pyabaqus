from .CommandRegister import CommandRegister


class RegisteredList(CommandRegister):
    """This class allows you to create a list that can be queried from the GUI and is capable
    of notifying the GUI when the contents of the list change. 
    The RegisteredList object is derived from the CommandRegister object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import customKernel

    """

    def __init__(self):
        """This method creates a RegisteredList object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            customKernel.RegisteredList

        Returns
        -------
            A RegisteredList object.
        """
        super().__init__()
        pass

    def Methods(self):
        """The RegisteredList object supports the same methods as a standard Python list object.
        """
        pass
