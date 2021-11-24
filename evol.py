#!/usr/bin/python3.8



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
import argparse

from os import path


from config import EvolSearchConfig

from fitness import FitnessFunction

from selection import SelectionFunction

from recombination import RecombinationFunction

from bitflapping import BitFlappingFunction


class EvolSearch:

	'''
		This class implements the evolution search algorithm.

	'''

	def __init__ (self):
		
		# Evolutionary search config file
		# self.evolConfig=None
		
		# Fitness function to be used
		self.fitnessFunction=None


		# Selection function to be used
		self.selectionFunction=None


		# Recombination function to be used
		self.recombinationFunction=None


		# Bit flapping function to be used
		self.bitFlappingFunction=None


		# Config file path
		self.cfgFile=None

		# Holds the configuration objects to be executed
		self.listOfConfigurations=list()


		# error codes dictionary
		self.errorCodes={
		'NO_CONFIG_FOUND': "No Config File Found",
		'NO_FITNESS_FUNCTION_FOUND':"Fitness Function Not Defined Yet",
		'NO_SELECTION_FUNCTION_FOUND':"Selection Function Not Defined Yet",
		'NO_RECOMBINATION_FUNCTION_FOUND': "Recombination Function Not Defined Yet",
		'NO_BIT_FLAPPING_FUNCTION_FOUND':"Bit Flapping Function Not Defined Yet",
		'EVOLUTION_MAX_LEVEL_REACHED': "Evoltion Maximum Level Reached",
		'BEST_SOLUTION_FOUND':"Best Solution Has Been Found",
		'PREPARING_REPORT': "The Algorithm Report Is Being Prepared",
		'NO_CFG_FILE_PROVIDED': "No Config File Specified Or Config File Does Not Exist",

		'RUNNING_PREDEFINED':'Running Pre-Defined Configuration',
		'CONFIG_OBJECTS_CREATED': 'Configuration Objects Have Been Created For The Algorithm',
		'EVOL_ALGO_STARTED':'Evolutionary Algorithm Has Been Started...\n'

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




	def parse_evol_config(self,config):
		'''
			This function checks for the config file.
		'''

		# if self.evolConfig is None:
		# 	self.evol_search_log(0,self.errorCodes['NO_CONFIG_FOUND'])

		# 	#TODO can we dynamically create this in evaluate_generation function?
		# else:
		self.fitnessFunction=FitnessFunction(config.fitnessFunc).getFitnessFunc()
			

		# 	# check whether the fitness function was returned or not
		# 	if self.fitnessFunction is None:
		# 		self.evol_search_log(0,self.errorCodes['NO_FITNESS_FUNCTION_FOUND'])
				
		# 		exit(1)


		self.selectionFunction=SelectionFunction(config.selectAlgo).get_selection_func()


			# # check whether the selection function was returned or not
			# if self.selectionFunction is None:
			# 	self.evol_search_log(0,self.errorCodes['NO_SELECTION_FUNCTION_FOUND'])
				
			# 	exit(1)


		self.recombinationFunction=RecombinationFunction(config.recombineAlgo).get_recomb_func()


			# # check whether the recombination function was returned or not
			# if self.recombinationFunction is None:
			# 	self.evol_search_log(0,self.errorCodes['NO_RECOMBINATION_FUNCTION_FOUND'])
				
			# 	exit(1)



		self.bitFlappingFunction=BitFlappingFunction(config.bitFlappingAlgo).get_bitflap_func()

			# # check whether the bit flapping function was returned or not
			# if self.bitFlappingFunction is None:
			# 	self.evol_search_log(0,self.errorCodes['NO_BIT_FLAPPING_FUNCTION_FOUND'])
				
			# 	exit(1)




	def generate_init_pop(self,config):
		'''
			This function generates the inital population.

			The size of the population is defined by the parameter'popSize'
			of the config object and the size of the solution is defined
			by the paramter 'problemSize' of the config object.
		'''


		populationList=[]


		for i in range(config.popSize):

			populationList.append(choices([0,1],weights=[1,1],k=config.problemSize))


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




	def should_b_terminated(self,maxGenEvol,generation,config):


		'''
			This function checks whether the evolution process should be
			terminated or not.

		'''

		# Check the maxEvolCnt in the config object. 

		if config.maxGenEvol==maxGenEvol:
			self.evol_search_log(1,self.errorCodes["EVOLUTION_MAX_LEVEL_REACHED"])
			return 1


		# check for the best solution which is a string of all 1s like:  11.....111.
		# The number of 1s is defined by the 'problemSize' parameter.

		# Remind that member in this loop, is a tuple of (member,fitnessValue)
		for member in generation:
			if member[0]==[1]*(config.problemSize):
				self.evol_search_log(1,self.errorCodes["BEST_SOLUTION_FOUND"])

				self.evol_search_log(1,self.errorCodes["PREPARING_REPORT"])

				return 1


		return 0



	def start_evol(self):
		'''
			This function starts the evolution process
		
		'''
		
		self.evol_search_log(1,self.errorCodes["EVOL_ALGO_STARTED"])




		for config in self.listOfConfigurations:




			
			#TODO 
			# check the config file first.
			self.parse_evol_config(config)



		
			# generate the initial population for the first generation
			initPopulation = self.generate_init_pop(config)


			# evaluate the the initial population
			currGeneration=self.evaluate_generation(initPopulation)




			# defines the number of loop execution
			maxGenEvol=0

		

			while not self.should_b_terminated(maxGenEvol,currGeneration,config):



				

				# Selecting parents from the current generation
				parentsPool=self.selectionFunction(currGeneration)


				# Shuffling the parentsPool
				shuffle(parentsPool)



				#TODO do we need further probability to select pairs?


				# Selecting elements of the parentsPool 2 by 2.
				parentPairs=[(parentsPool[0],parentsPool[1]) for i in range(0,len(parentsPool),2) ]




				# Performing recombination on the parent pairs
				parentsNotMated,offSprings=self.recombinationFunction(parentPairs,config.problemSize,config.combProb)



				# Performing bit flapping on the childs
				self.bitFlappingFunction(offSprings,config.problemSize,config.mutProb)

				

				# Evaluating the offSprings
				evaluatedOffspring=self.evaluate_generation(offSprings)




				# Mixing the offsprings with parents that were'nt mated in this step as
				# the current generation
				
				currGeneration=[*parentsNotMated,*evaluatedOffspring]
					

				# decrement the maxGenEvol 
				maxGenEvol+=1


			# print(currGeneration)	



	def evol_algo_argument_reader(self):

		'''
			This function implements the command line argument reader
		'''


		parser = argparse.ArgumentParser(description='Evolutionary Algorithm Help')

		parser.add_argument('-f','--file',  type=str, nargs=1,help='Specify A Config File Name')


		args = parser.parse_args()


		self.listOfConfigurations=[]

		if args.file:
			if (args.file)[0].endswith("config.cfg") and path.exists(args.file[0]):
				self.cfgFile=args.file[0]


				# Reading the file
				fhandle=open((args.file)[0])

				fileLines=fhandle.readlines()

				fhandle.close()


				for line in fileLines:

					line=line.strip().split(',')


					# Setting the parameters to be passed to the config object
					

					# Since some paramters are represented by '-' in the config.cfg,
					# we have to skip these parameters and let the config class decide
					# the value.


					configParams=['problemSize','popSize','combProb','mutProb',
									'selectAlgo','recombineAlgo','bitFlappingAlgo',
									'fitnessFunction','maxGenEvol']


					# Zipping parameter names with their corresponding value
					# in the config.cfg line
					paramTuple=tuple(zip(configParams,line))



					# Eliminating those parameters that their value has been set to
					# '-'

					# Create a lambda function converter that checks whthere we have to use float()
					# or not. The main reason is the numeric values in config.cfg is string
					# and cannot be used to create a config object.
					lambConv=lambda num: num if not num.isnumeric() else ( int(num) if (num.isnumeric() and float(num).is_integer()) else float(num) )


					paramDict = dict((x, lambConv(y)) for x, y in paramTuple if  y!='-')

			

					self.listOfConfigurations.append(EvolSearchConfig(**paramDict))



				self.evol_search_log(1,self.errorCodes['CONFIG_OBJECTS_CREATED'])





		
		if self.cfgFile is None:
			self.evol_search_log(1,self.errorCodes['NO_CFG_FILE_PROVIDED'])
			self.evol_search_log(1,self.errorCodes['RUNNING_PREDEFINED'])

			self.listOfConfigurations.append(EvolSearchConfig(popSize=100,problemSize=20))







# evolConfig=EvolSearchConfig(popSize=10,selectAlgo='fitprop',problemSize=4,recombineAlgo='uc',fitnessFunction="trap",bitFlappingAlgo="bfp")

# evolConfig=EvolSearchConfig(popSize=100,problemSize=20)




evolObj=EvolSearch()


evolObj.evol_algo_argument_reader()


evolObj.start_evol()

# tup = (("11", 4),)
# print(tup)

# dct = dict((y, x) for x, y in tup)
# print(dct)