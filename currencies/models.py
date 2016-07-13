from __future__ import unicode_literals

from django.db import models

class Currency(models.Model):
    text = models.CharField(max_length=3, primary_key=True,null=False, blank=False)

    def __unicode__(self):
        return self.text