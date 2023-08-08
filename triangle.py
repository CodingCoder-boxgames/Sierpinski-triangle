from settings import *
import pygame, sys
from random import randint
import random
from time import sleep

class Triangle():
	def __init__(self):
		self.font = pygame.font.Font('ARCADEPI.TTF', 20)
		self.display_screen = pygame.display.get_surface()
		self.cord_A = 0,HEIGTH - 2
		self.cord_B = WIDTH-200 ,0
		self.cord_C = WIDTH,HEIGTH - 2
		self.triangle_points = [self.cord_A,self.cord_B,self.cord_C]
		self.list_x, self.list_y = [200], [300] # x and y of the last dot 
		self.rectangle_list = []
		self.drew_first_point = False
		self.count = 1 # the total point in the triangle in total
		self.start = False

	def draw_points(self):
		self.text1 = self.font.render('Points: ' + str(self.count), True, (0, 255, 0))
		self.text2 = self.font.render('FPS: ' + str(FPS), True, (0, 255, 0))
		self.display_screen.blit(self.text1, self.text1.get_rect(topleft = (10,10)))
		self.display_screen.blit(self.text2, self.text2.get_rect(topleft = (10,30)))

		self.count = len(self.rectangle_list)
		for point in self.rectangle_list:
			pygame.draw.rect(self.display_screen, 'white', point)

	def pick_new_point(self):
		self.random_point = random.choice(self.triangle_points)
		self.mid_x  = (self.random_point[0] + self.list_x[-1])/ 2 
		self.mid_y = (self.random_point[1] + self.list_y[-1])/ 2
		self.list_x.append(self.mid_x)
		self.list_y.append(self.mid_y)
		self.rectangle_list.append(pygame.Rect(self.mid_x, self.mid_y, 2, 2))
		del self.list_x[0], self.list_y[0]
		self.drew_first_point = True
	def input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			self.start = True
		if keys[pygame.K_ESCAPE]:
			self.start = False

	def run(self):
		self.input()
		pygame.draw.polygon(self.display_screen, 'white',
			self.triangle_points, 2)

		self.draw_points()

		if self.start or self.drew_first_point == False:
			self.pick_new_point()

