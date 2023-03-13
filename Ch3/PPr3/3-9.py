import turtle

# define constants relating to screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Define constants relating to target
TARGET_WIDTH = 25
TARGET_HEIGHT = 25
TARGET_LOCATION = (100,250)

# Define constants relating to the projectile
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1

# Define directions
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

def drawTarget(target_location, width):
    turtle.penup()
    turtle.goto(target_location)
    turtle.pendown()
    direction = 0
    while direction < 360:
        turtle.forward(width)
        direction = direction + 90
        turtle.setheading(direction)



if __name__ == '__main__':
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    turtle.hideturtle()
    turtle.speed(0)
    drawTarget(TARGET_LOCATION, TARGET_WIDTH)
    
    turtle.Screen().exitonclick()
