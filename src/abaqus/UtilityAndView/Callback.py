"""These functions execute Python commands or functions.

"""


def addImportCallback(moduleName: str, callback: str, userData: str = ''):
    """This function defines a function to be called when a specified Abaqus/CAE module is
    imported. You cannot specify a custom module.
    For more information, see An example of a callback function.

    Notes
    -----
        This function can be accessed by:
        
        .. code-block:: python
        
            addImportCallback

    Parameters
    ----------
    moduleName
        A String specifying the name of a specified Abaqus/CAE module. 
    callback
        A Python function to be called. The interface definition of the callback function is 
        :`def functionName(moduleName, userData)`*moduleName* is a String.*userData* is the 
        object passed as the *userData* argument to the addImportCallback method. 
    userData
        Any Python object or None. This object is passed to the callback function. 

    """
    pass


def removeImportCallback(callback: str, userData: str):
    """This function removes a callback added in addImportCallback.

    Notes
    -----
        This function can be accessed by:
        
        .. code-block:: python
        
            removeImportCallback

    Parameters
    ----------
    callback
        A Python function to be called; it must be the same as the *callback* argument specified 
        in the original call to addImportCallback. 
    userData
        Any Python object or None; it must be the same as the *userData* argument specified in 
        the original call to addImportCallback. 

    """
    pass
