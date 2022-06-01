debts = {
'Ivanov': {'electricity': '140', 'water': '12', 'debt': '3100'},
'Doe': {'electricity': '280', 'water': '16', 'debt': '1475'},
'Smith': {'electricity': '320', 'water': '9', 'debt': '1600'},
'Kroft': {'electricity': '145', 'water': '12', 'debt': '2856'},
'Tulle': {'electricity': '120', 'water': '8', 'debt': '4550'},
'Yanson': {'electricity': '223', 'water': '4', 'debt': '1600'},
'Kuznetsov': {'electricity': '543', 'water': "12", "debt": "2300"},
}
subsid_e = 2300
subsid_w = 870
abonents = ["Ivanov", "Doe", "Smith", "Kroft", "Tulle", "Yanson", "Kuznetsov"]
total_w = None
total_e = None
for name, debt in zip(abonents, debts):
    if int(debts[name]["electricity"]) < 150:
        total = debts[name]["debt"]
        total_e = int(debts[name]["debt"]) - subsid_e
        print(f"{name}  use ", debts[name]["electricity"], "electricity so his subsid", subsid_e)
    else:
        print(f"{name} has no subsid, so amount to pay for electricity", debts[name]["debt"])
    if int(debts[name]["water"]) < 10:
        total = debts[name]["debt"]
        total_w = int(debts[name]["debt"]) - subsid_w
        print(f"{name}  use ", debts[name]["water"], " water so his his subsid", subsid_w)
    else:
        print(f"{name} has no subsid, so amount to pay for water", debts[name]["debt"])


