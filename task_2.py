import turtle
import math

def draw_pythagoras_tree(branch_length, angle, level, max_level):
    if level > max_level:
        return
    

    turtle.forward(branch_length)
    

    turtle.left(angle)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, angle, level + 1, max_level)
    

    turtle.right(2 * angle)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, angle, level + 1, max_level)
    

    turtle.left(angle)
    turtle.backward(branch_length)

def main():

    turtle.speed("fastest")
    turtle.left(90)
    

    max_level = int(input("Введіть рівень рекурсії: "))
    

    branch_length = 100
    angle = 45
    
    # Draw tree
    draw_pythagoras_tree(branch_length, angle, 0, max_level)
    
 
    turtle.done()

if __name__ == "__main__":
    main()
