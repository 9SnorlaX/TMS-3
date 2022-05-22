Total = 0
answer = {"Yes": "Yes", "No": "No"}
usluga_1 = None
usluga_2 = None
usluga_3 = None

while True:
    usluga_1 = input("Have u a grass to cut? ")
    if usluga_1 == answer["Yes"]:
        print("Ok, what area?")
        area = input()
        grass_costs = int(area) * 2 + 10
        Total += grass_costs
        print("Total amount:", Total)
    if usluga_1 == answer["No"]:
        print("Next quation")

    usluga_2 = input("Have any trees? ")
    if usluga_2 == answer["Yes"]:
        print("Ok, how many?")
        leaf_trees = input()
        leaf_costs = int(leaf_trees) * 20
        Total += leaf_costs
        print("Total amount:", Total)
    if usluga_2 == answer["No"]:
        print("Next quastion")

    usluga_3 = input("Have u any conifer trees? ")
    if usluga_3 == answer["Yes"]:
        print("Ok, how many?")
        conifer_trees = input()
        conifer_costs = int(conifer_trees) * 8
        Total += conifer_costs
        print("Total amount:", Total)
    if usluga_3 == answer["No"]:
        print("Next quastion")

    usluga_4 = input("Have u a pond? ")
    if usluga_4 == answer["Yes"]:
        print("Greate, what volume? ")
        pond_volume = input()
        if int(pond_volume) < 20:
            pond_clean = 6 * int(pond_volume)
        if int(pond_volume) > 20:
            pond_clean = 4 * int(pond_volume)
        Total += pond_clean
        print("Total amount", Total)
    if usluga_4 == answer["No"]:
        print("Total amount:", Total)
        print("Thanks, have a good day")
    break


