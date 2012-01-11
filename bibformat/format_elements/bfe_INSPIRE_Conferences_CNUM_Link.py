# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
"""BibFormat element - Prints CNUM for conferences
"""
__revision__ = "$Id$"

def format_element(bfo):
    """
    Prints CNUM for conferences from 111__g. With hyphons.
    """
    cnum = str(bfo.field('111__g'))

    string = cnum[:3] + '-' + cnum[3:5] + '-'

    if "-" in cnum:
        return cnum
    else:
        if len(cnum) == 8:
            day = cnum[5:7]
            nr = cnum[7]
            return string + day + '.' + nr
        else:
            day = cnum[5:]
            return string + day