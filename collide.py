from issgraph.sprite import Sprite

def collide(x, y, w, h, x2, y2, w2, h2):
	return x < x2+w2 and x2 < x+w and y < y2+h2 and y2 < y+h

def meetPlace(o1: Sprite, o2: Sprite, w1, h1, w2, h2):
	return o1.x < o2.x+(w2 * 25) and o2.x < o1.x+(w1 * 25) and o1.y < o2.y+(h2 * 20) and o2.y < o1.y+(h1 * 25)