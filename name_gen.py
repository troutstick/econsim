import random
import json

names = json.load(open("names.json"))

capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def chance(percent):
    """Has a PERCENT chance of returning True."""
    assert 0 <= percent <= 100, 'percent has to be between 0 and 100'
    return random.randint(0,100) <= percent

def mcify(str):
    """Adds 'Mc' to the beginning of str."""
    return 'Mc' + str

def name_generator():
    """Create a silly name. Or a serious one. Whatever it decides."""
    while True:
        first = random.choice(names["first"]).capitalize()
        middle = random.choice(names["middle"]).capitalize()
        last = random.choice(names["last"]).capitalize()

        if chance(10): # 10 percent chance of getting a mcname
            last = mcify(last)
        if chance(10):
            middle = mcify(middle)
        if chance(10):
            first = mcify(first)
        if chance(5):
            first = "m'" + first
        if chance(5):
            first = 'Dr. ' + first

        if chance(10):
            yield f"{first} {last}"
        else:
            yield f"{first} {middle} {last}"

def id_generator():
    """Generates a string consisting of a capital letter and a 3 digit number."""
    while True:
        id_letter = random.choice(capital_letters)
        id_num = random.randint(100, 999) # random 3 digit number
        yield f"{id_letter}{id_num}"