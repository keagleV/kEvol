#!/usr/bin/python3.8

import re
import argparse
from os import path
from ast import literal_eval
from itertools import product


class CrCfg:

	'''
		This class has implemented the tools for make all possible configurations,
		out the '.val' file.
	'''

	def __init__ (self):
		

		# Dictionary of regexes which define the rules for parsing the
		# .val file.
		self.matchingRules = {
		'populationSize': ['''\s*popSize\s*=\s*\[\s*([1-9]*[02468])(\s*,\s*([1-9]*[02468]))*\s*\]\s*''',0],
		'problemSize': ['''\s*probSize\s*=\s*\[\s*([1-9]+[0-9]*)(\s*,\s*([1-9]+[0-9]*))*\s*\]\s*''',0],
		'recombinationProb': ['''\s*recombProb\s*=\s*\[\s*((?!0+(?:\.0+)?$)\d?\d(?:\.\d\d*)?)(\s*,\s*((?!0+(?:\.0+)?$)\d?\d(?:\.\d\d*)?))*\s*\]\s*''',0],
		'mutationProb': ['''\s*mutProb\s*=\s*\[\s*((?!0+(?:\.0+)?$)\d?\d(?:\.\d\d*)?)(\s*,\s*((?!0+(?:\.0+)?$)\d?\d(?:\.\d\d*)?))*\s*\]\s*''',0],
		'selectionAlgo': ['''\s*selAlgo\s*=\s*\[\s*(fitprop|bintour)\s*\]\s*''',0],
		'recombAlgo': ['''\s*recombAlgo\s*=\s*\[\s*(spc|uc)\s*\]\s*''',0],
		'maxGenEvolve': ['''\s*maxGenEvol\s*=\s*\[\s*[1-9][0-9]*\s*\]\s*''',0],
		'fitnessFunction': ['''\s*fitnessAlgo\s*=\s*\[\s*(onemax|trap|peak)(\s*,\s*(onemax|trap|peak))*\s*\]\s*''',0],
		'bitFlappingAlgo': ['''\s*bitFlapAlgo\s*=\s*\[\s*(bfp)\s*\]\s*''',0]
		}


		# Dictionary of error codes for the program
		self.errorCodes={
		'NO_VAL_FILE_PROVIDED':'.val File Has Not Been Provided Or Found',
		'RULE_MULTI_DEFINITION': 'Multiple Definition Of Rule Has Been Detected On Line ',
		'RULE_NOT_CLEAR': 'Rule Has Not Been Defined Yet On Line ',
		'CONFIG_FILE_EXISTS': 'config.cfg Already Exists, Overwrite It? ',
		'NO_CONFIG_CREATED': "No Config File Corrupted Or Created",
		'CONFIG_FILE_CREATED': "Config File config.cfg Has Been Created"
		}

		# This variable holds the address of the .val file
		self.valFile=None



		# Lists below are going to store the values defined in
		# the .val file for each parameter.
		self.allCombinations=list()


		self.populationSizes=list()
		self.problemSizes=list()
		self.recombProbs=list()
		self.mutProbs=list()
		self.selAlgos=list()
		self.recombAlgos=list()
		self.maxGenEvols=list()
		self.fitnessFuncs=list()
		self.bitFlapAlgos=list()



	def crcfg_logging(self,status,mess):

		'''
			This function implements the configuration file generator logger.
		'''

		if status:
			print("[INF] {0}".format(mess))
		else:
			print("[ERR] {0}".format(mess))


	def argument_reader(self):

		'''
			This function implements the command line argument reader
		'''


		parser = argparse.ArgumentParser(description='Create Configuration File Help')

		parser.add_argument('-f','--file',  type=str, nargs=1,help='Specify A Value File Name')


		args = parser.parse_args()


		if args.file:
			if (args.file)[0].endswith(".val") and path.exists(args.file[0]):
				self.valFile=args.file[0]
		
		if self.valFile is None:
			self.crcfg_logging(0,self.errorCodes['NO_VAL_FILE_PROVIDED'])

			exit(1)


	def write_new_configurations(self):
		'''
			This function will write the new configurations to a config.cfg file. If file
			exists, then it will ask for the overwriting.
		'''


		if path.exists("config.cfg"):
			self.crcfg_logging(1,self.errorCodes['CONFIG_FILE_EXISTS'])

			userAnswer=str()

			while True:
				userAnswer=input("Overwrite?[y/n] ")
				if userAnswer.lower() in 'no n':

					self.crcfg_logging(1,self.errorCodes['NO_CONFIG_CREATED'])

					exit(0)
				elif userAnswer.lower() in 'y ye yes':

					break


		# Creating new file called config.cfg
		fhandle=open("config.cfg",'w')

		for combination in self.allCombinations:
				
				fhandle.write(','.join([str(f) for f in combination]) + '\n')


		fhandle.close()

		self.crcfg_logging(1,self.errorCodes['CONFIG_FILE_CREATED'])




	def parse_val_file(self):

		'''
			This function implements the parser of the .val file.


			*: This parser is a mini and light parser based on the regexes.
		'''

		
		fhandl=open(self.valFile)

		fileLines=fhandl.readlines()

		fhandl.close()


		for i in range(len(fileLines)):

			line=fileLines[i].strip()

			# Skip lines that are empty
			if not line or line.startswith('#'):
				continue

			else:
				if re.match(self.matchingRules['populationSize'][0],line):
					if self.matchingRules['populationSize'][1]==0: #TODO Bug on the state that we say popSize=[15] odd number

						listVals=re.search('\s*\[\s*([1-9]*[02468])(\s*,\s*([1-9]*[02468]))*\s*\]\s*',line).group(0)


						self.populationSizes=literal_eval(listVals)



						# Set its definition to 1
						self.matchingRules['populationSize'][1]=1
					else:
						# Multiple definition of this rule

						self.crcfg_logging(0,self.errorCodes['RULE_MULTI_DEFINITION']+str(i+1))
						exit(1)


				elif re.match(self.matchingRules['problemSize'][0],line):
					if self.matchingRules['problemSize'][1]==0: #TODO Bug on the state that we say popSize=[15] odd number

						listVals=re.search('\s*\[\s*([1-9]+[0-9]*)(\s*,\s*([1-9]+[0-9]*))*\s*\]\s*',line).group(0)

						
						self.problemSizes=literal_eval(listVals)



						# Set its definition to 1
						self.matchingRules['problemSize'][1]=1
					else:
						# Multiple definition of this rule

						self.crcfg_logging(0,self.errorCodes['RULE_MULTI_DEFINITION']+str(i+1))
						exit(1)

				
				elif re.match(self.matchingRules['recombinationProb'][0],line):
					if self.matchingRules['recombinationProb'][1]==0: #TODO Bug on the state that we say popSize=[15] odd number


						listVals=re.search('\s*\[\s*((?!0+(?:\.0+)?$)\d?\d(?:\.\d\d*)?)(\s*,\s*((?!0+(?:\.0+)?$)\d?\d(?:\.\d\d*)?))*\s*\]\s*',line).group(0)

						
						self.recombProbs=literal_eval(listVals)




						# Set its definition to 1
						self.matchingRules['recombinationProb'][1]=1
					else:
						# Multiple definition of this rule

						self.crcfg_logging(0,self.errorCodes['RULE_MULTI_DEFINITION']+str(i+1))
						exit(1)


				elif re.match(self.matchingRules['mutationProb'][0],line):
					if self.matchingRules['mutationProb'][1]==0: #TODO Bug on the state that we say popSize=[15] odd number


						listVals=re.search('\s*\[\s*((?!0+(?:\.0+)?$)\d?\d(?:\.\d\d*)?)(\s*,\s*((?!0+(?:\.0+)?$)\d?\d(?:\.\d\d*)?))*\s*\]\s*',line).group(0)

						
						self.mutProbs=literal_eval(listVals)


						# Set its definition to 1
						self.matchingRules['mutationProb'][1]=1
					else:
						# Multiple definition of this rule

						self.crcfg_logging(0,self.errorCodes['RULE_MULTI_DEFINITION']+str(i+1))
						exit(1)


				elif re.match(self.matchingRules['selectionAlgo'][0],line):
					if self.matchingRules['selectionAlgo'][1]==0: #TODO Bug on the state that we say popSize=[15] odd number

						listVals=re.search('\s*\[\s*(fitprop|bintour)\s*\]\s*',line).group(0)

						listVals=re.sub(r'([a-zA-Z]+)',r'"\1"',listVals)

						self.selAlgos=literal_eval(listVals)


						print(self.selAlgos)

						# Set its definition to 1
						self.matchingRules['selectionAlgo'][1]=1
					else:
						# Multiple definition of this rule

						self.crcfg_logging(0,self.errorCode['RULE_MULTI_DEFINITION']+str(i+1))
						exit(1)

				
				elif re.match(self.matchingRules['recombAlgo'][0],line):
					if self.matchingRules['recombAlgo'][1]==0: #TODO Bug on the state that we say popSize=[15] odd number

						listVals=re.search('\s*\[\s*(spc|uc)\s*\]\s*',line).group(0)


						listVals=re.sub(r'([a-zA-Z]+)',r'"\1"',listVals)


						self.recombAlgos=literal_eval(listVals)

						print(self.recombAlgos)

						# Set its definition to 1
						self.matchingRules['recombAlgo'][1]=1
					else:
						# Multiple definition of this rule

						self.crcfg_logging(0,self.errorCodes['RULE_MULTI_DEFINITION']+str(i+1))
						exit(1)

				
				elif re.match(self.matchingRules['maxGenEvolve'][0],line):
					if self.matchingRules['maxGenEvolve'][1]==0: #TODO Bug on the state that we say popSize=[15] odd number

						listVals=re.search('\s*\[\s*[1-9][0-9]*\s*\]\s*',line).group(0)


						self.maxGenEvols=literal_eval(listVals)

						print(self.maxGenEvols)

						# Set its definition to 1
						self.matchingRules['maxGenEvolve'][1]=1
					else:
						# Multiple definition of this rule

						self.crcfg_logging(0,self.errorCodes['RULE_MULTI_DEFINITION']+str(i+1))
						exit(1)

				
				elif re.match(self.matchingRules['fitnessFunction'][0],line):
					if self.matchingRules['fitnessFunction'][1]==0: #TODO Bug on the state that we say popSize=[15] odd number

						listVals=re.search('\s*\[\s*(onemax|trap|peak)(\s*,\s*(onemax|trap|peak))*\s*\]\s*',line).group(0)

						listVals=re.sub(r'([a-zA-Z]+)',r'"\1"',listVals)


						self.fitnessFuncs=literal_eval(listVals)

						print(self.fitnessFuncs)


						

						# Set its definition to 1
						self.matchingRules['fitnessFunction'][1]=1
					else:
						# Multiple definition of this rule

						self.crcfg_logging(0,self.errorCodes['RULE_MULTI_DEFINITION']+str(i+1))
						exit(1)

				
				elif re.match(self.matchingRules['bitFlappingAlgo'][0],line):
					if self.matchingRules['bitFlappingAlgo'][1]==0: #TODO Bug on the state that we say popSize=[15] odd number

						listVals=re.search('\s*\[\s*(bfp)\s*\]\s*',line).group(0)

						listVals=re.sub(r'([a-zA-Z]+)',r'"\1"',listVals)


						self.bitFlapAlgos=literal_eval(listVals)

						print(self.bitFlapAlgos)



						# Set its definition to 1
						self.matchingRules['bitFlappingAlgo'][1]=1
					else:
						# Multiple definition of this rule

						self.crcfg_logging(0,self.errorCodes['RULE_MULTI_DEFINITION']+str(i+1))
						exit(1)

						
				else:
					self.crcfg_logging(0,self.errorCode['RULE_NOT_CLEAR']+str(i+1))
					exit(1)


		# Now its time to combine all the lists and possible combinations

		# Checking for emptiness and fill with '-' to denote default
		if len(self.populationSizes)==0:
			self.populationSizes.append('-')

		if len(self.problemSizes)==0:
			self.problemSizes.append('-')

		if len(self.recombProbs)==0:
			self.recombProbs.append('-')

		if len(self.mutProbs)==0:
			self.mutProbs.append('-')

		if len(self.selAlgos)==0:
			self.selAlgos.append('-')

		if len(self.recombAlgos)==0:
			self.recombAlgos.append('-')

		if len(self.maxGenEvols)==0:
			self.maxGenEvols.append('-')

		if len(self.fitnessFuncs)==0:
			self.fitnessFuncs.append('-')

		if len(self.bitFlapAlgos)==0:
			self.bitFlapAlgos.append('-')


		self.allCombinations=list(product(self.problemSizes,
		self.populationSizes,
		self.recombProbs,
		self.mutProbs,
		self.selAlgos,
		self.recombAlgos,
		self.bitFlapAlgos,
		self.fitnessFuncs,
		self.maxGenEvols,
			))


		# Calling write function
		self.write_new_configurations()


crcfObj=CrCfg()

crcfObj.argument_reader()

crcfObj.parse_val_file()


