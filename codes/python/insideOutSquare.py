import turtle  #Inside_Out
wn = turtle.Screen()
wn.bgcolor("light green")
skk = turtle.Turtle()
skk.color("blue")
 
def myFunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size = size + 5
 
myFunc(6)
myFunc(26)
myFunc(46)
myFunc(66)
myFunc(86)
myFunc(106)
myFunc(126)
myFunc(146)
myFunc(166)
myFunc(186)
myFunc(206)
