import turtle            #Importing all needed libraries 
import math
import random
import time
from collections import deque

window = turtle.Screen()        #Initiate the screen 
window.bgcolor('white')         #Background color of screen is white 4
window.title("Corona Minus")    #Title of the window is Corona minus 
window.setup(1300, 700)         #Size of the screen 
window.bgpic('front.gif')
window.update()
time.sleep(5)
window.bgpic('white_bg.gif')
window.tracer(0) #speed optimization so that the user doesn't have to see every drawing.
canvas = window.getcanvas()     
closed= canvas.winfo_toplevel()
def button():
    turtle.hideturtle() #Creating button on right corner top dont see the turtle that is drawing the button 
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
    turtle.goto(270+10, 280+5)      #x+10, y+5
    turtle.write('help', font=('Arial', 12, 'normal')) #Writing "help" inside it
button()

for i in ["doctor_right.gif","front.gif", "blue_man_left.gif","blue_man_right.gif","red_man_right.gif","red_man_left.gif", "doctor_left.gif","stetho.gif", "mask.gif", "shopping_bag.gif","left_man.gif","right_man.gif","home.gif", "dot.gif","title.gif","corona.gif","girl_left.gif", "girl_right.gif","wall2.gif","san.gif", "gloves.gif" ]:
    turtle.register_shape(i) ##Register shapes. Make sure these are in the same directory as your python file.
  
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()        #usually pen is down becuase it writes we dont want that so pen up
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
        
    def go_up(self):  #When you go up x coordinate doesnt change but y gets +24 pixels 
        if (self.xcor(), self.ycor()+24) not in walls and life==True:self.goto(self.xcor(), self.ycor() +24)
            
    def go_down(self): #similar explaination for others
        if (self.xcor(), self.ycor()-24) not in walls and life==True:self.goto(self.xcor(), self.ycor()-24)
            
    def go_left(self):
        self.shape("girl_left.gif")
        if (player.xcor() - 24 , player.ycor()) not in walls and life==True: self.goto(player.xcor() - 24 , player.ycor())
        
    def go_right(self):
        self.shape("girl_right.gif")
        if (player.xcor() + 24, player.ycor()) not in walls  and life==True: self.goto(player.xcor() + 24, player.ycor())
                 
    def is_collision(self, something):#to check if player collides with treasure or any object
        distance = math.sqrt(((self.xcor()-something.xcor())**2) + ((self.ycor()-something.ycor())**2))
        if distance<5: return True #checking the distance to see if they are colse enough to consider a collision
        else: return False 
        
    def destroy(self):
        self.goto(3000,2000)
        self.hideturtle()

class Man(turtle.Turtle):        
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("right_man.gif")
        self.penup()             #usually pen is down becuase it writes we dont want that so pen up
        self.speed(0)
        
    def go_up(self): 
        if (self.xcor(), self.ycor()+24) not in walls:self.goto(self.xcor(), self.ycor() +24)#When you go up x coordinate doesnt change but y gets +24 pixels 

    def go_down(self): #similar explaination for others
        if (self.xcor(), self.ycor()-24) not in walls: self.goto(self.xcor(), self.ycor()-24)
            
    def go_left(self):
        self.shape("left_man.gif")
        if (player.xcor() - 24, player.ycor()) not in walls: self.goto(player.xcor() - 24, player.ycor())     

    def go_right(self):
        self.shape("right_man.gif")
        if (player.xcor() + 24, player.ycor()) not in walls: self.goto(player.xcor() + 24, player.ycor())
                
    def is_collision(self, something):#to check if player collides with treasure or any object
        distance = math.sqrt(((self.xcor()-something.xcor())**2) + ((self.ycor()-something.ycor())**2))
        if distance<5: return True#checking the distance to see if they are colse enough to consider a collision
        else: return False 
        
    def destroy(self):
        self.goto(4000,2000)
        self.hideturtle()
        
