Space_Travel = input("Where would you like to go?(Pyroxis, Cryosoria, Verdantora, Chronosphere) ").lower()
while not Space_Travel == "pyroxis":
    print("")
    print("You think to yourself not to waste your time on planets with nothing of interest at the moment.")
    print("")
    Space_Travel = input("Where would you like to go?(Pyroxis, Cryosoria, Verdantora, Chronosphere)").lower()
    print("")

if Space_Travel == "pyroxis":
    print("")
    print("You fly to Pyroxis.")
    print("")