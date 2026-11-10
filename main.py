# Лабораторная работа 3, вариант 77
# Симулятор космической торговли

import random
import trade_data
random.seed(67)




def show_help():
    print("Команды:")
    print("  buy <цена>   - купить 1 ед. товара по этой цене")
    print("  sell <цена>  - продать 1 ед. товара по этой цене")
    print("  prices       - товары и их обычные цены")
    print("  tip          - случайный совет торговца")
    print("  status       - кредиты и груз")
    print("  help         - показать эту подсказку")
    print("  exit         - выйти из игры")


def show_prices():
    print("Товары и обычные цены:")
    print(f"  {trade_data.TRADE_1_NAME}: {trade_data.TRADE_1_PRICE}")
    print(f"  {trade_data.TRADE_2_NAME}: {trade_data.TRADE_2_PRICE}")
    print(f"  {trade_data.TRADE_3_NAME}: {trade_data.TRADE_3_PRICE}")


def show_status(credits, cargo):
    print(f"Кредиты: {credits}")
    print(f"Груз: {cargo} из {trade_data.MAX_CARGO}")


def buy(credits, cargo, price, qty=1, max_cargo=trade_data.MAX_CARGO):
    # покупаем qty ед. по цене price, возвращаем новые кредиты и груз
    total = price * qty
    if total > credits:
        print(f"Не хватает кредитов: нужно {total}, а у вас {credits}.")
    elif cargo + qty > max_cargo:
        print("В трюме не хватает места.")
    else:
        credits = credits - total
        cargo = cargo + qty
        print(f"Купили {qty} ед. за {total}. Осталось кредитов: {credits}")
    return credits, cargo


def sell(credits, cargo, price, qty=1):
    # продаём qty ед. по цене price, возвращаем новые кредиты и груз
    if cargo < qty:
        print(f"Не хватает товара: нужно {qty}, а в трюме {cargo}.")
    else:
        credits = credits + price * qty
        cargo = cargo - qty
        print(f"Продали {qty} ед. за {price * qty}. Теперь кредитов: {credits}")
    return credits, cargo


def random_tip():
    number = random.randint(1, 3)
    if number == 1:
        print(f"Совет: обычная цена товара «{trade_data.TRADE_1_NAME}» около {trade_data.TRADE_1_PRICE}. Берите дешевле!")
    elif number == 2:
        print(f"Совет: обычная цена товара «{trade_data.TRADE_2_NAME}» около {trade_data.TRADE_2_PRICE}. Продавайте дороже!")
    else:
        print(f"Совет: обычная цена товара «{trade_data.TRADE_3_NAME}» около {trade_data.TRADE_3_PRICE}. Самый выгодный груз.")


credits = trade_data.START_CREDITS
cargo = 0

print("Добро пожаловать на борт, торговец!")
print(f"У вас {credits} кредитов, трюм пуст (вмещает {trade_data.MAX_CARGO} ед.).")
print("Напишите help, чтобы увидеть список команд.")

while True:
    command = input("> ").strip().lower()

    if command == "exit":
        print("Конец смены. Удачных полётов!")
        break

    elif command == "help":
        show_help()

    elif command == "status":
        show_status(credits, cargo)

    elif command == "prices":
        show_prices()

    elif command == "tip":
        random_tip()

    elif command == "buy" or command[:4] == "buy ":
        price_text = command[3:].strip()  # всё, что написано после buy
        # проверяю строку до int(), чтобы программа не упала на буквах
        if not price_text.isdecimal():
            print("Напишите цену числом, например: buy 50")
        elif int(price_text) == 0:
            print("Цена должна быть больше нуля.")
        else:
            credits, cargo = buy(credits, cargo, int(price_text))
            if random.randint(1, 4) == 1:  # иногда после сделки приходит совет
                random_tip()

    elif command == "sell" or command[:5] == "sell ":
        price_text = command[4:].strip()  # всё, что написано после sell
        if not price_text.isdecimal():
            print("Напишите цену числом, например: sell 80")
        elif int(price_text) == 0:
            print("Цена должна быть больше нуля.")
        else:
            credits, cargo = sell(credits, cargo, int(price_text))
            if random.randint(1, 4) == 1:
                random_tip()

    else:
        print("Не знаю такой команды. Напишите help.")
