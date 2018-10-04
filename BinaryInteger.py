class BinaryInteger:
	def __init__(self, binaryInt):
		self.bin = [int(d) for d in str(binaryInt)]

	def add(bin_a, bin_b):
		new_bin = [sum(x) for x in zip(bin_a.bin, bin_b.bin)]
		for x in range(len(new_bin)):
			if(new_bin[x] % 2 == 0):
				new_bin[x] = 0
			else:
				new_bin[x] = 1
		str_new = ''.join(str(e) for e in new_bin)
		return BinaryInteger(str_new)

	def multiply(bin_a, bin_b):
		new_bin = [x*y for x, y in zip(bin_a.bin, bin_b.bin)]
		str_new = ''.join(str(e) for e in new_bin)
		return BinaryInteger(str_new)

	def toString(self):
		str1 = ''.join(str(e) for e in self.bin)
		return str1

	def distance_from(self, other):
		difference = [x-y for x, y in zip(self.bin, other.bin)]
		for x in range(len(difference)):
			if (difference[x] == -1):
				difference[x] = 1
		count = 0
		for x in difference:
			count += x
		return count

	def __add__(self, other):
		new_bin = [sum(x) for x in zip(self.bin, other.bin)]
		for x in range(len(new_bin)):
			if(new_bin[x] % 2 == 0):
				new_bin[x] = 0
			else:
				new_bin[x] = 1
		str_new = ''.join(str(e) for e in new_bin)
		return BinaryInteger(str_new)		

	def __mul__(self, other):
		new_bin = [x*y for x, y in zip(self.bin, other.bin)]
		str_new = ''.join(str(e) for e in new_bin)
		return BinaryInteger(str_new)

	def __sub__(self, other):
		difference = [x-y for x, y in zip(self.bin, other.bin)]
		for x in range(len(difference)):
			if (difference[x] == -1):
				difference[x] = 1
		count = 0
		for x in difference:
			count += x
		return count

