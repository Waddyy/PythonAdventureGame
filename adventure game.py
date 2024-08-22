from time import sleep

# Initialises the statistics at the start of the first game play
Points = 10
Strength = None
Speed = None
Charisma = None
TextSpeed = 0

print("Hello! Welcome to Shadows of the Forgotten Path")

# Strength calculation
def strengthFunc(Points,TextSpeed):
    Strength = 0
    while Strength == 0:
        try:
            Strength = int(input("What is your character's strength? (0-8)" ))
        except ValueError:
            print("Incorrect value, please input a number between 0 and 8")
            continue
        else:
            sleep(0.5 + TextSpeed)
            print("Your character's strength is", Strength)
            sleep(1 + TextSpeed)
            print('You have,', Points - Strength, 'points left\n')
            break
    return Points - Strength, Strength

# Speed Calculation
def speedFunc(PointsA,TextSpeed):
    Speed = 0
    while Speed == 0:
        try:
            Speed = int(input("What is your character's speed? (0-8)" ))
        except ValueError:
            print("Incorrect value, please input a number between 0 and 8")
            continue
        else:
            sleep(0.5 + TextSpeed)
            print("Your character's speed is", Speed)
            sleep(1 + TextSpeed)
            print('You have,', PointsA - Speed, 'points left\n')
            break
    return PointsA - Speed, Speed

# Function to reset statistics
def resetStats():
    Points = 10
    Strength = 0
    Speed = 0
    Charisma = 0
    Name = None
    txtspeed = 0

# Menu, Make it a function
def storyStart(TextSpeed):
    resetStats()
    print("_______________________________________________\n")
    sleep(2)
    name = input("Please enter your character's name here: ")
    print("\nHi", name + ", nice to meet you. Here we will choose your text speed, and input your character's stats.\n")
    sleep(3)
    print("How quickly should text appear on the screen. The slow option will add 2 extra seconds between text appearing.\n A) Slow\n B) Fast")
    txtspd = 0
    while txtspd != 'a' or txtspd != 'b':
        txtspd = input("What is your selection? (A/B)").lower()
        if txtspd == 'a' or txtspd == 'b':
            break
        else:
            print('That is not a valid selection.\n')
    if txtspd == 'a':
        TextSpeed = 2
    print("The two stats are Strength and Speed. Strength affects how strong your character is, and their fighting ability\n")
    sleep(3 + TextSpeed)
    print("and Speed affects how quickly your character can avoid hits from another player, and how quickly they can escape from certain situations\n")
    sleep(3 + TextSpeed)
    print("Please keep in mind that these will affect what actions you can and can't do in the story, and you will only have 10 points to use\n")
    sleep(3 + TextSpeed)
    print("e.g if you strength is less than 4 you won't be able to overpower someone.\n")
    sleep(3 + TextSpeed)
    PointsA, Strength = strengthFunc(Points, TextSpeed)
    PointsB, Speed = speedFunc(PointsA, TextSpeed)
    sleep(0.5 + TextSpeed)
    print("Thank you", name + ", your story begins now...\n\n")
    return name, Speed, Strength

# First bit of story, and the first three choices to choose
def theFirstChoice():
    print("There are three paths before you, each one partially hidden by the mist. Which path do you take?\n A) Left path, which is overgrown, but faint whispers come from this direction\n B) Middle Path, which looks recently used, but with strange, non-human footprints visible\n C) Right Path, being rocky and treacherous, with a faint light flickering in the distance")

# Second part of story, and the next three choices to choose
def theSecondChoice():
    print("You've got a few courses of actions to overcome this flashes of memory. You can either:\n A) Force yourself to recall what happened, despite the pain and fear that comes with the memories\n B) Push the memories away, and focus on finding a way out of the forest\n C) Confront whatever is hunting you, and causing these overwhelming memories to haunt you\n")

# First sequence of story, to clean up code
def introStory(TextSpeed):
    print("You awaken in a dense, mist-covered forest with a sharp pain in your leg. The forest is eerily silent, with towering trees and underbrush so thick you can barely see your own hands.\n")
    sleep(4 + TextSpeed)
    print("You look down, and your leg is bleeding, and you can't remember how you got here, let alone what happened to cause the injury.\n")
    sleep(4 + TextSpeed)
    print("All you know is that you must find help before it's too late...\n")
    sleep(4 + TextSpeed)
    print("As you struggle to stand, you notice three faint trails leading into the unknown.\nEach paths seems to offer a different choice, and with each step, fragments of your memory begin to return.\n")
    sleep(4 + TextSpeed)
    print("But be careful, as not all memories are meant to be recovered.\n\n")

