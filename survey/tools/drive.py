#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 16:25:08 2018

@author: tuananhn
"""

import csv
import logging
import django
django.setup()
from survey.models import Video, VideoCategory
from django.db import *
from tqdm import tqdm


def read_csv(csvfile):
    r = csv.reader(csvfile, delimiter=",")
    for row in tqdm((r)):
        try:
            catId = row[-1]
            cat = VideoCategory.objects.filter(id=catId)[0]
            v = Video(vid=row[1], url=row[0], start=int(row[2]), end=int(row[3]), type=row[4], cat=cat)
            v.save()        
        except Exception as e:
            logging.debug(e)
        