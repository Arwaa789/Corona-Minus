import turtle
import math
import random
import time                 #shamsa
import sys                  #shamsa
from collections import deque#shamsa


alive, win  = True, False                             #shamsa

window = turtle.Screen()
window.bgcolor('white')
window.title("Corona Minus")
window.setup(700,700)
window.tracer(0)                                  # Quickens the speed

#creating button
turtle.hideturtle()
turtle.penup()
turtle.goto(-300, 300 )
turtle.pendown()
turtle.forward(50) 
turtle.left(90) 
turtle.forward(30) 
turtle.left(90) 
turtle.forward(50) 
turtle.left(90)
turtle.forward(30) 
turtle.left(90)
turtle.penup()
turtle.goto(-295, 306)
turtle.write('help', font=('Arial', 12, 'normal'))

##Register shapes
shapes = ["home.gif", "dot.gif", "title.gif","corona.gif","girl_left.gif", "girl_right.gif", "wall2.gif","san.gif", "mask.gif" ]
for i in shapes:
    turtle.register_shape(i)
    
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup() #usually pen is down becuase it writes we dont want that so pen up
        self.speed(0)
        
class Green(turtle.Turtle):    #shamsa 
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.speed(0)
        
class Yellow(turtle.Turtle):  #shamsa 
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("dot.gif")
        self.penup()
        self.speed(0)
        
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("girl_right.gif")
        self.penup()             #usually pen is down becuase it writes we dont want that so pen up
        self.speed(0)
        self.gold = 0
        
    def go_up(self): 
        if (self.xcor(), self.ycor()+24) not in walls:
            self.goto(self.xcor(), self.ycor() +24)#When you go up x coordinate doesnt change but y gets +24 pixels 

    def go_down(self): #similar explaination for others
        if (self.xcor(), self.ycor()-24) not in walls:
            self.goto(self.xcor(), self.ycor()-24)

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()
        self.shape("girl_left.gif")
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        self.shape("girl_right.gif")
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    def is_collision(self, something):#to check if player collides with treasure or any object
        a = self.xcor()-something.xcor()
        b = self.ycor()-something.ycor()
        #checking the distance to see if they are colse enough to consider a collision
        distance = math.sqrt((a**2) + (b**2))
        if distance<5:
            return True
        if distance>5:
            return False
        
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
    
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("san.gif")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)
        
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
class Mask(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("mask.gif")
        self.penup()
        self.speed(0)
        self.gold = 50
        self.goto(x, y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
class Home(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("home.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)    

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("corona.gif")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x,y)
        self.direction= random.choice(["up", "down", "left", "right"])
        
    def move(self):
        if self.direction =="up":
            dx=0
            dy=24                            #changes by Haania
        elif self.direction == "down":
            dx=0
            dy = -24
        elif self.direction == "left":
            dx=-24
            dy = 0   
        elif self.direction == "right":
            dx=24
            dy =0
        else:
            dx=0
            dy=0                   
        if self.is_close(player):#check if player is. close, if so , go in that direction
            if player.xcor()<self.xcor():
                self.direction= "left"
            if player.xcor()>self.xcor():
                self.direction="right"
            if player.ycor()<self.ycor():
                self.direction="down"
            if player.ycor()>self.ycor():
                self.direction="up"  
        #Calculate the spot
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy
        #Now we dont want enemy to pass through the wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #We will randomly choose another direction
            self.direction= random.choice(["up", "down", "left", "right"])
        turtle.ontimer(self.move, t= random.randint(100, 300)) #100 - 300 ms
        
    def is_close(self,other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        distance= math.sqrt((a**2)+(b**2))
        if distance< 75: return True
        else: return False 

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
                 
#this is the list for levels. we are keeping the first element of the list as empty list so that
#is id easier. if we call level[1] we gett the first level
levels=[""]
#this is our first level
level_1 =[
"           C",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXXXXT           XXXX", 
"X  XXXXXX   XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX        XX",
"XXXXXX  XX  XXXH       XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXX  XXXXX",
"X  XXX  MXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"XE               XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXXE        X",
"XXX                     X",
"XXXE        XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XX  XXXXXX              X",
"XX  XXXXXXXXXXXXXX  XXXXX",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX          XXXX        X",
"XXXXE                   X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]
level_2 =[
"           C",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP              X       X",
"X  XXXXXXXXXX  XXXXXXXXXX",
"X                       X",
"X  XXXXXXX  XXXXXXXXXXXXX",
"X  X     X  X           X",
"X  X  X  X  X  X  XXXX  X",
"X  X  XT X  X  X  X     X",
"X  X  XXXX  X  XXXXXXXXXX",
"X        X  X         EXX",
"X  XXXX  X  XXXXXXX XXXXX",
"X     X  X    MX        X",   
"XXXX  X  XXXXXXXXXX XXXXX",
"X  X  X                 X",
"X  X  XXXX  XXXXXXXXXXXXX",
"X  X  XE    X     X     X",
"X  X  X   XXXXXX  XXXX  X",
"X                       X",
"X  XXXXX             X  X",
"X  XXXXX  XXXXX  XXXXXXXX",
"X  X        XX        XXX",
"XE XXXX     XXX  XXX  XXX",
"XXXXXXX  X    X  XXXE  XX",
"XT         XXXXXXXXXX  HX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
 ]
levels.append(level_1)
levels.append(level_2)
treasures = []
masks=[]
homes=[]
enimies=[]
currentLevel=0
#create function that sets up the maze for a particular level
def setup_maze(level, no):
    currentLevel=no
    global start_x, start_y, end_x, end_y #i think ye na bhi karen tou chale ga #shamsa 
    for y in range(len(level)):
        for x in range(len(level[y])):
            #now we will get the character at each x,y coordinate
            character=level[y][x] 
            #we will calculate the screens x,y coordinate for this coordinates
            #note that the screen starts from 0,0 and our maze is 600 by 600 so the right most coordinate will be -288,288 because each box is of size 24.
            screen_x = -288 + (x*24)
            screen_y = 288 - (y*24)
            #checking if it is an X(which represents that there we need to place a brick for wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("wall2.gif")
                pen.stamp()
                walls.append((screen_x, screen_y)) #add coordinates to walls list
                
            if character == " " or character == "H":#shamsa 
                path.append((screen_x, screen_y))     # add " " and H to path list#shamsa 
                
            if character == "P":
                start_x , start_y = screen_x,screen_y
                player.goto(screen_x,screen_y)
            if character == "M":
                masks.append(Mask(screen_x, screen_y))
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))
            if character == "E":
                enimies.append(Enemy(screen_x, screen_y))
            if character == "C":
                pen.goto(screen_x, screen_y)
                pen.shape("title.gif")
                pen.stamp()            
            if character == "H":
                end_x , end_y = screen_x, screen_y #Global variables #shamsa 
                #pen.goto(screen_x, screen_y)
                #pen.shape("home.gif")
                #pen.stamp()
                homes.append(Home(screen_x, screen_y))
                
    return start_x , start_y , end_x, end_y #shamsa

#we are creating class instances. so if we use pen it calls the class Pen
pen = Pen()
green = Green() #shamsa 
yellow = Yellow()#shamsa 

player=Player()
walls = [] 
path = []#shamsa 
visited = set()#shamsa 
frontier = deque()#shamsa 
solution = {}      #shamsa                      # solution dictionary
start_x , start_y , end_x, end_y = setup_maze(levels[1], 1)

def button_click(x, y):
    if x>-300 and x<-250 and y>300 and y<330: # borders of button 
        if alive and player.gold>=5: # if the player has not died

            #shamsa : I had to do it in a way that the current position gets calculated and
            #then waheen se BFS for that I tried :
            #start_x , start_y = player.pos()[0] , player.pos()[1]
            #But its  not working that way
            search(start_x,start_y)
            backRoute(end_x, end_y)
        else:
            print('you donot have enough immunity points')
    
#################################################################

    
def search(x,y):
    frontier.append((x, y))
    solution[x,y] = x,y

    while len(frontier) > 0:          # exit while loop when frontier queue equals zero
        time.sleep(0)
        x, y = frontier.popleft()     # pop next entry in the frontier queue an assign to x and y location

        if(x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left
            cell = (x - 24, y)
            solution[cell] = x, y    # backtracking routine [cell] is the previous cell. x, y is the current cell
            frontier.append(cell)   # add cell to frontier list
            visited.add((x-24, y))  # add cell to visited list

        if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down
            cell = (x, y - 24)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x, y - 24))
            
        if(x + 24, y) in path and (x + 24, y) not in visited:   # check the cell on the  right
            cell = (x + 24, y)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x +24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up
            cell = (x, y + 24)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x, y + 24))
        green.goto(x,y)
        
