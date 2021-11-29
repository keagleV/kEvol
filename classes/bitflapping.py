from random	 import random




class BitFlappingFunction:

	'''
		This class, defines the bit flapping functions available to be
		used for the evolutionary algorithm.

	'''
	# bfp: bit flapp with probabilty
	def __init__ (self,bitFlapFunctionName="bfp"):

		self.functionName=bitFlapFunctionName;

		


	def get_bitflap_func(self):
		'''
			This function returns the selection function to be used.

		'''


		if self.functionName.lower()=="bfp":
			return self.bit_flapping_probability

		
		return None



	def bit_flapping_probability(self,childs,solutionSize,bitFlappingProb):
		'''
			This function implements the bit flapping with probabilty function.

		'''

		for child in childs:


			# Going through each bit
			for i in range(solutionSize):


				# I have used round(), since it would make the randomness much possible.
				if round(random(),1) == bitFlappingProb:
					
					# flipping the bit
					child[i]=child[i] | 1



	