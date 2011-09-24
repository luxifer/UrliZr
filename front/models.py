# -*- coding: utf-8 -*-

from django.db import models
from UrliZr.front.functions import genUid

class Urliz(models.Model):
  url = models.URLField(unique=True, verify_exists=True)
  uid = models.CharField(max_length=8, primary_key=True, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __unicode__(self):
    return self.uid

  def save(self, *args, **kwargs):
    uid = genUid()
    while Urliz.objects.filter(uid__exact=uid).count() > 0:
      uid = genUid()
    self.uid = uid
    super(Urliz, self).save(*args, **kwargs)
