#Importing all needed libraries 
import turtle
import math
import random
import time                 
#import sys                  
from collections import deque
#from playsound import playsound


window = turtle.Screen()  #Initiate the screen 
window.bgcolor('white')   #Background color of screen is white 
window.title("Corona Minus") #Title of the window is Corona minus 
window.setup(1300, 700)   #Size of the screen 
window.tracer(0) #speed optimization so that the user doesn't have to see every drawing.

canvas = window.getcanvas()  # or, equivalently: turtle.getcanvas()
closed= canvas.winfo_toplevel()

#Creating button on right corner top 
turtle.hideturtle() #dont see the turtle that is drawing the button 
turtle.penup()
turtle.goto(270, 280) 
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
turtle.goto(270+10, 280+5)#x +10, y+5
turtle.write('help', font=('Arial', 12, 'normal')) #Writing "help" inside it

##Register shapes. Make sure these are in the same directory as your python file. 
shapes = ["doctor_right.gif","blue_man_left.gif","blue_man_right.gif",
          "red_man_right.gif","red_man_left.gif", "doctor_left.gif",
          "stetho.gif", "mask.gif", "shopping_bag.gif","left_man.gif","right_man.gif",
          "home.gif", "dot.gif","title.gif","corona.gif","girl_left.gif", "girl_right.gif",
          "wall2.gif","san.gif", "gloves.gif" ]
for i in shapes:
    turtle.register_shape(i)

    
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup() #usually pen is down becuase it writes we dont want that so pen up
        self.speed(0)
        
class All_Paths(turtle.Turtle):     
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.speed(0)
        
class Shortest_Path(turtle.Turtle):  
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("dot.gif")
        self.penup()
        self.speed(0)
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
class Remove(turtle.Turtle):
    
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("white.gif")
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

class Man(turtle.Turtle):        
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("right_man.gif")
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
        self.shape("left_man.gif")
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        self.shape("right_man.gif")
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
        
