"""
The purpose of this program is to create the snake game, in which the player must try to maximize the length of the snake by eating the food. It also has obstacles which the player must avoid. 
"""
import pygame 
import time
import random


# colors
brown = (150, 75, 0)
green = (57, 112, 6)
purple = (82, 68, 93) 
burgundy = (117, 2, 2)
black= (0,0,0)
blue = (36, 116, 155)
light_blue = (192, 224, 235)
cream = (238, 238, 228)


class IntroScreen: # the intro screen of the game
  def __init__ (self):
    pygame.init()
    self.width = 1000 # setting width 
    self.height = 500 # setting height
    self.intro_screen = pygame.display.set_mode((self.width, self.height))
    pygame.display.set_caption("SNAKE GAME") # title of the screen
    self.bg = pygame.image.load("images//intro.jpg") # bg image of the screen
    self.intro_screen.blit(self.bg,(0,0))
    # fonts and font sizes
    self.font_title = pygame.font.Font("stereofidelic//stereofidelic.ttf", 75)
    self.font_body = pygame.font.Font("stereofidelic//stereofidelic.ttf", 30)
    # to play - text
    self.play_game = self.font_title.render('press space to play', True, cream)
    self.intro_screen.blit(self.play_game,(210,415))
    # rules - text
    self.rules_menu = self.font_body.render('press R for the rules', True, cream)
    self.intro_screen.blit(self.rules_menu,(570,220))
    pygame.display.update()

    #introducing other classes
    self.food = Food(self.intro_screen,self.width,self.height)
    self.ticker = timeTicker(self.intro_screen,self.width,self.height)
    self.fire = Fire(self.intro_screen,self.width,self.height)

    #images of bg and the controls
    self.rules = pygame.image.load("images//rules.jpg")
    self.controls_img = pygame.image.load("images//arrows.png")
    
   
    # to get the code to run without immediately quitting
    start = True
    while start == True:
      for event in pygame.event.get(): # getting the input from the user
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
              # adding text and images to rules screen
              self.intro_screen.blit(self.rules,(0,0))
              
              self.title = self.font_title.render('Rules', True, black)
              self.intro_screen.blit(self.title,(360,30))
              
              self.controls = self.font_body.render('Use the arrow keys to navigate the snake', True, black)
              self.intro_screen.blit(self.controls,(50,120))              
              self.intro_screen.blit(self.controls_img,(120,170))    

              self.special = self.font_body.render('—specials—', True, black)
              self.intro_screen.blit(self.special,(615,120))   

              self.objective = self.font_body.render('Objective: Get the snake to be as long as possible', True, black)
              self.how_to = self.font_body.render('Remain within the boundaries and avoid colliding the head with the body ', True, black)
              self.intro_screen.blit(self.objective,(50,330))              
              self.intro_screen.blit(self.how_to,(50,380))

              self.intro_screen.blit(self.food.img,(625,170))
              self.food_text = self.font_body.render('good', True, black)
              self.intro_screen.blit(self.food_text,(655,165))

              
              self.intro_screen.blit(self.ticker.img,(625,230))
              self.ticker_text = self.font_body.render('neutral', True, black)
              self.intro_screen.blit(self.ticker_text,(655,225))

      
              self.intro_screen.blit(self.fire.img,(625,280))
              self.fire_text = self.font_body.render('bad', True, black)
              self.intro_screen.blit(self.fire_text,(655,275))

              self.play_game = self.font_title.render('press space to play', True, black)
              self.intro_screen.blit(self.play_game,(210,415))

              pygame.display.update()

            
              if event.key == pygame.K_SPACE: # to start game
                Main()              
            if  event.key == pygame.K_m: # to return to main menu
                IntroScreen()
            if event.key == pygame.K_SPACE:
              Main()
            
              

