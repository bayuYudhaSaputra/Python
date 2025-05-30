import turtle

# prompt the user for inputting two point
x1, y1 = eval(input("Enter x1 and y1 for point 1 : "))
x2, y2 = eval(input("Enter x2 and y2 for point 2 : "))

# Compute the distance
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Display two points and the connecting line
turtle.penup()
turtle.goto(x1 , y1) # move to (x1, y1)
turtle.pendown()
turtle.write("Point 1")
turtle.goto(x2, y2) # Draw a line to (x2, y2)
turtle.write("Point 2")

# Move to the center point of the line
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.write(distance)

turtle.done()