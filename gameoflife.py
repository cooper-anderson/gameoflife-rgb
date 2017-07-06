#!/usr/bin/env python
from random import random

class GameOfLife(object):
	AREA_DEFAULT = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
	AREA_KNIGHTS = [[-1, -2], [1, -2], [-2, -1], [2, -1], [-2, 1], [2, 1], [-1, 2], [1, 2]]
	def __init__(self, width=16, height=16, rule_min=2, rule_max=3, neighbor_area=None):
		self.width = width
		self.height = height
		self.rule_min = rule_min
		self.rule_max = rule_max
		self.neighbor_area = neighbor_area
		if neighbor_area == None:
			self.neighbor_area = GameOfLife.AREA_DEFAULT
		print self.neighbor_area
		self.grid = [[False for y in range(self.height)] for x in range(self.width)]
	
	def random(self, threshold=.5):
		self.grid = [[random() <= threshold for y in range(self.height)] for x in range(self.width)]

	def clear(self):
		self.grid = [[False for y in range(self.height)] for x in range(self.width)]

	def glider(self):
		self.toggle(1, 0)
		self.toggle(2, 1)
		self.toggle(0, 2)
		self.toggle(1, 2)
		self.toggle(2, 2)

	def toggle(self, x=0, y=0):
		self.grid[x][y] = not self.grid[x][y]

	def count_neighbors(self, x=0, y=0):
		count = 0
		for cell in self.neighbor_area:
			if 0 <= x + cell[0] < self.width and 0 <= y + cell[1] < self.height and self.grid[x + cell[0]][y + cell[1]]:
				count += 1
		return count

	def update(self):
		neighbors = [[self.count_neighbors(x, y) for y in range(self.height)] for x in range(self.width)]
		for x in range(self.width):
			for y in range(self.height):
				count = neighbors[x][y]
				if count < self.rule_min or count > self.rule_max:
					self.grid[x][y] = False
				if count == self.rule_max:
					self.grid[x][y] = True

