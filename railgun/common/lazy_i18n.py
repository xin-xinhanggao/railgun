#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: railgun/common/lazy_i18n.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Contributors:
#   public@korepwx.com   <public@korepwx.com>
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.

from flask.ext.babel import gettext as _babel_gettext

"""
this module contains a serializable lazy gettext utility.
"""


class GetTextString(object):
    """keyword formattable and serializable lazy gettext string"""

    def __init__(self, text, **kwargs):
        self.text = text
        self.kwargs = kwargs

    def render(self):
        """render lazy string and get translated text"""
        return _babel_gettext(self.text, **self.kwargs)

    def __unicode__(self):
        return unicode(self.render())

    def __str__(self):
        return str(self.render())


gettext_lazy = GetTextString
