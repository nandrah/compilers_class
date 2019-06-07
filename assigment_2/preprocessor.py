#!/usr/bin/python

new_file = open("class2_modified.c", "w+") 
var_dict = {}
inside_if = False
inside_else = False
if_condition = False
else_condition = False

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

def replace_var(text):
	for var in var_dict:
		i = text.find(var)
		if i > -1: # It was found
			text = text.replace(var, var_dict[var])
	return text
		
def find_var(line):
	out_of_string = ""
	new_line = ""
	inside_of_string = False
	if "\"" in line:
		for c in line[:]:
			if c != "\"":
				out_of_string = out_of_string + c
			else:
				if not inside_of_string: # First "
					inside_of_string = True
					out_of_string = replace_var(out_of_string)
					new_line = new_line + out_of_string
					out_of_string = "\""
				else: 					 # Last "
					inside_of_string = False
					new_line = new_line + out_of_string + "\""
					out_of_string = ""
		if out_of_string:
			out_of_string = replace_var(out_of_string)
			new_line = new_line + out_of_string
	else:
		new_line = replace_var(line)
	return new_line

with open("class2.c", "r") as fd:
	archivo = fd.readlines()
	
for i, line in enumerate(archivo, start=1):
	line = line.rstrip() # removing trailing space
	#print ("line: %s" % line)
	if line.startswith("#include "):
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
			print ("Error: Wrong #include sintax at line %d: \n \t %s" % (i, line)) 
	
	elif line.startswith("#define "):
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
	
	elif line.startswith("#if "):
		inside_if = True
		if_var = ""
		if_value = ""
		for idx, c in enumerate(line[4:], start=4):
			if (c != ' ' and c != '='):
				if_var = if_var + c
			else:
				break
		if line[idx+2] == ' ':
			idx = idx + 3
		else:
			idx = idx + 2
		for c in line[idx:]:
			if_value = if_value + c
			
		try:
			if var_dict[if_var] == if_value:
				if_condition = True
		except KeyError:
			print ("Undefined variable: %s at line %d" % (if_var, i))
	
	elif line == "#else":
		if inside_if:
			inside_else = True
			inside_if = False
			if not if_condition:
				else_condition = True
		else:
			print("Error: No if, not else expected")
			
	
	elif line == "#endif":
		if (inside_if or inside_else):
			inside_if = False
			inside_else = False
	
	elif line.startswith("#undef "):
		var = line[7:]
		try:
			var_dict.pop(var)
		except KeyError:
			print ("Undefined variable: %s at line %d" % (var, i))
			
	elif line.startswith("//") or not line: # Checks for comments or empty lines
		new_file.write(line + "\n")
	
	elif not line.startswith("#"):
		if (not inside_if and not inside_else):
			line = find_var(line)
			new_file.write(line + "\n")
		else:
			if (inside_if and if_condition):
				line = find_var(line)
				new_file.write(line + "\n")
			elif (inside_else and else_condition):
				line = find_var(line)
				new_file.write(line + "\n")
			else:
				continue
fd.close()
new_file.close()
