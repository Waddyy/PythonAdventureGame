from time import sleep

Points = 10
Strength = 0
Speed = 0
Charisma = 0
print("Hello! Welcome to Shadows of the Forgotten Path")

#Strength calculation
def strengthFunc(Strength,Points):
    while Strength == 0:
        try:
            Strength = int(input("What is your character's strength? (0-8)" ))
        except ValueError:
            print("Incorrect value, please input a number between 0 and 8")
            continue
        # if Strength >= 8 or Strength <=0:
            # print("Incorrect value, please input a number between 0 and 8")
            # continue
        else:
            sleep(1)
            print("Your character's strength is", Strength)
            sleep(2)
            print('You have,', Points - Strength, 'points left\n')
            break
    return Points - Strength

#Speed Calculation
def speedFunc(Speed,PointsA):
    while Speed == 0:
        try:
            Speed = int(input("What is your character's speed? (0-8)" ))
        except ValueError:
            print("Incorrect value, please input a number between 0 and 8")
            continue
        # if Speed >= 8 or Speed <=0:
            # print("Incorrect value, please input a number between 0 and 8")
            # continue
        else:
            sleep(1)
            print("Your character's speed is", Speed)
            sleep(2)
            print('You have,', PointsA - Speed, 'points left\n')
            break
    return PointsA - Speed

#Function to reset statistics
def resetStats():
    Points = 10
    Strength = 0
    Speed = 0
    Charisma = 0
    Name = None

# Menu, Make it a function
def storyStart():
    resetStats()
    print("_______________________________________________\n")
    sleep(2)
    name = input("Please enter your character's name here: ")
    print("\nHi", name + ", nice to meet you. Here we will input your character's stats.\n")
    sleep(2)
    print("The two stats are Strength and Speed. Strength affects how strong your character is, and their fighting ability\n")
    sleep(5)
    print("and Speed affects how quickly your character can avoid hits from another player, and how quickly they can escape from certain situations\n")
    sleep(5)
    print("Please keep in mind that these will affect what actions you can and can't do in the story, and you will only have 10 points to use\n")
    sleep(4)
    print("e.g if you strength is less than 4 you won't be able to overpower someone.\n")
    sleep(4)
    PointsA = strengthFunc(Strength, Points)
    PointsB = speedFunc(Speed, PointsA)
    sleep(2)
    print("Thank you", name + ", your story begins now...\n\n")
    return name

def theFirstChoice():
    print("There are three paths before you, each one partially hidden by the mist. Which path do you take?\n A) Left path, which is overgrown, but faint whispers come from this direction\n B) Middle Path, which looks recently used, but with strange, non-human footprints visible\n C) Right Path, being rocky and treacherous, with a faint light flickering in the distance")

#First sequence of story, to clean up code
def introStory():
    print("You awaken in a dense, mist-covered forest with a sharp pain in your leg. The forst is eerily silent, with towering trees and unerbrush so thick you can barely see your own hands.\n")
    sleep(6)
    print("You look down, and your leg is bleeding, and you can't remember how you got here, let alone what happened to cause the injury.\n")
    sleep(6)
    print("All you know is that you must find help before it's too late...\n")
    sleep(6)
    print("As you struggle to stand, you notice three faint trails leading into the unknown.\nEach paths seems to offer a different choice, and with each step, fragments of your memory begin to return.\n")
    sleep(6)
    print("But be careful, as not all memories are meant to be recovered.\n\n")

