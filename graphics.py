import turtle

class Graphics():
	def __init__(self):
		self.width = 800
		self.height = 600
		self.tk = turtle.Screen()
		self.tk.title("IssGraph Window")

	def render(self):
		self.tk.mainloop()

	def screenSize(self, w, h):
		self.width, self.height = w, h
		self.tk.setup(self.width, self.height)

	def heading(self, head):
		self.tk.title(head)

	def paintBg(self, color):
		self.tk.bgcolor(color)