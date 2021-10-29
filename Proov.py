from random import choice
rock = "1"
paper = "2"
scissors = "3"
v1=["rock","paper","scissors"]
while True:
    bot = choice(v1)
    print("Камень = 1, Бумага = 2, Ножницы = 3")
    player = input("Выберай: ")

    if(bot == rock)and(player == rock):
        print("Ничья, ты и бот выбрали одинаковый предмет камень")
    elif(bot == rock)and(player == paper):
        print("Ты выиграл, у бота был камень")
    elif(bot == rock)and(player == scissors):
        print("Ты проиграл, у бота был камень")
    elif(bot == paper)and(player == rock):
        print("Ты проиграл, у бота была бумага")
    elif(bot == paper)and(player == paper):
        print("Ничья, ты и бот выбрали одинковый предмет бумага")
    elif(bot == paper)and(player == scissors):
        print("Ты выиграл, у бота была бумага")
    elif(bot == scissors)and(player == rock):
        print("Ты выиграл, у бота были ножницы")
    elif(bot == scissors)and(player == paper):
        print("Ты проиграл, у бота были ножницы")
    elif(bot == scissors)and(player == scissors):
        print("Ничья, ты и бот выбрали одиновый предмет ножницы")


    N = input("Хочешь продолжить игру? Y/N :")
    if N.upper() == "Y":
        print("Игра продожается")
    elif N.upper() == "N":
        print("Игра закончена лузер")

if N.upper=="Y":
    while True:
        print("Продолжаем игру")
        if read_key()=="Y":
            player=choice(v1)
        elif read_key()=="N":
            break

