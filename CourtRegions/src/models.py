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

"""Defines models for the CourtRegions application."""

from google.appengine.ext import db

class Court():
    """A location-aware model
    """
    name = db.StringProperty()
    address = db.StringProperty()
    phone_number = db.StringProperty()
    polygon = db.
    
    @staticmethod
    def public_attributes():
        """Returns a set of simple attributes on public school entities."""
        return [
          'name', 'address', 'phone_number'
        ]
    
    def _get_latitude(self):
        return self.location.lat if self.location else None
    
    def _set_latitude(self, lat):
        if not self.location:
            self.location = db.GeoPt()
        
        self.location.lat = lat
    
    latitude = property(_get_latitude, _set_latitude)
    
    def _get_longitude(self):
        return self.location.lon if self.location else None
    
    def _set_longitude(self, lon):
        if not self.location:
            self.location = db.GeoPt()
    
        self.location.lon = lon
    
    longitude = property(_get_longitude, _set_longitude)