def backRoute(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):    # stop loop when current cells == start cell
       
        yellow.goto(solution[x, y])        # move the yellow sprite to the key value of solution ()
        yellow.stamp()
        x, y = solution[x, y]               # "key value" now becomes the new key


#######################################
        
           


turtle.onscreenclick(button_click,1)        #1 means right click 0 means left click 

#The functions that we created for up/down/left/right now we need to call it on
#key i.e. Keyboard Binding

turtle.listen() 
turtle.onkey(player.go_left, "Left")            #Quotations show the arrow key on keyboard 
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_down, "Down")
turtle.onkey(player.go_up, "Up")


#turns off screen updates
window.tracer(0)

for enemy in enimies:
    turtle.ontimer(enemy.move, t=250) #It will move after every 250 milisecond 

#main game loop so that it keeps running
while True:
    #check for collision with treasure.we will iterate through treasure list for all the treasure
    for treasure in treasures:
        if treasure!='*' and player.is_collision(treasure):
            player.gold += treasure.gold
            win = True                                      #shamsa
            print("Immunity Points: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)
    for mask in masks:
        if player.is_collision(mask):
            player.gold += mask.gold
            win = True                                      #shamsa
            print("Immunity Points: {}".format(player.gold))
            mask.destroy()
            masks.remove(mask)
    for enemy in enimies:
        if player.is_collision(enemy):
            alive = False                            #shamsa
            print("Player Dies!")
            player.destroy()
    for home in homes:
        if player.is_collision(home):
            print ("level passed")
            setup_maze(levels[2],2)
    #Update screen
    window.update()
