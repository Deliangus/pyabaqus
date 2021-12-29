from abaqus.Sketcher.ConstrainedSketchBase import ConstrainedSketchBase


class ConstrainedSketchParameterModel(ConstrainedSketchBase):

    def Parameter(self, name: str, path: str = '', expression: str = '', previousParameter: str = ''):
        """This method creates a parameter and optionally associates a dimension with this
        parameter.

        Path
        ----
            - mdb.models[name].sketches[name].ConstrainedSketchParameter

        Parameters
        ----------
        name
            A String specifying the name of the ConstrainedSketchParameter object. No two parameters
            in the same ConstrainedSketch can have the same name.
        path
            A String specifying the ConstrainedSketchDimension object with which this parameter is
            associated.
        expression
            A String specifying the expression or value associated with the
            ConstrainedSketchParameter.
        previousParameter
            A String specifying the name of the previous ConstrainedSketchParameter, if it exists.
            The *previousParameter* argument implies an order among the parameters. No two
            parameters can reference the same parameter as the previous parameter.

        Returns
        -------
            A ConstrainedSketchParameter object.

        Exceptions
        ----------
            None.
            !img
        """
        pass
