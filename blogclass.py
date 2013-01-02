#!/usr/bin/env python
# encoding: utf-8
"""
WordpressGrab

Created by Max Fitton on 2012-12-16.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""
#in loc tags
import sys
from bs4 import BeautifulSoup

def get_list_of_posts(xml_file):
   list_of_posts = []
   sitemap = open(xml_file)
   soup = BeautifulSoup(sitemap, 'xml')
   for loctag in soup.find_all('loc'):
      list_of_posts.append( loctag.get_text() )
   print list_of_posts
   return list_of_posts
   
def main():
	get_list_of_posts('sitemap.xml')

if __name__ == '__main__':
	main()