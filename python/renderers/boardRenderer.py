# coding=UTF-8
import pygame
import formats.tileset as tileset
import renderers.tilesetRenderer as renderer

tilePath	= './'

# ----
# Render a board using pygame:
# ----
def render(board):
	global tilePath
	tileset.tilePath = tilePath

	windowX = board['width'] * 32
	windowY = board['height'] * 32

	window = pygame.display.set_mode((windowX, windowY)) 
	pygame.display.set_caption(board['filename'] + ' - ' + str(board['width']) + 'x' + str(board['height'])) 
	screen = pygame.display.get_surface() 
	screen.fill((0,0,0))
	offsetX = 0
	offsetY = 0

	tilesets = dict()

	x = 0
	y = 0

	renderedTiles = 0
	for layer in board['tileData']:
		for yData in layer:
			for xData in yData:
				tile = xData
				
				if tile > 0 and tile < len(board['tilesets']) and board['tilesets'][tile] != '':
					data = getTileData(board['tilesets'][tile])

					if data != False:
						if data['file'] not in tilesets.keys():
							tilesets[data['file']] = tileset.load(data['file'])

						renderer.renderTile(screen, tilesets[data['file']], data['tile'] - 1, x*32, y*32)
						renderedTiles += 1
				x += 1

			y += 1
			x = 0
		y = 0
		x = 0

	pygame.display.update()

# ----
# Get the tileset name and tile index from a tileset lookup table value
# ----
def getTileData(tileRef):
	index = tileRef.find('.tst')

	# TODO: add support for .tan files:
	if index == -1:
		return False

	index += 4

	return {'file': tileRef[:index], 'tile': int(tileRef[index:])}