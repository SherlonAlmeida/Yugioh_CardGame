import json

def print_not_found():
    print("-----------------------------------------------------------")
    print("--------------------- CARD NOT FOUND! ---------------------")
    print("-----------------------------------------------------------")

def show_card_info(cards_database, idx, card):
    curr_id = cards_database[idx]["id"]
    name = cards_database[idx]["name"]
    image = cards_database[idx]["card_images"][0]["image_url"]
    curr_type = cards_database[idx]["type"]
    description = cards_database[idx]["desc"]

    print("-----------------------------------------------------------")
    print("ID:", curr_id)
    print("NAME:", name)
    print("DESC:", description)
    print("IMAGE:", image)
    print("TYPE:", curr_type)
    if "Monster" in curr_type:
        print("ATK:", cards_database[idx]["atk"])
        print("DEF:", cards_database[idx]["def"])
    print("-----------------------------------------------------------")

def find_card_by_id(cards_database):
    id = int(input("Insert the card ID: "))
    found = False
    for idx, card in enumerate(cards_database):
        if card["id"] == id:
            #print(cards_database[idx]) #Show all Query
            show_card_info(cards_database, idx, card)
            found = True
            break
    if not found:
        print_not_found()

def find_card_by_name(cards_database):
    id = input("Insert the card NAME: ")
    found = False
    for idx, card in enumerate(cards_database):
        if id in card["name"]:
            show_card_info(cards_database, idx, card)
            found = True
    if not found:
        print_not_found()

"""The program starts here"""

#Open JSON finle
f = open("cardinfo.json")

#Convert to dict
cards_database = json.load(f)["data"]
n_cards = len(cards_database) 

#Perform queries
find_card_by_name(cards_database)
 
# Closing file
f.close()