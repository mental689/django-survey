#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 02:41:14 2018

@author: tuannguyen
"""

from builtins import super
import logging

from django.db import models
from django.db.models import Count
from random import randint
from .video_category import VideoCategory
from django.utils.translation import ugettext_lazy as _


class VideosManager(models.Manager):
    def random(self, catID):
        count = self.filter(cat__id=catID).aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.filter(cat__id=catID)[random_index]

class Video(models.Model):
    objects = VideosManager()
    url =  models.TextField(_("Link to the video"), blank=False, null=False)
    vid =  models.CharField(_("Video ID"), blank=True, null=False, max_length=50)
    type = models.IntegerField(default=0) # 0: youtube, 1: others
    cat = models.ForeignKey(VideoCategory, default=1, on_delete=models.CASCADE)
    start = models.IntegerField(_("Start time"), default=0)
    end = models.IntegerField(_("End time"), default=0)
    created = models.DateTimeField(_("Creation date"), auto_now_add=True)
    updated = models.DateTimeField(_("Update date"), auto_now=True)