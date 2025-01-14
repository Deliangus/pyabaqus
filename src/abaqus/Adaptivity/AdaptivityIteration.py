from .ErrorIndicatorResult import ErrorIndicatorResult
from .RuleResult import RuleResult


class AdaptivityIteration:
    """The AdaptivityIteration object contains information about a given iteration of the
    varying topology adaptivity process (adaptive remeshing). 

    Attributes
    ----------
    ruleResults: dict[str, RuleResult]
        A repository of :py:class:`~abaqus.Adaptivity.RuleResult.RuleResult` objects specifying the calculated results from sizing
        functions corresponding to the :py:class:`~abaqus.Adaptivity.RemeshingRule.RemeshingRule` objects for this iteration of an adaptivity
        process.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import job
        mdb.adaptivityProcesses[name].iterations[i]

    """

    # A repository of RuleResult objects specifying the calculated results from sizing 
    # functions corresponding to the RemeshingRule objects for this iteration of an adaptivity 
    # process. 
    ruleResults: dict[str, RuleResult] = dict[str, RuleResult]()

    def __init__(self, iteration: int, jobName: str, modelName: str, odbPath: str, remeshingErrors: int):
        """This method creates an AdaptivityIteration object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.adaptivityProcesses[name].AdaptivityIteration
        
        Parameters
        ----------
        iteration
            An Int specifying the sequence number for this iteration in the adaptivity process. 
        jobName
            A String specifying the name of the job that was run for this iteration. 
        modelName
            A String specifying the name of the model that was analyzed and remeshed in this 
            iteration. 
        odbPath
            A String specifying the path to the ODB file that was created for this iteration. 
        remeshingErrors
            An Int specifying the number of part instances which generated errors while remeshing 
            the model in this iteration of the adaptivity process. 

        Returns
        -------
            An AdaptivityIteration object.
        """
        pass

    def ErrorIndicatorResult(self, name: str, results: str) -> ErrorIndicatorResult:
        """This method creates an ErrorIndicatorResult with data for an error indicator variable in
        a RemeshingRule for a given adaptivity iteration.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.adaptivityProcesses[name].AdaptivityIteration
        
        Parameters
        ----------
        name
            A String specifying the name of the error indicator variable to which these results
            correspond.
        results
            A String-to-Float Dictionary specifying the calculated results from the sizing function
            corresponding to the error indicator variable represented by this ErrorIndicatorResult.

        Returns
        -------
            An ErrorIndicatorResult object.

        Raises
        ------
            AbaqusException.
        """
        self.ruleResults[name] = ruleResult = ErrorIndicatorResult(name, results)
        return ruleResult

    def RuleResult(self, name: str, indicatorResults: dict[str, ErrorIndicatorResult], numElems: int,
                   minSizeElemCount: int, satisfiedVars: tuple = ()) -> RuleResult:
        """This method creates a RuleResult with data for a RemeshingRule for a given adaptivity
        iteration.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.adaptivityProcesses[name].AdaptivityIteration
        
        Parameters
        ----------
        name
            A String specifying the name of the Remeshing Rule to which these results correspond.
        indicatorResults
            A repository of ErrorIndicatorResult objects specifying the calculated results from the
            sizing function corresponding to the error indicator variables for the Remeshing Rule.
        numElems
            An Int specifying the number of elements before remeshing in the region of the Remeshing
            Rule.
        minSizeElemCount
            An Int specifying the number of elements that were constrained to the minimum element
            size by the Remeshing Rule.
        satisfiedVars
            A sequence of Strings specifying the error indicator variables that have satisfied the
            Remeshing Rule.

        Returns
        -------
            A RuleResult object.

        Raises
        ------
            AbaqusException.
        """
        self.ruleResults[name] = ruleResult = RuleResult(name, indicatorResults, numElems, minSizeElemCount,
                                                         satisfiedVars)
        return ruleResult
