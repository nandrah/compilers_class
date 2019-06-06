#!/usr/bin/python
import os

def include_file(file_name):
	try:
		f = open(file_name, "r")
		file = f.readlines()
		for line in file:
			new_file.write(line)
		new_file.write("\n") # Make sure there is a newline at the end of file
		f.close()
	except FileNotFoundError:
		print ("Error: File \"%s\" was not found to be included" % (file_name))
		
def find_var(var, idx):
	pass

new_file = open("class2_modified.c", "w+") 

var_dict = {}

with open("class2.c", "r") as fd:
	archivo = fd.readlines()
	
for idx, line in enumerate(archivo, start=1):
	if line.startswith("#include "):
		line = line.rstrip() # removing trailing space
		if ((line[9] == "<" and line[-1] == ">") or 
			(line[9] == "\"" and line[-1] == "\"")):
			name = ""
			for c in line[10:-1]:
				if (c != '/' and c != '\\'):
					name = name + c
				else:
					if c == '/':
						name = name + "//" # escape slash
					else:
						name = name + "\\" # escape slash
			# print ("Name: ", name)
			include_file(name)
		else:
			print ("Error: Wrong #include sintax at line %d: \n \t %s" % (idx, line)) 
	
	elif line.startswith("#define "):
		line = line.rstrip() # removing trailing space
		var_name = ""
		value = ""
		for idx, c in enumerate(line[8:], start=8):
			if c != ' ': # stops when it finds a blank space
				var_name = var_name + c
			else:
				break
		for c in line[idx+1:]:
			value = value + c
		var_dict[var_name] = value
		# print ("[%s] = %s" % (var_name, var_dict[var_name]))
		
fd.close()
new_file.close()
