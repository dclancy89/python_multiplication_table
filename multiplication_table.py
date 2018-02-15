for y in range (0,13):
	rowstr = ""

	for x in range(0, 13):
		if x == 0 and y == 0:
			rowstr += "x"
			rowstr += " "
		elif x == 0 and y != 0:
			rowstr += str(y)
			rowstr += " "
		elif x != 0 and y == 0:
			rowstr += str(x)
			rowstr += " "
		else:
			rowstr += str(x * y)
			rowstr += " "
	print rowstr
