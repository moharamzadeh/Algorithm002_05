# aya character amalvand ast?
def isAmalvand(char):
	symbol = ['+', '-', '*', '/', '^', '(', ')']
	return not char in symbol

# aya mitavan yek character ra be entehaye yek reshteh ezafeh kard, tori ke sharayet infix bodan bargharar bashad?
def appendShodan(listInfix, char):
	amalgar = ['^','*','/','+','-']

	# list khali
	if not listInfix:
		if char == '(' or isAmalvand(char):
			return True
		return False

	# list khali nist
	else:
		lastCharInfix = listInfix[-1]

		# akharin char dar infix ra ba shartha barresi mikonim
		if lastCharInfix == '(':
			if isAmalvand(char) or char == '(':
				return True
			return False
		elif lastCharInfix == ')':
			if char in amalgar or (char == ')' and listInfix.count('(') > listInfix.count(')')): # agar tedad '(' bishtar bod mitavan ')' ezafeh kard
				return True
			return False
		elif isAmalvand(lastCharInfix):
			if char in amalgar:
				return True
			if char == ')' and listInfix.count('(') > listInfix.count(')'): # agar tedad '(' bishtar bod mitavan ')' ezafeh kard
				return True
			return False

		# last_char_infix: amalgar
		else:
			if char == '(' or isAmalvand(char):
				return True
			return False

# aya parantezha dar reshteh barabar hastand?
def __equalParantez(string):
	if string.count('(') == string.count(')'):
		return True
	return False

# aya reshteh infix ast?
def isInfix(string):
	# tabdil reshteh be list
	if isinstance(string, str):
		stringInfix = string
		string = []
		for i in stringInfix:
			string.append(i)

	# agar reshteh khali bashad ya tedad '(' ba ')' barabar nabashad, infix nist
	if (not string) or (not __equalParantez(string)):
		return False
	
	# akharin makan parantezbaz ya amalgar
	index_last_parantezbaz_amalgar = -1
	# akharin makan amalvan
	index_last_amalvand = -1

	# peymayesh andis dar reshteh
	for index in range(len(string)):
		# meghdar dehi be makan akharin amalgar ,va parantezbaz ya amalgar
		if isAmalvand(string[index]):
			index_last_amalvand = index
		if string[index] in ['+', '-', '*', '/', '^', '(']:
			index_last_parantezbaz_amalgar = index

		# agar hadaghal yeki az char dar reshteh sharayet infix bodan nadasht, pas reshteh infix nist
		if not appendShodan(string[0:index], string[index]):
			return False

	# amalgarha bayad beyn amalvandha bashand
	if index_last_parantezbaz_amalgar > index_last_amalvand:
		return False
	return True