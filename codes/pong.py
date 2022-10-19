###########
# Imports #
###########

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import simpleplot
import random

#############
# Variables #
#############

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

####################
# Helper functions #
####################

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    """Initializes tha ball"""
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if right: ball_vel = [random.randrange(4, 8), -5]
    else: ball_vel = [-random.randrange(3, 6), -5]

def paddle_init():
    """Initializes the paddles"""
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    paddle1_pos = [[PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT], [PAD_WIDTH, HEIGHT / 2 + HALF_PAD_HEIGHT]]
    paddle2_pos = [[WIDTH - PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH, HEIGHT / 2 + HALF_PAD_HEIGHT]]
    paddle1_vel = 0
    paddle2_vel = 0

def calculateMid(paddle):
    """Calculates midpoint for each paddle, much easier to move the paddle this way"""
    midpoint = int(paddle[0][1] + paddle[1][1]) / 2
    return midpoint

def midpointToCoord(midpoint, paddle):
    """Converts the midpoint back to line coordinates."""
    paddle[0][1] = midpoint - HALF_PAD_HEIGHT
    paddle[1][1] = midpoint + HALF_PAD_HEIGHT
    return paddle[0][1], paddle[1][1]

def checkSides():
    """Checks for the north and south wall and changes the velocity."""
    global ball_pos, ball_vel
    if (ball_pos[1] >= (HEIGHT - BALL_RADIUS) ): ball_vel[1] = - ball_vel[1]
    if (ball_pos[1] <= (BALL_RADIUS) ): ball_vel[1] = - ball_vel[1]

def checkGutters():
    """Checks for the gutters and moves the ball."""
    global ball_pos, ball_vel
    global score1, score2
    if (ball_pos[0] >= (WIDTH)):
        ball_init(False)
        score1 += 1
#        print str(score1)+" : "+str(score2)
    if (ball_pos[0] <= (BALL_RADIUS)):
        ball_init(True)
        score2 += 1
#        print str(score1)+" : "+str(score2)

def checkPaddles():
    """Checks for the Paddles and moves the ball."""
    global ball_pos, ball_vel, paddle1, paddle2
    if (ball_pos[1] in range(paddle1 - HALF_PAD_HEIGHT, paddle1 + HALF_PAD_HEIGHT)) and (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS):
        ball_vel[0] = - ball_vel[0]
    elif (ball_pos[1] in range(paddle2 - HALF_PAD_HEIGHT, paddle2 + HALF_PAD_HEIGHT)) and (ball_pos[0] >= WIDTH - (PAD_WIDTH + BALL_RADIUS)):
        ball_vel[0] = - ball_vel[0]

def movePaddles():
    """Moves the paddles according to the current paddle velocity."""
    global paddle1, paddle2, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    paddle1 = calculateMid(paddle1_pos)
    if (paddle1_pos[0][1] > 0) and (paddle1_pos[1][1] < HEIGHT):
        paddle1 = paddle1 + paddle1_vel
    else: paddle1 = paddle1 - (2 * paddle1_vel)
    paddle1_pos[0][1] = midpointToCoord(paddle1, paddle1_pos)[0]
    paddle1_pos[1][1] = midpointToCoord(paddle1, paddle1_pos)[1]

    paddle2 = calculateMid(paddle2_pos)
    if (paddle2_pos[0][1] > 0) and (paddle2_pos[1][1] < HEIGHT):
        paddle2 = paddle2 + paddle2_vel
    else: paddle2 = paddle2 - (2 * paddle2_vel)
    paddle2_pos[0][1] = midpointToCoord(paddle2, paddle2_pos)[0]
    paddle2_pos[1][1] = midpointToCoord(paddle2, paddle2_pos)[1]

def moveBall():
    """Moves the ball."""
    global ball_pos, ball_vel
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

############
# Handlers #
############

# define event handlers
def init():
    """Restart button uses this function"""
    global score1, score2  # these are ints
    ball_init(True)
    paddle_init()
    score1 = 0
    score2 = 0

def draw(c):
    """Draw handler"""
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel

    # update paddle's vertical position, keep paddle on the screen
    movePaddles()

    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # draw paddles
    c.draw_line(paddle1_pos[0], paddle1_pos[1], PAD_WIDTH, "White")
    c.draw_line(paddle2_pos[0], paddle2_pos[1], PAD_WIDTH, "White")

    # update ball
    checkSides()
    checkGutters()
    checkPaddles()
    moveBall()

    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    c.draw_text(str(score1), ((WIDTH / 2) - PAD_HEIGHT, (HEIGHT / 2) - PAD_HEIGHT), 45, "White")
    c.draw_text(str(score2), ((WIDTH / 2) + PAD_HEIGHT, (HEIGHT / 2) - PAD_HEIGHT), 45, "White")

def keydown(key):
    """Changes the velocity according to the key pressed."""
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -2
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 2
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -2
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 2

def keyup(key):
    """Sets the velocity back as soon as the user releases the key."""
    global paddle1_vel, paddle2_vel
    if (key == simplegui.KEY_MAP["w"]) or (key == simplegui.KEY_MAP["s"]):
        paddle1_vel = 0
    if (key == simplegui.KEY_MAP["up"]) or (key == simplegui.KEY_MAP["down"]):
        paddle2_vel = 0

######
# UI #
######

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)

########
# Main #
########

# start frame
init()
frame.start()
