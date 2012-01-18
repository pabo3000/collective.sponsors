Introduction
============

collective.sponsors is a Plone extension that adds an archetype for manage 
sponsors on your site. There is an additional view for folders containing sponsors.
Published sponsors which are tagged as "footer" will be displayed in the 
portal footer.


Installing
==========

This package requires Plone 4.0 or later (tested on 4.1).

Installing without buildout
---------------------------

Install this package in either your system path packages or in the lib/python
directory of your Zope instance. You can do this using either easy_install or
via the setup.py script.

Installing with buildout
------------------------

If you are using `buildout` to manage your instance installing
collective.sponsors is even simpler. You can install
collective.sponsors by adding it to the eggs line for your instance::

    [instance]
    eggs = collective.sponsors

After updating the configuration you need to run the ''bin/buildout'', which
will take care of updating your system.

Go to the 'Site Setup' page in the Plone interface and click on the 'Add/Remove Products' link.

Choose the product (check its checkbox) and click the 'Install' button.


Usage
=====

Upload an image into any folder of the portal and tag it as "background". Each object 
in this folder and below is rendered with the image as fullscreen background. 