# Function for the first event
def choice0(Sel1, name):
    if Sel1 == 'a':
        Sel1A = None

        print("You limp over towards the overgrown left, disappearing into the mist. It leads you further into the forest, as the whispering grows louder.\n")
        sleep(6)
        print("Once deep within the forest, you stumble upon a diary, yellowed with age, adorned with your name,", name + ", in gold. You pick it up and open it, the writing faded but still legible.\n")
        sleep(6)
        print("You make it out that it was someone much like you, lost in the forest. The author writes of a ritual gone awry, and about dark presence that stalks the woods.\n")
        sleep(6)
        print("As you read, the whispers grow louder, almost frantic, as if warning you of something.\n")
        sleep(6)
        print("You've got two courses of action:\n A) Stay and read more\n B) Flee the Whispers")

        while Sel1A != 'a' or Sel1A != 'b':
            Sel1A = input("What is your selection? (A/B)").lower()
            if Sel1A == 'a' or Sel1A == 'b':
                break
            else:
                print('That is not a valid selection.\n')

        if Sel1A == 'a':
            Sel1AA = None
            print('As you delve deeper into the diary, you discover that the author was a member of a cult, that performed a ritual in the forest\n')
            sleep(6)
            print("The ritual was meant to summon an ancient power, but it went horribly wrong. The whispers are voices of those who were sacrificed, and wish the same fate to come unto you.\n")
            sleep(8)
            print("Suddently, you hear footsteps behind you - a shadowy figure is approaching, and the whispers grow louder. You can either A) run, or B) fight. What do you do?")
            while Sel1AA != 'a' or Sel1AA != 'b':
                Sel1AA = input("What is your selection? (A/B)").lower()
                if Sel1AA == 'a' or Sel1AA == 'b':
                    break
                else:
                    print('That is not a valid selection.\n')
            if Sel1AA == 'a':
                if Strength >= 5:
                    print("You fight off the creature, and win. Once the shadow monster is down, you run away, following the path further into the forest.")
                    return
                elif Strength <= 4:
                    Go = input("You attempt to fight off the monster, but you're too weak. This marks an end to your journey. Do you wish to play again? (y/n)").lower()
                    if Go == 'y':
                        gameGo()
                    else:
                        exit()
            elif Sel1AA == 'b':
                if Speed >= 5:
                    print("You sprint as fast as you can along the 'path', and make it away. The footsteps of the monster can no longer be heard.")
                    return
                elif Speed <= 4:
                    Go = input("You attempt to sprint away, but you're too slow and the monster catches up to you. This marks an end to your journey. Do you wish to play again? (y/n)").lower()
                    if Go == 'y':
                        gameGo()
                    else:
                        exit()
        elif Sel1A == 'b':
            print("You drop the diary and run away. The whispers were giving you the creeps anyways.")
            sleep(6)
            print("The forest seems to fight you with every step, roots ane vines grabbing at your feet, but you manage to escape, and continue down the path.")
            return

    elif Sel1 == 'b':
        Sel1B = None

        print("You limp towards the misty middle path, creating your own footprints on top of the other, non humanoid ones.\n")
        sleep(6)
        print("As you follow the trail, you notice the forest around you becoming darker, the trees growing taller and more oppresive, and the air thick with humidity.\n")
        sleep(7)
        print("You reach a clearing where the trees form a natural circle, the center occupied by a strange creature, half hidden in the shadows.\n")
        sleep(6)
        print("Despite the creatures unnatural appearance, tall and humanoid with glowing eyes, it does not attack\nInstead, it tilts its head as if recognizing you, and then gestures toward a hidden cave entrance at the edge of the clearing.\n")
        sleep(8)
        print("Do you:\n A) Trust the creature, and enter the cave\n B) Back away, deciding that trusting the creature is too risky\n")

        while Sel1B != 'a' or Sel1B != 'b':
            Sel1B = input("What is your selection? (A/B)").lower()
            if Sel1B == 'a' or Sel1B == 'b':
                break
            else:
                print('That is not a valid selection.\n')

        if Sel1B == 'a':
            print("You cautiously approach the cave, and the creature steps aside to let you pass.\n")
            sleep(5)
            print("Inside, the walls are lined with ancient symbols, and in a corner you find a small altar with a glowing weapon on it.\n")
            sleep(6)
            print("You pick up the weapon, and continue further into the cave, eventually seeing light that leads to an exit, another clearing.\n")
            sleep(6)
            print("The creatures motives remain unclear, but you sense it wants you to succeed in whatever lies ahead.\n")
            return
        elif Sel1B == 'b':
            print("As you turn, and back away, the creature doesn't pursue you, but you feel its eyes on you as you retreat.\n")
            sleep(6)
            print("Instead of returning to the fork in the road, you choose to cut through the thick forest, which doubles as a way to escape the creature, if it chooses to follow you.\n")
            sleep(7)
            print("After awhile, you make it to a clearing with no sign of the creature. It appears safe to continue your journey\n")
            sleep(6)
            print("Though, you do wonder if you missed a crucial opportunity by not trusting the creature...")
            return

    elif Sel1 == 'c':
        print('balls')
        return 'c'



# GameCode
def gameGo():
    name = storyStart()
    introStory()
    theFirstChoice()
    Sel1 = None
    while Sel1 != 'a' or Sel1 != 'b' or Sel1 != 'c':
        Sel1 = input("What is your selection? (A/B/C)").lower()
        if Sel1 == 'a' or Sel1 == 'b' or Sel1 == 'c':
            break
        else:
            print('That is not a valid selection.\n')

    Event1 = choice0(Sel1, name)
    print(Event1)

gameGo()
