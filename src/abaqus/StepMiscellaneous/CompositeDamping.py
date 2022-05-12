from .CompositeDampingComponentArray import CompositeDampingComponentArray

from __init__ import *
from __future__ import annotations


class CompositeDamping:
    """A CompositeDamping object contains composite modal damping parameters.

    Attributes
    ----------
    components: CompositeDampingComponentArray
        A :py:class:`~abaqus.StepMiscellaneous.CompositeDampingComponentArray.CompositeDampingComponentArray` object.

    Notes
    -----
        This object can be accessed by:
        
        .. code-block:: python
        
           import step
           mdb.models[name].steps[name].compositeDamping

    """

    # A CompositeDampingComponentArray object.
    components: CompositeDampingComponentArray = CompositeDampingComponentArray(
    )