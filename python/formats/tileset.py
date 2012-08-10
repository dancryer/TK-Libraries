# coding=UTF-8
from binaryio import readUnsignedByte, readInt

tilePath = './'

# ----
# Read a tileset file.
# - 
# Notes:	Only handles a detail level of 1 (RGB, 32x32 tiles)
# ----
def load(tstFileName):
	tstFile = open(tilePath + tstFileName, 'rb')
	
	# Read the tileset header:
	thisTileset = dict()
	thisTileset['filename'] = tstFileName
	thisTileset['version'] = readInt(tstFile)
	thisTileset['count'] = readInt(tstFile)
	thisTileset['detail'] = readInt(tstFile)

	if thisTileset['detail'] != 1:
		print 'Sorry - Cannot read anything other than detail level 1 tilesets'
		return

	thisTileset['tiles'] = []

	for tile in range(thisTileset['count']):
		thisTile = []
		for x in range(32):
			thisX = []
			for y in range(32):
				r = readUnsignedByte(tstFile)
				g = readUnsignedByte(tstFile)
				b = readUnsignedByte(tstFile)

				thisX.append((r,g,b))
			thisTile.append(thisX)

		thisTileset['tiles'].append(thisTile)
	
	tstFile.close()

	return thisTileset