"""Meta-trees and meta-dragons."""


from turtle import Turtle
from sys import setrecursionlimit
setrecursionlimit(10000)


def tree(length):
    """
    Write a recursive turtle program to draw a binary tree.

    Start with a trunk 200px tall.
    Each new branch should be 3/5 as big as its trunk.
    Minimum branch size is 5px.
    Move turtle with: t.forward(), t.left(), t.right(), tree()

    :param length: height of the trunk or leaf
    """
    if length < 5:
        return
    else:
        t.forward(length)
        t.left(120)
        tree(3 * length / 5)
        t.right(120)
        tree(3 * length / 5)
        t.left(120)
        t.backward(length)

        # t.right(120)
        # tree(shrink * length)
        # t.right(60)
        # tree(shrink * length)
        # t.left(45)
        # t.backward(length)


def apply_dragon_rules(string):
    """
    Write a recursive function that replaces characters in string.

    Like so:
        "a" -> "aRbFR"
        "b" -> "LFaLb"
    apply_dragon_rules("a") -> "aRbFR"
    apply_dragon_rules("aa") -> "aRbFRaRbFR"
    apply_dragon_rules("FRaFRb") -> "FRaRbFRFRLFaLb"

    :param string: sentence with "a" and "b" characters that need to be replaced
    :return: new sentence with "a" and "b" characters replaced
    """
    if string == '':
        return ''
    elif string[0] == "a":
        return "aRbFR" + apply_dragon_rules(string[1::])
    elif string[0] == "b":
        return "LFaLb" + apply_dragon_rules(string[1::])
    else:
        return string[0] + apply_dragon_rules(string[1::])


def curve(string, depth):
    """
    Recursively generate the next depth of rules.

    Calls apply_dragon_rules() function `depth` times.
    curve("Fa", 2) -> "FaRbFRRLFaLbFR"

    :param string: current instruction string
    :param depth: how many times the rules are applied
    :return: instructionset at iteration 'depth'
    """
    a = depth
    if depth < 1:
        return string
    else:
        a -= 1
        return curve(apply_dragon_rules(string), a)



def format_curve(string):
    """
    Use recursions to remove  a  and  b  symbols from the instruction string.

    format_curve("Fa") -> "F"
    format_curve("FaRbFR") -> "FRFR"

    :param string: instruction string
    :return: clean instructions with only "F", "R", and "L" characters
    """
    if string == '':
        return ''
    elif string[0] == "F":
        return string[0] + format_curve(string[1::])
    elif string[0] == "R":
        return string + format_curve(string[1::])
    elif string[0] == "L":
        return string[0] + format_curve(string[1::])
    else:
        return format_curve(string[1::])


def draw_dragon(string, length):
    """Draw the dragon by reading the string recursively.

    Use t.right(), t.left(), t.forward() and draw_dragon() to move turtle.
        L - means turn 90 degrees to left and go forward
        R - means turn 90 degrees to right and go forward
        F - means don't turn just go forward

    :param string: instructions left to process
    :param length: how many pixels to move forward, left or right
    """
    pass


def get_line_length(dragon_width, depth):
    """Return one Turtle step length if the width and depth are known."""
    return dragon_width / (2 ** (1 / 2)) ** depth


def save(t: Turtle):
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    t.ht()  # hide him
    t.getscreen().getcanvas().postscript(file='tree.ps')


if __name__ == '__main__':
    t = Turtle()
    t.getscreen().bgcolor("#1c262b")
    t.color("#96004f")
    t.pensize(2)
    t.left(90)
    tree(200)

    '''
    s = curve("Fa", 8)
    s = format_curve(s)
    l = get_line_length(100, 8)
    draw_dragon(s, l)
    '''
    save(t)
    t.getscreen().exitonclick()
    print(apply_dragon_rules('FRaFRb'))  # FRaRbFRFRLFaLb
    print(curve("Fa", 2))  # "FaRbFRRLFaLbFR"
    print(format_curve("t"))
