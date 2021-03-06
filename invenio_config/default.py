# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Invenio default configuration."""

from __future__ import absolute_import, print_function

import warnings


class InvenioConfigDefault(object):
    """Load configuration from module."""

    def __init__(self, app=None):
        """Initialize extension."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Initialize Flask application."""
        # Ensure SECRET_KEY is set.
        SECRET_KEY = app.config.get('SECRET_KEY')

        if SECRET_KEY is None:
            app.config["SECRET_KEY"] = 'CHANGE_ME'
            warnings.warn(
                "Set configuration variable SECRET_KEY with random string",
                UserWarning)
