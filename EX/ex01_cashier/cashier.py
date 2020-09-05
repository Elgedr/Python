"""Cashier."""
coins_list = [50, 20, 10, 5, 1]
summa = int(input('Enter a sum: '))
sentide_arv_ = 0
for i in range(len(coins_list)):
    number1 = summa // (coins_list[i])
    sentide_arv_ = sentide_arv_ + number1
    summa = summa - (coins_list[i] * number1)
print(f"Amount of coins needed: {sentide_arv_}")
