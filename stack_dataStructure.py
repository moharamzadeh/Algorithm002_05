class Stack():
	def __init__(self):
		self.__items = []

	# ezafe kardan item be poshteh
	def push(self, data):
		self.__items.append(data)

	# hazf kardan akharin item az poshteh va brgrdandan on
	def pop(self):
		if not self.isEmpty():
			return self.__items.pop()
		else:
			raise IndexError('stack is empty')

	# check kardan khali bodan poshteh
	def isEmpty(self):
		if len(self.__items) == 0:
			return True
		else:
			return False

	# brgrdandan balatrin item poshteh
	def peek(self):
		if not self.isEmpty():
			return self.__items[-1]
		else:
			raise IndexError('stack is empty')

	# barayeh print kardan poshteh, self.__items ra be reshteh tabdil mikonad va barmigardanad
	def __str__(self):
		return ' '.join(self.__items)