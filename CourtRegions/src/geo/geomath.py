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

"""Defines common geo math functions used throughout the library."""



import math

import geotypes

RADIUS = 6378135


def distance(p1, p2):
  """Calculates the great circle distance between two points (law of cosines).

  Args:
    p1: A geotypes.Point or db.GeoPt indicating the first point.
    p2: A geotypes.Point or db.GeoPt indicating the second point.

  Returns:
    The 2D great-circle distance between the two given points, in meters.
  """
  p1lat, p1lon = math.radians(p1.lat), math.radians(p1.lon)
  p2lat, p2lon = math.radians(p2.lat), math.radians(p2.lon)
  # work out the internal value for the spherical law of cosines and clamp
  # it between -1.0 and 1.0 to avoid python rounding errors
  sloc = (math.sin(p1lat) * math.sin(p2lat) +
          math.cos(p1lat) * math.cos(p2lat) * math.cos(p2lon - p1lon))
  sloc = max(min(sloc, 1.0), -1.0)
  return RADIUS * math.acos(sloc)
