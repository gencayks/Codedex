import random 

symbols = ['cherry','grapes', 'watermelon', 'seven']

results = random.choices(symbols , k = 3)

print(results)

if all(symbol == 'cherry' for symbol in results):
    print("Cherry Jackpot!")
if all(symbol == 'grapes' for symbol in results):
    print("Grapes Jackpot!")
if all(symbol == 'watermelon' for symbol in results):
    print("Watermelon Jackpot!")
if all(symbol == 'seven' for symbol in results):
    print("Seven Jackpot!")
    
else:
    print("Try again!")
    

def play():
    while True:
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break
        results = random.choices(symbols , k = 3)
        print(results)
        if all(symbol == 'cherry' for symbol in results):
            print("Cherry Jackpot!")
        else:
            print("Try again!")