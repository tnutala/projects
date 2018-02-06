# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 13:06:50 2017

@author: tnuta
"""
import urllib

url= "https://pypi.python.org/pypi"

handle = urllib.request.urlopen(url)

html_gunk =  handle.read()

print(html_gunk)

