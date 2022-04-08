import turtle

class Sprite():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.shape = "square"
		self.tk = turtle.Turtle()
		self.tk.penup()

	def run(self, spd=0):
		self.tk.speed(spd)
		self.tk.shape(self.shape)
		self.tk.goto(self.x, self.y)

	def shape(self, shape):
		self.shape = shape
		self.tk.shape(self.shape)

	def penUp(self):
		self.tk.penup()

	def penDown(self):
		self.tk.pendown()

	def multiply(self, w, l):
		self.tk.shapesize(stretch_wid=w, stretch_len=l)

	def penSize(self, size):
		self.tk.pensize(size)

	def penColor(self, color):
		self.tk.pencolor(color)

	def paint(self, color):
		self.tk.color(color)

	def position(self, x, y):
		self.x, self.y = x, y
		self.tk.goto(x, y)

	def changeX(self, change):
		self.x += change
		self.position(self.x, self.y)

	def changeY(self, change):
		self.y += change
		self.position(self.x, self.y)

	def moveForward(self, steps):
		self.tk.forward(steps)

	def moveBackward(self, steps):
		self.tk.backward(steps)

	def move(self, _type, steps):
		if _type == "Forward":
			self.moveForward(steps)
		else:
			self.moveBackward(steps)

	def turnRight(self, turn):
		self.tk.right(turn)