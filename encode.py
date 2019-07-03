#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
URI encode an arbitrary string.
'''
import sys
import urllib.parse

print(' '.join([urllib.parse.quote(arg) for arg in sys.argv[1:]]))
