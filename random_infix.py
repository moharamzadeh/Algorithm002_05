from check_infix import *
import random
import string

# ijad yek list random az amalgarha va parantezha
def __randomAmalgarParantez(countAmalgar, countParantez):
	listAmalvand = list(string.ascii_uppercase) + list(map(str, list(range(1, 10))))
	listRandomAmalvandParantez = []
	for i in range(countAmalgar):
		listRandomAmalvandParantez.append(random.choice(listAmalvand))
	for i in range(countParantez):
		listRandomAmalvandParantez.append('(')
		listRandomAmalvandParantez.append(')')
	random.shuffle(listRandomAmalvandParantez)
	return listRandomAmalvandParantez

# ijad yek infix random
def randomInfix(countAmalvand):
	infix = []

	# meghdar delkhah barayeh tedad parantezha
	count_prantez = random.randint(0, ((countAmalvand * 2) // 7) + 2)

	listRandomAmalvand = __randomAmalgarParantez(countAmalvand, count_prantez)

	# ta zamani ke amalvand mande, edameh bedeh
	while countAmalvand > 0:
		amalgar = ['^','*','/','+','-']

		# har yek az azayeh list random ra barresi mekonad, aya mitavanad be infix ezafeh shavad ya na
		for symbol in listRandomAmalvand:
			if appendShodan(infix, symbol):
				infix.append(symbol)
				listRandomAmalvand.remove(symbol)
				if isAmalvand(symbol):
					countAmalvand -= 1
					if countAmalvand == 0: # agar hameh amalvandha estefadeh shod, digar amalvandi ezafe nashavad
						break
			else:
				randomOperator = random.choice(amalgar)
				if appendShodan(infix, randomOperator):
					infix.append(randomOperator)

	# agar parantez baz ezafe vojod dasht, be enteha parantez basteh ezafeh kon
	while infix.count('(') > infix.count(')'):
		infix.append(')')

	return ''.join(infix)
