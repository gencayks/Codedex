import random

bday_messages = ['Hope you have a very Happy Birthday!',
'It\'s your special day  get out there and celebrate! ',
'You were born and the world got better  everybody wins!',
'Have lots of fun on your special day!',
'Another year of you going around the sun!']

def birthday_message():
    return random.choice(bday_messages)

