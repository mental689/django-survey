#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 02:40:45 2018

@author: tuannguyen
"""

from builtins import super
import logging

from django.views.generic import TemplateView
from future import standard_library
from survey.models import Video

standard_library.install_aliases()


class MediaPage(TemplateView):

    template_name = 'survey/media.html'
    
    def get_context_data(self, **kwargs):
        context = super(MediaPage, self).get_context_data(**kwargs)
        videos = Video.objects.all()
        logging.debug(videos)
        return context