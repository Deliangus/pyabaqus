import typing

from ..Model.ModelBase import ModelBase
from .FieldOutputRequest import FieldOutputRequest
from .HistoryOutputRequest import HistoryOutputRequest
from abaqusConstants import *


class OutputModel(ModelBase):

    def FieldOutputRequest(self, name: str, createStepName: str, region: SymbolicConstant = MODEL,
                           variables: SymbolicConstant = PRESELECT, frequency: SymbolicConstant = 1,
                           modes: SymbolicConstant = ALL,
                           timeInterval: typing.Union[SymbolicConstant, float] = EVERY_TIME_INCREMENT,
                           numIntervals: int = 20, timeMarks: Boolean = OFF, boltLoad: str = '',
                           sectionPoints: SymbolicConstant = DEFAULT, interactions: str = None,
                           rebar: SymbolicConstant = EXCLUDE, filter: SymbolicConstant = None,
                           directions: Boolean = ON, fasteners: str = '', assembledFastener: str = '',
                           assembledFastenerSet: str = '', exteriorOnly: Boolean = OFF, layupNames: str = '',
                           layupLocationMethod: str = SPECIFIED, outputAtPlyTop: Boolean = False,
                           outputAtPlyMid: Boolean = True, outputAtPlyBottom: Boolean = False,
                           position: SymbolicConstant = INTEGRATION_POINTS):
        """This method creates a FieldOutputRequest object.

        Path
        ----
            - mdb.models[name].FieldOutputRequest

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the object is created.
        region
            The SymbolicConstant MODEL or a Region object specifying the region from which output is
            requested. The SymbolicConstant MODEL represents the whole model. The default value is
            MODEL.
        variables
            A sequence of Strings specifying output request variable or component names, or the
            SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for
            the given step. ALL represents all valid output variables. The default value is
            PRESELECT.
        frequency
            The SymbolicConstant LAST_INCREMENT or an Int specifying the output frequency in
            increments. The default value is 1.
        modes
            The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which
            output is desired. The default value is ALL.
        timeInterval
            The SymbolicConstant EVERY_TIME_INCREMENT or a Float specifying the time interval at
            which the output states are to be written. The default value is EVERY_TIME_INCREMENT.
        numIntervals
            An Int specifying the number of intervals during the step at which output database
            states are to be written. The default value is 20.
        timeMarks
            A Boolean specifying when to write results to the output database. OFF indicates that
            output is written immediately after the time dictated by the specified number of
            intervals. ON indicates that output is written at the exact times dictated by the
            specified number of intervals. The default value is OFF.
        boltLoad
            A String specifying a bolt load from which output is requested.
        sectionPoints
            The SymbolicConstant DEFAULT or a sequence of Ints specifying the section points for
            which output requested. The default is DEFAULT.
        interactions
            None or a sequence of Strings specifying the interaction names. The default value is
            None.The sequence can contain only one String.
        rebar
            A SymbolicConstant specifying whether output is requested for rebar. Possible values are
            EXCLUDE, INCLUDE, and ONLY. The default value is EXCLUDE.
        filter
            The SymbolicConstant ANTIALIASING or a String specifying the name of an output filter
            object. The default value is None.
        directions
            A Boolean specifying whether to output directions of the local material coordinate
            system. The default value is ON.
        fasteners
            A String specifying the fastener name. The default value is an empty string.
        assembledFastener
            A String specifying the assembled fastener name. The default value is an empty string.
        assembledFastenerSet
            A String specifying the set name from the model referenced by the assembled fastener,
            *assembledFastener*. The default value is an empty string.
        exteriorOnly
            A Boolean specifying whether the output domain is restricted to the exterior of the
            model. This argument is only valid if *region*=MODEL. The default value is OFF.
        layupNames
            A List of Composite Layer Names.
        layupLocationMethod
            A Symbolic constant specifying the method used to indicate the output locations for
            composite layups. Possible values are ALL_LOCATIONS, SPECIFIED and TYPED_IN. The default
            value is SPECIFIED.
        outputAtPlyTop
            A Boolean specifying whether to output at the ply top section point. The default value
            is False.
        outputAtPlyMid
            A Boolean specifying whether to output at the ply mid section point. The default value
            is True.
        outputAtPlyBottom
            A Boolean specifying whether to output at the ply bottom section point. The default
            value is False.
        position
            A SymbolicConstant specifying the position on an element where output needs to be
            written. Possible values are INTEGRATION_POINTS, AVERAGED_AT_NODES, CENTROIDAL, and
            NODES. The default value is INTEGRATION_POINTS.

        Returns
        -------
            A FieldOutputRequest object.

        Exceptions
        ----------
            None.
        """
        self.fieldOutputRequests[name] = FieldOutputRequest(name, createStepName, region, variables, frequency, modes,
                                                            timeInterval, numIntervals, timeMarks, boltLoad,
                                                            sectionPoints, interactions, rebar, filter, directions,
                                                            fasteners, assembledFastener, assembledFastenerSet,
                                                            exteriorOnly, layupNames, layupLocationMethod,
                                                            outputAtPlyTop, outputAtPlyMid, outputAtPlyBottom, position)
        return self.fieldOutputRequests[name]

    def HistoryOutputRequest(self, name: str, createStepName: str, region: SymbolicConstant = MODEL,
                             variables: SymbolicConstant = PRESELECT, frequency: SymbolicConstant = 1,
                             modes: SymbolicConstant = ALL,
                             timeInterval: typing.Union[SymbolicConstant, float] = EVERY_TIME_INCREMENT,
                             numIntervals: int = 20, boltLoad: str = '', sectionPoints: SymbolicConstant = DEFAULT,
                             stepName: str = '', interactions: str = None, contourIntegral: str = None,
                             numberOfContours: int = 0, stressInitializationStep: str = None,
                             contourType: SymbolicConstant = J_INTEGRAL, kFactorDirection: SymbolicConstant = MTS,
                             rebar: SymbolicConstant = EXCLUDE, integratedOutputSection: str = '',
                             springs: tuple = None, filter: SymbolicConstant = None, fasteners: str = '',
                             assembledFastener: str = '', assembledFastenerSet: str = '', sensor: Boolean = OFF,
                             useGlobal: Boolean = True):
        """This method creates a HistoryOutputRequest object.

        Path
        ----
            - mdb.models[name].HistoryOutputRequest

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the object is created.
        region
            The SymbolicConstant MODEL or a Region object specifying the region from which output is
            requested. The SymbolicConstant MODEL represents the whole model. The default value is
            MODEL.If the region is a surface region, the surface must lie within the general contact
            surface domain.
        variables
            A sequence of Strings specifying output request variable or component names, or the
            SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for
            the given step. ALL represents all valid output variables. The default value is
            PRESELECT.
        frequency
            The SymbolicConstant LAST_INCREMENT or an Int specifying the output frequency in
            increments. The default value is 1.
        modes
            The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which
            output is desired. The default value is ALL.
        timeInterval
            The SymbolicConstant EVERY_TIME_INCREMENT or a Float specifying the time interval at
            which the output states are to be written. The default value is EVERY_TIME_INCREMENT.
        numIntervals
            An Int specifying the number of intervals during the step at which output database
            states are to be written. The default value is 20.
        boltLoad
            A String specifying a bolt load from which output is requested. The default value is an
            empty string.
        sectionPoints
            The SymbolicConstant DEFAULT or a sequence of Ints specifying the section points for
            which output is requested. The default value is DEFAULT.
        stepName
            A String specifying the name of the step. The default value is an empty string.
        interactions
            None or a sequence of Strings specifying the interaction names. The default value is
            None.The sequence can contain only one String.
        contourIntegral
            A String specifying the contour integral name. The default value is None.
        numberOfContours
            An Int specifying the number of contour integrals to output for the contour integral
            object. The default value is 0.
        stressInitializationStep
            A String specifying the name of the stress initialization step. The default value is
            None.
        contourType
            A SymbolicConstant specifying the type of contour integral. Possible values are
            J_INTEGRAL, C_INTEGRAL, T_STRESS, and K_FACTORS. The default value is J_INTEGRAL.
        kFactorDirection
            A SymbolicConstant specifying the stress intensity factor direction. Possible values are
            MTS, MERR, and K110. The *kFactorDirection* argument is valid only if
            *contourType*=K_FACTORS. The default value is MTS.
        rebar
            A SymbolicConstant specifying whether output is requested for rebar. Possible values are
            EXCLUDE, INCLUDE, and ONLY. The default value is EXCLUDE.
        integratedOutputSection
            A String specifying the integrated output section. The default value is an empty string.
        springs
            A sequence of Strings specifying the springs/dashpots names. The default value is None.
            The sequence can contain only one String.
        filter
            The SymbolicConstant ANTIALIASING or a String specifying the name of an output filter
            object. The default value is None.
        fasteners
            A String specifying the fastener name. The default value is an empty string.
        assembledFastener
            A String specifying the assembled fastener name. The default value is an empty string.
        assembledFastenerSet
            A String specifying the set name from the model referenced by the assembled fastener,
            *assembledFastener*. The default value is an empty string.
        sensor
            A Boolean specifying whether to associate the output request with a sensor definition.
            The default value is OFF.
        useGlobal
            A Boolean specifying whether to output vector-valued nodal variables in the global
            directions. The default value is True.

        Returns
        -------
            A HistoryOutputRequest object.

        Exceptions
        ----------
            None.
        """
        self.historyOutputRequests[name] = HistoryOutputRequest(name, createStepName, region, variables, frequency,
                                                                modes, timeInterval, numIntervals, boltLoad,
                                                                sectionPoints, stepName, interactions, contourIntegral,
                                                                numberOfContours, stressInitializationStep, contourType,
                                                                kFactorDirection, rebar, integratedOutputSection,
                                                                springs, filter, fasteners, assembledFastener,
                                                                assembledFastenerSet, sensor, useGlobal)
        return self.historyOutputRequests[name]