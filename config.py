


class EvolSearchConfig:

	'''
		This class, defines the necessary parameters' configurations
		for the evolutionary algorithm

	'''

	def __init__(self, problemSize=1 , 
						popSize =1 ,
						combProb =1 ,
						mutProb =1 ,
						selectAlgo="fitprop",
						recombineAlgo="spc",
						bitFlappingAlgo='bfp',
						fitnessFunction="trap",
						maxGenEvol=300):

		# defines the solutions length
		self.problemSize= problemSize

		# defines the population size
		self.popSize= popSize

		# defines the probability of combining two parents
		self.combProb=combProb

		# defines the probability that a child gets mutated
		self.mutProb=mutProb

		# defines the selection algorithm to be used 
		self.selectAlgo=selectAlgo

		# defines the recombination algorithm to be used
		self.recombineAlgo=recombineAlgo

		# defines the fitness function to be used
		self.fitnessFunc=fitnessFunction

		# defines the number of generations to be evolved in the 
		# evolutionary algorithm
		self.maxGenEvol=maxGenEvol


		self.bitFlappingAlgo=bitFlappingAlgo



# class MultiEvolSearchConfig:

# 	'''
# 		This class, defines the multi config feature.
		
# 		This class has methods to a read a config.cfg file and produce a list
# 		of config objects.

# 	'''

# 	def __init__(self):


# 		# defines the solutions length
# 		self.problemSize= problemSize

# 		# defines the population size
# 		self.popSize= popSize

# 		# defines the probability of combining two parents
# 		self.combProb=combProb

# 		# defines the probability that a child gets mutated
# 		self.mutProb=mutProb

# 		# defines the selection algorithm to be used 
# 		self.selectAlgo=selectAlgo

# 		# defines the recombination algorithm to be used
# 		self.recombineAlgo=recombineAlgo

# 		# defines the fitness function to be used
# 		self.fitnessFunc=fitnessFunction

# 		# defines the number of generations to be evolved in the 
# 		# evolutionary algorithm
# 		self.maxGenEvol=maxGenEvol


# 		self.bitFlappingAlgo=bitFlappingAlgo