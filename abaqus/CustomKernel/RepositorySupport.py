from .CommandRegister import CommandRegister


class RepositorySupport(CommandRegister):
    """The RepositorySupport is a base class from which you can derive your own classes that
    are designed to contain custom repositories. Instances of this class can be queried from 
    the GUI and are capable of notifying the GUI when the contents of the instance change. 
    The RepositorySupport object is derived from the CommandRegister object. 

    Access
    ------
        - import customKernel
        - mdb.customData
        - session.customData
        - session.odbs[name].customData

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def __init__(self):
        """This method creates a RepositorySupport object.

        Path
        ----
            - customKernel.RepositorySupport

        Parameters
        ----------

        Returns
        -------
            A RepositorySupport object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def Repository(self, name: str, constructors: str):
        """This method installs a repository on the class. The repository is an instance of a
        RegisteredDictionary class. Refer to RegisteredDictionary for details on its methods.
        The objects stored in the repository are assumed to have an attribute called *name* that
        stores the key used to access the object in the repository. The name attribute will be
        modified by the changeKey method.

        Parameters
        ----------
        name
            A String specifying the name of the repository. 
        constructors
            A constructor or sequence of constructors specifying which classes will store their 
            instances in the repository. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
