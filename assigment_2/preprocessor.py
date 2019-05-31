#!/usr/bin/python
import re

include_glb = re.compile("^#include <.+>$")
include_lcl = re.compile("^#include \".+\"$")

file = open("class2.c", "r+")
for line in file:
	print (line)
	find = include_glb.findall(line)
	print (find)
	find = include_lcl.findall(line)
	print (find)

file.close()