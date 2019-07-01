#it is a mystery game that you have to solve mysteries and pick up clues
#clues - items
#mystery - lost things, items, people and the infinity stones
#mysteries have different groups of levels
#to find clues you explore around and go on journies
#to finsh the mystery you need to find all the clues and put them together
#you can use 3 hints
#if you can find the right people and they will point you in the right direction
#if you find the wrong people then they will point you in the wrong direction
#the wrong people are evil and the right people are good

def level_1_area(position):
    if position ==0:
        print ("you are in a forest. behind you there is a redwood tree to mark your spot. there is a city to your left")
    elif position ==-1:
        print ("you are in the meadows and getting close to the city")
    elif position ==-2:
        print ("you are in the city. this is the most likely place where you will find people that can help you.")
    elif position ==-3:
        print ("you are in the dessert. you can find a lot of stuff here hidden under the sand")
    elif position ==1:
        print ("you are in the grasslands. here you will find a lot of animals that can help you.")
    elif position ==2:
        print ("you are in the mountains. you can find a lot of stuff here hidden under the snow and rocks")

def level_one():
    #you are trying to find a lost item (cellphone)
    #this game will take place in a forest
    print ("there are 3 clues. Once you find all 3 clues put them together to help you solve the mystery")
    position =0
    hint =3
    has_glass =False
    has_plastic =False
    has_compass =False

    level_1_area(position)
    while True:
        action =input()
        if action =="left":
            if position <= -3:
                print("you can't move that far")
            else:
                position-=1
                level_1_area(position)
        elif action =="right":
            if position >= 2:
                print("you can't move that far")
            else:
                position+=1
                level_1_area(position)
        elif action =="hint":
            if hint ==3:
                print("there are clues in the trees of.................forest")
                hint =2
            elif hint ==2:
                print("there are clues burried under the snow")
                hint =1
            elif hint ==1:
                print("there are clues in the desert")
                hint =0
            else:
                print("you have no more hints")
        elif action =="look around":
            if position ==0:
                print ("you are in a forest. you see a lot of evergreen trees and a redwood tree to mark your spot.")
            elif position ==-1:
                print ("you are in the meadows. you see a lot of flowers, grass, and weeds. you can see faded buildings in the background too.")
            elif position ==-2: 
                print ("you are in the city. you see a lot of people walking around the street and tall buildings all around you.")
            elif position ==-3:
                print ("you are in the dessert. you see a lot of stuff here hidden half-way under the sand, no water, and no people")
            elif position ==1:
                print ("you are in the grasslands. here you will see a lot of animals that are cute, a lot of grass, and weeds.")
            elif position ==2:
                print ("you are in the mountains. you see a lot of stuff here hidden half-way under the snow and the rocks, frozen streams, and almost no people")
        elif action =="talk":
            #forest city grasslands mountains
            if position ==0:
                print("which person would you like to talk to: druids, hikers, or random people walking in the forest?")
                action =input()
                if action =="druids":
                    print("you are looking in the right biome. you just have to look closer.")
                elif action =="hikers":
                    print("i do not know what you are talkling about. all i have noticed is pieces of glass in trees.")
                elif action =="random people walking in the forest":
                    print("i do NOT know what you are talking about i am just random person walking in the forest")
                else:
                    print ("you can not talk to that person right now")
            elif position ==-2:
                print("which person would you like to talk to: random people walking down the street, trash people, guards, or heroes?")
                action =input()
                if action =="random people walking down the street":
                    print ("i do NOT know what you are talking about. i am JUST A PERSON! DO I LOOK LIKE A HERO TO YOU?!")
                elif action =="trash people":
                    print ("i do NOT know what you are talking about. i am JUST A PERSON! DO I LOOK LIKE A HERO TO YOU?! but i did see someone lose something in the mountains.")
                elif action =="guards":
                    print("i saw someone go in the forest with their cellphone and come out without their cellphone")
                elif action =="heroes":
                    print("i have more heroic stuff to do then finding a lost cellphone. you are going to need to solve this mystery on your own.")
                else:
                    print ("you can not talk to that person right now")
            elif position ==1:
                print("which person will you like to talk to: care-takers of animals or people who are getting ready to hike?")
                action =input()
                if action =="care-takers"or action =="care-takers of animals":
                    print("i think you should go to the desert. i saw some pieces of plastic there.")
                elif action =="people who are getting ready to hike" or action =="hikers":
                    print("when i was climbing the mountains i saw a compass in the snow and under a boulder.")
                else:
                    print ("you can not talk to that person right now")
            elif position ==2:
                print("would you like to talk to mountain climbers?")
                action =input()
                if action =="yes":
                    print("i have seen a compass here hidden under the snow and rocks, but that is all.")
            else:
                print("there are no people here")
        elif action =="grab":
            print ("what do you want to grab?")
            action =input()
            if (action =="a piece of glass" or action =="pieces of glass" or action =="glass") and position ==0:
                if has_glass:
                    print("you already have the piece of glass")
                else:
                    print("you now have a piece of glass")
                    has_glass =True
            elif (action =="a piece of plastic" or action =="pieces of plastic" or action =="plastic") and position ==-3:
                if has_plastic:
                    print("you already have the piece of plastic")
                else:
                    print("you now have a piece of plastic")
                    has_plastic =True
            elif (action =="a compass" or action =="compass") and position ==2:
                if has_compass:
                    print("you already have a compass")
                else:
                    print("you now have a compass")
                    has_compass =True
            else:
                print("you are not able to pick that up here")
            
            if has_glass and has_plastic and has_compass:
                print("You now have all the clues. Now you have completed the level.")
                break
        elif action =="quit":
            break
        else:
            print("that is not a command")

