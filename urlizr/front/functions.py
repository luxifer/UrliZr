"""
This file is part of UrliZr.

UrliZr is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

UrliZr is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with UrliZr.  If not, see <http://www.gnu.org/licenses/>.
"""

import string
from random import choice


def genUid():
  chars = string.letters + string.digits
  return u''.join(choice(chars) for i in range(8))
