class Parser(object):

	def __init__(self):
		self.dag 			= {}
		self._instructions 	= []

	def parse(self, filename):
		print("Parsing assembly instructions...")
		with open(filename, "rt") as file:
			instructions = [instruction.rstrip() for instruction in file.readlines()]
			for instruction in instructions:
				self._instructions.append(instruction)
		print("Parsing done.")

	def instructions(self):
		return self._instructions

parser = Parser()
parser.parse("code/unit_test.s")
print(parser.instructions())