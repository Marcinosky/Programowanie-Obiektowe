class SortedList:

	def __init__(self, given_list: list = [], *, given_key: str = None):
		if(given_list == [] and given_key == None):
			self.elements = []
			self.key = None
		elif(given_list != [] and given_key == None):
			self.elements = given_list
			self.elements.sort()
			self.key = None
		elif(given_list == [] and given_key != None):
			self.elements = []
			self.key = given_key
		else:
			self.elements = given_list
			self.key = given_key
			self.elements.sort(key=given_key)			# nie wiem jak zaimplementować klucz we własnych funkcjach

	def elements(self):
		return self._elements

	def key(self):
		return self.key	

	def clear(self):
		self.elements = []

	def _find_index(self, x, low, high):				# wyszukuje indeks szukanego elementu
		if high >= low:									# algorytmem wyszukiwania binarnego ale
			mid = low + (high - low)//2					# nie wiem jak wykorzystać to do dodawania
			if self.elements[mid] == x:
				return mid
			elif self.elements[mid] > x:
				return self._find_index(x, low, mid-1)
			else:
				return self._find_index(x, mid + 1, high)
		else:
			return None

	def add(self, added):								# add prostszą metodą
		self.elements.append(1)
		for i in range(len(self.elements)-1,0,-1):
			self.elements[i] = added
			if(self.elements[i-1] < added):
				break
			self.elements[i] = self.elements[i-1]	

	def pop(self):
		return self.elements.pop()

	def remove(self,value):
		self.elements.remove(value)

	def remove_every(self,value):
		for i in range(len(self.elements),0,-1):
			if(self.elements[i-1] == value):
				self.elements.remove(value)
				if(self.elements[i-2] != value):
					break

	def __delitem__(self, i):
		if(i>len(self.elements)-1 or i<0):
			return print("Index out of range")
		else:
			self.elements.remove(self.elements[i])

	def __getitem__(self, i):
		if(i>len(self.elements)-1):
			return print("Index out of range")
		else:
			return self.elements[i]

	def __setitem__(self, i, value):
		if(i>len(self.elements)-1 or i<0):
			return print("Index out of range")
		elif(i==len(self.elements)-1):
			if(value<self.elements[i]):
				return print("Value not sorted")
			else:
				self.elements[i] = value
		elif(i==0):
			if(value>self.elements[i+1]):
				return print("Value not sorted")
			else:
				self.elements[i] = value
		elif(value>self.elements[i+1] or value<self.elements[i-1]):
			return print("Value not sorted")
		else:
			self.elements[i] = value

	def __iter__(self):
		self.n = self.elements[0]
		self.ind = 0
		return self

	def __next__(self):
		result = self.n
		if self.ind < len(self.elements):
			self.ind += 1
			self.n += self.elements[self.ind]
			return result
		else:
			raise StopIteration

	def __reversed__(self):
		templist = []
		for i in range(len(self.elements)-1, -1, -1):
			templist.append(self.elements[i])
		return templist

	def __contains__(self, item):
		is_contained = False
		for element in self.elements:
			if element == item:
				is_contained = True
				break
		return is_contained

	def __len__(self):
		length = 0
		for _ in self.elements:
			length += 1
		return length

	def __str__(self):
		return f"{self.elements}"

	def copy(self):
		self.__copy__()

	def __copy__(self):
		return SortedList(self.elements, given_key=self.key)

	def extend(self, iterable):
		for item in iterable:
			self.elements.append(item)

	def count(self, counted):
		occurrences = 0
		for item in self.elements:
			if item == counted:
				occurrences += 1
		return occurrences

	def index(self, searched):
		for i in range(0, len(self.elements)):
			if searched == self.elements[i]:
				return i
		return None
