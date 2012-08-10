# coding=UTF-8
from binaryio import readString, readInt, readByte

boardPath = './'

# ----
# Load a RPG Toolkit board file.
# -
# Notes:	Currently only works with files in format version 2.4 (the most recent,
# 			I believe)
#			
#			Any commented properties are relevant to pre-2.4 board files.
#			
#			Only supports the tiles themselves so far, no shading, isometrics, etc.
# ----
def load(brdFileName):
	global boardPath

	brdFile = open(boardPath + brdFileName, 'rb')

	# Load the board file headers:
	board = dict()
	board['filename'] = brdFileName
	board['header'] = readString(brdFile)
	board['version_major'] = readInt(brdFile)
	board['version_minor'] = readInt(brdFile)
	board['version'] = float(str(board['version_major']) + '.' + str(board['version_minor']))
	
	if board['version_major'] != 2:
		print 'Cannot open board files older than 2.4'
		exit()

	if board['version_minor'] < 4:
		print 'Cannot open board files older than 2.4'
		exit()

	#board['registered'] = False if readInt(brdFile) == 0 else True
	#board['registeredString'] = readString(brdFile)
	board['width'] = readInt(brdFile)
	board['height'] = readInt(brdFile)
	board['layers'] = readInt(brdFile)
	board['coordinateType'] = readInt(brdFile)

	#board['startX'] = readInt(brdFile)
	#board['startY'] = readInt(brdFile)
	#board['startLayer'] = readInt(brdFile)
	#board['saveDisabled'] = False if readInt(brdFile) == 0 else True
	board['tilesetCount'] = readInt(brdFile)
	board['tilesets'] = []

	# Load all of the references to tiles within tilesets used by this board:
	for tilesetIndex in range(board['tilesetCount']-1):
		tileset = readString(brdFile)
		board['tilesets'].append(tileset)

	# I have no idea why (yet), but I always have to load an extra 30 bytes
	# from the file in order to find the beginning of the tile data
	for hax in range(15):
		readInt(brdFile)


	# Load the tile data from the file:
	board['tileData'] = []
	layer = 0
	skipTiles = 0
	index = 0
	while layer < board['layers']:
		y = 0
		thisLayer = []
		while y < board['height']:
			x = 0
			thisY = []
			while x < board['width']:
				# Handle compression:
				if skipTiles > 0:
					skipTiles -= 1
					thisY.append(index)

				else:
					index = readInt(brdFile)

					if index < 0:
						# If the index is less than zero, the next
						# N tiles are the same. 
						skipTiles = (-index) -1 

						# so we read the next index to get the tile
						# and then use that for skipTiles tiles
						index = readInt(brdFile)
						thisY.append(index)

					else:
						# Otherwise, just add the tile index
						# and move on
						thisY.append(index)

				x += 1
			y += 1
			thisLayer.append(thisY)
		layer += 1
		board['tileData'].append(thisLayer)

	# !!! Returning the board here, as the rest of the file format is not
	#		properly supported yet.
	return board
	#Shading goes here
	board['backgroundImage'] = readString(brdFile)
	board['DEPRECATED_foregroundImage'] = readString(brdFile)
	board['DEPRECATED_borderBackgroundImage'] = readString(brdFile)
	board['backgroundColor'] = readLong(brdFile)
	board['DEPRECATED_borderColor'] = readLong(brdFile)
	board['effect'] = readInt(brdFile)

	board['directionalLinks'] = []
	for i in range(3):
		board['directionalLinks'].append(readString(brdFile))

	board['battleSkill'] = readInt(brdFile)
	board['battleBackground'] = readString(brdFile)
	board['battleAllowed'] = bool(readInt(brdFile))
	board['DEPRECATED_dayNight'] = readInt(brdFile)
	board['DEPRECATED_battleNight'] = readInt(brdFile)
	board['DEPRECATED_battleNightSkill'] = readInt(brdFile)
	board['DEPRECATED_battleNightBackground'] = readString(brdFile)

	board['constants'] = []
	for i in range(9):
		board['constants'].append(str(readInt(brdFile)))

	board['backgroundMusic'] = readString(brdFile)


	board['layerTitles'] = []
	for i in range(7):
		board['layerTitles'].append(readString(brdFile))

	board['programCount'] = readInt(brdFile)
	board['programs'] = []
	for i in range(board['programCount'] -1):
		thisProgram = {}
		thisProgram['filename'] = readString(brdFile)
		thisProgram['x'] = readInt(brdFile)
		thisProgram['y'] = readInt(brdFile)
		thisProgram['layer'] = readInt(brdFile)
		thisProgram['graphic'] = readString(brdFile)
		thisProgram['activation'] = readInt(brdFile)
		thisProgram['initialVariable'] = readString(brdFile)
		thisProgram['finalVariable'] = readstring(brdFile)
		thisProgram['initialValue'] = readString(brdFile)
		thisProgram['finalValue'] = readString(brdFile)
		thisProgram['activationType'] = readInt(brdFile)
		board['programs'].append(thisProgram)

	board['enterProgram'] = readString(brdFile)
	board['DEPRECATED_backgroundProgram'] = readString(brdFile)

	board['itemCount'] = readInt(brdFile)
	board['items'] = []
	for i in range(board['itemCount'] -1):
		thisItem = {}
		thisItem['filename'] = readString(brdFile)
		thisItem['x'] = readInt(brdFile)
		thisItem['y'] = readInt(brdFile)
		thisItem['layer'] = readInt(brdFile)
		thisItem['activation'] = readInt(brdFile)
		thisItem['initialVariable'] = readString(brdFile)
		thisItem['finalVariable'] = readString(brdFile)
		thisItem['initialValue'] = readString(brdFile)
		thisItem['finalValue'] = readString(brdFile)
		thisItem['activationType'] = readInt(brdFile)
		thisItem['activationProgram'] = readString(brdFile)
		thisItem['multitaskProgram'] = readString(brdFile)
		board['items'].append(thisItem)

	if board['version_minor'] >= 3:
		board['threadCount'] = readLong(brdFile)
		board['threads'] = []
		for i in range(board['threadCount'] -1):
			board['threads'].append(readString(brdFile))
	
	brdFile.close()
	return board
