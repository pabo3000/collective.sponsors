# -*- coding: utf-8 -*-
"""Definition of the Sponsor content type
"""
from AccessControl import ClassSecurityInfo

from zope.interface import implements

from Products.CMFCore.permissions import View
from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from collective.sponsors import sponsorsMessageFactory as _

from collective.sponsors.interfaces import ISponsor
from collective.sponsors.config import PROJECTNAME

SponsorSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.ImageField(
        'banner',
        storage=atapi.AnnotationStorage(),
        allowable_content_types=('image/gif','image/jpeg','image/png'),
        language_independent=True,
        sizes= {'large'   : (768, 768),
                'banner'  : (468, 468),
                'preview' : (400, 400),
                'mini'    : (200, 200),
                'thumb'   : (96, 96),
                'tile'    :  (64, 64),
                'icon'    :  (32, 32),
                'listing' :  (16, 16),
               },
        widget=atapi.ImageWidget(
            label=_(u"Banner"),
            description=_(u"Please upload a banner as jpg, gif or png. "
                          u"The banner is displayed in the sponsors_view of a "
                          u"folder or collection. The full banner size (468 * 60) "
                          u"is recommendable."),
        ),
        validators=('isNonEmptyFile'),
    ),


    atapi.ImageField(
        'image',
        storage=atapi.AnnotationStorage(),
        allowable_content_types=('image/gif','image/jpeg','image/png'),
        language_independent=True,
        sizes= {'large'   : (768, 768),
               'preview' : (400, 400),
               'mini'    : (200, 200),
               'thumb'   : (96, 96),
               'tile'    :  (64, 64),
               'icon'    :  (32, 32),
               'listing' :  (16, 16),
              },
        widget=atapi.ImageWidget(
            label=_(u"Partner Logo"),
            description=_(u"Please upload the partner's logo. (jpg, gif or png)"
                          u"It will be displayed in the site's footer."),
        ),
        validators=('isNonEmptyFile'),
    ),


    atapi.StringField(
        'remoteUrl',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"URL"),
            description=_(u"Field description"),
        ),
    ),


    atapi.FixedPointField(
        'donation',
        storage=atapi.AnnotationStorage(),
        widget=atapi.DecimalWidget(
            label=_(u"Donation"),
            description=_(u"Enter the amount of donation in EUR. It is used for "
                          u"calculationg the partners order."),
        ),
        default=_(u"0.00"),
        validators=('isDecimal'),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

SponsorSchema['title'].storage = atapi.AnnotationStorage()
SponsorSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(SponsorSchema, moveDiscussion=False)


class Sponsor(base.ATCTContent):
    """A person or company who donates."""
    implements(ISponsor)

    meta_type = "Sponsor"
    schema = SponsorSchema

    security = ClassSecurityInfo()

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    banner = atapi.ATFieldProperty('banner')

    donation = atapi.ATFieldProperty('donation')

    image = atapi.ATFieldProperty('image')

    remoteUrl = atapi.ATFieldProperty('remoteUrl')

   # workaround to make resized images
    def __bobo_traverse__(self, REQUEST, name):
        """Transparent access to image scales
        """
        if name.startswith('image'):
            field = self.getField('image')
            image = None
            if name == 'image':
                image = field.getScale(self)
            else:
                scalename = name[len('image_'):]
                if scalename in field.getAvailableSizes(self):
                    image = field.getScale(self, scale=scalename)
            if image is not None and not isinstance(image, basestring):
                # image might be None or '' for empty images
                return image
        
        if name.startswith('banner'):
            field = self.getField('banner')
            image = None
            if name == 'banner':
                image = field.getScale(self)
            else:
                scalename = name[len('banner_'):]
                if scalename in field.getAvailableSizes(self):
                    image = field.getScale(self, scale=scalename)
            if image is not None and not isinstance(image, basestring):
                # image might be None or '' for empty images
                return image

        return base.ATCTContent.__bobo_traverse__(self, REQUEST, name)

    security.declareProtected(View, 'tag')
    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        return self.getField('image').tag(self, **kwargs)

atapi.registerType(Sponsor, PROJECTNAME)
