import numpy as np
from read_input_file import read_input_file
import re


class Map:
	"""this class represent the whole game and simulates its behaviour"""

	def __init__(self, input_file_path, output_file_name):
		"""
		input 	input_file_path: path to the input file
					ex: "/Users/charles/Workspace/carbone-it-exos/entry_file.txt"
				output_file_name: the name given to the output file
					ex: 'output_file.txt'

		atributes	dimensions: in format [<y>, <x>]
					mountainsList: in format [[<y0>, <x1>], ..., [<yi>, <xi>]]
					treasuresList: in format [[<y0>, <x1>], ..., [<yi>, <xi>]], 	
						-> coords are duplicated if multiple treasures are present on the same cell
					adventurersList: in format [{	
													'name': <name>, 
													'coords': [<y>, <x>], 
													'orientation': <N or W or E or S>, 
													'moves': <ex: 'AADADAGGA'>,
													'treasures': <number of treasures collected>
		  										}]
					nbSteps: total number of steps
					mapArray: representation of the map under a numpy array format
					tresuresDict: another representaion of treasures under a dict format 
						-> {<coords>: <nb treasures>}
					
		"""
		elements = read_input_file(input_file_path)

		self.dimensions = elements["C"]
		self.mountainsList = elements["M"]
		self.treasuresList = elements["T"]
		self.adventurersList = elements["A"]
		self.nbSteps = np.max([len(adventurer["moves"]) for adventurer in self.adventurersList])

		self.output_file_name = output_file_name


	@property
	def mapArray(self):
		"""build the array's map representation into self.mapArray"""
		_mapArray = np.chararray((self.dimensions[1], self.dimensions[0]), unicode=True)
		_mapArray[:] = '.'

		for mountainCoord in self.mountainsList:
			_mapArray[mountainCoord[1], mountainCoord[0]] = "M"

		for treasureCoord in self.treasuresList:
			if _mapArray[treasureCoord[1], treasureCoord[0]] == '.':
				_mapArray[treasureCoord[1], treasureCoord[0]] = 1
			else: 
				_mapArray[treasureCoord[1], treasureCoord[0]] =\
				 int(_mapArray[treasureCoord[1], treasureCoord[0]]) + 1

		for adventurer in self.adventurersList:
			adventurerCoords = adventurer["coords"]
			adventurerName = adventurer["name"]
			_mapArray[adventurerCoords[1], adventurerCoords[0]] = adventurerName

		return _mapArray


	@property
	def tresuresDict(self):
		"""
		representation of treasure under the following format
		ex: {'03': 2, '13': 3} -> 2 treasures in [0, 3] and 3 treasures in [1, 3]
		this is usful to build the output file
		"""
		_tresuresDict = {}
		for treasure in self.treasuresList:
			treasureStr = '{0}{1}'.format(treasure[0], treasure[1])
			if treasureStr not in list(_tresuresDict.keys()):
				_tresuresDict[treasureStr] = 1
			else:
				_tresuresDict[treasureStr] += 1

		return _tresuresDict
	


	def runStep(self, numStep):
		"""This function plays one round of the game"""
		for adventurer in self.adventurersList:
			# each adventurer are called one after another
			if numStep < len(adventurer["moves"]):
				coords = adventurer["coords"][:]
				orientation = adventurer["orientation"]
				move =  adventurer["moves"][numStep]

				if move == "A":
					#enter here if adventurer advances
					if orientation == "S":
						coords[1] += 1
					elif orientation == "N":
						coords[1] -= 1
					elif orientation == "E":
						coords[0] += 1
					elif orientation == "W":
						coords[0] -= 1

					if (coords[1] < self.dimensions[1]) & (coords[0] < self.dimensions[0]):
						#make sure the adventurer doesn't leave the map
						if bool(re.search(r'[\d\.]', self.mapArray[coords[1], coords[0]])):
							# enter here if the next cell is aviable (no mountain, no other adventurer)
							if bool(re.search(r'\d', self.mapArray[coords[1], coords[0]])):
								# enter here if adventurer reached a tresure
								self.treasuresList.remove(coords)
								# in this case we remove a corresponing treasure from the map
								adventurer["treasures"] += 1
								# and add it to the adventurer
								
							adventurer["coords"] = coords
							# then we update the adventurer coordinates
							


				if move == "D":
					# enter here if adventurer moves to one's right
					if orientation == "S":
						adventurer["orientation"] = "W"
					elif orientation == "N":
						adventurer["orientation"] = "E"
					elif orientation == "E":
						adventurer["orientation"] = "S"
					elif orientation == "W":
						adventurer["orientation"] = "N"

				if move == "G":
					# enter here if adventurer moves to one's left
					if orientation == "S":
						adventurer["orientation"] = "E"
					elif orientation == "N":
						adventurer["orientation"] = "W"
					elif orientation == "E":
						adventurer["orientation"] = "N"
					elif orientation == "W":
						adventurer["orientation"] = "S"


	def write_exit_file(self):
		"""
		this function build the output file
		"""
		text = 'C - {0} - {1}\n'.format(self.dimensions[0], self.dimensions[1])
		for mountain in self.mountainsList:
			text += 'M - {0} - {1}\n'.format(mountain[0], mountain[1])
		for treasureCoords, n in self.tresuresDict.items():
			text += 'T - {0} - {1} - {2}\n'.format(treasureCoords[0], treasureCoords[1], n)
		for adventurer in self.adventurersList:
			text += 'A - {0} - {1} - {2} - {3} - {4}\n'.format(adventurer['name'], 
				adventurer['coords'][0], 
				adventurer['coords'][1],
				adventurer['orientation'],
				adventurer['treasures'])

		with open(self.output_file_name, 'w') as f:
			f.write(text)


	def runGame(self):
		for numStep in range(self.nbSteps):
			self.runStep(numStep)
		
		self.write_exit_file()



if __name__ == "__main__":
	input_file_path = "/Users/charles/Workspace/carbone-it-exos/entry_file.txt"
	output_file_name = "output_file.txt"
	map = Map(input_file_path, output_file_name)
	map.runGame()

