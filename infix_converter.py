#!/usr/bin/python

operators = {'^':3, '/':2, '*':2, '+':1, '-':1, '(': 0, ')': 0}
operators_keys = operators.keys()

def swap_parenthesis(expression):
	result = ''
	for c in expression:
		if c == '(':
			result += ')'
		elif c == ')':
			result += '('
		else:
			result += c
	return result

def invert_string(expression):
	result = ''
	for i in range(len(expression)-1,-1,-1):
		result += expression[i]
	return result

def infix_to_prefix(expression):
	result = ''
	stack = []
	print ("Infix: %s" % expression)
	expression = swap_parenthesis(expression)
	expression = invert_string(expression)
	for c in expression:
		if c == '(':
			stack.append(c)
		elif c == ')':
			for i in range(0, len(stack)):
				top = stack.pop()
				if top != '(':
					result += top
				else:
					break
		elif c not in operators_keys:
			result += c
		elif c in operators_keys:
			if len(stack) > 0:
				val = operators[c]
				for i in range(0, len(stack)):
					top = stack.pop()
					if operators[top] >= val: # top has higher precedence
						result += top
						if(len(stack) == 0):
							stack.append(c)
					else:
						stack.append(top) # return back value to stack
						stack.append(c)
						break
			else:
				stack.append(c)
	for i in range(0, len(stack)):
		top = stack.pop()
		result += top
	result = invert_string(result)
	print ("Prefix: %s" % result)
	
def infix_to_postfix(expression):
	result = ''
	stack = []
	print ("Infix: %s" % expression)
	for c in expression:
		if c == '(':
			stack.append(c)
		elif c == ')':
			for i in range(0, len(stack)):
				top = stack.pop()
				if top != '(':
					result += top
				else:
					break
		elif c not in operators_keys:
			result += c
		elif c in operators_keys:
			if len(stack) > 0:
				val = operators[c]
				for i in range(0, len(stack)):
					top = stack.pop()
					if operators[top] >= val: # top has higher precedence
						result += top
						if(len(stack) == 0):
							stack.append(c)
					else:
						stack.append(top) # return back value to stack
						stack.append(c)
						break
			else:
				stack.append(c)
	for i in range(0, len(stack)):
		top = stack.pop()
		result += top
	print ("Postfix: %s" % result)
	
infix_to_prefix("(A+B^C)*D+E^5+8-7")
infix_to_postfix("(A+B^C)*D+E^5+8-7")
