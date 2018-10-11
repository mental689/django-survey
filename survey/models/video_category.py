#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 17:10:43 2018

@author: tuananhn
"""

from builtins import super
import logging

from django.db import models
from django.db.models import Count
from random import randint
from django.utils.translation import ugettext_lazy as _


class VideoCategory(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(_("Creation time"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated time"), auto_now_add=True)