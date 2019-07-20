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
		self.build_mapArray()


	def build_mapArray(self):
		"""build the array's map representation into self.mapArray"""
		self.mapArray = np.chararray((self.dimensions[1], self.dimensions[0]), unicode=True)
		self.mapArray[:] = '.'

		for mountainCoord in self.mountainsList:
			self.mapArray[mountainCoord[1], mountainCoord[0]] = "M"

		for treasure in self.TreasuresList:
			treasureCoord = treasure[0:2]
			treasureNb = treasure[1]
			self.mapArray[treasureCoord[1], treasureCoord[0]] = str(treasureNb)



if __name__ == "__main__":
	input_file_path = "/Users/charles/Workspace/carbone-it-exos/entry_file.txt"
	map = Map(input_file_path)
	print(map.mapArray)
