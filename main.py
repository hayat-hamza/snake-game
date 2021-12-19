import pygame
#imports usefal golbal vars to use in events
from pygame.locals import *
import time
#a func used to drow the bolck to use it at moving

class Snake:
	def __init__(self,parent_screen,direction="right"):
		self.direction=direction
		self.parent_screen=parent_screen
		#load image from computer
		self.block=pygame.image.load("resources/block.jpg")
		#blit used to drow in window
		self.x=100
		self.y=100

	def draw(self):
		#we put fill here se that the prev block is cleared 
		self.parent_screen.fill((47, 163, 92))
		self.parent_screen.blit(self.block,(self.x,self.y))
		pygame.display.flip()

	def set_direction_left(self):
		self.direction="left"
		return self.direction
		
	def set_direction_right(self):
		self.direction="right"
		return self.direction

	def set_direction_up(self):
		self.direction="up"
		return self.direction

	def set_direction_down(self):
		self.direction="down"
		return self.direction


	def move(self,direction):
		if self.direction=="right":
			self.x+=10

		if self.direction=="left":
			self.x-=10
		if self.direction=="up":
			self.y-=10

		if self.direction=="down":
			self.y+=10


class Game:
	def __init__(self):
		pygame.init()	#initalize whole module
		#set mode inittialize game window
		#500 and 500 are dimentions
		#used slef to be able to call surface later with objects
		self.surface=pygame.display.set_mode((500,500))
		#flip is necessary to display the color
		self.surface.fill((47, 163, 92))
		self.direction="right"
		self.snake=Snake(self.surface,self.direction)	#because a game has a snake in it
		self.snake.draw()

	def run(self):
		running=True

		#while tp keep it always running instead of timer
		#pygame offers different types of events
		while running:
			for event in pygame.event.get():
				#keydown means the keyboard is pressed
				if event.type==KEYDOWN:
					if event.key==K_ESCAPE:
						running=False
					if event.key==K_UP:
						self.snake.direction=self.snake.set_direction_up()
					if event.key==K_DOWN:
						self.snake.direction=self.snake.set_direction_down()
					if event.key==K_RIGHT:
						self.snake.direction=direction=self.snake.set_direction_right()
					if event.key==K_LEFT:
						self.snake.direction=self.snake.set_direction_left()


				#close the window
				elif event.type==QUIT:
					running=False

			self.snake.move(self.snake.direction)
			self.snake.draw()
			time.sleep(0.2)


if __name__=="__main__":
	game=Game()	#created object game from class Game
	game.run()




