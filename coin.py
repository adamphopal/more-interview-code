#Greedy Algorithm:
# greedy method
def num_coins(cents):
    coins = [25, 10, 5, 1]
    count = 0
    for coin in coins:
        while cents >= coin:
            cents = cents - coin
            count = count + 1

    return count

#print('greedy method:', num_coins(32))


def min_coin_change(cents, coins_available, coins_so_far):
    if sum(coins_so_far) == cents:
        yield coins_so_far
    elif sum(coins_so_far) > cents:
        pass
    elif coins_available == []:
        pass
    else:
        for c in min_coin_change(cents, coins_available[:], coins_so_far+[coins_available[0]]):
            yield c
        for c in min_coin_change(cents, coins_available[1:], coins_so_far):
            yield c

cents = int(input("Please the amount of change:" ))
coins = [1, 10, 25]


solutions = [s for s in change(cents, coins, [])]
for s in solutions:
    continue
   # print(s)

print('change amount being used:', cents, 'cents')
print('Coins available to use:', coins)
print('optimal solution:', min(solutions, key=len))
print('number of coins used:', len(s))


#https://www.youtube.com/watch?v=HWW-jA6YjHk&list=PL_557Q1uZ7gLfEajI2TZDU80Y3kkpAxti&index=2