class Doctor(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("doctor_right.gif")
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
        self.shape("doctor_left.gif")
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        self.shape("doctor_right.gif")
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
        
class Gloves(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("gloves.gif")
        self.penup()
        self.speed(0)
        self.gold = 50
        self.goto(x, y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Stethoscope(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("stetho.gif")
        self.penup()
        self.speed(0)
        self.gold = 20
        self.goto(x, y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
        
class Shopping_Bag(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("shopping_bag.gif")
        self.penup()
        self.speed(0)
        self.gold = 20
        self.goto(x,y)
        
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
        
    
class Home(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("home.gif")
        self.penup()
        self.speed(0)
        self.goto(x,y)
        
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("corona.gif")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x,y)
        self.direction= random.choice(["up", "down", "left", "right"]) #Random motion of enemy 
        
    def move(self):
        if self.direction =="up":
            dx, dy = 0 , 24                          
        elif self.direction == "down":
            dx, dy = 0 , -24
        elif self.direction == "left":
            dx, dy = -24, 0
        elif self.direction == "right":
            dx, dy = 24, 0
        else:
            dx, dy = 0, 0
                   
        if self.is_close(player): #If the player is in the proximity of virus, the virus will detect
                                  #its presence and move in that direction. (is_close function is made
                                  #below. 
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
        
    def is_close(self,other): #if distance is less than 75 than it would be considered
                              #that the virus is in close proximity to the human    
        a , b = self.xcor()-other.xcor() , self.ycor()- other.ycor()
        distance= math.sqrt((a**2)+(b**2))
        if distance< 75: return True
        else: return False
        
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()    
        
class Score(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(90, 280)
        self.write("Score: {}".format(0), align="left", font=("Monotype Corsiva", 30, "bold"))
        self.hideturtle()
        
class Die(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.hideturtle()
        
class Infected_and_normal(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("blue_man_left.gif")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x,y)
        self.direction= random.choice(["up", "down", "left", "right"]) #Random motion of enemy 
        
    def move(self):
        if self.direction =="up":
            dx, dy = 0 , 24                          
        elif self.direction == "down":
            dx, dy = 0 , -24
        elif self.direction == "left":
            dx, dy = -24, 0
            if self.shape()=="blue_man_right.gif": self.shape("blue_man_left.gif")
            elif self.shape()=="red_man_right.gif": self.shape("red_man_left.gif")
        elif self.direction == "right":
            dx, dy = 24, 0
            if self.shape()=="blue_man_left.gif": self.shape("blue_man_right.gif")
            elif self.shape()=="red_man_left.gif": self.shape("red_man_right.gif")
        else:
            dx, dy = 0, 0
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #We will randomly choose another direction
            self.direction= random.choice(["up", "down", "left", "right"])
        turtle.ontimer(self.move, t= random.randint(100, 300)) #100 - 300 ms
        
    def is_collision(self, something):
        a = self.xcor()-something.xcor()
        b = self.ycor()-something.ycor()
        #checking the distance to see if they are colse enough to consider a collision
        distance = math.sqrt((a**2) + (b**2))
        if distance<5 and something.shape()=="corona.gif":
            
            if self.shape()=="blue_man_right.gif":
                #playsound("Short-Single-Cough-www.fesliyanstudios.com.mp3")
                self.shape("red_man_right.gif")
            if self.shape()=="blue_man_left.gif":
                #playsound("Short-Single-Cough-www.fesliyanstudios.com.mp3")
                self.shape("red_man_left.gif")
        if distance<5 and (something.shape()=="red_man_left.gif" or something.shape()=="red_man_red.gif"):
            if self.shape()=="blue_man_right.gif":
                #playsound("Short-Single-Cough-www.fesliyanstudios.com.mp3")
                self.shape("red_man_right.gif")
            if self.shape()=="blue_man_left.gif":
                #playsound("Short-Single-Cough-www.fesliyanstudios.com.mp3")
                self.shape("red_man_left.gif")
        #This code can be alternatively written as :
    # if distance<5 and ((something.shape()=="red_man_left.gif" or something.shape()=="red_man_red.gif")
    #or (something.shape()=="corona.gif")):               

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
level_1 =[                   #First level maze design 
"           C",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XP              T+N E                             X",
"X  XXXXXXXXXX  XXXXXXXXXXXXX  XXXXXXX  XXXXXXXXXXXX",
"Xs          X                 X               XX  X",
"X  XXXXXXX  XXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXT X",
"X  XM    X  X           X  X                 XXX  X",
"X  X  X  X  X  X  XXXX  X  X  XXXXXXXXXXXXX  XXX  X",
"X  X  X  X  X  XN X        X  X  X        XN      X",
"X  X  XXXX  X  XXXXXXXXXX  X  X  XXXX  X  X  XX   X",
"X  X     X  X          X   X           X  X  XX  +X",
"X  XXXX  X  XXXXXXX XXXXXXXX  XXXXXXXXXXXXX  XX  XX",
"XN    X  X     X              XN             XX   X",
"XXXX  X  XXXXXXXXXX XXXXXXXXXXX  XXXXXXXXXX  XXX  X",
"X  X  X                    X     X     X  X  XXX  X",
"X  X  XXXX  XXXXXXXXXXXXX  X  XXXX  X  X  X  XX   X",
"X  X  X     X     X     X  X  X     X     X  XX  XX",
"X  X  X  XXXXXXX  XXXX  X  X  X  XXXXXXXXXX  XX  XX",
"XM                      X  X  X              XX  XX",
"X XXXXXX N           X  X  X  X  XXX        XXXE XX",
"X XXXXXX XXXXXX XXXXXXXXX    XX XX   XXXXXXXXXX  XX",
"X X    X    XXX X     XXXXXXXXX XX  XXXXXXX    X XX",
"X XXXX XXXX XXX X XXX XXXG   XX    XX    XX XX X XX",
"X XXXX    X     X XXX XXX XX XXXXXXXX XX XX XX   XX",
"X     XX XXXXXXX XXX     XX          XX    XXXX  HX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 ]
level_2 =[
"           C",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X   XXXXXT     N     XXXX      XX    XXXXXX   XXX X", 
"X  XXXXXX   XXXXXX  XXXXX   XXXXX  N XXXXXX   XXX X",
"X       XX  XXXXXX  XXXXX   XXXXX  XXXXXXXX   XXX X",
"X      MXX  XXX            XXXXXX           NXXXX X",
"XXXXXX  XX  XXXXXX         XXXXXX   XXXXXX  XXXXXXX",
"XXXXXX  XX  XXXXXX  XXXXX           XXXXXX    XXXXX",
"XXXXXX  XX    XXXX  XXXXXXXXXXXXX   XXXXXXX   XXXXX",
"X  XXX        XXXXH  XXXXXXXXXX    XXXXXXXX      XX",
"X  XXX  XXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXX     NXX",
"X         XXXXXXXXXXXXXXX          XXXXXS P   XXXXX",
"XE               XXXXXXXX    XXXXXXXXXXX  XXXXXXXXX",
"XXXXXXXXXXXX     XXXXX     XXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXX  XXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXX  XXXXXXXXXX                      XXXXXXXXXXXXXX",
"XXX                     XXXXXXXX     XXXXX     XXXX",
"XXX         XXXXXXXXXXXXXXXXXXXXXX   XXXXX   XXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX     XXXX   XXXXX   XXXXXX",
"XXXXXXXXXX              X                    XXXXXX",
"XX  XXXXXX                    XXXXXXXXXXXXXXXXXXXXX",
"XX  XXXXXXXXXXXXXX  XXXXXXXX       XXXXXXXXXXXXXXXX",
"XX  NXXXXXXXXXXXXX  XXXXX     XXXXXXXXXXXXXXXXXXXXX",
"XXE                        X                       ",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
 ]

level_3=[    #THIS IS THIRD LEVEL DESIGN
"           C",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXP            XX      XX                         X",
"XX             XX      XXXX  XXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXX  XXXXXXXXXX         X               XX  X",
"XXXXXXXXX  XXXXXXXXXX  XX  XXXXXXXXXXXXXXXXXXXXXT X",
"XX                     XX  X                 XXX  X",
"X                          X  XXXXXXXXXXXXX  XXX  X",
"X   XXXXXXXXXXX   XXXXXXX  X  X  X        XN      X",
"XX       XX       X        X  X  XXXX  X  X  XX   X",
"XX       XX       XX   XX  X           X  X  XX  +X",
"XXXXXX   XX            XXXXX  XXXXXXXXXXXXX  XX  XX",
"XX       XX                   XN             XX   X",
"XXXXXXXXXXX  XXXXXXXXXXXXXXXXXX  XXXXXXXXXX  XXX  X",
"XXXXXXXXXXX  XXXXXXXXXXXX  X     X     X  X  XXX  X",
"X     XX               XX  X  XXXX  X  X  X  XX   X",
"X     XX                   X  X     X     X  XX  XX",
"XXXX  XX       XXXXXXXXXX  X  X  XXXXXXXXXX  XX  XX",
"X     XX       XXXXXXXXXX  X  X  XXX        XXXE XX",
"X   XXXXXXXXX  XX                XXX        XXXE XX",
"X              XX      XXXXXXXX     XXXXXXX    X XX",
"X           XXXXXXX    XXG   XX    XX    XX    X XX",
"XXXXXXXXXX  XXXXXXX          XXXXX    XX    XX   XX",
"XX  XX                 XXXX          XX    XXXX  HX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]
#In the list for levels. we are keeping the first element of the list as empty string so that
#it is easier for us to call levels i.e levels[1] will call level one. If we donot do this step
#levels[0] would mean the 1st level. This step is therefore done just for the sake of our
#simplification and is hence not mandatory.

levels, treasures, masks, enimies, homes, stethoscopes, gloves, dots, shopping,infected_and_normal = ["", level_1, level_2, level_3], [], [],[], [], [], [], [], [], []

#Creating function that sets up the maze for a particular level

def setup_maze(level):
    global end_x, end_y
    for y in range(len(level)):
        for x in range(len(level[y])):
            character=level[y][x]
            
            #now we will get the character at each x,y coordinate
            #we will calculate the screens x,y coordinate for this coordinates
            #note that the screen starts from 0,0 and our maze is 600 by 600 so the right most
            #coordinate will be -288,288 because each box is of size 24.
            
            screen_x = -588 + (x*24)
            screen_y = 288 - (y*24)
            
            #checking if it is an X(which represents that there we need to place a brick for wall)
            
            if character == "X" :
                pen.goto(screen_x, screen_y)
                pen.shape("wall2.gif")
                pen.stamp()
                walls.append((screen_x, screen_y))    #add coordinates to walls list
                
            if character == " " or character == "H":  #This is done for the sake of BFS 
                path.append((screen_x, screen_y))     # add " " and H to path list
                
            if character== "S":
                stethoscopes.append(Stethoscope(screen_x, screen_y))
                
            if character == "P":
                #start_x , start_y = screen_x,screen_y
                player.goto(screen_x,screen_y)
                
            if character == "M":
                masks.append(Mask(screen_x, screen_y))
            if character== "N":
                infected_and_normal.append(Infected_and_normal(screen_x, screen_y))
                 
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))
            if character=="G":
                gloves.append(Gloves(screen_x, screen_y))
                 
            if character == "E":
                enimies.append(Enemy(screen_x, screen_y))
                
            if character == "C":
                pen.goto(screen_x, screen_y)
                pen.shape("title.gif")
                pen.stamp()
                
            if character == "H":
                end_x , end_y = screen_x, screen_y
                homes.append(Home(screen_x, screen_y))
                
            if character=="V":
                shopping.append(Shopping_Bag(screen_x,screen_y))

    return end_x, end_y 

#we are creating class instances. so if we use pen it calls the class Pen

pen = Pen()
all_paths = All_Paths()  
shortest_path = Shortest_Path()
die=Die()
score=Score()
player=Player()

walls = [] 
path = []
visited = set()
frontier = deque()
solution = {}                       #solution dictionary
end_x, end_y = setup_maze(levels[1])
maze="level1"

def closing():
    global z
    z= False

closed.protocol("WM_DELETE_WINDOW", closing)
z=True
starting_time=0
flag=False
def button_click(x, y):
    global flag
    global starting_time
    if x>=250+30 and x<=300+30 and y>=240+30 and y<=270+30: # borders of button
        
        if player.gold>=50: # if the player has not died
            flag=True
            current_pos_x, current_pos_y = player.pos()
            search(current_pos_x, current_pos_y)
            window.tracer(1)
            backRoute(end_x, end_y, current_pos_x, current_pos_y)
            #window.tracer(0)
            #search(current_pos_x, current_pos_y)
            #window.tracer(1)
            starting_time = time.time()
            window.tracer(0)
            

        else:
            print('you donot have enough immunity points')
def button_playagain(x,y):
    if x>=-70 and x<=70 and y>=-100 and y<=-60:
        walls.clear()
        pen.clear()
        global treasures
        global masks
        global enimies
        global homes
        global gloves
        global infected_and_normal
        for treasure in treasures:
            Treasure.destroy(treasure)
            treasures.remove(treasure)
        for mask in masks:
            Mask.destroy(mask)
            masks.remove(mask)
        for enemy in enimies:
            Enemy.destroy(enemy)
            enimies.remove(enemy)
        for home in homes:
            home.destroy()
            homes.remove(home)
        for glove in gloves:
            glove.destroy()
            gloves.remove(glove)
        for infected in infected_and_normal:
            infected.destroy()
            infected_and_normal.remove(infected)
        player.destroy()
        player=Player()
        
        end_x, end_y = setup_maze(levels[1])
        maze="level1"
        turtle.hideturtle()
        turtle.onscreenclick(button_click,1)        #1 means right click 0 means left click 
        turtle.listen() 
        turtle.onkey(player.go_left, "Left")            #Quotations show the arrow key on keyboard 
        turtle.onkey(player.go_right, "Right")
        turtle.onkey(player.go_down, "Down")
        turtle.onkey(player.go_up, "Up")

                #turns off screen updates
                
        for enemy in enimies:
            turtle.ontimer(enemy.move, t=250) #It will move after every 250 milisecond
        for infected in infected_and_normal:
            turtle.ontimer(infected.move, t=250)
        

            

def search(x,y):
    frontier.append((x, y))
    solution[x,y] = x,y
    while len(frontier) > 0: # exit while loop when frontier queue equals zero
        time.sleep(0)
        x, y = frontier.popleft()   # pop next entry in the frontier queue an
                      #assign to x and y location
        if(x - 24, y) in path and (x - 24, y) not in visited and (x - 24, y) not in walls :  # check the cell on the left
            cell = (x - 24, y)
            solution[cell] = x, y    # backtracking routine [cell] is the previous cell. x, y is the current cell
            frontier.append(cell)   # add cell to frontier list
            visited.add((x-24, y))  # add cell to visited list

        if (x, y - 24) in path and (x, y - 24) not in visited and (x, y - 24) not in walls :  # check the cell down
            cell = (x, y - 24)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x, y - 24))
            
        if(x + 24, y) in path and (x + 24, y) not in visited and (x + 24, y) not in walls :   # check the cell on the  right
            cell = (x + 24, y)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x +24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited and (x, y + 24) not in walls :  # check the cell up
            cell = (x, y + 24)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x, y + 24))
        
        all_paths.goto(x,y)
stamps=[]
def backRoute(x, y, current_pos_x, current_pos_y):
    global stamps
    
    shortest_path.goto(x, y)
    stamps.append(shortest_path.stamp())
    while (x, y) != (current_pos_x, current_pos_y):    # stop loop when current cells == start cell
       
        shortest_path.goto(solution[x, y])        # move the yellow sprite to the key value of solution ()
        stamps.append(shortest_path.stamp())
        x, y = solution[x, y]               # "key value" now becomes the new key
    #stamps.append(shortest_path.stamp())


def backRoute1():
    global stamps
    for i in stamps:
        shortest_path.clearstamp(i)
    shortest_path.hideturtle()
        
  #  shortest_path.goto(x, y)
 #   shortest_path.clear()
   # while (x, y) != (current_pos_x, current_pos_y):    # stop loop when current cells == start cell
       
    #    shortest_path.goto(solution[x, y])        # move the yellow sprite to the key value of solution ()
        #shortest_path.clear()
        #x, y = solution[x, y]



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
    
for infected_n_normal in infected_and_normal:
    turtle.ontimer(infected_n_normal.move, t=250) #It will move after every 250 milisecond

def dead():
    die.goto(-10,-50)
    die.write("PLAYER DIES!",True, align="center", font=("Arial",30,"bold"))
    die.hideturtle()
    turtle.clear()
    print("Player Dies!")
    player.destroy()
    window.bye()
    turtle.hideturtle() #dont see the turtle that is drawing the button 
    turtle.penup()
    turtle.goto(-70, -100) 
    turtle.pendown()
    turtle.forward(140) 
    turtle.left(90) 
    turtle.forward(40) 
    turtle.left(90) 
    turtle.forward(140) 
    turtle.left(90)
    turtle.forward(40) 
    turtle.left(90)
    turtle.penup()
    turtle.goto(-70+10, -100+5)#x +10, y+5
    turtle.write('Play Again', font=('Arial', 18, 'bold'))
    turtle.onscreenclick(button_playagain,1) 
        
#main game loop so that it keeps running
while z==True:
    #check for collision with treasure.we will iterate through treasure list for all the treasure
    if flag==True:
            print("hello")
            
            time_limit = 10

            if time.time() - starting_time >=time_limit:
                backRoute1()
                flag=False
    if not z:
        break
        
    for treasure in treasures:
        if treasure!='*' and player.is_collision(treasure):
            player.gold += 50          
            score.clear()
            score.write("Score: {}".format(player.gold), align="left", font=("Arial", 20, "normal"))
            print("Immunity Points: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)
    for bag in shopping:
        if bag!='*' and player.is_collision(bag):
            player.gold += bag.gold     
            score.clear()
            score.write("Score: {}".format(player.gold), align="left", font=("Arial", 20, "normal"))
            print("Immunity Points: {}".format(player.gold))
            bag.destroy()
            shopping.remove(bag)
            
    for stethoscope in stethoscopes:
        if stethoscope!='*' and player.is_collision(stethoscope):
            player.gold += stethoscope.gold                                 
            score.clear()
            score.write("Score: {}".format(player.gold), align="left", font=("Arial", 20, "normal"))

            print("Immunity Points: {}".format(player.gold))
            stethoscope.destroy()
            stethoscopes.remove(stethoscope)
    for mask in masks:
        if player.is_collision(mask):
            player.gold += 50
            score.clear()
            score.write("Score: {}".format(player.gold), align="left", font=("Arial", 20, "normal"))
            print("Immunity Points: {}".format(player.gold))
            mask.destroy()
            masks.remove(mask)
    for glove in gloves:
        if player.is_collision(glove):
            player.gold += glove.gold
            score.clear()
            score.write("Score: {}".format(player.gold), align="left", font=("Arial", 20, "normal"))
            print("Immunity Points: {}".format(player.gold))
            glove.destroy()
            gloves.remove(glove)
    for enemy in enimies:
        for infected_n_normal in infected_and_normal:
            infected_n_normal.is_collision(enemy)
            
        if player.is_collision(enemy)and player.gold<100:
            dead()
            
    for infected_n_normal in infected_and_normal:
        if player.is_collision(infected_n_normal) and (infected_n_normal.shape()=="red_man_left.gif" or infected_n_normal.shape()=="red_man_right.gif"):
            if player.gold<100:
                dead()
            else:
                player.gold-=100            
                score.clear()
                score.write("Score: {}".format(player.gold), align="left", font=("Arial", 20, "normal"))
                print("Immunity Points: {}".format(player.gold))
        for i in infected_and_normal:
            i.is_collision(infected_n_normal)

            
    for home in homes:
        if player.is_collision(home) and maze=="level3":
            if maze=="level2":
                if len(shopping)!=0:
                    print("You need to collect your grocery first in order to reach home.")
                    break
            die.goto(-10,50)
            die.write("Congratulations! \nYou have saved yourself from the virus",True, align="center", font=("Arial",20,"bold"))
            die.hideturtle()
            #turtle.clear()
            player.destroy()
        if player.is_collision(home):
            if maze=="level2":
                if len(stethoscopes)!=0:
                    print("Dr. you need to collect your stethoscope first, to reach to the hospital")
                    break
            walls.clear()
            pen.clear()
            for treasure in treasures:
                Treasure.destroy(treasure)
                treasures.remove(treasure)
            for mask in masks:
                Mask.destroy(mask)
                masks.remove(mask)
            for enemy in enimies:
                Enemy.destroy(enemy)
                enimies.remove(enemy)
            for home in homes:
                home.destroy()
                homes.remove(home)
            for glove in gloves:
                glove.destroy()
                gloves.remove(glove)
            for infected in infected_and_normal:
                infected.destroy()
                infected_and_normal.remove(infected)
            player.destroy()
            if maze=="level1":
                print ("level passed")
                player=Doctor()
                start_x, start_y = setup_maze(levels[2])
                maze="level2"
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
                    turtle.ontimer(enemy.move, t=250)
                for infected in infected_and_normal:
                    turtle.ontimer(infected.move, t=250) #It will move after every 250 milisecond

                
            elif maze=="level2":
                print ("level passed")
                player=Man()
                end_x, end_y = setup_maze(levels[3])
                maze="level3"
                turtle.hideturtle()
                turtle.onscreenclick(button_click,1)        #1 means right click 0 means left click 

                #The functions that we created for up/down/left/right now we need to call it on
                #key i.e. Keyboard Binding

                turtle.listen() 
                turtle.onkey(player.go_left, "Left")            #Quotations show the arrow key on keyboard 
                turtle.onkey(player.go_right, "Right")
                turtle.onkey(player.go_down, "Down")
                turtle.onkey(player.go_up, "Up")

                #turns off screen updates
                
                for enemy in enimies:
                    turtle.ontimer(enemy.move, t=250) #It will move after every 250 milisecond
                for infected in infected_and_normal:
                    turtle.ontimer(infected.move, t=250)
    #if player.is_collision(homes[-1]):
     #           break
        
            
    #Update screen
    window.update()
turtle.bye()
