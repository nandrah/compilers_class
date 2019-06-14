#!/usr/bin/python

symbol_table = open("symbol_table.txt", "w+")

pre_proc = {'#' : 'Preprocessor directive'}

operators_1c = { '=' : 'Assignment Operator','+': 'Additon Operator', '-' : 'Substraction Operator', \
				 '/' : 'Division Operator', '*' : 'Multiplication Operator', ';' : 'Semicolon', ',' : 'Comma'}
oprts_1c_keys = operators_1c.keys()
			  
operators_2c = {'++' : 'Increment Operator', '--' : 'Decrement Operator'}

oprts_2c_keys = operators_2c.keys()
			  
comments = {r'//' : 'Single Line Comment',r'/*' : 'Multiline Comment Start', r'*/' : 'Multiline Comment End', '/**/' : 'Empty Multiline comment'}
comms_keys = comments.keys()

datatype = {'int': 'Integer','float' : 'Floating Point', 'char': 'Character','long': 'long int'}
datatype_keys = datatype.keys()

keyword = {'return' : 'return'}
keyword_keys = keyword.keys()

delimiter = {';':'terminator symbol semicolon (;)'}
delimiter_keys = delimiter.keys()

blocks = {'{' : 'Blocked Statement Body Open', '}':'Blocked Statement Body Closed'}
block_keys = blocks.keys()

builtin_functions = {'printf' : 'printf function'}

non_identifiers = ['_','-','+','/','*','`','~','!','@','#','$','%','^','&','*','(',')','=','|','"',':',';','{'
,'}','[',']','<','>','?','/']

parenthesis = {'(' : 'Left parenthesis', ')' : 'Right parenthesis'}
parenthesis_keys = parenthesis.keys()

quotes = {'"' : 'quotes', "'" : "simple quote"}
quotes_keys = quotes.keys()

numerals = ['0','1','2','3','4','5','6','7','8','9','10']

white_space = ' '
l_parenthesis = '('
r_parenthesis = ')'
lexeme = ''
is_data = False
inside_quotes = False
string_tokens = {}
char_tokens = {}
string_in_quotes = ''

string_tokens.update(operators_2c)
string_tokens.update(comments)
string_tokens.update(datatype)
string_tokens.update(keyword)
string_tokens.update(delimiter)
string_tokens.update(builtin_functions)
string_tokens_keys = string_tokens.keys()

char_tokens.update(operators_1c)
char_tokens.update(blocks)
char_tokens.update(parenthesis)
char_tokens_keys = char_tokens.keys()

def is_next_character(string, char):
	string = string.lstrip()
	if string[0] == char:
		return True
	return False
	


with open("class2.c", "r") as fd:
	archivo = fd.readlines()
	
for row, line in enumerate(archivo, start=1):
	#line = line.lstrip() # removing space at the start 
	line = line.rstrip()
	if line.startswith('#'):
		symbol_table.write("%s, %s, %d, %d\n" % (pre_proc['#'], line, row, 1))
		continue
	if line.startswith('/'):
		if line[1] == '/':
			symbol_table.write("%s, %s, %d, %d\n" % ("Single line comment: ", line, row, 1))
			continue
	for col, c in enumerate(line, start=1):
		if not inside_quotes and c not in quotes_keys:
			if c != white_space and c not in char_tokens_keys:
				lexeme += c # adding a char each time
				if lexeme in datatype_keys:
					is_data = True
					symbol_table.write("%s, %s, %d, %d\n" % (datatype[lexeme], lexeme, row, col-len(lexeme)))
					lexeme = ''
				elif (col < len(line)): # if not last character
					if (line[col] == white_space or line[col] in char_tokens_keys) and is_data and (lexeme[0] not in non_identifiers):
						if not is_next_character(line[col:], l_parenthesis):
							symbol_table.write("%s, %s, %d, %d\n" % ("Identifier1", lexeme, row, col-len(lexeme)))
						else:
							symbol_table.write("%s, %s, %d, %d\n" % ("Function name", lexeme, row, col-len(lexeme)))
						lexeme = ''
						is_data = False
					elif line[col] == white_space or line[col] in char_tokens_keys or lexeme in string_tokens_keys:
						if lexeme != '':
							try:
								symbol_table.write("%s, %s, %d, %d\n" % (string_tokens[lexeme], lexeme, row, col-len(lexeme)))
								lexeme = ''
							except KeyError:
								symbol_table.write("%s, %s, %d, %d\n" % ("Identifier2", lexeme, row, col-len(lexeme)))
								lexeme = ''
			elif line[col-1] in char_tokens_keys:
				symbol_table.write("%s, %s, %d, %d\n" % (char_tokens[line[col-1]], line[col-1], row, col))
				lexeme = ''
		elif line[col-1] in quotes_keys:
			if inside_quotes:
				symbol_table.write("%s, %s, %d, %d\n" % ("String in quotes", string_in_quotes, row, col-len(string_in_quotes)))
				string_in_quotes = ''
			symbol_table.write("%s, %s, %d, %d\n" % (quotes[line[col-1]], line[col-1], row, col))
			inside_quotes = not inside_quotes
		else:
			string_in_quotes += c
		
	is_data = False

symbol_table.close()