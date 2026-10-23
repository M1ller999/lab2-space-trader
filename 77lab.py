# Лабораторная работа 2, вариант 77
# Симулятор космической торговли

credits = 1000   # кредиты
cargo = 0        # сколько товара в трюме
max_cargo = 10   # вместимость трюма

print("Добро пожаловать на борт, торговец!")
print(f"У вас {credits} кредитов, трюм пуст (вмещает {max_cargo} ед.).")
print("Команды: buy <цена>, sell <цена>, status, exit")

while True:
    command = input("> ").strip().lower()

    if command == "exit":
        print("Конец смены. Удачных полётов!")
        break

    elif command == "status":
        print(f"Кредиты: {credits}")
        print(f"Груз: {cargo} из {max_cargo}")

    elif command == "buy" or command[:4] == "buy ":
        price_text = command[3:].strip()  # всё, что написано после "buy"
        # проверяем строку до int(), чтобы программа не упала на буквах
        if not price_text.isdecimal():
            print("Напишите цену числом, например: buy 50")
        else:
            price = int(price_text)
            if price == 0:
                print("Цена должна быть больше нуля.")
            elif price > credits:
                print(f"Не хватает кредитов: нужно {price}, а у вас {credits}.")
            elif cargo >= max_cargo:
                print("Трюм полон, класть больше некуда.")
            else:
                credits = credits - price
                cargo = cargo + 1
                print(f"Купили 1 ед. за {price}. Осталось кредитов: {credits}")

    elif command == "sell" or command[:5] == "sell ":
        price_text = command[4:].strip()  # всё, что написано после "sell"
        if not price_text.isdecimal():
            print("Напишите цену числом, например: sell 80")
        else:
            price = int(price_text)
            if price == 0:
                print("Цена должна быть больше нуля.")
            elif cargo == 0:
                print("Трюм пуст, продавать нечего.")
            else:
                credits = credits + price
                cargo = cargo - 1
                print(f"Продали 1 ед. за {price}. Теперь кредитов: {credits}")

    else:
        print("Не знаю такой команды. Есть: buy <цена>, sell <цена>, status, exit")
