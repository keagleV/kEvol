from random import randint
from random import uniform

class RecombinationFunction:

	'''
		This class, defines the recombination functions available to be
		used for the evolutionary algorithm.

	'''

	def __init__ (self,recombFunctionName="spc"):

		self.functionName=recombFunctionName;

		


	def get_recomb_func(self):
		'''
			This function returns the selection function to be used.

		'''


		if self.functionName.lower()=="spc":
			return self.single_point_crossover

		elif self.functionName.lower()=="uc":
			return self.uniform_crossover
		
		return None



	def single_point_crossover(self,parentPairs,solutionSize,recombProb):
		'''
			This function implements the single point crossover recombination function.

		'''

		newGeneration=[]


		# This list contains those parents that did not
		parentsNotMated=[]

		for pair in parentPairs:


			# For each pair, based on the recombintion probabilty, we decide
			# whether to recombine or not.


			# I have used round(), since it would make the randomness much possible.
			if round(uniform(0,1),1) == recombProb:


				# Excluding  parent members from the pairs which each pair is with 
				# form of (member,fitness)
				parent1=pair[0][0]
				parent2=pair[1][0]


				# Choosing a random point to break the solutions into two parts.
				crossOverPoint=randint(1,solutionSize-1)

				


				# Creating new childs out of the parents and appeding them to
				# the newGeneration. 

				# Important Note: New childs are only members that are being added.
				# In other words, we are adding tuples of (member,fitness)

				newGeneration.append(parent1[:crossOverPoint]+parent2[crossOverPoint:])

				newGeneration.append(parent2[:crossOverPoint]+parent1[crossOverPoint:])



			else:
				# In this case we would not recombine the parent pairs and so we
				# add them without chaning to the newGeneration.


				#TODO
				# Important Node: Adding the parents would be done as a tuple of
				# (member,fitness) since it makes the evaluation of the new generation
				# much more efficient because there if no necc ??????????????


				parentsNotMated.append(pair[0])
				parentsNotMated.append(pair[1])



				



		# returning newGeneration which is our new generation of childs
		return parentsNotMated,newGeneration



	def uniform_crossover(self,parentPairs,solutionSize,recombProb):
		'''
			This function implements the uniform crossover recombination function.
		'''


		newGeneration=[]


		# This list contains those parents that did not
		parentsNotMated=[]

		for pair in parentPairs:


			# For each pair, based on the recombintion probabilty, we decide
			# whether to recombine or not.


			# I have used round(), since it would make the randomness much possible.
			if round(uniform(0,1),1) == recombProb:


				# Excluding  parent members from the pairs which each pair is with 
				# form of (member,fitness)
				parent1=pair[0][0]
				parent2=pair[1][0]

				child1=[]
				child2=[]

				for i in range(len(parent1)):

					# If the random number is 1 then we assign the gene to
					# the first child,otherwise, we assign it to the second child.
					if randint(1,2)==1:
						child1.append(parent1[i])

						# Adding the corresponding gene in parent2 to the child2
						child2.append(parent2[i])

					else:

						child2.append(parent1[i])

						# Adding the corresponding gene in parent2 to the child1
						child1.append(parent2[i])



				# Adding the new childs to the the newGeneration
				newGeneration.append(child1)
				newGeneration.append(child2)




			else:
				# In this case we would not recombine the parent pairs and so we
				# add them without chaning to the newGeneration.


				#TODO
				# Important Node: Adding the parents would be done as a tuple of
				# (member,fitness) since it makes the evaluation of the new generation
				# much more efficient because there if no necc ??????????????


				parentsNotMated.append(pair[0])
				parentsNotMated.append(pair[1])



				



		# returning newGeneration which is our new generation of childs
		return parentsNotMated,newGeneration

