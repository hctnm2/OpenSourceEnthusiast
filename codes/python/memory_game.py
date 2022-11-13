
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

HEIGHT = 100
WIDTH = 800
CARD_HEIGHT = 100
CARD_WIDTH = 50
number_list = [] # list with the numbers
deck = []
exposed = []
cool = []
card_color = "#006400"
text_color = "#006400"
TEXT_SIZE = 28 #px
CARD_LINE_COLOR = "#FF0000"
INIT_STATE = "unflipped"
moves = 0

####################
# Helper functions #
####################

# helper function to initialize globals
def init():
    global deck, number_list, card_color, text_color, exposed, cool, moves
    number_list = [range(1,9) for i in range(2)]
    number_list = number_list[0] + number_list[1]
    random.shuffle(number_list) # Everyday I'm shuffeling
    INIT_STATE = "unflipped"
    i = 0
    cool = []
    moves = 0

    while i < len(number_list):
        text_position = [((i * CARD_WIDTH) + (CARD_WIDTH / 2) -10), CARD_HEIGHT - 40]
        card = [([i*CARD_WIDTH, 0], [(i+1)*CARD_WIDTH, 0], [(i+1)*CARD_WIDTH, CARD_HEIGHT], [i*CARD_WIDTH, CARD_HEIGHT]), 1, CARD_LINE_COLOR, card_color, number_list[i], text_position, text_color, INIT_STATE]
        deck.append(card)
        i += 1

def checkcard():
    global deck, cool
    for card in deck:
        for c in cool:
            if c == card[4] and card[7] == "flipped":
                card[7] = "exposed"

def clean():
    global moves
    for card in deck:
        if card[7] == "flipped":
            card[7] = "unflipped"
    moves += 1

############
# Handlers #
############

# define event handlers
def mouseclick(pos):
    global exposed, cool
    for card in deck:
        if ((card[0][0][0] <= pos[0]) and (card[0][1][0] >= pos[0]) and (card[7] == "unflipped") and len(exposed) < 2):
            card[3] = "#000000"
            card[6] = "#FFFFFF"
            card[7] = "flipped"
            exposed.append(card[4])
            break

        if len(exposed) >= 2:
           exposed = []
           clean()
           break

# cards are logically 50x100 pixels in size
def draw(canvas):
    global deck, exposed, cool, moves
    i = 0
    for card in deck:
        canvas.draw_polygon(deck[i][0], deck[i][1], deck[i][2], deck[i][3])
        if len(exposed) == 0:
            card[3] = "#006400"
            card[6] = "#006400"
        if card[7] == "exposed":
            card[3] = "#000000"
            card[6] = "#FFFFFF"
        canvas.draw_text(str(card[4]), card[5], TEXT_SIZE, card[6])
        i += 1

    if len(exposed) == 2 and exposed[0] == exposed[1]:
            cool.append(exposed[0])
            cool.append(exposed[1])
            exposed.pop()
            exposed.pop()
            moves += 1

    checkcard()
    l.set_text("Moves = " + str(moves))

######
# UI #
######

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")

########
# Main #
########

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
