"""Cashier."""
coins_list = [50, 20, 10, 5, 1]
sentide_arv_ = int(input('Enter a sum: '))
coins = 0
for i in coins_list:
    number1 = sentide_arv_ // i
    coins = coins + number1
    sentide_arv_ = sentide_arv_ - i * number1

print(f"Amount of coins needed: {sentide_arv_}")
