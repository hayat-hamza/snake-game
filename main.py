import pygame
#imports usefal golbal vars to use in events
from pygame.locals import *
import time
# imports random
import random

SIZE=40

class Apple:
	def __init__(self,parent_screen):
		self.parent_screen=parent_screen
		self.image=pygame.image.load("resources/apple.jpg")
		self.x=SIZE*3
		self.y=SIZE*3

	def move(self):
		# randint generates a random integar between the first parameter and the second
		
		self.x=random.randint(1,19)*SIZE
		self.y=random.randint(1,14)*SIZE




	def draw(self):
		#we put fill here se that the prev block is cleared 
		self.parent_screen.blit(self.image,(self.x,self.y))
		pygame.display.flip()

class Snake:
	def __init__(self,parent_screen,length,direction="right"):
		self.direction=direction
		self.length=length
		self.parent_screen=parent_screen
		#load image from computer
		self.block=pygame.image.load("resources/block.jpg")
		#blit used to drow in window
		#making array of blocks of size 40
		self.x=[SIZE]*length
		self.y=[SIZE]*length

	def draw(self):
		#we put fill here se that the prev block is cleared 
		self.parent_screen.fill((47, 163, 92))
		for i in range(self.length):
			self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
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
		for i in range(self.length-1,0,-1):
			self.x[i]=self.x[i-1]
			self.y[i]=self.y[i-1]

		if self.direction=="right":
			self.x[0]+=SIZE

		if self.direction=="left":
			self.x[0]-=SIZE

		if self.direction=="up":
			self.y[0]-=SIZE

		if self.direction=="down":
			self.y[0]+=SIZE


	def increase_length(self):
		self.length+=1
		self.x.append(-1)
		self.y.append(-1)

class Game:
	def __init__(self):
		pygame.init()	#initalize whole module
		pygame.display.set_caption("Snake and Apple game")
		pygame.mixer.init()
		#set mode inittialize game window
		#500 and 500 are dimentions
		#used slef to be able to call surface later with objects
		self.surface=pygame.display.set_mode((800,600))
		#flip is necessary to display the color
		self.surface.fill((47, 163, 92))
		self.direction="right"
		self.snake=Snake(self.surface,1,self.direction)	#because a game has a snake in it
		self.snake.draw()

		self.apple=Apple(self.surface)
		self.apple.draw()


	def play(self):
		self.snake.move(self.snake.direction)
		self.snake.draw()
		#self.apple.move_apple()
		self.apple.draw()
		self.display_score()
		pygame.display.flip()
		self.is_collision()
		time.sleep(0.2)

	def run(self):
		running=True
		pause=False
		#while tp keep it always running instead of timer
		#pygame offers different types of events
		while running:

			for event in pygame.event.get():
				#keydown means the keyboard is pressed
				if event.type==KEYDOWN:
					if event.key==K_RETURN:
						pause=False

					if not pause:
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
			try:
				if not pause:
					self.play()

			except Exception as e:
				self.show_game_over()
				pause=True
				self.reset()
		

				


	def is_collision(self):
		#snake colliding with apple
		if self.snake.x[0]==self.apple.x and self.snake.y[0]==self.apple.y:
			self.apple.move()
			self.snake.increase_length()
			sound=pygame.mixer.Sound("resources/ding.mp3")
			pygame.mixer.Sound.play(sound)

		#snake collide with snake	
		#started with 3 becuse the head will never collide with head or fist 2
		for i in range (3,self.snake.length):
			if self.snake.x[0]==self.snake.x[i] and self.snake.y[0]==self.snake.y[i]:
				sound=pygame.mixer.Sound("resources/crash.mp3")
				pygame.mixer.Sound.play(sound)
				raise "GAME OVER"


		#collision with window bondries
		if self.snake.x[0]<0 or self.snake.x[0]>800 or self.snake.y[0]<0 or self.snake.y[0]>600:
			sound=pygame.mixer.Sound("resources/crash.mp3")
			pygame.mixer.Sound.play(sound)

			raise "GAME OVER"


	def display_score(self):
		font=pygame.font.SysFont('arial',30)
		#to store the score and displaye it
		score=font.render(f"Score: {self.snake.length}",True,(255,255,255))
		#we always need surface display it on it any object
		self.surface.blit(score,(600,10))	
		pygame.display.flip()

	def show_game_over(self):
		self.surface.fill((235, 64, 52))
		font=pygame.font.SysFont('arial',30)
		text1=font.render(f"GAME OVER,Score: {self.snake.length}",True,(15, 15, 15))
		text2=font.render("To play again press enter",True,(15, 15, 15))
		self.surface.blit(text1,(400,300))	
		self.surface.blit(text2,(400,400))	
		pygame.display.flip()


	def reset(self):
		self.snake=Snake(self.surface,1,self.direction)	#because a game has a snake in it

if __name__=="__main__":
	game=Game()	#created object game from class Game
	game.run()




