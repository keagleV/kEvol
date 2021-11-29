from random import choices

from random import randint



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

		if totalFiteness ==0:
			# Set the total fitness to 1 to avoid zero division. The
			# value of 1 does not matter anymore, since in this algorithm
			# we are dividing each fitness value by total fitness. Since, each
			# fitness value is a non-negative number, if the total fitness is 0, 
			# we can deduce that each one was 0.
			totalFiteness=1




		# Calculate the fitness proportion for each member of the population
		fitnessProp=[ member[1]/totalFiteness for member in generation ]

		## In the case that all the probabilites are zero, we assign 1 to each
		# so we can use python's choices in the process of selecting. In this case
		# all the members have same weight to be selected.
		if fitnessProp == [0]*len(generation):
			fitnessProp=[1]*len(generation)


		# In the next step we have to select members of the generation based
		# on the fitnessProp list. For that we use choices function from python's 
		# random libraray. The output should be a (len(generation))-member list.

		return choices(generation,weights=fitnessProp,k=len(generation))




	def bin_tournament(self,generation):
		'''
			This function implements the binary tournament selection function.
		'''

		# New Generation to be returned
		newGeneration=[]


		# First define the size of the next generation.
		# The size of the next generation is the size of the current generation.

		nextGenerationSize=len(generation);

		for i in range(nextGenerationSize):

			# Choosing a random number which indicates the index of the memeber of
			# the generation to be selected.
			randNum=randint(0,nextGenerationSize-1)

			newGeneration.append(generation[randNum])



		return newGeneration

		
