from abaqusConstants import *
from .EventSeries import EventSeries
from .EventSeriesType import EventSeriesType
from ..Model.ModelBase import ModelBase


class TableCollectionModel(ModelBase):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        mdb.models[name]

    """

    def EventSeries(self, name: str, createStepName: str, eventSeriesType: str, transformType: str = NONE,
                    timeSpan: str = STEP_TIME, transformations: str = '', fileName: str = '',
                    data: str = '') -> EventSeries:
        """This method creates an EventSeries object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].EventSeriesData
        
        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A string specifying the step name.
        eventSeriesType
            A string specifying the type of event series.
        transformType
            A Symbolic constant specifying the type of transformation. Possible values are NONE,
            BOTH, TRANSLATE, and ROTATE. The default value is NONE.
        timeSpan
            A Symbolic constant specifying time. Possible values are TOTAL_TIME and STEP_TIME. The
            default value is STEP_TIME.
        transformations
            An Array specifying the required transformations over event series data.
        fileName
            A String specifying the filename.
        data
            An Array of double specifying the values of fields provided in EventSeriesType.

        Returns
        -------
            An EventSeries object.

        Raises
        ------
            RangeError.
        """
        self.eventSeriesDatas[name] = eventSeries = EventSeries(name, createStepName, eventSeriesType, transformType,
                                                                timeSpan, transformations, fileName, data)
        return eventSeries

    def EventSeriesType(self, name: str, createStepName: str, fields: str = '') -> EventSeriesType:
        """This method creates an EventSeriesType object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].EventSeriesType
        
        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A string specifying the step name.
        fields
            A String array specifying fields. The default value is an empty array.

        Returns
        -------
            A EventSeriesType object.

        Raises
        ------
            RangeError.
        """
        self.eventSeriesTypes[name] = eventSeriesType = EventSeriesType(name, createStepName, fields)
        return eventSeriesType
