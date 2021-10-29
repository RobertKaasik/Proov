print("Камень Ножницы Бумага")

Rock = 1
Paper = 2
Scissors = 3

def play_game():

    computer = get_random()

    play = get_play()

    if play == "1" or play == "2" or play == "3":
        play == True
    else:
        play == False
        print("Error")
        play = input("Введи пожалуйста 1 это камень, 2 это бумага,и 3 это камень: ")

    if play == computer:
        print("Ничья,попробуй заного!")
        tie_score += 1

    else:
        get_score(computer, play)

    print("The computer chose: ", computer)
    print("The player chose: ", play)


def display_message():
    print("Добро пожаловать!")
    print("Ты сейчас играешь в камень ножницы бумага против компьютера.")
    print("Игра состоит из полного рандома так что не надо злится.")
    print("1  это камен,2 это бумага,3 это ножницы.")
    print("Кто выиграет тот и выиграет!")
    print("Желаю удачи!")

def get_random():
    import random

    computer = random.randint(1, 3)
    return computer


def get_play():
    play = input("Введи 1 это камен, 2 это бумага,и 3 это ножницы: ")
    return play

def get_score(computer, play):

    if computer == 1 and play == 2:
        score = ("Игрок выиграл")
        print("Бумага победила камень, Игрок выиграл")
        player_wins += 1

    elif computer == 1 and play == 3:
        score = ("Компьютер выиграл")
        print("Ножницы победили бумагу, Компьютер выиграл")
        computer_wins += 1


    elif computer == 2 and play == 3:
        score = ("Игрок выиграл")
        print("Ножницы победили бумагу, Игрок выиграл")
        player_wins += 1

    elif computer == 2 and play == 1:
        score = ("Компьютер выиграл")
        print("Бумага победила камен, Компьютер выиграл")
        computer_wins += 1

    elif computer == 3 and play == 1:
        score = ("Игрок выиграл")
        print("Камень выиграл ножницы, Игрок выиграл")
        player_wins += 1

    elif computer == 3 and play == 2:
        score = ("Компьютер выиграл")
        print("Ножницы победили бумагу, Компьютер выиграл")
        computer_wins += 1

print("_____________________________________________________________________________")

from random import choice
bot = choice(("Камень","Ножницы","Бумага"))
print("Выберай")
player = input(" Камень = 1, Бумага = 2, Ножницы = 3 ")
rock = 1
paper = 2
scissors = 3
if(bot == rock)and(player == rock):
    print("Ничья")
elif(bot == rock)and(player == paper):
    print("Ты выиграл")
elif(bot == rock)and(player == scissors):
    print("Ты проиграл")
elif(bot == paper)and(player == rock):
    print("Ты проиграл")
elif(bot == paper)and(player == paper):
    print("Ничья")
elif(bot == paper)and(player == scissors):
    print("Ты выиграл")
elif(bot == scissors)and(player == rock):
    print("Ты выиграл")
elif(bot == scissors)and(player == paper):
    print("Ты проиграл")
elif(bot == scissors)and(player == scissors):
    print("Ничья")
