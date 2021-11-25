from statistics import mean
from statistics import pstdev


class EvolAlgoExecReport:
	'''
		This class implements each evolutionary algorithm's configuration's
		execution report.
	'''

	def __init__(self):

		# Exection index
		self.execIndex=int()

		# Best fitness for the exection
		self.bestFitness=int()

		# Execution state
		self.execState=str()

		# Fitness function execution count
		self.fitnessFuncCount=int()





	def set_exec_state(self,state):
		'''
			This function sets the state of the current execution
		'''
		self.execState=state


	def get_exec_state(self):
		'''
			This funcion returns the execution state of this execution
		'''
		return self.execState


	def set_exec_index(self,index):
		'''
			This function sets the execution index of the configuration

		'''
		self.execIndex=index


	def set_best_fitness(self,bestFitness):
		'''
			This function sets the execution best fitness of the current 
			execution of the configuration

		'''
		self.bestFitness=bestFitness


	def get_exec_bfitness(self):
		'''
			This funcion returns the best fitness of this execution
		'''
		return self.bestFitness


	def set_fitness_func_call_count(self,callCount):
		'''
			This function sets the number of fitness function calls
		'''

		self.fitnessFuncCount=callCount


	def get_fitness_func_call_count(self):
		'''
			This function returns the number of times the fitness function was
			called.
		'''
		return self.fitnessFuncCount




class EvolAlgoConfigReport:
	'''
		This class implements each evolutionary algorithm configuration's report.
	'''


	def __init__(self,evolConfig):

		# The config that we are producing report for
		self.config=evolConfig


		# Configuration index
		self.configIndex=int()


		# Total number of the execution of the configuration
		self.numOfExecution=int()


		# List of all the execution's report of the configuration
		self.execReports=list()

		# Mean value of the fitnesses of the configuration
		self.meanValue=int()

		# Standard deviation of the fitnesses of the configuration
		self.standDev=int()

		# Mean value of the fitness function execution for each configuration
		self.meanValueFF=int()

		# Standard deviation of the fitnesses function calls
		self.standDevFF=int()

		# This holds the fitness values of all the execution of this configuration.
		# It is used for optimization for calculating the standard deviation. Since
		# we have listed the fitnesses in mean calculation, we can prevenet to 
		# create such a list again for calculating the standard deviation.
		self.listOfFitnesses=list()

		# Holds the index of execution which had the best fitness value
		self.bestExecutionIndex=int()

		# Holds the best fitness value of the executions
		self.bestExecutionFitness=-1


	def get_report_config(self):
		'''
			This function returns the config object itself
		'''
		return self.config


	def execution_increment(self):

		'''
			This function increments the number of execution for the configuration

		'''

		self.numOfExecution+=1

	
	
	def add_execution_report(self,execReport):

		'''
			This function will add the execution report of the configuration to list
			of all the exec reports
		'''

		self.execReports.append(execReport)


		# Check for the best execution fitness
		if execReport.bestFitness > self.bestExecutionFitness:

			# Updating the best fitness value
			self.bestExecutionFitness = execReport.bestFitness 
			
			# Updating the index of the best fitness value's execution
			self.bestExecutionIndex=self.numOfExecution   # +1 is because the indexes are 0-based
	
	
	def set_config_index(self,index):
		'''
			This function sets the configuration index.
		'''

		self.configIndex=index




	def calculate_statistic_values(self):
		'''
			This function calculates the statistical values
		'''
		listOfFitnesses=[execObj.bestFitness for execObj in self.execReports]
		
		
		self.meanValue=mean(listOfFitnesses)


		self.standDev=pstdev(listOfFitnesses)


		# Statistical values for the fitness function call count

		listOfFFCalls=[execObj.fitnessFuncCount for execObj in self.execReports]



		self.meanValueFF=mean(listOfFFCalls)


		self.standDevFF=pstdev(listOfFFCalls)
	


	def get_exec_reports(self):
		'''
			This function returns the execution reports of this configuration
		'''
		return self.execReports