from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from collective.sponsors import sponsorsMessageFactory as _



class ISponsor(Interface):
    """A person or company who donates."""

    # -*- schema definition goes here -*-
    donation = schema.Float(
        title=_(u"Donation"),
        required=False,
        description=_(u"Enter the amount of donation in EUR. It is used for "
                      u"calculationg the partners order."),
    )
#
    image = schema.Bytes(
        title=_(u"Image"),
        required=True,
        description=_(u"Field description"),
    )
#
    remoteUrl = schema.TextLine(
        title=_(u"URL"),
        required=False,
        description=_(u"Field description"),
    )
#
