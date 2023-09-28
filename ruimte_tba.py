
print("")
print("You are the (soon to be) infamous Space Explorer, Captain Nova Starfinder.")
print("After hearing about a pirate with very valuable treasure hidden in the solar system,")
print("you start your journey into deep space until you find a space wreckage.")
print("You look around your ship and see your spacehelmet and your McDonalds pattented food cube.")
print("")
Put_On_Space_Helmet = input("Would you like to put on your space helmet?(Yes or No): ").lower()
if Put_On_Space_Helmet == 'yes':
    print("")
    print("You put on your space helmet...")
    print("")

    View_Space_Wreckage = input("Would you like to view the space wreckage?(Yes or No): ").lower()
    print("")
    while not View_Space_Wreckage == 'yes':
        print("Guess we're just waiting around then....")
        print("")
        View_Space_Wreckage = input("Would you like to view the space wreckage?(Yes or No): ").lower()

    print("")
    print("You exit your ship to board the Space Wreckage.")
    print("You see bits of debris floating all around you.")
    print("")
    print("Entering the space wreckage....")
    print("")
    print("As you enter the space wreckage you look around and spot a 'Handy-Dandy XenoBlaster' with 2 !")
    print("")
    print("While exploring other areas of the wreckage you come across Zarnak The Talkative XenoMorph!")
    print("You spot him as he spots you!")
    print("")
    print("He screams at you: 'AHHH FRESH MEAT FROM WEAK PREY!'")
    print("")

    Pocket_Knife = input("Do you instinctually pull out your pocket knife?!(You've always had it BTW)(Yes or No): ").lower()
    print("")
    if Pocket_Knife == 'yes':
        print("Captain Nova pulls out his pocket knife, rushes at the Xenomorph and stabs him in his chest!")
        print("Green-Yellowish blood starts gushing out of the Xenomorph and burns your hand!")
        print("While you're distracted from the pain, HE BITES YOUR ENTIRE HEAD OFF!")
        print("Oh you died BTW :(")
        print("")

    else:
        XenoBlaster1 = input("Do you pull out your Handy-Dandy XenoBlaster?!(Yes or No): ").lower()
        if XenoBlaster1 == 'no':
            print("")
            print("He immediately lunges at you! HE CLAWS YOUR EYES OUT AND STARTS EATING YOUR GUTS")
            print("YOUR STUPID ASS JUST DIED!")
            print("")
        else:
            print("")
            print("YOU GRAB YOUR BLASTER AND FIRE OFF A SHOT INTO HIS WEIRD LOOKING SHOULDER!")
            print("HE FLIES BACKWARDS AND HITS HIS HEAD ON A WALL!")
            print("He quickly scurries away!")
            print("")
            print("After he scurries away you look around and find a journal near a body in the wreckage")
            print("After somewhat of a close inspection you begin feeling intregued by the journal")
            print("It looks like there are pictures of a POWERFUL PIRATE with a handheld CHROME PYRAMID")
            print("The book states that the CHROME PYRAMID gives the person that holds it 9 LIVES!")
            print("It states that the pirate has lived for more than 350 years.")
            print("After dying multiple times in the Galactic war it seems that he only has 3 lives left.")
            print("")
            print("Further expection reveals something about Pyroxis; a scorched planet, where endless seas of sand meet rivers of molten lava.")
            print("We're looking for a specific location with Massive Lava Falls.")
            print("")

            Return_To_Ship = input("Do we look around or return to our ship?(Look or Return): ").lower()
            print("")
            while not Return_To_Ship == 'return':
                print("Looking around...")
                print("On a floating desk we find '2 Raygun Capsules' in the drawers")
                print("")
                Return_To_Ship = input("Do we look around or return to our ship?(Look or Return): ").lower()
            
            print("")
            print("Returning to ship...")
            print("Heading to ship deck...")
            print("")

            Space_Travel = input("Where would you like to go?(Pyroxis, Cryosoria, Verdantora, Chronosphere) ").lower()
            
            while not Space_Travel == "pyroxis":
                print("")
                print("You think to yourself not to waste your time on planets with nothing of interest at the moment.")
                print("")
                Space_Travel = input("Where would you like to go?(Pyroxis, Cryosoria, Verdantora, Chronosphere)").lower()
        
        if Space_Travel == "pyroxis":
            print("")
            print("You fly to Pyroxis.")
            print("")
            


            





else:
    print("")
    print("Captain Nova Starfinder has been introduced to the vacuum of space where he immediately gaspes for air that wasn't there,")
    print("realizing the gravity of his predicament, he immediately dies :( ")
    print("")