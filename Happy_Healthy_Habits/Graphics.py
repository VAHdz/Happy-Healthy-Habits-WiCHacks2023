from turtle import *

screen = Screen()
screen.bgpic("kitchen.png")

def neutral(size):
    setup(1150, 650, 0, 0)
    healthBar(size)
    screen.addshape("neutralBrick.gif")
    neutralB = Turtle()
    neutralB.hideturtle()
    neutralB.penup()
    neutralB.shape("neutralBrick.gif")
    neutralB.goto(450, -200)
    neutralB.showturtle()

def happy(size):
    setup(1150, 650, 0, 0)
    healthBar(size)
    screen.addshape("happyBrick.gif")
    happyB = Turtle()
    happyB.hideturtle()
    happyB.penup()
    happyB.shape("happyBrick.gif")
    happyB.goto(100, -85)
    happyB.showturtle()

def angry(size):
    setup(1150, 650, 0, 0)
    healthBar(size)
    screen.addshape("angryBrick.gif")
    angryB = Turtle()
    angryB.hideturtle()
    angryB.penup()
    angryB.shape("angryBrick.gif")
    angryB.goto(100, -85)
    angryB.showturtle()

def healthBarBackground():
    up()
    hideturtle()
    goto(-225, 175)
    fillcolor("white")
    begin_fill()
    for i in range(2):
        down()
        pensize(10)
        circle(20, 90)
        fd(50)
        circle(20, 90)
        forward(275)
        up()
    end_fill()


def healthBar(size):
    speed("fastest")
    healthBarBackground()
    up()
    hideturtle()
    goto(-500, 190)
    fillcolor("green")
    begin_fill()
    for i in range(2):
        pensize(1)
        circle(5, -90)
        fd(-50)
        circle(5, -90)
        forward(-size)
        up()
    end_fill()

def round1(size):
    neutral(size)
    screen.addshape("WaterBottle.gif")
    water = Turtle()
    water.hideturtle()
    water.up()
    water.shape("WaterBottle.gif")
    water.shapesize(10)
    water.goto(-200, -150)
    water.showturtle()

    screen.addshape("soda.gif")
    soda = Turtle()
    soda.hideturtle()
    soda.up()
    soda.shape("soda.gif")
    soda.shapesize(10)
    soda.goto(100, -125)
    soda.showturtle()

def round2(size):
    neutral(size)
    screen.addshape("carrot.gif")
    carrot = Turtle()
    carrot.hideturtle()
    carrot.up()
    carrot.shape("carrot.gif")
    carrot.shapesize(10)
    carrot.goto(-250, -70)
    carrot.showturtle()

    screen.addshape("chips.gif")
    chips = Turtle()
    chips.hideturtle()
    chips.up()
    chips.shape("chips.gif")
    chips.shapesize(10)
    chips.goto(100, -100)
    chips.showturtle()

def round3(size):
    neutral(size)
    screen.addshape("apple.gif")
    apple = Turtle()
    apple.hideturtle()
    apple.up()
    apple.shape("apple.gif")
    apple.shapesize(10)
    apple.goto(-200, -100)
    apple.showturtle()

    screen.addshape("chocolateBar.gif")
    candyBar = Turtle()
    candyBar.hideturtle()
    candyBar.up()
    candyBar.shape("chocolateBar.gif")
    candyBar.shapesize(10)
    candyBar.goto(150, -100)
    candyBar.showturtle()

def round4(size):
    neutral(size)
    screen.addshape("Burger.gif")
    burger = Turtle()
    burger.hideturtle()
    burger.up()
    burger.shape("Burger.gif")
    burger.shapesize(10)
    burger.goto(-200, -150)
    burger.showturtle()

    screen.addshape("salad.gif")
    salad = Turtle()
    salad.hideturtle()
    salad.up()
    salad.shape("salad.gif")
    salad.shapesize(10)
    salad.goto(120, -145)
    salad.showturtle()


def round5(size):
    neutral(size)
    screen.addshape("milkShake.gif")
    milkshake = Turtle()
    milkshake.hideturtle()
    milkshake.up()
    milkshake.shape("milkShake.gif")
    milkshake.shapesize(10)
    milkshake.goto(-190, -115)
    milkshake.showturtle()

    screen.addshape("smoothie.gif")
    smoothie = Turtle()
    smoothie.hideturtle()
    smoothie.up()
    smoothie.shape("smoothie.gif")
    smoothie.shapesize(10)
    smoothie.goto(150, -140)
    smoothie.showturtle()



if __name__ == "__main__":
    # round1(0)
    # clearscreen()
    #
    # screen.bgpic("kitchen.png")
    # round2(0)
    # clearscreen()
    #
    # screen.bgpic("kitchen.png")
    # round3(0)
    # clearscreen()
    #
    # screen.bgpic("kitchen.png")
    # round4(0)
    # clearscreen()
    #
    # screen.bgpic("kitchen.png")
    # round5(0)
    # clearscreen()

    done()