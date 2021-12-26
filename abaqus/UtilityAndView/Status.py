import typing

"""These functions display status information. 

Access
------

Table Data
----------

Corresponding analysis keywords
-------------------------------

"""

@typing.overload
def mileston(message: str):
    """This function displays a string in the prompt area.

    Path
    ----
        - milestone

    Parameters
    ----------
    message
        A String specifying the text to display. 

    Returns
    -------
        None. 

    Exceptions
    ----------
        None. 
    """
    pass

@typing.overload
def mileston(message: str, percent: int):
    """This function displays a percentage complete message in the prompt area.

    Path
    ----
        - milestone

    Parameters
    ----------
    message
        A String specifying the text to display. 
    percent
        An Int specifying the percentage complete. 

    Returns
    -------
        None. 

    Exceptions
    ----------
        None. 
    """
    pass

@typing.overload
def mileston(message: str, object: str, done: int, total: int):
    """This function displays a message in the prompt area indicating the number done out of a
    total. The form of the message is `operation: object nn out of nn`

    Path
    ----
        - milestone

    Parameters
    ----------
    message
        A String specifying the operation. 
    object
        A String specifying the object. 
    done
        An Int specifying the number being processed. 
    total
        An Int specifying the total number. 

    Returns
    -------
        None. 

    Exceptions
    ----------
        None. 
    """
    pass

def mileston(*args, **kwargs):
    pass
