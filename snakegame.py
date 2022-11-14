import random
import pygame as pg
from pygame.locals import *
from pygame.math import Vector2
from time import sleep

class Main:
  def __init__(self):
    self.snake = Snake()
    self.fruit = Fruit()
  def update(self):
    self.fruit.draw_fruit()
    self.snake.draw_snake()
    self.snake.move_snake()
    self.check_snake_eat()
    self.check_snake_in_screen()
    self.check_snake_collision_itself()

  def update_direction(self, direction):
    
    self.snake.direction=direction

  def check_snake_eat(self):
    if(self.fruit.pos == self.snake.body[0]):
      self.eat()
  def eat(self):
    last_body_piece = self.snake.body[-1]
    new_body_piece = last_body_piece + self.snake.direction
    self.snake.body.insert(-1, new_body_piece)
    self.fruit = Fruit()
  def check_snake_in_screen(self):
      if(self.snake.body[0].y > cell_number):
        exit()
      elif(self.snake.body[0].y < -1):
        exit()
      elif(self.snake.body[0].x > cell_number):
        exit()    
      elif(self.snake.body[0].x < -1):
        exit()
  def check_snake_collision_itself(self):
    for body in self.snake.body:
      if(self.snake.body[0] + self.snake.direction == body):
        exit()
class Snake:
  def __init__(self):
    self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10),Vector2(8,10),Vector2(9,10)]
    self.direction = Vector2(0,1)

  def draw_snake(self):
    for body in self.body:
      
      rect = pg.Rect(int(body.x * cell_size), int(body.y * cell_size), cell_size, cell_size)
      pg.draw.rect(screen, (255,0,0), rect)
      
  def move_snake(self):
    body_copy = self.body[:-1]
    body_copy.insert(0,body_copy[0] + self.direction)
    self.body = body_copy

    

class Fruit:
  def __init__(self):
    self.x = random.randint(0, cell_number -1)
    self.y = random.randint(0, cell_number - 1)
    self.pos = Vector2(self.x, self.y)
  def draw_fruit(self):
    fruit_rect = pg.Rect(int(self.x * cell_size), int(self.y * cell_size), cell_size, cell_size)
    pg.draw.rect(screen, (126,166,144), fruit_rect)

pg.init()

cell_size = 40
cell_number = 20

screen = pg.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pg.time.Clock()

mainGame = Main()
last_direction = "y"
while True:

  clock.tick(10)
  screen.fill(color=(175,215,70))
  

  for event in pg.event.get():
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
      pg.quit()
    if event.type == KEYDOWN:
      if(event.key == K_w and last_direction != "y"):
        mainGame.update_direction(Vector2(0,-1))
        last_direction = "-y"
      elif (event.key == K_a and last_direction != "x"):
        mainGame.update_direction(Vector2(-1,0))
        last_direction = "-x"
      elif (event.key == K_s and last_direction != "-y"):
        mainGame.update_direction(Vector2(0,1))
        last_direction = "y"
      elif (event.key == K_d and last_direction != "-x"):
        mainGame.update_direction(Vector2(1,0))
        last_direction = "x"

  mainGame.update()
  
  pg.display.update()
