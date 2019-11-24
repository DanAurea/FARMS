class Analyzer(object):

	def __init__(self):
		pass

	def analyze(self):
		pass

	def show(self):
		instructions 		=	[("vld1", 2), ("vmull.s16", 1), ("vaddw.s16",1), ("vaddw.s16",1), ("vqrshrun.s32",1), ("vst1",2)]
		ncycles		 		=	0
		total_latency 		=	0
		total_throughput	=	0

		print("Cycles" + "\t"*2 + "Execution throughput" + "\t"*2 + "Instruction")
		for instruction in instructions:
			print(str(instruction[1]) + "\t"*7 + instruction[0])
		print("Total latency: " + str(total_latency))
		print("Total throughput: " + str(total_throughput))

analyzer = Analyzer()
analyzer.show()