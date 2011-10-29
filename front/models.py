# -*- coding: utf-8 -*-
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

from django.db import models
from UrliZr.front.functions import genUid

class Urliz(models.Model):
  url = models.URLField(unique=True, verify_exists=True)
  uid = models.CharField(max_length=8, primary_key=True, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  hit = models.BigIntegerField()
  
  def __unicode__(self):
    return self.uid

  def save(self, *args, **kwargs):
    uid = genUid()
    while Urliz.objects.filter(uid__exact=uid).count() > 0:
      uid = genUid()
    self.uid = uid
    super(Urliz, self).save(*args, **kwargs)
