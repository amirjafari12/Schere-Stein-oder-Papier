import random

generel_choices = ["Schere", "Stein", "Papier"]

computer_choice = random.choice(generel_choices)

def again():
    play_again = input("Möchtest du nochmal spielen [y/n]?: ")
    while True:
        if play_again == "y":
            return game()
        else:
            break


def game():
    user_choice = input("Bitte wähle zwischen Schere, Stein oder Papier: ")
    print(f"computer choice ist: {computer_choice}")
    while True:

        if user_choice == computer_choice:
            print("unentschieden")
            again()
            break

        if user_choice == "Schere" and computer_choice == "Papier":
            print("user gewinnt")
            again()
            break

        elif user_choice == "Papier" and computer_choice == "Stein":
            print("user gewinnt")
            again()
            break


        elif user_choice == "Stein" and computer_choice == "Schere":
            print("user gewinnt")
            again()
            break

        else:
            print("computer gewinnt")
            again()
            break

game()
print("Du bist aus dem Spiel jetzt raus")
