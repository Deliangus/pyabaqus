from abaqusConstants import *
from .AdaptivityIteration import AdaptivityIteration
from ..Job.ModelJob import ModelJob
from ..UtilityAndView.Repository import Repository


class AdaptivityProcess:

    """The AdaptivityProcess object defines a series of jobs that will be submitted for 
    analysis. Abaqus performs adaptive remeshing between each job. 

    Access
    ------
        - import job
        - mdb.adaptivityProcesses[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A SymbolicConstant specifying the status of the adaptivity process. Possible values are 
    # SUBMITTED, RUNNING, ABORTED, TERMINATED, and COMPLETED. 
    status: SymbolicConstant = None

    # A repository of AdaptivityIteration objects specifying the AdaptivityIteration objects 
    # received during running the adaptivity process. 
    iterations: Repository[str, AdaptivityIteration] = None

    def __init__(self, name: str, job: ModelJob, maxIterations: int = 3, jobPrefix: str = ''):
        """This method creates an AdaptivityProcess object.

        Path
        ----
            - mdb.AdaptivityProcess

        Parameters
        ----------
        name
            A String specifying the name of the Adaptivity Process. 
        job
            A ModelJob object specifying a job to be used as the prototype for all analysis jobs run 
            by the adaptivity process. 
        maxIterations
            An Int specifying the maximum number of analysis jobs that will be run by the Adaptivity 
            Process. Abaqus performs adaptive remeshing between each analysis. The default value is 
            3. 
        jobPrefix
            A String specifying the prefix to use for jobs created by the adaptivity process. An 
            empty string indicates that the name of the adaptivity process should be used. The 
            default value is an empty string. 

        Returns
        -------
            An AdaptivityProcess object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def submit(self, waitForCompletion: Boolean = OFF, datacheckJob: Boolean = False, 
               continueJob: Boolean = False):
        """This method begins the process of analysis and adaptive remeshing.

        Parameters
        ----------
        waitForCompletion
            A Boolean specifying whether to interrupt the execution of a script until the end of the 
            adaptive remeshing process is reached. 
        datacheckJob
            A Boolean specifying whether to run the adaptivity as a datacheck analysis. The default 
            value is False. The datacheckJob and continueJob arguments cannot both be True. 
        continueJob
            A Boolean specifying whether to run the adaptivity as a continuation analysis. The 
            default value is False. The datacheckJob and continueJob arguments cannot both be True. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self, maxIterations: int = 3, jobPrefix: str = ''):
        """This method modifies the AdaptivityProcess object.

        Parameters
        ----------
        maxIterations
            An Int specifying the maximum number of analysis jobs that will be run by the Adaptivity 
            Process. Abaqus performs adaptive remeshing between each analysis. The default value is 
            3. 
        jobPrefix
            A String specifying the prefix to use for jobs created by the adaptivity process. An 
            empty string indicates that the name of the adaptivity process should be used. The 
            default value is an empty string. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
