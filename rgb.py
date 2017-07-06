#!/usr/bin/env python
from gameoflife import GameOfLife
import curses, time

framerate = 15

screen = curses.initscr()
curses.start_color()
curses.noecho()
curses.cbreak()
screen.keypad(1)
screen.nodelay(1)
curses.curs_set(0)
height, width = screen.getmaxyx()

game = GameOfLife(width=(width-1) * 3, height=height)
game.random()

curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_GREEN)
curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_CYAN)
curses.init_pair(4, curses.COLOR_RED, curses.COLOR_RED)
curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA)
curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_WHITE)

try:
	while True:
		# screen.clear()
		game.update()
		c = screen.getch()
		if c == ord('q'):
			break
		elif c == ord('r'):
			game.random()
		elif c == ord('c'):
			game.clear()
		elif c == ord('g'):
			game.glider()
		for y in range(height):
			for x in range(width - 1):
				count = (4 * game.grid[3 * x][y]) + (2 * game.grid[3 * x + 1][y]) + game.grid[3 * x + 2][y]
				# if count > 0:
				screen.addstr(y, x, ' ', curses.color_pair(count if count != 0 else 8))
		screen.refresh()
		time.sleep(1.0 / framerate)
finally:
	curses.endwin()

