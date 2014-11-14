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
    f_output = codecs.open(output_file, 'wb')

with codecs.open(input_file,'r', encoding='utf-8') as f_input:

    d = json.load(f_input)
    
    for id in d['portals']['idOthers']['bkmrk']:
        gpscoords=d['portals']['idOthers']['bkmrk'][id]["latlng"]
        portalname=d['portals']['idOthers']['bkmrk'][id]["label"].replace(",","")
        str = '%s;https://www.ingress.com/intel?ll=%s&z=18&pll=%s;0\n' % (portalname, gpscoords, gpscoords)
        if output_file != '':
            str = str.encode('utf-8')
            f_output.write(str)
        else:
            if sys.version_info < (3, 0):
                str = str.encode('utf-8')
            sys.stdout.write(str)

f_input.close()
if output_file != '':
    f_output.close()
