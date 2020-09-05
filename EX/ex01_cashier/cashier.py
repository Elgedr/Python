"""Cashier."""
coins_list = [50, 20, 10, 5, 1]
summa = int(input('Enter a sum: '))
coins = 0
for i in coins_list:
    number1 = summa//i
    coins = coins + number1
    summa = summa - i * number1

print(f"amount of coins needed: {summa}")