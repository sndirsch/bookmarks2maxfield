#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
  bookmarks2maxfield.py <input_file> [<output_file>]

Description:
  Input generator for Ingress Maxfield
  (http://www.ingress-maxfield.com), which uses the export of the
  IITC Bookmarks Plugin as input.

  1. Mark your portal set in IITC as bookmarks (Bookmarks Plugin).
  2. Export it as file.
  3. Run this script with the exported file as <input_file> and use the 
     result (standard output or content of <output_file>) as input for 
     Ingress Maxfield (http://www.ingress-maxfield.com)

  input_file:
    IITC Bookmark Plugin export in JSON format, e.g. 'bookmarks.json'
    
  output_file:
    generated output in CSV format, e.g. 'maxfield.csv'
"""  

import sys
import codecs
import json
from docopt import docopt

args = docopt(__doc__)

input_file = args['<input_file>']
output_file = ''
if args['<output_file>'] != None:
    output_file = args['<output_file>']

# Always write to stdout in UTF-8, independent of the locale:
if sys.version_info < (3, 0):
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout)
else:
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer)

with codecs.open(input_file,'r', encoding='utf-8') as f_input:

    d = json.load(f_input)

    output = ''
    for id in sorted(
            d['portals']['idOthers']['bkmrk'],
            key=lambda x: d['portals']['idOthers']['bkmrk'][x]['label']):
        gpscoords=d['portals']['idOthers']['bkmrk'][id]["latlng"]
        portalname=d['portals']['idOthers']['bkmrk'][id]["label"]
        output +='%s;https://www.ingress.com/intel?ll=%s&z=18&pll=%s;0\n' % (portalname, gpscoords, gpscoords)
    if output:
        if output_file:
            with codecs.open(output_file, 'wb', encoding='utf-8') as f_output:
                f_output.write(output)
        else:
            sys.stdout.write(output)
