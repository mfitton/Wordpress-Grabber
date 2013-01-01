#!/usr/bin/env python
# encoding: utf-8
"""
WordpressGrab

Created by Max Fitton on 2012-12-16.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import urllib
import re

class BlogPost:
   '''
   Class that can parse the contents of a wordpress html blog post link and create
   text files with the date of the post, the title, the author, and the text, in
   that order.
   
   Takes a web address to a wordpress blog post for an argument.
     
   '''
	def __init__(self, filename):
	   text = urllib.urlopen(filename).read()
	   
	def get_title(text):
	   '''Gets the post title with regex'''
	   match = re.search(r"<title>\s([ \w]+) &laquo",text)
	   title = match.group(1)
	def get_body(text):
	   '''Gets the post body with regex and removes <p> tags and the like, replacing
	      them with tabs '''
	   match = re.search(r"")
	
	def parse(text):
	   
	

if __name__ == '__main__':
	pass