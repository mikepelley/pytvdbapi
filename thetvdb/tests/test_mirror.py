# -*- coding: utf-8 -*-

# Copyright 2011 Björn Larsson

# This file is part of thetvdb.
#
# thetvdb is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# thetvdb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with thetvdb.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os

from thetvdb import xmlhelpers, mirror, error
import utils
import basetest

class TestMirror(basetest.TheTVDBTest):
    def setUp(self):
        super(TestMirror, self).setUp()

        data = utils.file_loader(os.path.join(self.path, "mirrors.xml"))
        self.mirrors = mirror.MirrorList(xmlhelpers.generate_tree(data))

    def tearDown(self):
        super(TestMirror, self).tearDown()

    def test_mirror_list_length(self):
        """It should be possible to use len() on the mirror list"""

        self.assertEqual( len(self.mirrors), 1 )

    def test_get_mirror_type(self):
        """It should be possible to get a mirror with the correct mirror type"""
        m = self.mirrors.get_mirror(mirror.TypeMask.BANNER)
        self.assertEqual(m.type_mask & mirror.TypeMask.BANNER,
                         mirror.TypeMask.BANNER)

        m = self.mirrors.get_mirror(mirror.TypeMask.XML)
        self.assertEqual(m.type_mask & mirror.TypeMask.XML,
                         mirror.TypeMask.XML)

        m = self.mirrors.get_mirror(mirror.TypeMask.ZIP)
        self.assertEqual(m.type_mask & mirror.TypeMask.ZIP,
                         mirror.TypeMask.ZIP)

    def test_iterate_mirrors(self):
        """It should be possible to iterate over the list of mirrors"""
        for m in self.mirrors:
            pass

    def test_invalid_mirror_type(self):
        """function should raise TheTvDBError if no mirror is found or an
        invalid type is used"""

        self.assertRaises( error.TheTvDBError, self.mirrors.get_mirror, 100)


if __name__ == "main":
    sys.exit( unittest.main() )