class Doctor(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("doctor_right.gif")
        self.penup()             #usually pen is down becuase it writes we dont want that so pen up
        self.speed(0)
        
    def go_up(self): 
        if (self.xcor(), self.ycor()+24) not in walls:self.goto(self.xcor(), self.ycor() +24)#When you go up x coordinate doesnt change but y gets +24 pixels 
    
    def go_down(self): #similar explaination for others
        if (self.xcor(), self.ycor()-24) not in walls: self.goto(self.xcor(), self.ycor()-24)
            
    def go_left(self):
        self.shape("doctor_left.gif")
        if (player.xcor() - 24,player.ycor()) not in walls: self.goto(player.xcor() - 24,player.ycor())    

    def go_right(self):
        self.shape("doctor_right.gif")
        if (player.xcor() + 24, player.ycor()) not in walls: self.goto(player.xcor() + 24, player.ycor())
                 
    def is_collision(self, something):#to check if player collides with treasure or any object
        distance = math.sqrt(((self.xcor()-something.xcor())**2) + ((self.ycor()-something.ycor())**2))
        if distance<5:return True#checking the distance to see if they are colse enough to consider a collision
        else : return False 
        
    def destroy(self):
        self.goto(5000,2000)
        self.hideturtle()
    
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("san.gif")
        self.penup()
        self.speed(0)
        self.goto(x,y)
        
    def destroy(self):
        self.goto(6000,2000)
        self.hideturtle()
        
class Mask(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("mask.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(8000,2000)
        self.hideturtle()
        
class Gloves(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("gloves.gif")
        self.penup()
        self.goto(x, y)

    def destroy(self):
        self.goto(9000,2000)
        self.hideturtle()

class Stethoscope(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("stetho.gif")
        self.penup()
        self.goto(x, y)

    def destroy(self):
        self.goto(-2000,2000)
        self.hideturtle()
        
class Shopping_Bag(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("shopping_bag.gif")
        self.penup()
        self.goto(x,y)
        
    def destroy(self):
        self.goto(-3000,2000)
        self.hideturtle()
        
class Home(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("home.gif")
        self.penup()
        self.goto(x,y)
        
    def destroy(self):
        self.goto(-4000,2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("corona.gif")
        self.penup()
        self.goto(x,y)
        self.direction= random.choice(["up", "down", "left", "right"]) #Random motion of enemy 
        
    def move(self):
        if self.direction =="up": dx, dy = 0 , 24                      
        elif self.direction == "down": dx, dy = 0 , -24
        elif self.direction == "left": dx, dy = -24, 0
        elif self.direction == "right": dx, dy = 24, 0
        else: dx, dy = 0, 0     
        if self.is_close(player): #If the player is in the proximity of virus, the virus will detect
                                  #its presence and move in that direction. (is_close function is made
                                  #below. 
            if player.xcor()<self.xcor():self.direction= "left"
            if player.xcor()>self.xcor():self.direction="right"
            if player.ycor()<self.ycor():self.direction="down"
            if player.ycor()>self.ycor():self.direction="up"  
                
        move_to_x,move_to_y = self.xcor() + dx, self.ycor() + dy     #Calculate the spot
        if (move_to_x, move_to_y) not in walls:     self.goto(move_to_x, move_to_y) #we dont want enemy to pass through the wall
        else:
            self.direction= random.choice(["up", "down", "left", "right"])#We will randomly choose another direction
        turtle.ontimer(self.move, t= random.randint(100, 300))            #100 - 300 ms
        
    def is_close(self,other): #if distance is less than 75 than it would be considered that the virus is in close proximity to the human   
        distance= math.sqrt(((self.xcor()-other.xcor())**2)+((self.ycor()- other.ycor())**2))
        if distance< 75: return True
        else: return False
        
    def destroy(self):
        self.goto(-6000,2000)
        self.hideturtle()    
        
class Score(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(-600, 280)
        self.write("Precautionary Points: {}".format(0), align="left", font=("Times New Roman", 20, "bold"))
        self.hideturtle()
class Levelbar(turtle.Turtle):
     def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(500, 280)
        self.write("Level: {}".format(0), align="left", font=("Times New Roman", 20, "bold"))
        self.hideturtle()

class Die(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()


class End(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
class Infected_and_normal(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("blue_man_left.gif")
        self.penup()
        self.goto(x,y)
        self.direction= random.choice(["up", "down", "left", "right"]) #Random motion of enemy 
        
    def move(self):
        if self.direction =="up": dx, dy = 0 , 24                          
        elif self.direction == "down": dx, dy = 0 , -24
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
        else:  #We will randomly choose another direction
            self.direction= random.choice(["up", "down", "left", "right"])
        turtle.ontimer(self.move, t= random.randint(100, 300)) #100 - 300 ms
        
    def is_collision(self, something): #checking the distance to see if they are colse enough to consider a collision
        distance = math.sqrt(((self.xcor()-something.xcor())**2) + ((self.ycor()-something.ycor())**2))
        if distance<5 and (something.shape()=="corona.gif" or (something.shape()=="red_man_left.gif" or something.shape()=="red_man_red.gif")):
            return True
        
    def change(self):
        if self.shape()=="blue_man_right.gif":
            self.shape("red_man_right.gif")
        if self.shape()=="blue_man_left.gif":
            self.shape("red_man_left.gif")
        if self.shape()=="blue_man_right.gif":
            self.shape("red_man_right.gif")
        if self.shape()=="blue_man_left.gif":
            self.shape("red_man_left.gif") 
    
    def destroy(self):
        self.goto(-7000,2000)
        self.hideturtle()
level_1 =[
    "                         C",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXXXXT     N     XXXX      XXE   XXXXXX       X", 
"X  XXXXXX   XXXXXX  XXXXX   XXXXX  N XXXXXX   XXX X",
"X       XX  XXXXXX  XXXXX   XXXXX  XXXXXXXX   XXX X",
"X      MXX  XXX            XXXXXX           NXXXX X",
"XXXXXX  XX  XXXXXX         XXXXXX   XXXXXX  XXXXXXX",
"XXXXXX  XX  XXXXXX  XXXXX T         XXXXXX    XXXXX",
"XXXXXX  XX    XXXX  XXXXXXXXXXXXX   XXXXXXX   XXXXX",
"XN XXX        XXXX   XXXXXXXXXX    XXXXXXXX      XX",
"X  XXX  XXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXX     NXX",
"X         XXXXXXXXXXXXXXXN         XXXXX      XXXXX",
"XE               XXXXXXXX    XXXXXXXXXXXM XXXXXXXXX",
"XXXXXXXXXXXX     XXXXX     XXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXX  XXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXX  XXXXXXXXXX                      XXXXXXXXXXXXXX",
"XXX                     XXXXXXXX     XXXXX     XXXX",
"XXX         XXXXXXXXXXXXXXXXXXXXXX   XXXXX   XXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX     XXXX   XXXXX   XXXXXX",
"XXXXXXXXXX G            X                    XXXXXX",
"XX  XXXXXX                    XXXXXXXXXXXXXXXXXXXXX",
"XX  XXXXXXXXXXXXXX  XXXXXXXX       XXXXXXXXXXXXXXXX",
"XX  NXXXXXXXXXXXXX  XXXXX     XXXXXXXXXXXXXXXXXXXXX",
"XXE                        X                     HX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
 ]
level_2=[    
"                          C",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXP           SXX      XXN                        X",
"XX             XX      XXXX  XXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXX  XXXXXXXXXX         X               XX  X",
"XXXXXXXXX  XXXXXXXXXX  XX  XXXXXXXXXXXXXXXXXXXXXT X",
"XX                     XX  XN                XXX  X",
"X                          X  XXXXXXXXXXXXX  XXX  X",
"X   XXXXXXXXXXX   XXXXXXX  X  X  X        XN      X",
"XXE      XX       X        X  X  XXXX  X  X  XX   X",
"XX       XX       XX   XX  X           X  X  XX   X",
"XXXXXX   XX            XXXXX  XXXXXXXXXXXXX  XX  XX",
"XXN      XXN           XXX    XN             XX   X",
"XXXXXXXXXXX  XXXXXXXXXXXXXXXXXX  XXXXXXXXXX  XXX  X",
"XXXXXXXXXXXE XXXXXXXXXXXXX       X     X  X  XXX  X",
"X     XX               XX  X  XXXX  X  X  X  XX   X",
"XM    XX                   X  X     X     X  XX  XX",
"XXXX  XX       XXXXXXXXXX  X  X  XXXXXXXXXX  XX  XX",
"X     XX       XXXXXXXXXX  X  X  XXX        XXX  XX",
"X   XXXXXXXXX  XX                XXX        XXXE XX",
"X              XX      XXXXXXXX     XXXXXXX    X XX",
"XN          XXXXXXX    XXG   XX    XX    XX    X XX",
"XXXXXXXXXX  XXXXXXXE         XXXXX    XX    XX   XX",
"XX  XX                 XXXX          XX          HX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]
level_3 =[
"                         C",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XP              TXN E                             X",
"X  XXXXXXXXXX  XXXXXXXXXXXXX  XXXXXXX  XXXXXXXXXXXX",
"Xs          X  X    X         X               XX  X",
"X  XXXXXXX  X  X    X   X  XXXXXXXX        XXXXXT X",
"X  XM    X  X  X    X   X   X                XXX  X",
"X  X  X  X  X  X  XXXX  X  X  XXXXXXXXXXXXX  XXX  X",
"X  X  X  X  X  XN X  X  X  X  X  X        XN      X",
"X  X  XXXX  X  X  X  XXXX  X  X  XXXX  X  X  XX   X",
"X  X     X  XV             X           X  X  XX  XX",
"X  X  X  X  X  X XXXXXXXX  XXXXXXXXXXXXX  XX XX  XX",
"XN    X  XG    X        X     XN             XX   X",
"XXXX  X  XXXXXXXXXX     XXXXXXX  XXXXXXXXXX  XXX  X",
"X  X  X                 X  XE    X     X  X  XXX  X",
"X  X  XXXX  XXXXXXXXXXXXX  X  XXXX  X  X  X  X    X",
"X  X  X     X     X     X  X  X     X     X  XN   X",
"X  X  X  XXXXXXX  XXXX  X  X  X  XXXXXXXXXX  X    X",
"XM                      X  X  X  X      X    X   XX",
"X XXXXXX N           X     X  X  X      X   XX E XX",
"X XXXXXX XXXXXX XXXXXXXXX    XX XX      XXXXXXX  XX",
"X X    X    XXXEX     XXXXXXXXX                  XX",
"X XXXX XXXX XXX X XXX XXX    XX    XX    XX XX   XX",
"X XXXX    X     X XXX XXX XX XXXXXXXX XX XX XX   XX",
"X     XX XXXXXX XXXX     XX          XX    XXXX  HX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 ]
#In the list for levels. we are keeping the first element of the list as empty string so that it is easier for us to call levels i.e levels[1] will call level one. If we donot do this step levels[0] would mean the 1st level. This step is therefore done just for the sake of our simplification and is hence not mandatory.
levels, treasures, masks, enimies, homes, stethoscopes, gloves, dots, shopping,infected_and_normal = ["", level_1, level_2, level_3], [], [],[], [], [], [], [], [], []
def setup_maze(level):
    global end_x, end_y, life
    for y in range(len(level)):
        for x in range(len(level[y])):
            character=level[y][x]
#now we will get the character at each x,y coordinate we will calculate the screens x,y coordinate for this coordinates note that the screen starts from 0,0 and our maze is 600 by 600 so the right most coordinate will be -288,288 because each box is of size 24.
            screen_x, screen_y = -588 + (x*24), 288 - (y*24)
            if character == "X" : #X == Wall
                pen.goto(screen_x, screen_y)
                pen.shape("wall2.gif")
                pen.stamp()
                walls.append((screen_x, screen_y))    #add coordinates to walls list
            if character == " " or character == "H": path.append((screen_x, screen_y)) # add " " and H to path list #This is done for the sake of BFS so that BFS tracks from empty path to home   
            if character== "S":  stethoscopes.append(Stethoscope(screen_x, screen_y))
            if character == "P":
                start_x , start_y, life = screen_x,screen_y, True 
                player.goto(screen_x,screen_y)
            if character== "M": masks.append(Mask(screen_x, screen_y))
            if character== "N": infected_and_normal.append(Infected_and_normal(screen_x, screen_y))
            if character== "T": treasures.append(Treasure(screen_x, screen_y))
            if character== "G": gloves.append(Gloves(screen_x, screen_y))
            if character== "E": enimies.append(Enemy(screen_x, screen_y))
            if character=="V": shopping.append(Shopping_Bag(screen_x,screen_y))
            if character =="C":
                pen.goto(screen_x, screen_y)
                pen.shape("title.gif")
                pen.stamp()
            if character == "H":
                end_x , end_y = screen_x, screen_y
                homes.append(Home(screen_x, screen_y))
    return end_x, end_y 

#we are creating class instances. so if we use pen it calls the class Pen
pen, all_paths, shortest_path, die, score, levelbar, player, end= Pen(), All_Paths(), Shortest_Path(), Die(), Score(),Levelbar(), Player(), End()
collided, walls, path, visited, frontier, solution=[], [], [], set(), deque(), {}#solution dictionary
life=False
end_x, end_y = setup_maze(levels[1])
maze="level1"
levelbar.clear()
levelbar.goto(500, 280)
levelbar.write("Level: 1", align="left", font=("Times New Roman", 20, "bold"))
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
    if x>=270 and x<=320 and y>=280 and y<=310: # borders of button
        
        if gold>=50: # if the player has not died
            flag=True
            #solution={}
            current_pos_x, current_pos_y = player.pos()
            #print("c:",current_pos_x,current_pos_y)
            #print("e:",end_x, end_y)
            search(current_pos_x, current_pos_y)
            window.tracer(0)
            backRoute(end_x, end_y, current_pos_x, current_pos_y)
            starting_time = time.time()
            window.tracer(0)
        else:
            print('you donot have enough Precautionary points')
def button_playagain(x,y):
    global player
    global maze
    if x>=-70 and x<=70 and y>=-100 and y<=-60:
        walls.clear()
        pen.clear()
        for treasure in treasures:          treasure.destroy()
        for mask in masks:                  mask.destroy()
        for enemy in enimies:               enemy.destroy()
        for home in homes:                  home.destroy()
        for glove in gloves:                glove.destroy()
        for infected in infected_and_normal:infected.destroy()
        for stethoscope in stethoscopes:
            stethoscope.destroy()
            stethoscopes.remove(stethoscope)
        for s in shopping:
            s.destroy()
            shopping.remove(s)
        #solution={}
        #frontier=[]
        player.destroy()
        die.clear()
        turtle.clear()
        player.clear()
        gold=0
        score.write("Precautionary Points: {}".format(gold), align="left", font=("Times New Roman", 20, "bold"))
        maze="level1"
        levelbar.clear()
        levelbar.goto(500, 280)
        levelbar.write("Level: 1", align="left", font=("Times New Roman", 20, "bold"))
        player=Player()
        turtle.hideturtle() #dont see the turtle that is drawing the button 
        button()
        end_x, end_y = setup_maze(levels[1])
        turtle.hideturtle()
        turtle.onscreenclick(button_click,1)        #1 means right click 0 means left click 
        turtle.listen() 
        turtle.onkeypress(player.go_left, "Left")            #Quotations show the arrow key on keyboard 
        turtle.onkeypress(player.go_right, "Right")
        turtle.onkeypress(player.go_down, "Down")
        turtle.onkeypress(player.go_up, "Up")
        for enemy in enimies:   turtle.ontimer(enemy.move, t=250) #It will move after every 250 milisecond
        for infected in infected_and_normal: turtle.ontimer(infected.move, t=250)
    
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
        shortest_path.goto(solution[x, y])         
        stamps.append(shortest_path.stamp())
        x, y = solution[x, y]               # "key value" now becomes the new key

def backRoute1():
    global stamps
    global visited
    global solution
    for i in stamps: shortest_path.clearstamp(i)

    shortest_path.hideturtle()
    stamps=[]
    solution={}
    visited=set()
    
turtle.onscreenclick(button_click,1)        #1 means right click 0 means left click

#The functions that we created for up/down/left/right now we need to call it on key i.e. Keyboard Binding

turtle.listen() 
turtle.onkeypress(player.go_left, "Left")            #Quotations show the arrow key on keyboard
turtle.onkeypress(player.go_right, "Right")
turtle.onkeypress(player.go_down, "Down")
turtle.onkeypress(player.go_up, "Up")

#turns off screen updates
#window.tracer(0)

for enemy in enimies: turtle.ontimer(enemy.move, t=250) #It will move after every 250 milisecond    
for infected_n_normal in infected_and_normal: turtle.ontimer(infected_n_normal.move, t=250) #It will move after every 250 milisecond

def dead():
    die.goto(-10,-50)
    die.write("PLAYER DIES!",True, align="center", font=("Arial",30,"bold"))
    die.hideturtle()
    turtle.clear()
    print("Player is Infected!")
    player.destroy()
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
    turtle.goto(-70+10, -100+5)
    turtle.write('Play Again', font=('Arial', 18, 'bold'))
    turtle.onscreenclick(button_playagain,1)

def new():
    walls.clear()
    pen.clear()
    for i in treasures+masks+enimies+gloves+infected_and_normal: i.destroy()
    for stethoscope in stethoscopes:
        stethoscopes.remove(stethoscope)
    for home in homes:
        home.destroy()
        
    player.destroy()
    
flag_1, flag_2=False, False
gold=0
while z==True: #main game loop so that it keeps running
    #check for collision with treasure.we will iterate through treasure list for all the treasure
    if flag==True:
        time_limit = 10
        if time.time() - starting_time >=time_limit:
            backRoute1()
            flag=False
    if flag_1==True:
            time_1 = 3
            if time.time() - starting_time_1 >=time_1:
                end.clear()
                flag_1=False
    for col in collided:
            time_2 = 6
            if time.time() - col[1] >=time_2:
                col[0].change()
    if not z: break
        
    for treasure in treasures:
        if  player.is_collision(treasure):
            gold += 50         
            score.clear()
            score.goto(-600, 280)
            score.write("Precautionary Points: {}".format(gold), align="left", font=("Times New Roman", 20, "bold"))
            print("Precautionary Points: {}".format(gold))
            treasure.destroy()
            treasures.remove(treasure)
    for bag in shopping:
        if  player.is_collision(bag):
            gold += 80     
            score.clear()
            score.goto(-600, 280)
            score.write("Precautionary Points: {}".format(gold), align="left", font=("Times New Roman", 20, "bold"))
            print("Precautionary Points: {}".format(gold))
            bag.destroy()
            shopping.remove(bag)
            
    for stethoscope in stethoscopes:
        if player.is_collision(stethoscope):
            gold += 80                                
            score.clear()
            score.goto(-600, 280)
            score.write("Precautionary Points: {}".format(gold), align="left", font=("Times New Roman", 20, "bold"))
            print("Precautionary Points: {}".format(gold))
            stethoscope.destroy()
            stethoscopes.remove(stethoscope)
    for mask in masks:
        if player.is_collision(mask):
            gold += 50
            score.clear()
            score.goto(-600, 280)
            score.write("Precautionary Points: {}".format(gold), align="left", font=("Times New Roman", 20, "bold"))
            print("Precautionary Points: {}".format(gold))
            mask.destroy()
            masks.remove(mask)
    for glove in gloves:
        if player.is_collision(glove):
            gold += 50
            score.clear()
            score.goto(-600, 280)
            score.write("Precautionary Points: {}".format(gold), align="left", font=("Times New Roman", 20, "bold"))
            print("Precautionary Points: {}".format(gold))
            glove.destroy()
            gloves.remove(glove)
            
    for enemy in enimies:
        for infected_n_normal in infected_and_normal:
            if infected_n_normal.is_collision(enemy) == True: collided.append((infected_n_normal, time.time()))
        if player.is_collision(enemy):
            gold-=20
            print("Precautionary Points: {}".format(gold))
            score.clear()
            score.goto(-600, 280)
            score.write("Precautionary Points: {}".format(gold), align="left", font=("Times New Roman", 20, "bold"))
            if gold<0:
                gold=0
                score.clear()
                score.goto(-600, 280)
                score.write("Precautionary Points: {}".format(gold), align="left", font=("Times New Roman", 20, "bold"))
                dead()
                
    for infected_n_normal in infected_and_normal:
        if player.is_collision(infected_n_normal) and (infected_n_normal.shape()=="red_man_left.gif" or infected_n_normal.shape()=="red_man_right.gif"):
            gold-=20
            print("Precautionary Points: {}".format(gold))
            score.clear()
            score.goto(-600, 280)
            score.write("Precautionary Points: {}".format(gold), align="left", font=("Times New Roman", 20, "bold"))
            if gold<0:
                gold=0
                score.clear()
                score.goto(-600, 280)
                score.write("Precautionary Points: {}".format(gold), align="left", font=("Times New Roman", 20, "bold"))
                dead()
        for i in infected_and_normal:
            if i.is_collision(infected_n_normal) ==True:
                collided.append((i, time.time()))
                
    for home in homes:
        if player.is_collision(home) and maze=="level3":
            if len(shopping)!=0:
                starting_time_1=time.time()
                end.goto(-10,50)
                end.write("You need to collect your grocery bag before reaching home.",True, align="center",  font=("Arial",20,"bold"))
                end.hideturtle()
                flag_1=True       
            else:
                die.clear()
                die.goto(-10,50)
                die.write("Congratulations! \nYou have saved yourself from the virus",True, align="center", font=("Arial",20,"bold"))
                die.hideturtle()
                player.destroy()
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
                turtle.goto(-70+10, -100+5)
                turtle.write('Play Again', font=('Arial', 18, 'bold'))
                turtle.onscreenclick(button_playagain,1)
                    
        if player.is_collision(home):
            if maze=="level1":
                new()
                print ("level passed")
                player=Doctor()
                end_x, end_y = setup_maze(levels[2])
                score.clear()
                score.goto(-600, 280)
                gold=0
                score.write("Precautionary Points: {}".format(gold), align="left", font=("Times New Roman", 20, "bold"))
                print("Precautionary Points: {}".format(gold))
                maze="level2"
                levelbar.clear()
                levelbar.goto(500, 280)
                levelbar.write("Level: 2", align="left", font=("Times New Roman", 20, "bold"))
                turtle.onscreenclick(button_click,1)        #1 means right click 0 means left click 
                turtle.listen() 
                turtle.onkeypress(player.go_left, "Left")            #Quotations show the arrow key on keyboard
                turtle.onkeypress(player.go_right, "Right")
                turtle.onkeypress(player.go_down, "Down")
                turtle.onkeypress(player.go_up, "Up")
                for enemy in enimies:
                    turtle.ontimer(enemy.move, t=250)
                for infected in infected_and_normal:
                    turtle.ontimer(infected.move, t=250) #It will move after every 250 milisecond
            elif maze=="level2":
                if len(stethoscopes)!=0:
                   starting_time_1=time.time()
                   end.goto(-10,50)
                   end.write("Doctor you need to collect your stethoscope first, before reaching hospital",True, align="center", font=("Arial",20,"bold"))
                   end.hideturtle()
                   flag_1=True
                else:   
                    new()
                    print ("level passed")
                    player=Man()
                    end_x, end_y = setup_maze(levels[3])
                    score.clear()
                    score.goto(-600, 280)
                    gold=0
                    score.write("Precautionary Points: {}".format(gold), align="left", font=("Times New Roman", 20, "bold"))
                    print("Precautionary Points: {}".format(gold))
                    maze="level3"
                    levelbar.clear()
                    levelbar.goto(500, 280)
                    levelbar.write("Level: 3", align="left", font=("Times New Roman", 20, "bold"))
                    turtle.onscreenclick(button_click,1)        #1 means right click 0 means left click 
                    turtle.listen() 
                    turtle.onkeypress(player.go_left, "Left")            #Quotations show the arrow key on keyboard
                    turtle.onkeypress(player.go_right, "Right")
                    turtle.onkeypress(player.go_down, "Down")
                    turtle.onkeypress(player.go_up, "Up")
                    for enemy in enimies:turtle.ontimer(enemy.move, t=250)
                    for infected in infected_and_normal: turtle.ontimer(infected.move, t=250) #It will move after every 250 milisecond

    #Update screen
    window.update()
turtle.bye()
