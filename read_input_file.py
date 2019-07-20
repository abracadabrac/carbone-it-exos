def read_input_file(input_file_path):
	"""
	this function reads the input_file and returs a dictionary in the fallowing format
	{
	"C": [{<width's map>}, {<lenght's map>}],
	"M": [[<y0>, <x1>], ..., [<yi>, <xi>]],
	"T": [[<y0>, <x1>], ..., [<yi>, <xi>]], 	# coords are duplicated if multiple treasures are present on it
	"A": [{	'name': <name>, 
			'coords': [<y>, <x>], 
			'orientation': <N or W or E or S>, 
			'moves': <ex: 'AADADAGGA'>
		  }]
	}
	"""
	with open(input_file_path, "r") as f: inputData = f.read()
	lines = inputData.split("\n")

	elementsDict = {"C": [], "M": [], "T": [], "A": []}

	for line in lines:
		lineSplit = line.split("\u200b")
		elemType = lineSplit[0]
		if elemType in ["C", "M", "T"]:
			elemData = lineSplit[1].split(" - ")[1:]
			elemData = [int(e) for e in elemData]
			if elemType == "C":
				elementsDict["C"] = elemData
			elif elemType == "M":
				elementsDict["M"].append(elemData)
			elif  elemType == "T":
				for treasure in range(elemData[2]):
					elementsDict["T"].append(elemData[:2])

		elif elemType == "A":
			elemData = lineSplit[1].split("-")[1:]
			elementsDict[elemType].append({
					"name": elemData[0],
					"coords": elemData[1:3],
					"orientation": elemData[3],
					"moves": elemData[4]
				}
			)

	return elementsDict


if __name__ == "__main__":
	input_file_path = "/Users/charles/Workspace/carbone-it-exos/entry_file.txt"
	elements = read_input_file(input_file_path)
	print(elements)
