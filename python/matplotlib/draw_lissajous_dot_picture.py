""" Draws a Lissajous figure with numbered, labeled dots. """
"""Utilizes a class Ldot (has dot coordinates, label and more"""

import turtle
from turtle import *
import math
import dot_labeler
import ldot
import os		# 20220611

global screen_edge



def draw_figure(t):
	"""Computes locations of (maxpoints) dots; draws them, with numeric labels"""
	global screen_edge
	oldpoints = []
	dotradius = 5
	maxpoints = 300
	fontsize = 12
	i2 = 0
	t.speed(10)
	t.penup()
	t.home()
	for i in range(maxpoints + 1):
		t.penup()
		newpoint = Lissajous_point( 2 * float(i) / maxpoints )
		if not point_too_close( newpoint, oldpoints, dotradius ):
			t.goto( newpoint )
			t.pendown()
			t.dot(dotradius)
			t.penup()
			i2 = i2 + 1
			oldpoints.append( newpoint )
			dot_labeler.draw_label( t,i2 )
	t.penup()
	t.home()

def Lissajous_point(x):
	"""Computes the coordinates of a dot, based on its index"""
	global screen_edge
	return [ screen_edge * 0.4 * math.sin(5 * math.pi * x), \
		screen_edge * 0.4 * math.sin( 4 * math.pi * x ) ]

def point_too_close( newpoint, oldpoints, dotradius ):
	"""Uses only distance between dots; ignores labels"""
	for oldpoint in oldpoints:
		if point_distance(oldpoint, newpoint) < 3 * dotradius:
			return True
	return False

def point_distance(oldpoint, newpoint):
	"""Computes Pythagorean distance between two dots"""
	return math.sqrt( (oldpoint[0]-newpoint[0])**2 + \
		(oldpoint[1]-newpoint[1])**2 )

def my_turtle_setup():
	""" sets up Turtle, Screen objects; opens screen """
	global screen_edge #, dist_from_center
	screen_edge = 900
	turtle.setup(screen_edge, screen_edge, 250, 50)
	t, s = [ Turtle(), Screen() ]
	s.mode("logo")
	t.penup()
	t.hideturtle()
	turtle.clear()
	turtle.title("Lissajous Dot-Picture")
	turtle.radians()
	return [t, s]

def erase_center(t):
	""" Erase the pesky persistent turtle at the center of the canvas"""
	t.home()
	t.color("white")
	t.dot(25)
	t.color("black")

def bringTerminalForward():
		os.system('osascript -e \'tell application "System Events" to ' + \
				'tell process "Terminal" to set frontmost to true\'')

#  Main  ######################################################################
t, s = my_turtle_setup()
erase_center(t)
draw_figure(t)
bringTerminalForward()
s.mainloop()


