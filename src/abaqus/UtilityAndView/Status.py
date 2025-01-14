import typing

"""These functions display status information. 

"""


@typing.overload
def milestone(message: str):
    """This function displays a string in the prompt area.

    Notes
    -----
        This function can be accessed by:
        
        .. code-block:: python
        
            milestone

    Parameters
    ----------
    message
        A String specifying the text to display. 

    """
    pass


@typing.overload
def milestone(message: str, percent: int):
    """This function displays a percentage complete message in the prompt area.

    Notes
    -----
        This function can be accessed by:
        
        .. code-block:: python
        
            milestone

    Parameters
    ----------
    message
        A String specifying the text to display. 
    percent
        An Int specifying the percentage complete. 

    """
    pass


@typing.overload
def milestone(message: str, object: str, done: int, total: int):
    """This function displays a message in the prompt area indicating the number done out of a
    total. The form of the message is `operation: object nn out of nn`

    Notes
    -----
        This function can be accessed by:
        
        .. code-block:: python
        
            milestone

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

    """
    pass


def milestone(*args, **kwargs):
    pass
