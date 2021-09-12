# **************************** Multiplayer number guessing game ********************************

# Importing Libraries
import random
from datetime import datetime


def number():
    chances = 1
    while True:
        print("\nAttempt number:", chances)
        get = int(input(f"\nGuess the number between {a} and {b}:"))
        if get >= a and get <= b:
            if get == num:
                print("Congratulation...! You guess the correct number...!")
                print(f"You took {chances} chances to guess the correct number...")
                points.append(chances)
                break
            elif get < num:
                print(f"Wrong guess...! Please enter greater number.")
            else:
                print(f"Wrong guess...! Please enter smaller number.")
        else:
            print("Invalid Input...! Please enter the valid input..!")
            continue
        chances += 1
        continue

def check_points():
    if points[0] < points[1]:
        print(f"\n{name_1} is win by {points[1] - points[0]} points..")
    elif points[0] > points[1]:
        print(f"\n{name_2} is win by {points[0] - points[1]} points..")
    else:
        print("\nThis is draw because of same points..!")

def play_quit():
    play_game = input("\n\nEnter any key to continue or \"Q\" to quit...!")
    if play_game.capitalize() == "Q":
        print("Thanks for your valuable time that you spend with us....! We expect, you will be back soon...! Take care and stay home...!")
        exit()
    else:
        print("Enjoy the programme...!\n")

def login(msg):
    global name_1
    global name_2
    with open("record.txt", "a") as f:
        f.write(f"{name_1.capitalize()} and {name_2.capitalize()} are {msg} on {datetime.now()}\n")

if __name__ == '__main__':
    print("\nWelcome to Multi-player NUMBER GUESSING game made by Sachin Dabhade\n")
    name_1 = input("Enter first player name: ")
    name_2 = input("Enter second player name: ")
    print("\nHello " + name_1.capitalize() + " and " + name_2.capitalize() + "! Best of Luck!")
    print("\nThe game is about to start!\n Let's play and win!\n\n")
    login("Playing the multiplayer number guessing game")

    try:
        a = int(input("Enter the first number in range: "))
        b = int(input("Enter the second number in range: "))
        if a < b:
            if a>100 or a<-100 or b>100 or b<-100:
                print("Number should be lesser than 100 and greater than -100..")
                exit()
        else:
            print("first number should be lesser than the second one...!")
            exit()
    
    except Exception as e:
        print("Invalid Input...!\n")
        exit()
    points = []
    play = 1
    
    while True:
        if play % 2 != 0:
            num = random.randint(a, b)
            print("\nThis is first inning...!")
            print(f"{name_1} will guess the number..")
            number()
            play += 1
        if play % 2 == 0:
            num = random.randint(a, b)
            print("\nThis is second inning...!")
            print(f"{name_2} will guess the number..")
            number()
        else:
            print("Something wents wrong...!\n")
            exit()
        check_points()
        points.clear()
        play_quit()
