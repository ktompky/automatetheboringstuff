import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinFlips = []
    for i in range(100):
        if random.randint(0,1):
            coinFlips.append('H')
        else:
            coinFlips.append('T')
    for i in range(100-6):
        if coinFlips[i] == coinFlips[i+1] == coinFlips[i+2] == coinFlips[i+3]== coinFlips[i+4] == coinFlips[i+5]:
            numberOfStreaks += 1
            break

    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100 ))