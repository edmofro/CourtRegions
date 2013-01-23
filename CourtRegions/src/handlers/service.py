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

"""Service /s/* request handlers."""

import os
import sys
import wsgiref.handlers

from django.utils import simplejson

from google.appengine.ext import db
from google.appengine.ext import webapp

from geo import geotypes

from models import Court


def _merge_dicts(*args):
    """Merges dictionaries right to left. Has side effects for each argument."""
    return reduce(lambda d, s: d.update(s) or d, args)


class SearchService(webapp.RequestHandler):
    """Handler for search requests."""
    def get(self):
        def _simple_error(message, code=400):
            self.error(code)
            self.response.out.write(simplejson.dumps({
              'status': 'error',
              'error': { 'message': message },
              'results': []
            }))
            return None
          
        
        self.response.headers['Content-Type'] = 'application/json'
        
               
        try:
            center = geotypes.Point(float(self.request.get('lat')),
                                    float(self.request.get('lon')))
        except ValueError:
            return _simple_error('lat and lon parameters must be valid latitude '
                                 'and longitude values.')
        
        
        
          
        try:
            # Get appropriate court given center   
            
            courts = # Find all region polygons from database
            
            result = courts[0]
            
            for court in courts:
                if court.polygon.containsLocation(center):
                    result = court
                    break
                else:
                    return _simple_error('Address did not match to any court region.')
                     
            public_attrs = Court.public_attributes()
            
            results_obj = [
                _merge_dicts({
                  'lat': result.location.lat,
                  'lng': result.location.lon,
                  },
                  dict([(attr, getattr(result, attr))
                        for attr in public_attrs]))]
            
            self.response.out.write(simplejson.dumps({
              'status': 'success',
              'results': results_obj
          }))
        except:
            return _simple_error(str(sys.exc_info()[1]), code=500)


def main():
    application = webapp.WSGIApplication([
        ('/s/search', SearchService),
        ],
        debug=('Development' in os.environ['SERVER_SOFTWARE']))
    wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
    main()
