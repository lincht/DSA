import turtle
import numpy as np


TREE_COLOR = 'green'


def tree(branch_len, t):
    """Recursively draw a tree."""
    
    # Base case
    if branch_len > 5:
        
        # Set branch thickness proportional to branch_len
        t.pensize(branch_len * 0.1)
        
        # Use leaf color if branch_len gets very short
        if branch_len <= 15:
            t.color('yellowgreen')
        
        t.forward(branch_len)
        
        # Select branch angles at random
        rangle = np.random.randint(15, 45)
        langle = np.random.randint(15, 45)
        
        # Select branch decrements at random
        rdelta = np.random.randint(5, 15)
        ldelta = np.random.randint(5, 15)
        
        # Right branch
        t.right(rangle)
        tree(branch_len-rdelta, t)
        
        # Left branch (need to undo right angle)
        t.left(rangle + langle)
        tree(branch_len-ldelta, t)
        
        t.right(langle)
        t.backward(branch_len)
        
        # Reset color
        t.color(TREE_COLOR)


def main():
    
    # Create turtle
    t = turtle.Turtle()
    # Create a singleton screen
    scr = turtle.Screen()
    
    # Initial setting
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color(TREE_COLOR)
    
    # Draw tree
    tree(75, t)
    
    # Put turtle into a wait mode until you click inside the window
    scr.exitonclick()


if __name__ == '__main__':
    main()
