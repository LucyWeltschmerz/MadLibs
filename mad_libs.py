import random

user_input = input('Enter a number between 1 to 3 or let the game choose for you: ')
if user_input == '':
    user_input = 0
else:
    user_input = int(user_input)
print(user_input)


def first_template():
    time = input('Please input number: ')
    measure_of_time = input('Please input a measure of time: ')
    transportation = input('Please input a method of transportation: ')
    adj = input('Please input an adjective describing a place: ')
    adj_2 = input('Please inout an adjective: ')
    noun = input('Please input a noun: ')
    color = input('Please input a color: ')
    body_part = input('Please input a part of body: ')
    verb = input('Please input a verb: ')
    number = input('Please input a number: ')
    noun_2 = input('Please input a noun: ')
    noun_3 = input('Please input a noun: ')
    body_part_2 = input('Please input a part of body: ')
    verb_2 = input('Please input a verb: ')
    noun_4 = input('Please input a noun: ')
    adj_3 = input('Please input an adjective: ')
    silly_word = input('Please input a silly word: ')
    noun_5 = input('Please input a noun: ')

    template_text = f'It was about {time} {measure_of_time} ago when I arrived at the hospital in a{transportation}.' \
                    f'The hospital is a/an {adj} place, there are a lot of {adj_2} {noun} here.' \
                    f'There are nurses here who have {color} {body_part}. ' \
                    f'If someone wants to come into my room I told them that they have to {verb} ' \
                    f'first. I’ve decorated my room with {number} {noun_2}. ' \
                    f'Today I talked to a doctor and they were wearing a {noun_3} on their {body_part_2}. ' \
                    f'I heard that all doctors {verb_2} {noun_4} every day for breakfast. ' \
                    f'The most {adj_3} thing about being in the hospital is the {silly_word} {noun_5}!'

    return template_text


def second_template():
    name = input('Please input a name: ')
    noun_1 = input('Please input a noun: ')
    feeling_1 = input('Please input an adjective describing a feeling: ')
    verb_1 = input('Please input a verb: ')
    feeling_2 = input('Please input an adjective describing a feeling: ')
    animal = input('Please input an animal: ')
    verb_2 = input('Please input a verb: ')
    color = input('Please input a color: ')
    verb_ing = input('Please input a verb ending in ing (e.g. going): ')
    adverb = input('Please input an adverb ending in ly (e.g. happily): ')
    number = input('Please input a number: ')
    time = input('Please input measure of time: ')
    silly_word = input('Please input a silly word: ')
    noun_2 = input('Please input a noun: ')

    template_text = f'This weekend I am going camping with {name}. I packed my lantern, ' \
                    f'sleeping bag, and {noun_1}. I am so {feeling_1} to {verb_1} in a tent. I am {feeling_2} ' \
                    f'we might see a(n) {animal}, I hear they’re kind of dangerous. While we’re camping, ' \
                    f'we are going to hike, fish, and {verb_2}. I have heard that the {color} lake is great for ' \
                    f'{verb_ing}. Then we will {adverb} hike through the forest for {number} ' \
                    f'{time}. If I see a {color} {animal} while hiking, I am going to bring it home as a ' \
                    f'pet! At night we will tell {number} {silly_word} stories and roast {noun_2} around the campfire!!'

    return template_text


def third_template():
    name = input('Please input a name: ')
    adj = input('Please input an adjective: ')
    color = input('Please input a color: ')
    animal = input('Please input an animal: ')
    place = input('Please input a place: ')
    adj_2 = input('Please input an adjective: ')
    magical_creature_1 = input('Please input a name of magical creature in plural form: ')
    adj_3 = input('Please input an adjective')
    magical_creature_2 = input('Please input a name of magical creature in plural form: ')
    house_room = input('Please input a name of a house room: ')
    noun = input('Please input a noun: ')
    noun_2 = input('Please input a noun: ')
    noun_3_pl = input('Please input a noun in plural form: ')
    adj_4 = input('Please input an adjective: ')
    noun_4_pl = input('Please input a noun in plural form: ')
    number = input('Please input a number: ')
    time = input('Please input a measure of time: ')
    verb_ing = input('Please input a verb ending in -ing: ')
    adj_5 = input('Please input an adjective: ')
    noun_5 = input('Please input a noun: ')

    template_text = f'Dear {name}, I am writing to you from a {adj} castle in an ' \
                    f'enchanted forest. I found myself here one day after going for a ride on a {color} {animal} in ' \
                    f'{place}. There are {adj_2} {magical_creature_1} and {adj_3} {magical_creature_2} ' \
                    f'here! In the {house_room} there is a pool full of {noun}. I fall asleep each ' \
                    f'night on a {noun_2} of {noun_3_pl} and dream of {adj_4} {noun_4_pl}. It feels as ' \
                    f'though I have lived here for {number} {time}. I hope one day you can visit, ' \
                    f'although the only way to get here now is {verb_ing} on a {adj_5} {noun_5}!!'

    return template_text


templates = [first_template, second_template, third_template]


if user_input == 1:
    print(first_template())
elif user_input == 2:
    print(second_template())
elif user_input == 3:
    print(third_template())
else:
    random_template = random.choice(templates)
    print(random_template())

