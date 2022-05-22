Total = 0
answer = {"Yes": "Yes", "No": "No"}
grass_cut = None
leaf_cut = None

while True:
    grass_cut = input("Have u a grass to cut? ")
    if grass_cut == answer["Yes"]:
        print("Ok, what area?")
        area = input()
        grass_costs = int(area) * 3
        Total += grass_costs
        print("Total amount:", Total)
    if grass_cut == answer["No"]:
        print("Next quation")

    leaf_cut = input("Have any trees? ")
    if leaf_cut == answer["Yes"]:
        print("Ok, how many?")
        trees = input()
        leaf_costs = int(trees) * 3
        Total += leaf_costs
        print("Total amount:", Total)
    if grass_cut == answer["No"]:
        print("Total amount:", Total)
    break


