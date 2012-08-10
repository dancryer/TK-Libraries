# coding=UTF-8
import os, sys, pygame
import formats.tileset as tileset
import renderers.tilesetRenderer as renderer


# Tell the tileset format loader which path to use for loading tilesets:
tileset.tilePath = os.path.realpath('../testFiles/tiles/') + '/'

# Load the tileset file:
testBoard = tileset.load('RPGMaker951.tst')

# Initialise pygame:
pygame.init()

# Render the tileset:
renderer.render(testBoard)

# Pygame event loop:
clock = pygame.time.Clock()

while True:
	clock.tick(60)
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			sys.exit(0)
