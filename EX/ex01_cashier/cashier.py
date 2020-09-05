coins_list = [50, 20, 10, 5, 1]
summa = int(input('Enter a sum: '))
coins = 0
for i in coins_list:
    print(f"Сейчас работаем с монетой: {i}")
    number1 = summa//i
    print(number1)
    coins = coins + number1
    print(coins)
    summa = summa - i * number1
    print(summa)