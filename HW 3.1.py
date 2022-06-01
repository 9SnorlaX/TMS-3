items = ["Jeans"]
strategy = {"LIFO": "LIFO", "FIFO": "FIFO"}
no_answer = ""
donated_item = None
donate = None

what_strategy = input("What strategy would u like to try? ")
if what_strategy == strategy["LIFO"]:
    while donated_item != no_answer:
        donated_item = input("What u can give us? ")
        items.append(donated_item)
        print("Thank u, next")
if donated_item == no_answer:
    print("Thank you")
    print("Hey we have some items to give away")
    while items != []:
        print(items.pop(0), "for u")
        print("Next one")
    if items == []:
        print("Sorry, we have nothing")

if what_strategy == strategy["FIFO"]:
    while donated_item != no_answer:
        donated_item = input("What u can give us? ")
        items.append(donated_item)
        print("Thank u, next")
if donated_item == no_answer:
    print("Thank you")
    print("Hey we have some items to give away")
    while items != []:
        print(items.pop(-1), "for u")
        print("Next one")
    if items == []:
        print("Sorry, we have nothing")