class snake():
  def __init__ (self, master,x,y, length):
    self.master = master
    self.length = length 
    self.bg = pygame.image.load("images//background.png")
    self.img = pygame.image.load("images//snake.png")
 
    self.x = [] 
    self.y = []   
    for a in range(self.length): #creating a list of the coordinates of the snake so that it can be maneuvered
      self.x.append(160)
      self.y.append(160)
  
  def movement(self,direction):
    self.direction = direction
    for a in range(self.length-1,0,-1): # to get the snake to move in a chain-like way
      self.x[a] = self.x[a-1]
      self.y[a] = self.y[a-1]
    # to get the direction to change upon the keys' control
    if self.direction == 'w':
      self.y[0] -= 20
    elif self.direction == 's':
      self.y[0] += 20
    elif self.direction == 'a':
      self.x[0] -= 20
    elif self.direction == 'd':
      self.x[0] += 20
      
    self.drawing() # draw the snake
  
  def drawing(self): # drawing the sqaures of the snake
    self.master.blit(self.bg,(0,0))
    for n in range(self.length):
      self.master.blit(self.img,(self.x[n],self.y[n]))     

  def extend(self): # extending the length of the snake
    self.length += 1
    self.x.append(160)
    self.y.append(160)

class timeTicker: # speeds up time
  def __init__(self,master,screen_width, screen_height):
    self.master = master
    self.x_limit = screen_width//20 - 1
    self.y_limit =  screen_height//20 - 1
    self.img = pygame.image.load("images//clock.png")
    self.x = 40
    self.y = 80
    
  def clock(self):
    self.master.blit(self.img,(self.x,self.y))

  def randomizer(self): # to change the position of the hourglass randomly
    # to randomize the position of the food such that it aligns with the snake's squares/blocks
    self.x = (random.randint(0,self.x_limit)) * 20 
    self.y = (random.randint(0,self.y_limit)) * 20

    
class Food: # food for the snake
  def __init__(self,master,screen_width, screen_height):
    self.master = master
    self.x_limit = screen_width//20 - 1
    self.y_limit =  screen_height//20 - 1
    self.img = pygame.image.load("images//food.png")
    self.x = 240
    self.y = 240
  
  def show_food(self): # show the food on the screen
    self.master.blit(self.img,(self.x,self.y))

  def randomizer(self):
    # to randomize the position of the food such that it aligns with the snake's squares/blocks
    self.x = (random.randint(0,self.x_limit)) * 20 
    self.y = (random.randint(0,self.y_limit)) * 20
    

class Fire: # must avoid element
  def __init__(self,master,screen_width, screen_height):
    self.master = master
    self.x_limit = screen_width//20 - 1
    self.y_limit =  screen_height//20 - 1
    self.img = pygame.image.load("images//fire.png")
    self.x = 500
    self.y = 300
  
  def show(self):
    self.master.blit(self.img,(self.x,self.y))
    
  def randomizer(self):
    # to randomize the position of the food such that it aligns with the snake's squares/blocks
    self.x = (random.randint(0,self.x_limit)) * 20 
    self.y = (random.randint(0,self.y_limit)) * 20
 
   
