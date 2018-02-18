#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from glob import glob
from os.path import getmtime
from pystache import render

__author__ = "Sangwhan Moon"
__copyright__ = "Copyright 2018, Sangwhan Moon"
__credits__ = ["Sangwhan Moon"]
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Sangwhan Moon"


files = glob('docs/*.html')
files.sort(key=getmtime)

metadata = []
header = dict(header='<h1><a href="index.html">한글로 배우는 Pytudes</a></h1>')

# Step 1: Aggregate metadata from pre-rendered notebooks.

for filename in files:
    if filename == 'docs/index.html':
        continue

    with open(filename, 'r') as html_file:
        print('Reading metadata from %s' % (filename))
        soup = BeautifulSoup(html_file, "lxml")
        metadata.append(dict(title=soup.find('h1').text[:-1], path=filename.replace('docs/', '')))

# Step 2: Generate index from aggregated metadata.

with open('docs/index.html', 'w') as index_file:
    with open('scripts/template.html', 'r') as template_file:
        template_text = template_file.read()
    
    print('Rendering index file')
    
    patched = render(template_text, { **header, **dict(items=metadata) })
    index_file.write(patched)

# Step 3: Patch up header boilerplate in each notebook file.

for filename in files:
    if filename == 'docs/index.html':
        continue

    with open(filename, 'r') as html_file:
        html_text = html_file.read()
        patched = render(html_text, header)
        
    print('Patching up headers in %s' % (filename))
    
    with open(filename, 'w') as html_file:
        html_file.write(patched)
