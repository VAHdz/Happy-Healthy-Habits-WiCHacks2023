from dataclasses import dataclass
import Graphics
import time
@dataclass
class Bricksy:
    isHappy: bool
    happiness_level: int


def initial_bricksy():
    return Bricksy(False, 0)

# make a variable called initial size, and set it to 0 at the start. With each round, do either init size plus 55,
# or init size minus 0
# add in condition after calling round1 that if bricksy is happy, add 55, otherwise do nothing, if bricksy is
# unhappy, then leave size as is
#after calling round2, if bricksy is unhappy, remove 55 from init size


def round1(bricksy, init_size):
    Graphics.round1(init_size)
    choice1 = input("Which is the healthier choice? Type in " + "\"water\"" + " or " + "\"soda\"" + ":")
    if choice1 == "water":
        bricksy.happiness_level += 10
        bricksy.isHappy = True
        Graphics.clearscreen()
        Graphics.screen.bgpic("kitchen.png")
        Graphics.happy(init_size + 55)
        # make call to happy graphic and increase health bar
    elif choice1 == "soda":
        bricksy.happiness_level -= 10
        bricksy.isHappy = False
        Graphics.clearscreen()
        Graphics.screen.bgpic("kitchen.png")
        Graphics.angry(0)

    else:
        print("That's not included in the given choices! Please try again")
        return round1(bricksy, init_size)


def round2(bricksy, init_size):
    Graphics.round2(init_size)
    choice2 = input("Which is the healthier choice? Type in " + "\"carrots\"" + " or " + "\"chips\"" + ":")
    if choice2 == "carrots":
        bricksy.happiness_level += 10
        bricksy.isHappy = True
        Graphics.clearscreen()
        Graphics.screen.bgpic("kitchen.png")
        Graphics.happy(init_size + 55)

    elif choice2 == "chips":
        bricksy.happiness_level -= 10
        bricksy.isHappy = False
        if bricksy.happiness_level < 0:
            Graphics.clearscreen()
            Graphics.screen.bgpic("kitchen.png")
            Graphics.angry(0)
            print("You killed off Bricksy!")
            time.sleep(1.5)
            quit()
        Graphics.clearscreen()
        Graphics.screen.bgpic("kitchen.png")
        Graphics.angry(init_size - 55)
    else:
        print("That's not included in the given choices! Please try again")
        return round2(bricksy, init_size)


def round3(bricksy, init_size):
    Graphics.round3(init_size)
    choice3 = input("Which is the healthier choice? Type in " + "\"apple \"" + " or " + "\"candy bar\"" + ":")
    if choice3 == "apple":
        bricksy.happiness_level += 10
        bricksy.isHappy = True
        Graphics.clearscreen()
        Graphics.screen.bgpic("kitchen.png")
        Graphics.happy(init_size + 55)
    elif choice3 == "candy bar":
        bricksy.happiness_level -= 10
        bricksy.isHappy = False
        if bricksy.happiness_level < 0:
            Graphics.clearscreen()
            Graphics.screen.bgpic("kitchen.png")
            Graphics.angry(0)
            print("You killed off Bricksy!")
            time.sleep(1.5)
            quit()
        Graphics.clearscreen()
        Graphics.screen.bgpic("kitchen.png")
        Graphics.angry(init_size - 55)
    else:
        print("That's not included in the given choices! Please try again")
        return round3(bricksy, init_size)


def round4(bricksy, init_size):
    Graphics.round4(init_size)
    choice4 = input("Which is the healthier choice? Type in " + "\"burger\"" + " or " + "\"salad\"" + ":")
    if choice4 == "salad":
        bricksy.happiness_level += 10
        bricksy.isHappy = True
        Graphics.clearscreen()
        Graphics.screen.bgpic("kitchen.png")
        Graphics.happy(init_size + 55)
    elif choice4 == "burger":
        bricksy.happiness_level -= 10
        bricksy.isHappy = False
        if bricksy.happiness_level < 0:
            Graphics.clearscreen()
            Graphics.screen.bgpic("kitchen.png")
            Graphics.angry(0)
            print("You killed off Bricksy!")
            time.sleep(1.5)
            quit()
        Graphics.clearscreen()
        Graphics.screen.bgpic("kitchen.png")
        Graphics.angry(init_size - 55)
    else:
        print("That's not included in the given choices! Please try again")
        return round4(bricksy, init_size)

def round5(bricksy, init_size):
    Graphics.round5(init_size)
    choice5 = input("Which is the healthier choice? Type in " + "\"milkshake\"" + " or " + "\"smoothie\"" + ":")
    if choice5 == "smoothie":
        bricksy.happiness_level += 10
        bricksy.isHappy = True
        Graphics.clearscreen()
        Graphics.screen.bgpic("kitchen.png")
        Graphics.happy(init_size + 55)
    elif choice5 == "milkshake":
        bricksy.happiness_level -= 10
        bricksy.isHappy = False
        if bricksy.happiness_level < 0:
            Graphics.clearscreen()
            Graphics.screen.bgpic("kitchen.png")
            Graphics.angry(0)
            print("You killed off Bricksy!")
            time.sleep(1.5)
            quit()
        Graphics.clearscreen()
        Graphics.screen.bgpic("kitchen.png")
        Graphics.angry(init_size - 55)
    else:
        print("That's not included in the given choices! Please try again")
        return round5(bricksy, init_size)


def allCorrect(bricksy):
    if bricksy.happiness_level == 50:
        return "You got a perfect score!"
    else:
        return "Have a good day!"


def main():
    print("Welcome to the Happy Health Habits! Your goal is to feed Bricksy to keep him alive!")
    print("How to Play:")
    print("Type in the healthier option from the foods displayed to increase Bricksy's health! " +
          "Choose carefully or risk making Bricksy angry!")
    init_size = 0
    brick = initial_bricksy()
    round1(brick, init_size)
    time.sleep(1.5)
    Graphics.clearscreen()
    Graphics.screen.bgpic("kitchen.png")
    if brick.isHappy:
        init_size += 55
    elif not brick.isHappy and brick.happiness_level > 0:
        init_size -= 55
    elif brick.happiness_level < 0:
        print("You killed off Bricksy!")
        quit()

    round2(brick, init_size)
    time.sleep(1.5)
    Graphics.clearscreen()
    Graphics.screen.bgpic("kitchen.png")
    if brick.isHappy:
        init_size += 55
    elif not brick.isHappy:
        init_size -= 55

    round3(brick, init_size)
    time.sleep(1.5)
    Graphics.clearscreen()
    Graphics.screen.bgpic("kitchen.png")

    if brick.isHappy:
        init_size += 55
    elif not brick.isHappy:
        init_size -= 55

    round4(brick, init_size)
    time.sleep(1.5)
    Graphics.clearscreen()
    Graphics.screen.bgpic("kitchen.png")
    if brick.isHappy:
        init_size += 55
    elif not brick.isHappy:
        init_size -= 55

    round5(brick, init_size)
    time.sleep(1.5)
    Graphics.clearscreen()
    Graphics.screen.bgpic("kitchen.png")
    if brick.isHappy:
        init_size += 55
    elif not brick.isHappy:
        init_size -= 55

    print("Thank you for playing! " + allCorrect(brick))


main()