from abaqusConstants import *


class NumberFormat:
    """The NumberFormat object is a formatting template used to define formatting options for
    certain numeric output.This page 
    discusses:Access[NumberFormat(...)](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-numberformatpyc.htm?ContextScope=all#simaker-numberformatnumberformatpyc)Members 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import visualization
        session.defaultFieldReportOptions.numberFormat
        session.fieldReportOptions.numberFormat
        session.journalOptions.defaultFormat
        session.journalOptions.fieldReportFormat
        session.journalOptions.geometryFormat

    """

    def __init__(self, blankPad: Boolean = ON, format: SymbolicConstant = ENGINEERING, numDigits: int = 6,
                 precision: int = 0):
        """This method creates a NumberFormat object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            session.defaultFieldReportOptions.NumberFormat
            session.fieldReportOptions.NumberFormat
            session.journalOptions.NumberFormat
        
        Parameters
        ----------
        blankPad
            A Boolean specifying whether the printed digits should be padded with blank characters 
            to ensure equal sized fields. The *blankPad* argument is useful when your printed output 
            includes columns. The default value is ON. 
        format
            A SymbolicConstant specifying the formatting type. Possible values are ENGINEERING, 
            SCIENTIFIC, and AUTOMATIC. The default value is ENGINEERING. 
        numDigits
            An Int specifying the number of digits to be displayed in the result. *numDigits* >0>0. 
            The default value is 6. 
        precision
            An Int specifying the number of decimal places to which the number is to be truncated 
            for display. *precision* ≤0≤0. If *precision* =0, no truncation is applied. The default 
            value is 0. 

        Returns
        -------
            A NumberFormat object.
        """
        pass
