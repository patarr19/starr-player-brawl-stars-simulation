from sys import exec_prefix
from colorama import Fore, init

# ---------------------------------Расчет наибольщего дамажа-------------------------------- #
def calcMostDamage():
    try:
        # получаем урон от игроков
        firsrPlayer = int(input("Введите общий урон от первого игрока"))
        secondPlayer = int(input("Введите общий урон от второго игрока"))
        thirdPlayer = int(input("Введите общий урон от третьего игрока"))

        # проверяем, чтобы не были ниже нуля
        if firsrPlayer  < 0 or secondPlayer < 0 or thirdPlayer < 0:
            print("Server error 2")
            return

        # находим максимальный из всех игроков урон
        mostDamagePlayer = max(firsrPlayer,secondPlayer,thirdPlayer)

        # создаем пустой список
        topPlayers = []

        # если самый большой урон у того или другого игрока, помещаем его в конец списка
        if mostDamagePlayer == firsrPlayer:
            topPlayers.append("первого")
        if mostDamagePlayer == secondPlayer:
            topPlayers.append("второго")
        if mostDamagePlayer == thirdPlayer:
            topPlayers.append("третьего")

        # проверяем длину списка, если длина = 1, значит там один игрок, и у него самый большой урон. по такому принципу проверяем дальше
        if len(topPlayers) == 1:
            print(f"У {topPlayers[0]} игрока самый большой урон. Он нанес {mostDamagePlayer}")
        if len(topPlayers) == 2:
            print(f"У {topPlayers[0]} игрока и {topPlayers[1]} игрока одинаковый урон. Они нанесли {mostDamagePlayer}")
        if len(topPlayers) == 3:
            print(f"У всех игроков одинаковый урон {mostDamagePlayer}")

    except ValueError:
        print("Server error 1")
# ---------------------------------Расчет наибольщего хила-------------------------------- #
def calcMostHeal():
    try:
        # получаем хил от всех игроков
        firsrPlayer = int(input("Введите общий хил от первого игрока"))
        secondPlayer = int(input("Введите общий хил от второго игрока"))
        thirdPlayer = int(input("Введите общий хил от третьего игрока"))

        # проверяем, не меньше ли нуля введенные значения
        if firsrPlayer < 0 or secondPlayer < 0 or thirdPlayer < 0:
            print("Хил игрока не могут быть отрицательным. server error 2")
            return

        # находим максимальный хил из всех
        mostHeal = max(firsrPlayer, secondPlayer, thirdPlayer)

        # создаем пустой список
        topPlayers = []

        # если игрок имеет самый большой хил, то добавляем его в конец списка
        if mostHeal == firsrPlayer:
            topPlayers.append("первого")
        if mostHeal == secondPlayer:
            topPlayers.append("второго")
        if mostHeal == thirdPlayer:
            topPlayers.append("третьего")

        # проверяем длину
        if len(topPlayers) == 1:#если длина = 1, то значит там один игрок, у которого самый большой хил
            print(f"У {topPlayers[0]} игрока самый большой хил за всю игру - {mostHeal}")
        if len(topPlayers) == 2:#если длина = 2, значит там 2 игрока, имеющие самый максимальный хил, то есть у них он одинаковый
            print(f"У {topPlayers[0]} и {topPlayers[1]} игроков одинаковый хил - {mostHeal}")
        if len(topPlayers) == 3:# если длина 3, то в список с максимальным хилом вошли все три игрока, значит хил у все одинаковый
            print(f"У всех игроков одинаковый хил - {mostHeal}")

    except ValueError:
        print("erver error 1")

# ---------------------------------Расчет звездного игрока-------------------------------- #
def calcStarrPlayer():
    try:
        # получаем урон от игроков
        firsrPlayer1 = int(input("Введите общий урон от первого игрока"))
        secondPlayer1 = int(input("Введите общий урон от второго игрока"))
        thirdPlayer1 = int(input("Введите общий урон от третьего игрока"))

        # получаем хил от всех игроков
        firsrPlayer2 = int(input("Введите общий хил от первого игрока"))
        secondPlayer2 = int(input("Введите общий хил от второго игрока"))
        thirdPlayer2 = int(input("Введите общий хил от третьего игрока"))

        # проверяем, не меньше ли нуля введенные данные
        if firsrPlayer1 < 0 or secondPlayer1 < 0 or thirdPlayer1 < 0 or firsrPlayer2 < 0 or secondPlayer2 < 0 or thirdPlayer2 < 0:
            print("server error 2")
            return
        if firsrPlayer1 == 0 or secondPlayer1 == 0 or thirdPlayer1 == 0 or firsrPlayer2 == 0 or secondPlayer2 == 0 or thirdPlayer2 == 0:
            print("Невозможно расчитать звездного игрока, так как одно или несколько из значений равно нулю")
            return

        # находим максимальный дамаж и хил у игроков
        mostDamage = max(firsrPlayer1, secondPlayer1, thirdPlayer1)
        mostHeal = max(firsrPlayer2, secondPlayer2, thirdPlayer2)

        # создаем пустой список
        starrPlayer = []

        # если у игрока максимальный урон и максимальный хилл, добавляем его в конец списка
        if firsrPlayer1 == mostDamage and firsrPlayer2 == mostHeal:
            starrPlayer.append("первый")
        if secondPlayer1 == mostDamage and secondPlayer2 == mostHeal:
            starrPlayer.append("второй")
        if thirdPlayer1 == mostDamage and thirdPlayer2 == mostHeal:
            starrPlayer.append("третий")

        # если есть такой игрок
        if starrPlayer:
            # если длина списка 1, то там один игрок
            if len(starrPlayer) == 1:
                #называем его
                print(f"⭐ {starrPlayer[0]} игрок является звездным игроком. У него {mostDamage} урона и {mostHeal} хила")
            # если длина списка 2, то там два игрока
            if len(starrPlayer) == 2:
                # называем их
                print(f"{starrPlayer[0]} игрок и {starrPlayer[1]} игрок являются звездными игроками. "
                      f"Нанесли они {mostDamage} урона и восполнили {mostHeal} хила")
            # если длина списка 3, то тужа вошли все 3 игрока, и у них у все максимальный(одинаковый) хил и урон
            if len(starrPlayer) == 3:
                # называем их
                print(f"Все три игрока являются звездными игроками. Они нанесли {mostDamage} урона и восполнили {mostHeal} хила")
        # если нету такого игрока
        else:
            print("Звездного игрока нету")

    except ValueError:
        print("server error 1")

# ---------------------------------Точка входа в программу-------------------------------- #
if __name__ == "__main__":
    init()

    rainbowColors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA]
    text = "Добро пожаловать в симуляцию расчета звездного игрока и т.д!"

    for i, char in enumerate(text):
        color = rainbowColors[i % len(rainbowColors)]
        print(color + char, end="")

    print(Fore.RESET)

    try:
        choose = int(input("Выберите действие: 1:Расчистать урон; 2: Расчитать хил;"
                           " 3: Расчитать Звездного игрока; 4: Расчитать средний и общий урон; "
                           "5: Расчитать игрока, набравший наибольшее кол-во киллов "))
        if choose == 1:
            calcMostDamage()
        elif choose == 2:
            calcMostHeal()
        elif choose == 3:
            calcStarrPlayer()
        elif choose == 4:
            pass
        elif choose == 5:
            pass
        else:
            print("server error 3")

    except ValueError:
        print("server error 1")

# добавить файл.txt с описанием ошибок