# Second sequence of story, to clean up code
def secondEventIntro(TextSpeed):
    print('As you step into the clearing, you experience flashes of memory\n')
    sleep(3 + TextSpeed)
    print("The unexpected flashes of memories become overwhelming, forcing you to stop moving forward and to take a break\n")
    sleep(4 + TextSpeed)
    print("You take a seat on a rock in the clearing, light streaming into your eyes")
    sleep(4 + TextSpeed)

# Function for the first event
def choice0(Sel1, name, Strength, Speed, TextSpeed):

    # Event 1, Left Path
    if Sel1 == 'a':
        Sel1A = None

        print("You limp over towards the overgrown left, disappearing into the mist. It leads you further into the forest, as the whispering grows louder.\n")
        sleep(4 + TextSpeed)
        print("Once deep within the forest, you stumble upon a diary, yellowed with age, adorned with your name,", name + ", in gold. You pick it up and open it, the writing faded but still legible.\n")
        sleep(4 + TextSpeed)
        print("You make it out that it was someone much like you, lost in the forest. The author writes of a ritual gone awry, and about dark presence that stalks the woods.\n")
        sleep(4 + TextSpeed)
        print("As you read, the whispers grow louder, almost frantic, as if warning you of something.\n")
        sleep(4 + TextSpeed)
        print("You've got two courses of action:\n A) Stay and read more\n B) Flee the Whispers")

        while Sel1A != 'a' or Sel1A != 'b':
            Sel1A = input("What is your selection? (A/B)").lower()
            if Sel1A == 'a' or Sel1A == 'b':
                break
            else:
                print('That is not a valid selection.\n')
        # 1, Left Path, Read Diary
        if Sel1A == 'a':
            Sel1AA = None
            print('As you delve deeper into the diary, you discover that the author was a member of a cult, that performed a ritual in the forest\n')
            sleep(4 + TextSpeed)
            print("The ritual was meant to summon an ancient power, but it went horribly wrong. The whispers are voices of those who were sacrificed, and wish the same fate to come unto you.\n")
            sleep(6 + TextSpeed)
            print("Suddently, you hear footsteps behind you - a shadowy figure is approaching, and the whispers grow louder. You can either A) run, or B) fight. What do you do?")
            while Sel1AA != 'a' or Sel1AA != 'b':
                Sel1AA = input("What is your selection? (A/B)").lower()
                if Sel1AA == 'a' or Sel1AA == 'b':
                    break
                else:
                    print('That is not a valid selection.\n')
            # 1, Left, Diary, Fight
            if Sel1AA == 'b':
                if Strength >= 5:
                    print("You fight off the creature, and win. Once the shadow monster is down, you run away, following the path further into the forest, coming to a clearing\n\n")
                    return False
                elif Strength <= 4:
                    Go = input("You attempt to fight off the monster, but you're too weak. This marks an end to your journey. Do you wish to play again? (y/n)").lower()
                    if Go == 'y':
                        gameGo()
                    else:
                        exit()
            # 1, Left, Diary, Run
            elif Sel1AA == 'a':
                if Speed >= 5:
                    print("You sprint as fast as you can along the 'path', and make it away to a clearing. The footsteps of the monster can no longer be heard\n\n")
                    return False
                elif Speed <= 4:
                    Go = input("You attempt to sprint away, but you're too slow and the monster catches up to you. This marks an end to your journey. Do you wish to play again? (y/n)").lower()
                    if Go == 'y':
                        gameGo()
                    else:
                        exit()
        # 1, Left Path, Run Away
        elif Sel1A == 'b':
            print("You drop the diary and run away. The whispers were giving you the creeps anyways\n")
            sleep(4 + TextSpeed)
            print("The forest seems to fight you with every step, roots ane vines grabbing at your feet, but you manage to escape, and continue down the path, eventually coming to a clearing\n\n")
            return

    # Event 1, Middle Path
    elif Sel1 == 'b':
        Sel1B = None

        print("You limp towards the misty middle path, creating your own footprints on top of the other, non humanoid ones.\n")
        sleep(4 + TextSpeed)
        print("As you follow the trail, you notice the forest around you becoming darker, the trees growing taller and more oppresive, and the air thick with humidity.\n")
        sleep(5 + TextSpeed)
        print("You reach a clearing where the trees form a natural circle, the center occupied by a strange creature, half hidden in the shadows.\n")
        sleep(4 + TextSpeed)
        print("Despite the creatures unnatural appearance, tall and humanoid with glowing eyes, it does not attack\nInstead, it tilts its head as if recognizing you, and then gestures toward a hidden cave entrance at the edge of the clearing.\n")
        sleep(6 + TextSpeed)
        print("Do you:\n A) Trust the creature, and enter the cave\n B) Back away, deciding that trusting the creature is too risky\n")

        while Sel1B != 'a' or Sel1B != 'b':
            Sel1B = input("What is your selection? (A/B)").lower()
            if Sel1B == 'a' or Sel1B == 'b':
                break
            else:
                print('That is not a valid selection.\n')
        # 1, Middle path, Cave Entry
        if Sel1B == 'a':
            print("You cautiously approach the cave, and the creature steps aside to let you pass.\n")
            sleep(3 + TextSpeed)
            print("Inside, the walls are lined with ancient symbols, and in a corner you find a small altar with a glowing weapon on it.\n")
            sleep(4 + TextSpeed)
            print("You pick up the weapon, and continue further into the cave, eventually seeing light that leads to an exit, another clearing.\n")
            sleep(4 + TextSpeed)
            print("The creatures motives remain unclear, but you sense it wants you to succeed in whatever lies ahead.\n")
            return True
        # 1, Middle Path, Back Away
        elif Sel1B == 'b':
            print("As you turn, and back away, the creature doesn't pursue you, but you feel its eyes on you as you retreat.\n")
            sleep(4 + TextSpeed)
            print("Instead of returning to the fork in the road, you choose to cut through the thick forest, which doubles as a way to escape the creature, if it chooses to follow you.\n")
            sleep(5 + TextSpeed)
            print("After awhile, you make it to a clearing with no sign of the creature. It appears safe to continue your journey\n")
            sleep(4 + TextSpeed)
            print("Though, you do wonder if you missed a crucial opportunity by not trusting the creature...")
            return False

    # Event 1, Right Path
    elif Sel1 == 'c':
        Sel1C = None

        print("You limp towards the right path, where the ground is rocky and uneven, and you begin to wonder if you're even up to taking this path\n")
        sleep(4 + TextSpeed)
        print("As you stumble over rocks, the light you saw earlier becomes brighter, and you realise it's coming from an old, abandoned campsite\n")
        sleep(4 + TextSpeed)
        print("The campsite is deserted, but it shows signs of recent use- a fire pit with embers still glowing, a torn tent and scattered supplies\n")
        sleep(4 + TextSpeed)
        print("Among the supplies you find bandages and a small knife, which you quickly pocket.\nYou also discover a bloodstained journal, its pages filled with hurried, almost frantic writing\n")
        sleep(4 + TextSpeed)
        print("You sit down by the fire pit, and start reading the journal. Its entries detail a struggle against an unseen force, one the writer couldn't escape...\n")
        sleep(5 + TextSpeed)
        print("This place seems sketchy, especially the bloodstained journal's entries, but there may be more to uncover. Do you:\n A) Take the supplies and move on\n B) Stay and Investigate Further\n")

        while Sel1C != 'a' or Sel1C != 'b':
            Sel1C = input("What is your selection? (A/B)").lower()
            if Sel1C == 'a' or Sel1C == 'b':
                break
            else:
                print('That is not a valid selection.\n')

        # 1, Right Path, Flee Campsite
        if Sel1C == 'a':
            print("You bandage up your injured leg, the relief helping you to think more clearly\n")
            sleep(3 + TextSpeed)
            print("Armed with a knife, you feel slightly more prepared for whatever lies ahead\n")
            sleep(3 + TextSpeed)
            print("You leavge the camp behind, but the journal's words stick with you, making you more cautious and suspicious of anything, or anyone you might encounter next\n")
            return True

        # 1, Right Path, Investigae Campsite
        elif Sel1C == 'b':
            Sel1CA = None
            print("As you continue searching, you find more signs of a struggle- a torn piece of clothing, scratches on the rocks, and a broken compass\n")
            sleep(4 + TextSpeed)
            print("Just as you're about to give up, you notice something buried in the dirt near the fire pit.\nDigging it up reveals it to be a small, locked box\n")
            sleep(4 + TextSpeed)
            print("Without the key, you can't open it, but you decide to take it with you anyways\n")
            sleep(4 + TextSpeed)
            print("However the delay has cost you precious time, and as you start to leave, you hear the sound of something approaching through the trees-\nYou're not alone anymore\n")
            sleep(5 + TextSpeed)
            print("You're unsure of what it is, but it may be dangerous. You can either:\n A) Fight the entity\n B) Flee from the entity\n")

            while Sel1CA != 'a' or Sel1CA != 'b':
                Sel1CA = input("What is your selection? (A/B)").lower()
                if Sel1CA == 'a' or Sel1CA == 'b':
                    break
                else:
                    print('That is not a valid selection.\n')

            if Sel1CA == 'a':
                if Strength >= 5:
                    print("You fight off the entity, and win. Once the unknown entity is down, you run away, following the path further into the forest, coming to a clearing.\n\n")
                    return True
                elif Strength <= 4:
                    Go = input("You attempt to fight off the entity, but you're too weak. This marks an end to your journey. Do you wish to play again? (y/n)").lower()
                    if Go == 'y':
                        gameGo()
                    else:
                        exit()
            # 1, Left, Diary, Run
            elif Sel1CA == 'b':
                if Speed >= 5:
                    print("You sprint as fast as you can along the path, and make it away. The rustling of the entity can no longer be heard. You come across a clearing.\n\n")
                    return True
                elif Speed <= 4:
                    Go = input("You attempt to sprint away, but you're too slow and the entity catches up to you. This marks an end to your journey. Do you wish to play again? (y/n)").lower()
                    if Go == 'y':
                        gameGo()
                    else:
                        exit()

