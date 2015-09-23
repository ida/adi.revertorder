from Acquisition import aq_inner
from Acquisition import aq_parent

from OFS.interfaces import IOrderedContainer

def revertOrder(obj, eve):
    """
    Use IOrderedContainer interface to move an object to top of folder on creation.
    """
    parent = obj.aq_inner.aq_parent
    ordered = IOrderedContainer(parent, None)
    if ordered is not None:
        ordered.moveObjectToPosition(obj.getId(), 0)

