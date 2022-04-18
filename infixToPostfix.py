from stack_dataStructure import *
from check_infix import isAmalvand

def __olaviat(amalgar):
	amalgarOlavait = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
	return amalgarOlavait[amalgar]

# aya amalgar mitavanad be stack push shavad?
def __pushShodan(amalgar, stack):
	return stack.isEmpty() or stack.peek() == '(' or __olaviat(stack.peek()) < __olaviat(amalgar)

# print kardan marahel hal
def __printInfixToPostfix(stack, postfix, step):
	print(step, 'stack:\t', stack)
	print('postfix:\t', ''.join(postfix))
	print()

# tabdil ebart mianvadi be pasvandi
def infixToPostfix(infix, printTerminal=False):	
	postfix = []
	stack = Stack()
	step = 1
	
	print('+ infix:', infix)
	print()

	# peymayesh vrodi(infix)
	for char in infix:
		if isAmalvand(char):
			postfix.append(char)

		elif char == '(':
			stack.push(char)

		elif char == ')':
			top = stack.pop()
			while top != '(':
				postfix.append(top)
				top = stack.pop()

		# char: amalgar
		else:
			# ta zamani ke char betavanad dar poshteh push shavad, anasor poshteh ra pop mikonim va dar postfix vared mikonim
			while not __pushShodan(amalgar=char, stack=stack):
				postfix.append(stack.pop())
			stack.push(char)

		# agar meghdar characterha az meghdar moshakhas kamtar bod, chap konad
		if printTerminal is True:
			__printInfixToPostfix(stack, postfix, step)
			step += 1

	# agar poshteh khali nabod, tamam amalgarha ra be akhar postfix ezafeh mikonad
	while not stack.isEmpty():
		postfix.append(stack.pop())

		# agar meghdar characterha az meghdar moshakhas kamtar bod, chap konad
		if printTerminal is True:
			__printInfixToPostfix(stack, postfix, step)
			step += 1

	postfix = ''.join(postfix)
	print('+ postfix:', postfix)
	print('-'*50)
	return postfix