from abaqusConstants import *

class HistoryVariable:

    """The HistoryVariable object stores history data. 

    Access
    ------
        - import visualization
        - session.odbData[name].historyVariables[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the history request label. This String is read-only. 
    name: str = ''

    # A String specifying the legend text. This String is read-only. 
    legendLabel: str = ''

    # A tuple of (String, Int, SymbolicConstant) tuples specifying the steps. This sequence is 
    # read-only. Each inner sequence contains the following elements:*stepLabel*: A String 
    # specifying the step label.*stepNumber*: An Int specifying the step 
    # number.*procedureDomain*: A SymbolicConstant specifying the analysis type of the step, 
    # which can have these values: “TIME,” “FREQUENCY,” or “MODAL.” 
    steps: SymbolicConstant = None
