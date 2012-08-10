# coding=UTF-8
import os, sys, pygame
import formats.board as board
import renderers.boardRenderer as renderer

# Tell the board format loader where to look for boards:
board.boardPath = os.path.realpath('../testFiles/boards/') + '/'

# Tell the board renderer which path to use for loading tilesets:
renderer.tilePath = os.path.realpath('../testFiles/tiles/') + '/'

# Load the board file:
testBoard = board.load('modorodar.brd')

# Initialise pygame:
pygame.init()

# Render the board:
renderer.render(testBoard)

# Pygame event loop:
clock = pygame.time.Clock()

while True:
	clock.tick(60)
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			sys.exit(0)
