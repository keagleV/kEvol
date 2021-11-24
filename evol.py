#!/bin/python3



'''
> range 1,100 to population
goftan random
math

>> sample estefade nashod bejash choices estefade kardam
'''






from random import sample
from random import shuffle
from itertools import combinations
from random import choices



from config import EvolSearchConfig

from fitness import FitnessFunction

from selection import SelectionFunction

from recombination import RecombinationFunction

from bitflapping import BitFlappingFunction


class EvolSearch:

	'''
		This class implements the evolution search algorithm.

	'''

	def __init__ (self,evolConfig=None):
		
		# Evolutionary search config file
		self.evolConfig=evolConfig
		
		# Fitness function to be used
		self.fitnessFunction=None


		# Selection function to be used
		self.selectionFunction=None


		# Recombination function to be used
		self.recombinationFunction=None


		# Bit flapping function to be used
		self.bitFlappingFunction=None



		# error codes dictionary
		self.errorCodes={
		'NO_CONFIG_FOUND': "No Config File Found",
		'NO_FITNESS_FUNCTION_FOUND':"Fitness Function Not Defined Yet",
		'NO_SELECTION_FUNCTION_FOUND':"Selection Function Not Defined Yet",
		'NO_RECOMBINATION_FUNCTION_FOUND': "Recombination Function Not Defined Yet",
		'NO_BIT_FLAPPING_FUNCTION_FOUND':"Bit Flapping Function Not Defined Yet",
		'EVOLUTION_MAX_LEVEL_REACHED': "Evoltion Maximum Level Reached",
		'BEST_SOLUTION_FOUND':"Best Solution Has Been Found",
		'PREPARING_REPORT': "The Algorithm Report Is Being Prepared"
		}


		# number of generation evolved
		self.genEvolCnt=0



	def evol_search_log(self,status,mess):

		'''
			This function has implemented the algorithm logging 
			process.

			Logging level can be ERR and INF which represent error and
			informative respectively. 

		'''

		loggingLevel='ERR'

		if status==1:
			loggingLevel='INF'

		print("[{0}] {1} ".format(loggingLevel,mess))




	def parse_evol_config(self):
		'''
			This function checks for the config file.
		'''

		if self.evolConfig is None:
			self.evol_search_log(0,self.errorCodes['NO_CONFIG_FOUND'])

			#TODO can we dynamically create this in evaluate_generation function?
		else:
			self.fitnessFunction=FitnessFunction(self.evolConfig.fitnessFunc).getFitnessFunc()
			

			# check whether the fitness function was returned or not
			if self.fitnessFunction is None:
				self.evol_search_log(0,self.errorCodes['NO_FITNESS_FUNCTION_FOUND'])
				
				exit(1)


			self.selectionFunction=SelectionFunction(self.evolConfig.selectAlgo).get_selection_func()


			# check whether the selection function was returned or not
			if self.selectionFunction is None:
				self.evol_search_log(0,self.errorCodes['NO_SELECTION_FUNCTION_FOUND'])
				
				exit(1)


			self.recombinationFunction=RecombinationFunction(self.evolConfig.recombineAlgo).get_recomb_func()


			# check whether the recombination function was returned or not
			if self.recombinationFunction is None:
				self.evol_search_log(0,self.errorCodes['NO_RECOMBINATION_FUNCTION_FOUND'])
				
				exit(1)



			self.bitFlappingFunction=BitFlappingFunction(self.evolConfig.bitFlappingAlgo).get_bitflap_func()

			# check whether the bit flapping function was returned or not
			if self.bitFlappingFunction is None:
				self.evol_search_log(0,self.errorCodes['NO_BIT_FLAPPING_FUNCTION_FOUND'])
				
				exit(1)




	def generate_init_pop(self):
		'''
			This function generates the inital population.

			The size of the population is defined by the parameter'popSize'
			of the config object and the size of the solution is defined
			by the paramter 'problemSize' of the config object.
		'''


		populationList=[]


		for i in range(self.evolConfig.popSize):
			# populationList.append(sample(range(0,2),self.evolConfig.problemSize))

			populationList.append(choices([0,1],weights=[1,1],k=self.evolConfig.problemSize))


		return populationList



	def evaluate_generation(self,generation):

		'''
			This function evaluates the generation by using the fitness function
			defined in the config object.

		'''

		# newGeneration is list of tuples that each tuple is as follows:
		# (member of the generation, fitness value)

		newGeneration=self.fitnessFunction(generation)
		

		return newGeneration




	def create_report(self,generation):
		pass




	def shouldBTerminated(self,maxGenEvol,generation):


		'''
			This function checks whether the evolution process should be
			terminated or not.

		'''

		# Check the maxEvolCnt in the config object. 

		if self.evolConfig.maxGenEvol==maxGenEvol:
			self.evol_search_log(1,self.errorCodes["EVOLUTION_MAX_LEVEL_REACHED"])
			return 1


		# check for the best solution which is a string of all 1s like:  11.....111.
		# The number of 1s is defined by the 'problemSize' parameter.

		# Remind that member in this loop, is a tuple of (member,fitnessValue)
		for member in generation:
			if member[0]==[1]*(self.evolConfig.problemSize):
				self.evol_search_log(1,self.errorCodes["BEST_SOLUTION_FOUND"])

				self.evol_search_log(1,self.errorCodes["PREPARING_REPORT"])

				return 1


		return 0



	def start_evol(self):
		'''
			This function starts the evolution process
		
		'''
		
		# check the config file first.
		self.parse_evol_config()

		
		# generate the initial population for the first generation
		initPopulation = self.generate_init_pop()


		# evaluate the the initial population
		currGeneration=self.evaluate_generation(initPopulation)




		# defines the number of loop execution
		maxGenEvol=0

	

		while not self.shouldBTerminated(maxGenEvol,currGeneration):



			

			# Selecting parents from the current generation
			parentsPool=self.selectionFunction(currGeneration)


			# Shuffling the parentsPool
			shuffle(parentsPool)



			#TODO do we need further probability to select pairs?


			# Selecting elements of the parentsPool 2 by 2.
			parentPairs=[(parentsPool[0],parentsPool[1]) for i in range(0,len(parentsPool),2) ]




			# Performing recombination on the parent pairs
			parentsNotMated,offSprings=self.recombinationFunction(parentPairs,self.evolConfig.problemSize,self.evolConfig.combProb)



			# Performing bit flapping on the childs
			self.bitFlappingFunction(offSprings,self.evolConfig.problemSize,self.evolConfig.mutProb)

			

			# Evaluating the offSprings
			evaluatedOffspring=self.evaluate_generation(offSprings)




			# Mixing the offsprings with parents that were'nt mated in this step as
			# the current generation
			
			currGeneration=[*parentsNotMated,*evaluatedOffspring]
				

			# decrement the maxGenEvol 
			maxGenEvol+=1


		# print(currGeneration)	



		







# evolConfig=EvolSearchConfig(popSize=10,selectAlgo='fitprop',problemSize=4,recombineAlgo='uc',fitnessFunction="trap",bitFlappingAlgo="bfp")

evolConfig=EvolSearchConfig(popSize=100,problemSize=20)



evolObj=EvolSearch(evolConfig)

evolObj.start_evol()


