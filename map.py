import numpy as np
from read_input_file import read_input_file


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
		self.TreasuresList = elements["T"]
		self.adventurersList = elements["A"]

	@property
	def _mapArray(self):
		"""build the array's map representation into self.mapArray"""
		mapArray = np.chararray((self.dimensions[1], self.dimensions[0]), unicode=True)
		mapArray[:] = '.'

		for mountainCoord in self.mountainsList:
			mapArray[mountainCoord[1], mountainCoord[0]] = "M"

		for treasureCoord in self.TreasuresList:
			if mapArray[treasureCoord[1], treasureCoord[0]] == '.':
				mapArray[treasureCoord[1], treasureCoord[0]] = 1
			else: 
				mapArray[treasureCoord[1], treasureCoord[0]] =\
				 int(mapArray[treasureCoord[1], treasureCoord[0]]) + 1

		for adventurer in self.adventurersList:
			adventurerCoords = adventurer["coords"]
			print(adventurerCoords)
			adventurerName = adventurer["name"]
			mapArray[adventurerCoords[1], adventurerCoords[0]] = adventurerName[0]

		return mapArray



if __name__ == "__main__":
	input_file_path = "/Users/charles/Workspace/carbone-it-exos/entry_file.txt"
	map = Map(input_file_path)
	print(map._mapArray)
