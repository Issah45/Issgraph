import turtle

def keyPress(func, key):
	turtle.onkeypress(func, key)

def keyRelease(func, key):
	turtle.onkeyrelease(func, key)

def keyDown(func, key):
	turtle.onkey(func, key)

def bindKeys():
	turtle.listen()