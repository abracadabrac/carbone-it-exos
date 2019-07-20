import numpy as np
from read_input_file import read_input_file
import re


class Map:
	"""this class represent the map"""
	def __init__(self, input_file_path):
		"""
		input 	input_file_path: path to the input file
					ex: "/Users/charles/Workspace/carbone-it-exos/entry_file.txt"
					
		"""
		elements = read_input_file(input_file_path)

		self.dimensions = elements["C"]
		self.mountainsList = elements["M"]
		self.treasuresList = elements["T"]
		self.adventurersList = elements["A"]
		self.nbSteps = np.max([len(adventurer["moves"]) for adventurer in self.adventurersList])


	@property
	def _mapArray(self):
		"""build the array's map representation into self.mapArray"""
		mapArray = np.chararray((self.dimensions[1], self.dimensions[0]), unicode=True)
		mapArray[:] = '.'

		for mountainCoord in self.mountainsList:
			mapArray[mountainCoord[1], mountainCoord[0]] = "M"

		for treasureCoord in self.treasuresList:
			if mapArray[treasureCoord[1], treasureCoord[0]] == '.':
				mapArray[treasureCoord[1], treasureCoord[0]] = 1
			else: 
				mapArray[treasureCoord[1], treasureCoord[0]] =\
				 int(mapArray[treasureCoord[1], treasureCoord[0]]) + 1

		for adventurer in self.adventurersList:
			adventurerCoords = adventurer["coords"]
			adventurerName = adventurer["name"]
			mapArray[adventurerCoords[1], adventurerCoords[0]] = adventurerName

		return mapArray


	def runStep(self, numStep):
		for adventurer in self.adventurersList:
			if numStep < len(adventurer["moves"]):
				coords0 = adventurer["coords"][:]
				coords1 = coords0[:]
				if adventurer["orientation"] == "S":
					coords1[1] += 1
				if adventurer["orientation"] == "N":
					coords1[1] -= 1
				if adventurer["orientation"] == "E":
					coords1[0] += 1
				if adventurer["orientation"] == "W":
					coords1[0] -= 1

				print(self._mapArray[coords1[1], coords1[0]])
				if bool(re.search(self._mapArray[coords1[1], coords1[0]], r'[0123456789\.')):
					# enter here if next step is not a mountain
					adventurer["coords"] = coords1


	def runGame(self):
		for numStep in range(self.nbSteps):
			self.runStep(numStep)



if __name__ == "__main__":
	input_file_path = "/Users/charles/Workspace/carbone-it-exos/entry_file.txt"
	map = Map(input_file_path)
	print(map._mapArray)

	map.runGame()
	print(map._mapArray)
