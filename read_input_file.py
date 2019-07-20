def read_input_file(input_file_path):
	"""
	this function reads the input_file and returs a dictionary in the fallowing format
	{
	"C": [[{width's map}, {lenght's map}]],
	"M": [[{y of mountain 0}, {x of mountain 1}], ..., [{y of mountain i}, {x of mountain i}]],
	"T": [[{nb fo treasures 0}, {y of treasures 0}, {x of treasures 1}], ..., 
		  [{nb fo treasures i}, {y of treasures i}, {x of treasures i}]]
	"A": []
	}
	"""
	with open(input_file_path, "r") as f: inputData = f.read()
	# this function build a Dict of all elements of the game
	lines = inputData.split("\n")
	#print("lines\n", lines)
	elementsDict = {"C": [], "M": [], "T": [], "A": []}
	for line in lines:
		lineSplit = line.split("\u200b")
		elemType = lineSplit[0]
		if elemType in ["C", "M", "T"]:
			elemData = lineSplit[1].split(" - ")[1:]
			elemData = [int(e) for e in elemData]
			if elemType == "C":
				elementsDict[elemType] = elemData
			else:
				elementsDict[elemType].append(elemData)
		elif elemType == "A":
			elemData = lineSplit[1].split("-")[1:]
			elementsDict[elemType].append(elemData)

	return elementsDict


if __name__ == "__main__":
	input_file_path = "/Users/charles/Workspace/carbone-it-exos/entry_file.txt"
	elements = read_input_file(input_file_path)
	print(elements)