# Second Sequence of the story
def choice2(Sel2, name, Strength, Speed, TextSpeed, Weapon):
    # Event 2, Remember
    if Sel2 == 'a':
        print("You decide to concentrate on remembering what had happened, and your memory begins to all come together\n")
        sleep(4 + TextSpeed)
        print("But as you gain your memory, you feel a cold presence watching you, as if something from that ritual is hunting you. The forest seems to respond to your determination.\n")
        sleep(5 + TextSpeed)
        print("You remember being part of something- A group of people gathered around an altar, chanting in an ancient language\n")
        sleep(4 + TextSpeed)
        print("You recall the sensation of something going terribly wrong, a surge of power, and then pain in your leg\n")
        sleep(4 + TextSpeed)
        print("The memory is hazy, but one thing is clear: you were involved in a ritual and it marked you as a sacrifice.\n")
        sleep(4 + TextSpeed)
        print("The more you remember about the ritual, the more your leg throbs in pain\n")
        sleep(3 + TextSpeed)
        print("The knowledge of this sacrifice weighs heavily on you, but it gives you a sense of purpose. You must find the source of the ritual, and either complete it or break it to free yourself\n")
        sleep(6 + TextSpeed)
        print("Do you either:\n A) Seek redemption, finding the altar and attempting to reverse the ritual\n B)Accept your Fate, believing that there is no escape from the curse\n")

        Sel2A = None
        while Sel2A != 'a' or Sel2A != 'b':
            Sel2A = input("What is your selection? (A/B)").lower()
            if Sel2A == 'a' or Sel2A == 'b':
                break
            else:
                print('That is not a valid selection.\n')

        if Sel2A == 'a':
            print("You decide to seek out the source of the ritual, heading across the clearing down another path, deeper into the forest\n\n")
            return
        elif Sel2A == 'b':
            print("You decide that there is no escape from the curse, and that it is fate for this sequence of events to repeat for eternity.\n")
            sleep(3 + TextSpeed)
            go = input('This awards you the *FATALIST* ending. Do you wish to play again? (Y/N) ').lower()
            if go == 'y':
                gameGo()
            else:
                exit()
    # Event 2, Ignore
    if Sel2 == 'b':
        Sel2B = None

        print("These memories coming back to you now in this clearing seems unusual, as if invoked by a presence, the whispers?\n")
        sleep(4 + TextSpeed)
        print("It must be the forest trying to distract you, so you try to push them away and focus on finding a way out of the forest\n")
        sleep(4 + TextSpeed)
        print("But after awhile of moving forwards, the memories don't leave you alone- they linger at the edges of your consciousness\n")
        sleep(4 + TextSpeed)
        print("Your mind gets foggier, and everytime you think you've found a way forward, the path seems to loop back on itself\n")
        sleep(4 + TextSpeed)
        print("Despite your best efforts, you can't shake the feeling that you're being watched and the sense of disorientation grows with each step\n")
        sleep(4 + TextSpeed)
        print("The forest is playing tricks on you, and you're losing the battle to stay focus. Do you:\n A) Find a landmark to regain your sense of direction\n B) Sit and rest, to hope some clarity returns\n")

        Sel2B = None
        while Sel2B != 'a' or Sel2B != 'b':
            Sel2B = input("What is your selection? (A/B)").lower()
            if Sel2B == 'a' or Sel2B == 'b':
                break
            else:
                print('That is not a valid selection.\n')

        if Sel2B == 'a':
            sleep(1)
            print("You start sumbling back towards the direction you came from, aiming to find the clearing and rock from before\n")
            sleep(4 + TextSpeed)
            print("A few minutes later, a flicker of light can be seen in the distance")
            sleep(2 + TextSpeed)
            print("Getting closer, it appears its the same clearing as before, exactly what you were aiming to find\n")
            sleep(4 + TextSpeed)
            print("Its sense of familiarity helps clear your mind ever so slightly, allowing you to think clearer\n")
            return

        elif Sel2B == 'b':
            ancientblade = Weapon
            outcome1 = None
            if ancientblade == True:
                outcome1 = "You reach into your pocket and pull out the blade you picked up from before, and slay the monster.\nThe whispers stop, and your leg's pain slowly dies away. Maybe the stuff about it being a failed ritual was just from this mind altering entity?\nThis awards you the *VICTOR* ending.\n"
            elif ancientblade == False:
                outcome1 = "There's isn't anything you can do. You attempt to overpower the entity, but it's no use.\nYou lose, and everything goes black. Maybe this is destined to happen over and over?\nThis does not award you a proper ending, but if you play again you might win.\n"
            print("It's all getting too much for you, so a rest is what you need right now. You find a rock and sit down...\n")
            sleep(4 + TextSpeed)
            print("Your eyes feel heavy, and you're starting to ache from all the walking around. Maybe a small sleep couldn't do too much harm\n\n")
            sleep(4 + TextSpeed)
            print("-A few hours later-")
            sleep(1 + TextSpeed)
            print("A low growling stirs you, rustling in the bushes far away.\n")
            sleep(4 + TextSpeed)
            print("A twig snaps off to your left, and then suddenly- you're tackled to the ground by some entity from the left\n")
            sleep(4 + TextSpeed)
            print("Maybe this was the thing that was whispering in the forest the whole time?", outcome1)
            sleep(6 + TextSpeed)
            go = input('Do you wish to play again? (Y/N) ').lower()
            if go == 'y':
                gameGo()
            else:
                exit()

    # Event 2, Confront
    if Sel2 == 'c':
        print()


# GameCode
def gameGo():
    name, Speed, Strength = storyStart(TextSpeed)

    introStory(TextSpeed)
    theFirstChoice()

    Sel1 = None
    while Sel1 != 'a' or Sel1 != 'b' or Sel1 != 'c':
        Sel1 = input("What is your selection? (A/B/C)").lower()
        if Sel1 == 'a' or Sel1 == 'b' or Sel1 == 'c':
            break
        else:
            print('That is not a valid selection.\n')

    Weapon = choice0(Sel1, name, Strength, Speed, TextSpeed)

    secondEventIntro(TextSpeed)
    theSecondChoice()
    Sel2 = None
    while Sel2 != 'a' or Sel2 != 'b' or Sel2 != 'c':
        Sel2 = input("What is your selection? (A/B/C)").lower()
        if Sel2 == 'a' or Sel2 == 'b' or Sel2 == 'c':
            break
        else:
            print('That is not a valid selection.\n')

    choice2(Sel2, name, Strength, Speed, TextSpeed, Weapon)
    return

# Game is go
gameGo()