class Main: # the main game class
  def __init__ (self):
    
    self.timer = pygame.time.Clock() # to keep track of the time to control the speed
    self.speed = 10
    self.score = 0 # initial score
    self.width = 1000
    self.height = 500
    
    self.screen = pygame.display.set_mode((self.width, self.height))
    self.playing_screen_width = 800 # to separate it from the score panel
    pygame.display.set_caption("SNAKE GAME")
    self.bg = pygame.image.load("images//background.png")
    self.screen.blit(self.bg,(0,0))
    self.screen.fill(blue)
    pygame.display.update()
    
    self.display = pygame.image.load("images//display.png")
    # midpoints
    self.x = self.playing_screen_width//2 
    self.y = self.height//2

    self.snake = snake(self.screen,self.x,self.y,1)
    self.dir = None
    
    self.food = Food(self.screen,self.playing_screen_width,self.height)
  
    self.food.show_food()

    self.ticker = timeTicker(self.screen,self.playing_screen_width,self.height)
    self.ticker.clock()

    self.fire = Fire(self.screen,self.playing_screen_width,self.height)
    self.fire.show()

    self.game()
    
  def game_end(self): # game over function
    self.font = pygame.font.Font("stereofidelic//stereofidelic.ttf", 150)
    self.text = self.font.render("Game Over",True, light_blue)
    self.screen.blit(self.text,(200,150))
    pygame.display.update()
    
  def game(self): # the actual game itself
    game_run = True  
    
    while game_run == True:  
        self.font = pygame.font.Font("stereofidelic//stereofidelic.ttf", 60)
        self.font_body = pygame.font.Font("stereofidelic//stereofidelic.ttf", 20)
        self.screen.fill(blue)
        self.msg = str(self.score)
        self.text = self.font.render(f'Score:{self.msg}',True, light_blue)
        self.screen.blit(self.text,(825,50))
        self.screen.blit(self.display,(837,325))
        self.screen.blit(self.food.img,(830,150))
        self.food_desc = self.font_body.render('food',True, light_blue)
        self.screen.blit(self.food_desc,(865,150))
      
        self.screen.blit(self.ticker.img,(830,190))
        self.ticker_desc = self.font_body.render('time speeder',True, light_blue)
        self.screen.blit(self.ticker_desc,(865,190))

      
        self.screen.blit(self.fire.img,(830,230))
        self.fire_desc = self.font_body.render('fire',True, light_blue)
        self.screen.blit(self.fire_desc,(865,230))
        
      
        for event in pygame.event.get():# getting the input from the user to move the snake
            if event.type == pygame.QUIT: # to end game 
                game_run = False  
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_UP:
                 self.dir = 'w'
              elif event.key == pygame.K_DOWN:
                 self.dir = 's'
              elif event.key == pygame.K_RIGHT:
                 self.dir = 'd'
              elif event.key == pygame.K_LEFT:
                 self.dir = 'a'

        self.snake.movement(self.dir)
        self.snake.drawing()
        self.food.show_food()
        self.ticker.clock()
        self.fire.show()
        pygame.display.update()
      
        # extending the length of the snake upon eating food
        if self.snake.x[0] < self.food.x +20 and self.snake.x[0]>=self.food.x and self.snake.y[0] < self.food.y + 20 and self.snake.y[0]>=self.food.y:
          self.score += 1
          self.snake.extend()
          self.food.randomizer()
          if self.score > 0 and self.score % 3 == 0: # to keep changing the positions of the special elements
            self.ticker.randomizer() 
            self.fire.randomizer()

      # if it interacts with the speeding time element
        if self.snake.x[0] < self.ticker.x +20 and self.snake.x[0]>=self.ticker.x and self.snake.y[0] < self.ticker.y + 20 and self.snake.y[0]>=self.ticker.y:
          self.speed += 1
          self.ticker.randomizer()  

      # if it encounters the fire element, game ends
        if self.snake.x[0] < self.fire.x +20 and self.snake.x[0]>=self.fire.x and self.snake.y[0] < self.fire.y + 20 and self.snake.y[0]>=self.fire.y:
            game_run = False
            self.game_end()
            time.sleep(1.7)
            self.end_screen()

      # if the snake collides with itself, game ends
        for n in range(1, len(self.snake.x)):
          if self.snake.x[n] == self.snake.x[0] and self.snake.y[n] == self.snake.y[0]:
            game_run = False
            self.game_end()
            time.sleep(1.7)
            self.end_screen()
            
      # if the snake leaves the screen, the game ends
        for n in range(len(self.snake.x)):      
          if self.snake.x[n] > self.playing_screen_width-20 or self.snake.x[n] < 0 or self.snake.y[n] > self.height or self.snake.y[n] < 0:
            game_run = False
            self.game_end()
            time.sleep(1.7)
            self.end_screen()
    
        self.timer.tick(self.speed) # speed of the snake
   
  def end_screen(self): # end screen display
    self.screen.fill(blue)
    self.font_title = pygame.font.Font("stereofidelic//stereofidelic.ttf", 150)
    self.font_body = pygame.font.Font("stereofidelic//stereofidelic.ttf", 40)
    self.msg = str(self.score)
    self.text = self.font_title.render(f'Final Score: {self.msg}',True, light_blue)
    self.screen.blit(self.text,(210,100))
    self.subtext_1 = self.font_body.render('press m for the main menu',True, light_blue)
    self.screen.blit(self.subtext_1,(330,305))
    self.subtext_2 = self.font_body.render('press space to play again',True, light_blue)
    self.screen.blit(self.subtext_2,(330,385))
          
    pygame.display.update()

IntroScreen() # to start the game
    