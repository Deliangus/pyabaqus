import typing

from abaqusConstants import *


class HistoryOutput:
    """The HistoryOutput object contains the history output at a point for the specified
    variable. 

    Attributes
    ----------
    data: float
        A tuple of pairs of Floats specifying the pairs (**frameValue**, **value**) where
        **frameValue** is either time, frequency, or mode and **value** is the value of the
        specified variable at **frameValue**. (This value depends on the type of the variable.)
    conjugateData: float
        A tuple of pairs of Floats specifying the imaginary portion of a specified complex
        variable at each frame value (time, frequency, or mode). The pairs have the form
        (**frameValue**, **value**).

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import odbAccess
        session.odbs[name].steps[name].historyRegions[name].historyOutputs[name]

    """

    # A tuple of pairs of Floats specifying the pairs (*frameValue*, *value*) where 
    # *frameValue* is either time, frequency, or mode and *value* is the value of the 
    # specified variable at *frameValue*. (This value depends on the type of the variable.) 
    data: float = None

    # A tuple of pairs of Floats specifying the imaginary portion of a specified complex 
    # variable at each frame value (time, frequency, or mode). The pairs have the form 
    # (*frameValue*, *value*). 
    conjugateData: float = None

    def __init__(self, name: str, description: str, type: SymbolicConstant,
                 validInvariants: SymbolicConstant = None):
        """This method creates a HistoryOutput object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.odbs[name].steps[name].historyRegions[name].HistoryOutput
        
        Parameters
        ----------
        name
            A String specifying the output variable name. 
        description
            A String specifying the output variable. 
        type
            A SymbolicConstant specifying the output type. Only SCALAR is currently supported. 
        validInvariants
            A sequence of SymbolicConstants specifying which invariants should be calculated for 
            this field. Possible values are MAGNITUDE, MISES, TRESCA, PRESS, INV3, MAX_PRINCIPAL, 
            MID_PRINCIPAL, and MIN_PRINCIPAL. The default value is an empty sequence. 

        Returns
        -------
            A HistoryOutput object.
        """
        pass

    @typing.overload
    def addData(self, frame: str, value: str):
        """This method adds data to the *data* member of the HistoryOutput object.
        
        Parameters
        ----------
        frame
            A Double specifying the frame value. *frame* can be specified in step time, frequency, 
            or mode number. 
        value
            A Double specifying the value of the variable at the frame value specified in *frame*. 
        """
        pass

    @typing.overload
    def addData(self, frame: tuple, value: tuple):
        """This method adds data to the *data* member of the HistoryOutput object.
        
        Parameters
        ----------
        frame
            A sequence of Floats specifying the frame values. *frame* can be specified in step time, 
            frequency, or mode number. 
        value
            A sequence of Floats specifying the value of the variable at the frame values specified 
            in *frame*.

        Raises
        ------
            If the length of *frame* is not the same as the length of *value* a ValueError is 
            raised. 
        """
        pass

    @typing.overload
    def addData(self, data: tuple):
        """This method adds data to the *data* member of the HistoryOutput object.
        
        Parameters
        ----------
        data
            A sequence of pairs of Floats specifying the pairs (*frameValue*, *value*) where 
            *frameValue* is either time, frequency, or mode and *value* is the value of the 
            specified variable at *frameValue*. (This value depends on the type of the variable.) 
        """
        pass

    def addData(self, *args, **kwargs):
        pass
