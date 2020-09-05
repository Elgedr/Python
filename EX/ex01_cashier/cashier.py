"""Cashier."""
coins_list = [50, 20, 10, 5, 1]
summa = int(input('Enter a sum: '))
coins = 0
for i in range(len(coins_list)):
    number1 = summa // (coins_list[i])
    coins = coins + number1
    summa = summa - (coins_list[i] * number1)
print(coins)
