import random

first_names = (
[
'bob', 'harold', 'mark', 'richard', 'ken', 'beatrice', 'blazer',
'pax', 'madeleine', 'jasper', 'hodor', 'periwinkle', 'victoria', 'sophia',
'sophie', 'ryan', 'samuel', 'jesus', 'josephine', 'harold', 'reginald',
'steve', 'george', 'doctorpastor', 'jeb', 'william', 'irene', 'penny',
'jennifer', 'jenny', 'ashley', 'alexander', 'alex', 'violet', 'phineas',
'rocketeater', 'rocketeer', 'capitalist', 'trinity', 'dallas', 'ernst'
]
)

middle_names = (
[
'alexandros', 'druci', 'levon', 'liechtensteiner', 'panera',
'udica', 'haggis', 'h.', 'addison', 'bartholomew', 'brainiac',
'tuna', 'america', 'georgium', 'mettaton', 'henrietta', 'rip',
'sanic', 'bionicle', 'histogram', 'braintuna', 'unicorn',
'yves', 'anakin', 'cobra', 'capitalism', 'backspace', 'randint'
]
)

prefixes = (
[
'mc'
]
)

last_names = (
[
'maxwell', 'green', 'python', 'anderson', 'peters', 'piggalonius',
'ainsley', 'tyler', 'ross', 'fernley', 'zimmer', 'reynolds', 'samson',
'oppenheimer', 'miller', 'baker', 'nakamura', 'wang', 'biggs', 'master',
'black', 'smith', 'white', 'single', 'daniels', 'andrews', 'myers',
'schmidt', 'mason', 'jobs', 'ping'
]
)

capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mc = 'Mc'

first_len = len(first_names)
middle_len = len(middle_names)
last_len = len(last_names)
r = random.randrange

def chance(percent):
    """Has a PERCENT chance of returning True."""
    assert 0 <= percent <= 100, 'percent has to be between 0 and 100'
    return r(101) < percent

def name_generator():
    while True:
        first = first_names[r(first_len)].capitalize()
        middle = middle_names[r(middle_len)].capitalize()
        last = last_names[r(last_len)].capitalize()

        if chance(10): # 10 percent chance of getting a mcname
            last = mc + last
        if chance(10):
            middle = mc + middle
        if chance(10):
            first = mc + first
        if chance(5):
            first = "m'" + first
        if chance(5):
            first = 'Dr. ' + first

        if chance(10):
            yield f"{first} {last}"
        else:
            yield f"{first} {middle} {last}"

def id_generator():
    while True:
        id_letter = random.choice(capital_letters)
        id_num = random.randint(100, 999) # random 3 digit number
        yield f"{id_letter}{id_num}"
