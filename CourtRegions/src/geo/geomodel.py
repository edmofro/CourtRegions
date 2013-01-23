#!/usr/bin/python2.5
#
# Copyright 2013 Edwin Monk-Fromont
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Defines the GeoModel class for running basic geospatial queries on
single-point geographic entities in Google App Engine.
"""



import copy
import logging
import math
import sys

from google.appengine.ext import db

import geocell
import geomath
import geotypes
import util

DEBUG = False


@staticmethod
def region_fetch(query, center):
    """Performs a region fetch on the given query.

    Fetches the court region matching the given query

    Args:
      query: A db.Query on entities of this kind.
      center: A geotypes.Point or db.GeoPt indicating the center point around
          which to search for matching entities.
      
    Returns:
      The fetched court region

    Raises:
      Any exceptions that google.appengine.ext.db.Query.fetch() can raise.
    """   

    return //TODO
