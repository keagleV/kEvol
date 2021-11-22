from random import choices

class SelectionFunction:

	'''
		This class, defines the selection functions available to be
		used for the evolutionary algorithm.

	'''

	def __init__ (self,selectionFunctionName="fitprop"):

		self.functionName=selectionFunctionName;

		


	def get_selection_func(self):
		'''
			This function returns the selection function to be used.

		'''


		if self.functionName.lower()=="fitprop":
			return self.fit_proportionate

		elif self.functionName.lower()=="bintour":
			return self.bin_tournament
		
		return None



	def fit_proportionate(self,generation):
		'''
			This function implements the fitness proportionate selection function.

		'''

		# First calculate the total fitness.
		totalFiteness=sum(member[1] for member in generation)




		# Calculate the fitness proportion for each member of the population
		fitnessProp=[ member[1]/totalFiteness for member in generation ]



		# In the next step we have to select members of the generation based
		# on the fitnessProp list. For that we use choices function from python's 
		# random libraray. The output should be a (len(generation))-member list.

		return choices(generation,weights=fitnessProp,k=len(generation))




	def bin_tournament(self,generation):


		pass
