from .AnalyticalField import AnalyticalField


class ExpressionField(AnalyticalField):
    """The ExpressionField object defines a spatially varying field whose value is calculated
    from a user-supplied mathematical expression. 
    The ExpressionField object is derived from the AnalyticalField object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import fields
        mdb.models[name].analyticalFields[name]

    """

    def __init__(self, name: str, expression: str, localCsys: str = None, description: str = ''):
        """This method creates an ExpressionField object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].ExpressionField
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        expression
            A String specifying the Python expression to evaluate in space. Variables are X, Y, and 
            Z; R, Th, and Z; or R, Th, and P based on the selected coordinate system. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the field. If 
            *localCsys*=None, the field is defined in the global coordinate system. The default 
            value is None. 
        description
            A String specifying the description of the field. The default value is an empty string. 

        Returns
        -------
            An ExpressionField object. 

        Raises
        ------
            TextException. 
        """
        super().__init__()
        pass

    def setValues(self, localCsys: str = None, description: str = ''):
        """This method modifies the ExpressionField object.
        
        Parameters
        ----------
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the field. If 
            *localCsys*=None, the field is defined in the global coordinate system. The default 
            value is None. 
        description
            A String specifying the description of the field. The default value is an empty string. 
        """
        pass
