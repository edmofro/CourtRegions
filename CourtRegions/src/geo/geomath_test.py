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

"""Unit tests for geomath.py."""



import unittest

import geomath
import geotypes


class GeomathTests(unittest.TestCase):
  def test_distance(self):
    # known distances using GLatLng from the Maps API
    calc_dist = geomath.distance(geotypes.Point(37, -122),
                                 geotypes.Point(42, -75))
    known_dist = 4024365

    # make sure the calculated distance is within +/- 1% of known distance
    self.assertTrue(abs((calc_dist - known_dist) / known_dist) <= 0.01)

  def test_distance_rounding(self):
    # Test location that can cause math domain error (due to rounding) unless
    # the distance function clamps the spherical law of cosines value between
    # -1.0 and 1.0. 
    calc_dist = geomath.distance(geotypes.Point(47.291288, 8.56613),
                                 geotypes.Point(47.291288, 8.56613))
    known_dist = 0.0
    self.assertTrue(calc_dist == known_dist)


if __name__ == '__main__':
  unittest.main()
