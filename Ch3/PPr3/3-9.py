import turtle

# define constants relating to screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Define constants relating to target
TARGET_WIDTH = 25
TARGET_HEIGHT = 25
TARGET_BL = (100, 250)

# Define constants relating to the projectile
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1

# Define directions
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180


def draw_target(width):
    turtle.penup()
    turtle.goto(TARGET_BL)
    turtle.pendown()
    direction = 0
    while direction < 360:
        turtle.forward(width)
        direction = direction + 90
        turtle.setheading(direction)


def center():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(EAST)
    turtle.showturtle()
    turtle.speed(PROJECTILE_SPEED)


def launch(angle, force):
    distance = force * FORCE_FACTOR
    turtle.pendown()
    turtle.setheading(angle)
    turtle.forward(distance)


def check_won():
    if (TARGET_BL[0] <= turtle.xcor() <= (TARGET_BL[0] + TARGET_WIDTH) and
            TARGET_BL[1] <= turtle.ycor() <= (TARGET_BL[1] + TARGET_WIDTH)):
        return True
    else:
        return False


if __name__ == '__main__':
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    turtle.hideturtle()
    turtle.speed(0)
    draw_target(TARGET_WIDTH)
    center()

    # Get user inputs
    projectile_angle = float(input('Enter projectile angle: '))
    projectile_force = float(input('Enter projectile force: '))

    # Launch turtle
    launch(projectile_angle, projectile_force)
    if check_won():
        print('You win!')
    else:
        print('You lose!')
    turtle.Screen().exitonclick()
