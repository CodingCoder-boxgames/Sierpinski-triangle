
# import stuff
import pygame, sys
from settings import *
from triangle import Triangle
# ctrl + b to start
class Game:
	def __init__(self):
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption(TITLE) # give title
		self.clock = pygame.time.Clock()
		self.triangle = Triangle() #initialize triangle class
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			pygame.display.update()
			self.screen.fill(BG_COLOUR) # draw background
			self.triangle.run() # run the program

game = Game()
game.run()