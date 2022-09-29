import turtle, math

def draw_label(t,i):
	"""Draw a label for a given point."""
	# Position of label relative to point depends on point's location.
	turtle.radians()
	position = t.position()
	fontsize = 12
	
	# Calculate the point's angle
	if position[0] == 0.0 and position[1] == 0.0:
		angle = 0.0
	else:
		if position[0] == 0.0:
			angle = math.pi/2 if position[1] >= 0.0 else 3.0 * math.pi/2
		else:
			angle0 = math.asin(position[1]/math.sqrt(position[0]**2 + position[1]**2))
			if position[1] >= 0.0:
				angle = angle0 if position[0] >= 0.0 else math.pi - angle0
			else:
				angle = math.pi - angle0 if position[0] <= 0.0 else \
					2*math.pi + angle0

	if angle < math.pi/4:
		t.goto(position[0] + fontsize/3, position[1] - fontsize * 0.6)
		t.write(' ' + str(i), font=("Menlo", fontsize, "normal"))
	elif angle < 3 * math.pi/4:
		t.goto(position[0], position[1] + fontsize * 0.4)
		t.write(str(i), align='center', font=("Menlo", fontsize, "normal"))
	elif angle < 5 * math.pi/4:
		t.goto(position[0] - fontsize/3, position[1] - fontsize * 0.6)
		t.write(str(i) + ' ', align='right', font=("Menlo", fontsize, "normal"))
	elif angle < 7 * math.pi/4:
		t.goto(position[0], position[1] - 1.8 * fontsize)
		t.write(str(i), align='center', font=("Menlo", fontsize, "normal"))	
	else:
		t.goto(position[0] + fontsize/3, position[1] - fontsize * 0.6)
		t.write(' ' + str(i-4), font=("Menlo", fontsize, "normal"))
