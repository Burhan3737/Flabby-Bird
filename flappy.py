import pygame
import random
import time

# initialize pygame
pygame.init()

class Object:
  def __init__(self, x=0, y=0,gravity=0,velocity=0):
    self.x = x
    self.y = y
    self.gravity=gravity
    self.velocity=velocity


  def set_x(self, r):
        self.x = r

  def set_y(self, r):
        self.y = r


  def set_gravity(self, r):
        self.gravity = r

  def set_velocity(self, r):
        self.velocity = r


  def get_x(self):
        return self.x
  
  def get_y(self):
        return self.y
  
  def get_gravity(self):
        return self.gravity
    
  def get_velocity(self):
        return self.velocity




# set up window
screen = pygame.display.set_mode((250, 400))
pygame.display.set_caption("Flappy Bird")

# load assets

font = pygame.font.Font(None, 36)
text_over = font.render(f"GAME OVER", True, (255, 255, 255))
counter = 0
bg_img = pygame.image.load("background-night.png").convert()
bird_img = pygame.image.load("bird.png").convert_alpha()

bird_img2=pygame.image.load("bird.png").convert_alpha()
pipe_img = pygame.image.load("pip.png").convert_alpha()
pipe_img_inv = pygame.transform.rotate(pipe_img, 180)
 

rotate=True
# set up game objects
bird=Object()
pipe=Object()


bird.set_x(50)
bird.set_y(250)
bird.set_velocity(0)
bird.set_gravity(0.2)


pipe.set_x(400)
pipe.set_y(random.randint(100, 200))
pipe.set_velocity(-2) 


delayUP=0 # delay to show up motion of bird
level=0
gameSpeed=0.020

# game loop
while True:
    delayUP+=1
    level+=1
    
    if(level>=500):
        level=0
        if gameSpeed>0 :
          gameSpeed-=0.0005
      

    time.sleep(gameSpeed)

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                 
             bird.set_velocity(-3)
             if delayUP<10 and rotate==True:
                  rotate=False
                  bird_img=pygame.transform.rotate(bird_img, 45)
                 

                 

    # update bird position
    bird.set_y(bird.get_y()+bird.get_velocity()) 
    bird.set_velocity(bird.get_velocity()+bird.get_gravity())

    # update pipe position
    pipe.set_x(pipe.get_x()+pipe.get_velocity())
    if pipe.get_x() < -50:
        pipe.set_x(250)
        pipe.set_y(random.randint(200, 400))

    # check for collision
    if bird.get_y()+32 > pipe.get_y() or bird.get_y() < pipe.get_y() -87:
        if pipe.get_x()<80 and pipe.get_x()>20:
            screen.blit(text_over, (50, 200))
            pygame.display.update()
            event = pygame.event.wait()
            pygame.quit()
 
    if bird.get_y()>410:
        
        screen.blit(text_over, (50, 175))
        pygame.display.update()
        event = pygame.event.wait()
        pygame.quit()
        

    #update score
    if pipe.get_x() == bird.get_x():
       counter+=1


    #set back to original
    if delayUP>=10:
        delayUP=0
        rotate=True
        bird_img=bird_img2
    
    # draw objects
    screen.blit(bg_img, (0, 0))
    screen.blit(bird_img, (bird.get_x(), bird.get_y()))
    screen.blit(pipe_img, (pipe.get_x(), pipe.get_y()))
    screen.blit(pipe_img_inv, (pipe.get_x(), pipe.get_y() -400))
    text = font.render(f"Score: {counter}", True, (255, 255, 255))
    screen.blit(text, (0, 0))
    
    pygame.display.update()