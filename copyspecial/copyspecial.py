#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

# Extract the names of the special files
def special_files(dir):
	cmd = 'ls ' + dir
	(stat, out) = commands.getstatusoutput(cmd)
	if stat:
		print 'Please enter a valid directory name'
		sys.exit(0)
	strs = re.findall(r'\S+__\S+__\.\S+', out)
	return strs

# Creating the absolute paths
def gen_path(strs, dir1):
	fpath = []
	for filename in strs:
		path = os.path.join(dir1, filename)
		ab_path = os.path.abspath(path)
		fpath.append(ab_path)
	return fpath	


def to_zip(fnames, tozip):
	for name in fnames:
		cmd = 'zip -j ' +  tozip + ' ' + name
		(stat, out) = commands.getstatusoutput(cmd)
		if stat:
			print 'Please enter a valid destination name', stat
			sys.exit(0)

# Copying the file to a diff directory
def to_dir(fnames, todir):
	if not os.path.isdir(todir):
		cmd = 'mkdir ' + todir
		(stat, out) = commands.getstatusoutput(cmd)
	for name in fnames:
		cmd = 'cp ' +  name + ' ' + todir
		(stat, out) = commands.getstatusoutput(cmd)
		if stat:
			print 'Please enter a valid destination name', stat
			sys.exit(0)
	

def main():
	# This basic command line argument parsing code is provided.
	# Add code to call your functions below.
	# Make a list of command line arguments, omitting the [0] element
	# which is the script itself.
	args = sys.argv[1:]
	if not args:
		print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
		sys.exit(1)
	# todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
	
	todir = ''
	if args[0] == '--todir':
		todir = args[1]
		del args[0:2]
	
	tozip = ''
	if args[0] == '--tozip':
		tozip = args[1]
		del args[0:2]
	
	if len(args) == 0:
		print "error: must specify one or more dirs"
		sys.exit(1)
	
	# +++your code here+++
	# Call your functions
	
	dir_name = args[0]
	list_strs = special_files(dir_name)
	list_abs_fname = gen_path(list_strs, dir_name)
	
	if tozip:
		to_zip(list_abs_fname, tozip)
	if todir:
		to_dir(list_abs_fname, todir)
  
if __name__ == "__main__":
  main()
