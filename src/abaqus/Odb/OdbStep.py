import typing

from .HistoryPoint import HistoryPoint
from .HistoryRegion import HistoryRegion
from .OdbFrame import OdbFrame
from .OdbLoadCase import OdbLoadCase
from .OdbStepBase import OdbStepBase


class OdbStep(OdbStepBase):

    def HistoryRegion(self, name: str, description: str, point: HistoryPoint, loadCase: str = None) -> HistoryRegion:
        """This method creates a HistoryRegion object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                session.odbs[name].steps[name].HistoryRegion
        
        Parameters
        ----------
        name
            A String specifying the name of the HistoryRegion object.
        description
            A String specifying the description of the HistoryRegion object.
        point
            A HistoryPoint object specifying the point to which the history data refer.
        loadCase
            None or an OdbLoadCase object specifying the load case associated with the HistoryRegion
            object. The default value is None.

        Returns
        -------
            A HistoryRegion object.
        """
        self.historyRegions[name] = historyRegion = HistoryRegion(name, description, point, loadCase)
        return historyRegion

    @typing.overload
    def Frame(self, incrementNumber: int, frameValue: float, description: str = '') -> OdbFrame:
        """This method creates an OdbFrame object and appends it to the frame sequence.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                session.odbs[name].steps[name].Frame
        
        Parameters
        ----------
        incrementNumber
            An Int specifying the frame increment number within the step. The base frame has
            normally increment number 0, and the results run from 1. In case of multiple load cases,
            the same increment number is duplicated for each load case.
        frameValue
            A Float specifying the value in units determined by the *domain* member of the Step
            object. The equivalent in the time domain is *stepTime*; in the frequency domain the
            equivalent is *frequency*; and in the modal domain the equivalent is *mode*.
        description
            A String specifying the contents of the frame. The default value is an empty string.

        Returns
        -------
            An OdbFrame object.
        """
        pass

    @typing.overload
    def Frame(self, mode: int, frequency: float, description: str = '') -> OdbFrame:
        """This constructor creates an OdbFrame object in the frequency domain and appends it to
        the frame sequence. The arguments to the constructor are valid only when
        *domain*=FREQUENCY or *domain*=MODAL.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                session.odbs[name].steps[name].Frame
        
        Parameters
        ----------
        mode
            An Int specifying the eigenmode. This member is valid only if *domain*=MODAL.
        frequency
            A Float specifying the frequency. This member is valid only if *domain*=FREQUENCY or if
            the *procedureType* member of the Step object=FREQUENCY. The default value is 0.0.
        description
            A String specifying the contents of the frame. The default value is an empty string.

        Returns
        -------
            An OdbFrame object.
        """
        pass

    @typing.overload
    def Frame(self, loadCase: OdbLoadCase, description: str = '', frequency: float = 0) -> OdbFrame:
        """This constructor creates an OdbFrame object for a specific load case and appends it to
        the frame sequence.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                session.odbs[name].steps[name].Frame
        
        Parameters
        ----------
        loadCase
            An OdbLoadCase object specifying the load case for the frame.
        description
            A String specifying the contents of the frame. The default value is an empty string.
        frequency
            A Float specifying the frequency. This member is valid only if *domain*=FREQUENCY or if
            the *procedureType* member of the Step object=FREQUENCY. The default value is 0.0.

        Returns
        -------
            An OdbFrame object.
        """
        pass

    def Frame(self, *args, **kwargs) -> OdbFrame:
        frame = OdbFrame(*args, **kwargs)
        self.frames.append(frame)
        return frame

    def OdbLoadCase(self, name: str) -> OdbLoadCase:
        """This method creates an OdbLoadCase object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                session.odbs[*name*].steps[*name*].LoadCase
        
        Parameters
        ----------
        name
            A String specifying the name of the OdbLoadCase object.

        Returns
        -------
            An OdbLoadCase object.
        """
        self.loadCases[name] = odbLoadCase = OdbLoadCase(name)
        return odbLoadCase
