from plone.memoize.view import memoize
from plone.app.layout.viewlets import common as base
from Products.CMFCore.interfaces import IFolderish
from Products.CMFCore.interfaces import ISiteRoot
from Products.CMFCore.utils import getToolByName

class SponsorsViewlet(base.ViewletBase):
    """ Add a div with a list of sponsor logos
    """

    @memoize
    def sponsors(self):
        """ 
        Get a list of sponsors
        """
        context = self.context.aq_inner
        catalog = getToolByName(context, 'portal_catalog')

        sponsors = [brain.getObject() for brain 
                    in catalog.searchResults({'portal_type': 'Sponsor', 
                                             'review_state': 'published',
                                             'Subject': 'footer'})]
        return [dict(id=sponsor.id,
                     title=sponsor.Title(),
                     remoteUrl=sponsor.getRemoteUrl(),
                     image=sponsor.getImage(),
                     url=sponsor.absolute_url()) 
                for sponsor in sponsors
                ]
