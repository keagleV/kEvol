#!/usr/bin/python3


from pandas import  read_csv 
import argparse
from os import path
from matplotlib.pyplot import show
from matplotlib.pyplot import plot




class Reporter:
	'''
		This class has implemented the reporter for the evolutionary
		algorithm.
	'''


	def __init__(self):
		
		# Holds the report file path
		self.reportFile=None

		# Report file handler
		self.rh=None

		# Holds the fitness function used for the evolutionary algorithm
		self.fitnessFunctions=list()


		self.errorCodes={
		'NO_REPORT_FILE_PROVIDED': 'No Report File Provided'

		}



	def reporter_logging(self,status,mess):

		'''
			This function implements the reporter logger.
		'''

		if status:
			print("[INF] {0}".format(mess))
		else:
			print("[ERR] {0}".format(mess))



	def argument_reader(self):

		'''
			This function implements the command line argument reader
		'''


		parser = argparse.ArgumentParser(description='Reporter Help')

		parser.add_argument('-f','--file',  type=str, nargs=1,help='Specify A Report File Name')


		args = parser.parse_args()


		if args.file:
			if (args.file)[0].endswith("report.csv") and path.exists(args.file[0]):
				self.reportFile=args.file[0]
		
		if self.reportFile is None:
			self.reporter_logging(0,self.errorCodes['NO_REPORT_FILE_PROVIDED'])

			exit(1)



	def init_prompt(self):
		'''
			This function prompts a message describing this function.
		'''

		reportStr='''This program is a reporter for the evolutionary algorithm. \n\n[..] This program is a rudimentay and novel reporter which gives some basic analysis and some basic plottings. \n\n'''

		print(reportStr)


	def read_report_file(self):
		'''
			This function reads the report file provided in the command line.
		
		'''
		self.rh=read_csv(self.reportFile)

	def present_general_report(self):


		# Finding the fitness function used in the configuration
		fitnessFunctions=self.rh.fitnessFunction.to_list()

		# Unique this list
		self.fitnessFunctions=list(set(fitnessFunctions))


		print("# Fitness functions: {0}".format(str(len(self.fitnessFunctions))))
		print("--------------------------------------")
		print("Report for each fitness function:\n")

		for ff in self.fitnessFunctions:
			self.present_per_ff_report(ff)


	def present_per_ff_report(self,fitnessFunction):

		'''
			This function represents report for each fitness function
		'''
		filteredByff = (self.rh[self.rh['fitnessFunction'] == fitnessFunction  ])
		# print(filteredByff)
		# TODO finding the best config by sorting.
		# Maximum mean and Minimum standard deviation
		sortedByMeanSd=filteredByff.sort_values(by=["CFG_MEAN","CFG_SD"], ascending=[False,True])


		# Best solution is the first row
		bestSol=sortedByMeanSd.iloc[0]


		# Finding the parameters of the best solution except the fitness function itself
		#TODO eliminate the ff function
		bestsolParams= bestSol.loc['popSize':'maxGenEvol']

		#Now filter the 'filteredByff' dataframe with the prameters we have found
		filteredByParams= filteredByff[ (filteredByff['popSize']== bestsolParams.popSize) &
										(filteredByff['combProb']== bestsolParams.combProb) &
										(filteredByff['mutProb']== bestsolParams.mutProb) &
										(filteredByff['selectAlgo']== bestsolParams.selectAlgo) &
										(filteredByff['bitFlappingAlgo']== bestsolParams.bitFlappingAlgo) &
										(filteredByff['maxGenEvol']== bestsolParams.maxGenEvol) ]

		
		# For algorithm performance
		meanFitnessValues= filteredByParams.CFG_MEAN.to_list()

		sdFitnessValues= filteredByParams.CFG_SD.to_list()

		# For fitness function call count

		meanFitnessCallsValues= filteredByParams.FFC_MEAN.to_list()

		sdFitnessCalssValues= filteredByParams.FFC_SD.to_list()


		problemSizes= filteredByParams.problemSize.to_list()
		
		

		plot(problemSizes,meanFitnessCallsValues)
		plot(problemSizes,sdFitnessCalssValues)


		#TODO figure data

		# plot(problemSizes,meanFitnessValues)
		# plot( problemSizes,sdFitnessValues)

		show()






obj=Reporter()
obj.argument_reader()
obj.init_prompt()
obj.read_report_file()
obj.present_general_report()

# fd=pd.read_csv("report.csv",usecols=["fitnessFunction"])

# ll=(fd.fitnessFunction.to_list())


# print(list(set(ll)))