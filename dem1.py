# Step 1: Make all the "turtle" commands available to us.
import turtle

# Step 2: Create a new turtle. We'll call it "bob"
bob = turtle.Turtle()

# Step 3: Move in the direction Bob's facing for 50 pixels

for j in range(18):
    for i in range(3):
        bob.forward(100)
        bob.left(120)
        bob.pencolor((.8, i / 3, j / 18))
        # print(j/36, i/4)
    bob.left(20)

# Step 4: We're done!
turtle.done()