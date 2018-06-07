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
from survey.models import Video
from django.db import *
from tqdm import tqdm


def read_csv(csvfile):
    r = csv.reader(csvfile, delimiter=",")
    for row in tqdm(enumerate(r)):
        try:
            v = Video(vid=row[0], url=row[1], type=row[2])
            v.save()
        except Exception as e:
            logging.debug(e)
        