def level_2_area(position):
    if position ==0:
        print ("you are in the city. this is the most likely place where you will find people that can help you.")
    elif position ==-1:
        print ("you are in the grasslands. here you will find a lot of animals that can help you.")
    elif position ==-2:
        print ("you are in the village. this is the most likely place where you will make friends.")
    elif position ==-3:
        print ("you are in the meadows. you see some people.")
    elif position ==1:
        print ("you are in a forest. behind you there is a redwood tree to mark your spot. there is a city to your left")
    elif position ==2:
        print ("you are in the dessert. you can find a lot of stuff here hidden under the sand")
    elif position ==3:
        print ("you are in the mountains. you can find a lot of stuff here hidden under the snow and rocks")

def level_two():
    print ("there are 4 clues. Once you find all 4 clues put them together to help you solve the mystery")
    position =0
    hint =2
    has_rainbow_cloth =False
    has_kitten =False
    has_lollipop =False
    has_flower =False

    level_2_area(position)
    while True:
        action =input()
        if action =="left":
            if position <= -3:
                print("you can't move that far")
            else:
                position-=1
                level_2_area(position)
        elif action =="right":
            if position >= 3:
                print("you can't move that far")
            else:
                position+=1
                level_2_area(position)
        elif action =="hint":
            if hint ==2:
                print("there are clues in the village")
                hint =1
            elif hint ==1:
                print("there are clues in the mountains")
                hint =0
            else:
                print("you have no more hints")
        elif action =="look around":
            if position ==0:
                print ("you are in the city. you see a bunch of people bustling aruond and trash people picking up trash.")
            elif position ==-1:
                print ("you are in the grasslands. you see animals, people taking care of them, and a lot of grass.")
            elif position ==-2:
                print ("you are in the village. you see some small houses and big houses.")
            elif position ==-3:
                print ("you are in the meadows. you see some buildings in the background and a lot of grass.")
            elif position ==1:
                print ("you are in a forest. you see a redwood tree to mark your spot.")
            elif position ==2:
                print ("you are in the dessert. you see a lot of stuff here hidden half-way under the sand.")
            elif position ==3:
                print ("you are in the mountains. you see a lot of snow, boulders, and some rocks.")
        elif action =="talk":
            #city meadows village
            if position ==0:
                print("which person would you like to talk to: musicians, trash people, or guards?")
                action =input()
                if action =="musicians":
                    print ("i saw a kid walk in the forest and never come back, though they might have, just i wasn't paying attention, but other than that there has been nothing")
                elif action =="trash people":
                    print ("i do NOT know what you are talking about, but i did see something that looked like a rainbow cloth in the trash cans.")
                elif action =="guards":
                    print("i do not know what happened, but i did see a lollipop in the desert.")
                else:
                    print ("you can not talk to that person right now")
            elif position ==-3:
                print("which person would you like to talk to: gardeners or a weird person?")
                action =input()
                if action =="gardeners":
                    print ("i saw someone take a flower back to their home in the village.")
                elif action =="weird person":
                    print ("about talking are you what know not do i. YOU TO HERO A LIKE LOOK I DO.")
                else:
                    print ("you can not talk to that person right now")
            elif position ==-2:
                print("which person will you like to talk to: farmers or bakers?")
                action =input()
                if action =="bakers":
                    print("i think you should go to the mountains. i saw a kitten there.")
                elif action =="farmers":
                    print("i don't know. all i saw was a kitten who stole my crops and then ran off to the mountains.")
                else:
                    print ("you can not talk to that person right now")
            else:
                print("there are no people here")
        elif action =="grab":
            print ("what do you want to grab?")
            action =input()
            if (action =="a rainbow cloth" or action =="rainbow cloth") and position ==0:
                if has_rainbow_cloth:
                    print("you already have the rainbow cloth")
                else:
                    print("you now have a rainbow cloth")
                    has_rainbow_cloth =True
            elif (action =="a kitten" or action =="kitten") and position ==3:
                if has_kitten:
                    print("you already have the kitten")
                else:
                    print("you now have a kitten")
                    has_kitten =True
            elif (action =="a lollipop" or action =="lollipop") and position ==2:
                if has_lollipop:
                    print("you already have a lollipop")
                else:
                    print("you now have a lollipop")
                    has_lollipop =True
            elif (action =="a flower" or action =="flower") and position ==-2:
                if has_flower:
                    print("you already have a flower")
                else:
                    print("you now have a flower")
                    has_flower =True
            else:
                print("you are not able to pick that up here")
            
            if has_rainbow_cloth and has_kitten and has_lollipop and has_flower:
                print("You now have all the clues. Now you have completed the level.")
                break
        elif action =="quit":
            break
        else:
            print("that is not a command")

print ("welcome to marvel mysteries")
while True:
    print ("do you want to play or quit")
    a =input()
    if a =="play":
        print("pick a level (1 or 2)")
        a =input()
        if a =="1":
            level_one()
        elif a =="2":
            level_two()
        else:
            print ("that is not a level")
    elif a =="quit":
        exit()
    else:
        print ("that is not an option")