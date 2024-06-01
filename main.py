import datetime
import bday_messages

today = datetime.date.today()
next_birthday = datetime.date(today.year, 12, 31)
time_difference = next_birthday - today

if today == next_birthday:
    print(bday_messages.birthday_message())
else:
    print("My next birthday is " + str(time_difference.days) + " days away.")
    
    