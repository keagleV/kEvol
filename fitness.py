from math import prod




class FitnessFunction:

	'''
		This class, defines the fitness functions available to be
		used for the evolutionary algorithm.
	'''

	def __init__ (self,fitnessFunctionName="onemax"):

		self.functionName=fitnessFunctionName;

		


	def getFitnessFunc(self):
		'''
			This function returns the fitness function to be used.

		'''


		if self.functionName.lower()=="onemax":
			return self.oneMax

		elif self.functionName.lower()=="peak":
			return self.peak

		elif self.functionName.lower()=="trap":
			return self.trap

		
		return None



	def oneMax(self,generation):

		#TODO  eliminate the both cases of 

		newGeneration=[]
		for member in generation:
			

			# We encounter list, when we are going to whether evaluate the
			# initial population or the next generation children.

			# This can improve the performace since it does not calculate the fitness
			# for parents that have not maded. Mated parents are in the form of tuple.
			if type(member)==type([]):
				newGeneration.append((member,sum(member)))
			else:
				newGeneration.append(member)  # tuples are added without any calculation


	
	

		return newGeneration

	def peak(self,generation):


		newGeneration=[]
		for member in generation:
			newGeneration.append((member,prod(member)))


		return newGeneration



	def trap(self,generation):

		newGeneration=[]
		for member in generation:
			newGeneration.append((member,3*len(member)*prod(member)-sum(member)))
		

		return newGeneration

