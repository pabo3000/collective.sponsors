from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from plone.memoize.instance import memoize

from collective.sponsors import sponsorsMessageFactory as _


class ISponsorView(Interface):
    """
    Sponsor view interface
    """

    def test():
        """ test method"""


class SponsorView(BrowserView):
    """
    Sponsor browser view
    """
    implements(ISponsorView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    @memoize
    def sponsors(self):
        """
        returns a list of dicts of sponsors in this folder
        """
        return sorted([dict(id=sponsor.id,
                            title=sponsor.Title(),
                            remoteUrl=sponsor.getRemoteUrl(),
                            image=sponsor.getBanner(),
                            donation=sponsor.getDonation(),
                            url=sponsor.absolute_url()) 
                       for sponsor in self.context.listFolderContents(contentFilter=
                                                                      {"portal_type" : "Sponsor",
                                                                       "review_state": "published",})
                if not sponsor.getBanner()==''
                ], key=lambda sponsor: sponsor['donation'])

    def folder(self):
        """
        returns folder attrs.
        """
        return dict(title=self.context.Title())