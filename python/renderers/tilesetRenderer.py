# coding=UTF-8
import pygame, sys

tileSurfaces = dict()

def render(tileset):
	windowX = 288
	windowY = (tileset['count']/9)*32

	pygame.init()
	window = pygame.display.set_mode((windowX, windowY)) 
	pygame.display.set_caption(tileset['filename'] + ' - ' + str(tileset['count']) + ' tiles') 
	screen = pygame.display.get_surface() 
	offsetX = 0
	offsetY = 0

	for tileIndex in range(tileset['count']):
		renderTile(screen, tileset, tileIndex, offsetX, offsetY)

		offsetX += 32

		if (offsetX + 32) > windowX:
			offsetX = 0
			offsetY += 32

	pygame.display.update()

	while True:
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				sys.exit(0)

def renderTile(surface, tileset, tileIndex, offsetX, offsetY):
	global tileSurfaces

	if tileset['filename'] not in tileSurfaces:
		tileSurfaces[tileset['filename']] = dict()

	if tileIndex not in tileSurfaces[tileset['filename']]:
		thisTileSurface = pygame.Surface((32, 32))
		tile = tileset['tiles'][tileIndex]
		pixel = 0

		pixelArray = pygame.PixelArray(thisTileSurface)
		x = 0
		y = 0
		for xData in tile:
			for yData in xData:
				pixelArray[x, y] = yData
				y += 1
			x += 1
			y = 0

		tileSurfaces[tileset['filename']][tileIndex] = pixelArray.make_surface()


	surface.blit(tileSurfaces[tileset['filename']][tileIndex], (offsetX, offsetY))