#Project Description: Using OOP principles and the Turtle Module to create the popular Snake Game 


import turtle #Module that is graphics library that allows you to draw shapes and patterns on the screen
import time #Module to add delays 
import random #Positions food randomly

delay = 0.1

#Score 

score = 0 
high_score = 0 

#Set up the Screen 

wn = turtle.Screen() 
wn.title("Snake Game Ver: Turtle")
wn.bgcolor("Black")
wn.setup(width=600, height =600)
wn.tracer(0) #Turns off the screen updates


#Snake Head (Creating a Turtle Object)
head = turtle.Turtle()
head.speed(0) #Not actual speed but Animation Speed (0 is the fastest animation speed)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "up" 

#Food Object 
food = turtle.Turtle()
food.speed(0) #Not actual speed but Animation Speed (0 is the fastest animation speed)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen Object - Writes Caption of Score at Top

# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup() # Corrected here
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0   High Score: 0", align = "center", font=("Courier", 24, "normal"))


#Functions - Movement of Snake Head
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move(): 
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
 
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
 
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Keyboard Bindings - Binding movement functions to keyboard

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


# Main game loop 

while True: 
    wn.update()

    # Check for collision with the border 
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor()>280 or head.ycor()<-280:
        time.sleep(1) #Game delays for a second then repositions
        head.goto(0,0) #Snake head resets position
        head.direction = "stop" #Snake Head Stops movment

        #Hide the segments 
        for segment in segments: 
            segment.goto(1000,1000) #Moves Grey new segments to off screen so when there's a border collision the segments disappears
        
        #Clear the segments list 
        segments.clear() #Clear the segments list loop so no news segments show up after border collision 

        #Reset the Score 
        score = 0

        pen.clear() #clears previous writing so pen does not write ontop of itself 
        pen.write(f"Score: {score}   High Score: {high_score}", align="center", font=("Courier", 24, "normal")) 

        # Reset the delay 
        delay = 0.1 


    if head.distance(food) < 20: #If head collides with food
        #Move food to random spot
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)

        #Add a segment to snake body
        new_segement = turtle.Turtle()
        new_segement.speed(0)
        new_segement.shape("square")
        new_segement.color("grey")
        new_segement.penup()
        segments.append(new_segement)

        # Shorten the delay 
        delay -= 0.001 

        #Increase score 
        score +=10 
        if score > high_score: 
            high_score = score 

        pen.clear() #clears previous writing so pen does not write ontop of itself 
        pen.write(f"Score: {score}   High Score: {high_score}", align="center", font=("Courier", 24, "normal"))


    # Move the end segments first in reverse order 

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    # Move segment 0 to where the head is 

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check for body collision (we do this after we move - after move() 
    for segment in segments: 
        if segment.distance(head) < 20: 
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            #Hide segments 
            for segment in segments: 
                segment.goto(1000,1000) #Moves Grey new segments to off screen so when there's a body collision the segments disappears
        
            #Clear the segments list 
            segments.clear() #Clear the segments list loop so no news segments show up after body collision 

            #Reset the Score 
            score = 0

            # Reset the delay 
            delay = 0.1 

    time.sleep(delay)

wn.mainloop()