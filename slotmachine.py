import random 

symbols = ['cherry','grapes', 'watermelon', 'seven']

results = random.choices(symbols , k = 3)

print(results)

if all(symbol == 'cherry' for symbol in results):
    print("Cherry Jackpot!")