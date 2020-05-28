import random
import sys
import time

pl_animals = ['piesek', 'żyrafa', 'tygrys', 'jaskółka', 'hipopotam', 'tygrys', 'szympans', 'krokodyl', 'delfin',
              'niedźwiedź', 'antylopa', 'gepard', 'pantera']
pl_fruit = ['jabłko', 'ananas', 'truskawki', 'porzeczki', 'maliny', 'brzoskwinia', 'borówki', 'gruszka', 'cytryna',
            'jagoda', 'mandarynka', 'pomarańcza', 'winogrona']
pl_jobs = ['marynarz', 'nauczyciel', 'sportowiec', 'programista', 'kierowca', 'sprzedawca', 'dziennikarz', 'piosenkarz',
           'architekt', 'piekarz', 'fotograf', 'lekarz']

eng_animals = ['elephant', 'crocodile', 'panther', 'monkey', 'gorilla', 'cheetah', 'chameleon', 'chicken', 'hedgehog',
               'giraffe', 'butterfly', 'rabbit', 'gosling']
eng_fruit = ['strawberry', 'raspberry', 'pineapple', 'orange', 'honeydew', 'bananas', 'coconut', 'blueberry',
             'watermelon', 'dragonfruit', 'passionfruit', 'papaya']
eng_jobs = ['teacher', 'musician', 'dancer', 'programmer', 'builder', 'firefighter', 'policeman', 'photographer',
            'waitress', 'baker', 'lawyer', 'journalist', 'astronaut']

ger_animals = ['elefant', 'gorilla', 'gepard', 'krokodil', 'kaninchen', 'schmetterling', 'giraffe', 'schwein', 'frosch',
               'pferde', 'fisch', 'hund', 'vogel', 'schlange']
ger_fruit = ['zitrone', 'wasseermelone', 'orange', 'trauben', 'apfel', 'ananas', 'melone', 'birne', 'erdbeere',
             'blaubeere', 'kirsche', 'limone', 'pflaume']
ger_jobs = ['bauer', 'anwalt', 'ingenieur', 'lehrerin', 'kellner', 'pilot', 'richter', 'bibliothekar', 'politikerin',
            'architektin', 'schriftsteller', 'friseur']


def main_menu():
    print("\n \t\t ——————————————————————— \n\t\t|    W I S I E L E C    | \n\t\t ———————————————————————\n")
    time.sleep(1)
    print("Witaj w grze!")
    time.sleep(1)
    print("\nCo chcesz zrobić? Wpisz odpowiednią cyfrę!")
    time.sleep(1)
    print("\n[1] Nowa gra \n[2] Zakończ \n[3] Zobacz ranking wyników \n\n> ")
    time.sleep(1)


def play():
    user_input = input()
    print("Wybrałeś:", user_input)
    time.sleep(1)
    if user_input == "1":
        hangman()

    elif user_input == "2":
        print("Dzięki za grę, miłego dnia!\n")
        quit()
    elif user_input == "3":
        print("Jeśli jeszcze nie grałeś, wpisz 0!\n")
        top_scorers()
        quit()
    else:
        print("Błąd! Niepoprawny wybór!")
        quit()


#
# def get_high_score():
#     high_score = 0
#     try:
#         high_score_file = open("high_score.txt", "r")
#         high_score = int(high_score_file.read())
#         high_score_file.close()
#         print("Najwyższy wynik to ", high_score)
#     except IOError:
#         print("Nie ma jeszcze żadnych wyników.")
#     except ValueError:
#         print("Wprowadziłeś niepoprawny wynik :(")
#     return high_score
#
#
# def save_high_score(new_high_score):
#     try:
#         high_score_file = open("high_score.txt", "w")
#         high_score_file.write(str(new_high_score))
#         high_score_file.close()
#     except IOError:
#         print("Błąd! Nie można zapisać wyniku!")
#
#
# def rank():
#     high_score = get_high_score()
#     current_score = 0
#     try:
#          current_score = int(input("Jaki jest Twój wynik?"))
#     except ValueError:
#         print("Błąd! Wynik musi być liczbą!")
#
#     if current_score > high_score:
#         print("Brawo! Nowy rekord!")
#         save_high_score(current_score)
#     else:
#         print("Niestety nie udało Ci się pobić rekordu. Powodzenia następnym razem :)")


def graphics(guesses, answer):
    if (guesses == 0):
        print('\n')

    elif (guesses == 1):
        print("""



                    _   _
                   |     | ______
                   |             |
                   | ____________|

                    """)
    elif (guesses == 2):
        print("""
                           ____
                          |    |
                          |    
                          |   
                          |  
                          |   
                        _ | _
                       |     | ______
                       |             |
                       | ____________|

                        """, )
    elif (guesses == 3):
        print("""
                           ____
                          |    |
                          |    o
                          |  
                          |  
                          |   
                        _ | _
                       |     | ______
                       |             |
                       | ____________|

                         """)
    elif (guesses == 4):
        print("""
                           ____
                          |    |
                          |    o
                          |    | 
                          |    |
                          |    
                        _ | _
                       |     | ______
                       |             |
                       | ____________|

                         """)

        print("*** Pamiętaj, że w dowolnym momencie możesz poprosić o podpowiedź wpisując 'pomoc' ***\n")

    elif (guesses == 5):
        print("""
                           ____
                          |    |
                          |    o
                          |  / | 
                          |    |
                          |   
                        _ | _
                       |     | ______
                       |             |
                       | ____________|

                        """)
    elif (guesses == 6):
        print("""
                           _____
                          |     |
                          |     o
                          |   / | \\
                          |     |
                          |   
                        _ | _
                       |     | ______
                       |             |
                       | ____________|

                        """)

        print("*** Pamiętaj, że w każdej chwili możesz poprosić o podpowiedź wpisując 'pomoc' ***\n")

    elif (guesses == 7):
        print("""
                           _____
                          |     |
                          |     o
                          |   / | \\
                          |     |
                          |    /
                        _ | _
                       |     | ______
                       |             |
                       | ____________|

                        """)

    elif (guesses == 8):
        print("""
                               _____
                              |     |
                              |     o
                              |   / | \\
                              |     |
                              |    / \\
                            _ | _
                           |     | ______
                           |             |
                           | ____________|
            \n
                            """)
        time.sleep(1)
        print("Hasło brzmiało: " + answer.upper() + "\n")
        time.sleep(1)
        print("\nPrzegrałes :( \nCzy chcesz zagrać jeszcze raz? Wprowadź odpowiednią cyfrę.")
        time.sleep(1)
        print("\n[1] Tak \n[2] Nie")
        time.sleep(1)
        yes_no()
        return


def selectWord():
    print("Czy chcesz wgrać plik .txt czy użyć jednego z domyślnych słów? Wprowadź odpowiednią cyfrę.")
    time.sleep(1)
    user_choice = input("[1] Mój plik .txt \n[2] Losowe gotowe hasło \n> ")
    if user_choice == "1":
        # f = input("Proszę wpisać ścieżkę do pliku, z którego pochodzić będzie hasło.")
        f = 'C:\\Users\marty\OneDrive\Pulpit\positive-words.txt'
        file = open(f, 'r')
        words = file.readlines()
        my_word = ''

        while len(my_word) < 3:
            my_word = random.choice(words)
        my_word = str(my_word).strip('[]')
        my_word = str(my_word).strip('-')
        my_word = str(my_word).strip('-')
        my_word = str(my_word).strip('\"')
        my_word = str(my_word).strip("\'\'")
        my_word = str(my_word).strip("''")
        my_word = str(my_word).strip("\n")
        my_word = str(my_word).strip("\r")
        my_word = my_word.lower()
        return my_word

    elif user_choice == "2":
        language = input(
            "Jaki język wybierasz? Wprowadź odpowiednią cyfrę.\n [1] Polski \n [2] Angielski \n [3] Niemiecki \n> ")
        if language == "1":
            category = input(
                "Jaką kategorię wybierasz? Wprowadź odpowiednią cyfrę.\n [1] zwierzątka \n [2] owoce \n [3] zawody \n")
            if category == "1":
                word = random.choice(pl_animals)
                word = word.lower()
            elif category == "2":
                word = random.choice(pl_fruit)
                word = word.lower()
            elif category == "3":
                word = random.choice(pl_jobs)
                word = word.lower()
            return word

        elif language == "2":
            category = input(
                "Jaką kategorię wybierasz? Wprowadź odpowiednią cyfrę.\n [1] animals \n [2] fruit \n [3] jobs \n")
            if category == "1":
                word = random.choice(eng_animals)
                word = word.lower()
            elif category == "2":
                word = random.choice(eng_fruit)
                word = word.lower()
            elif category == "3":
                word = random.choice(eng_jobs)
                word = word.lower()
            return word

        elif language == "3":
            category = input(
                "Jaką kategorię wybierasz? Wprowadź odpowiednią cyfrę.\n [1] Tiere\n [2] Obst\n [3] Beruf\n")
            if category == "1":
                word = random.choice(ger_animals)
                word = word.lower()
            elif category == "2":
                word = random.choice(ger_fruit)
                word = word.lower()
            elif category == "3":
                word = random.choice(ger_jobs)
                word = word.lower()
            return word

    else:
        time.sleep(1)
        print("Błąd! Wprowadź swój wybór ponownie!")
        selectWord()


def hangman():
    guesses = 0
    word = selectWord()
    word_list = list(word)
    blanks = "_" * len(word)
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    guess_list = []
    print("Zaczynamy grę!\n")
    time.sleep(1)
    print("*** Pamiętaj, że w każdej chwili możesz poprosić o podpowiedź wpisując 'pomoc' ***\n")
    graphics(guesses, word)
    print("\n" + "" + ' '.join(blanks_list) + "\n")
    time.sleep(1)
    print("Wpisz literę!")

    while guesses < 8:
        guess = str(input("> "))
        guess = guess.lower()
        score = 8
        if guess == "pomoc":
            if word[0] not in guess_list:
                print("Pierwsza litera to: " + word[0])
                score = 7
            elif word[1] not in guess_list:
                print("Druga litera to: " + word[1])
                score = 6.5
            elif word[2] not in guess_list:
                print("Trzecia litera to: " + word[2])
                score = 6
            elif word[3] not in guess_list:
                print("Czwarta litera to: " + word[3])
                score = 5.5
            elif word[4] not in guess_list:
                print("Piąta litera to: " + word[4])
                score = 5
            elif word[5] not in guess_list:
                print("Szósta litera to: " + word[5])
                score = 4
            elif word[6] not in guess_list:
                print("Siódma litera to: " + word[6])
                score = 2
            elif word[3] not in guess_list:
                print("Ósma litera to: " + word[7])
                score = 2
            elif word[4] not in guess_list:
                print("Dziewiąta litera to: " + word[8])
                score = 1
            elif word[-2] not in guess_list:
                print("Przedostatnia litera to: " + word[-2])
                score = 0
            elif word[-1] not in guess_list:
                print("Ostatnia litera to: " + word[-1])
                score = 0
            final_score = score
        elif len(guess) > 1:
            print("Wpisz tylko jedną literę.")
        elif guess == "":
            print("Wpisz literę!")
        elif guess in guess_list:
            print("Już użyłeś tej litery! Wpisz nową!")
            print(' '.join(guess_list))
        else:
            guess_list.append(guess)
            i = 0
            while i < len(word):
                if guess == word[i]:
                    new_blanks_list[i] = word_list[i]
                i = i + 1
            if new_blanks_list == blanks_list:
                print("Tej litery nie ma w haśle.")
                guesses = guesses + 1
                graphics(guesses, word)
                if guesses < 8:
                    print("Zgaduj dalej!")
                    print(' '.join(blanks_list))

            elif word_list != blanks_list:
                blanks_list = new_blanks_list[:]
                print(' '.join(blanks_list))

                if word_list == blanks_list:
                    print("\nBrawo! Wygrałeś!")
                    print("Twój wynik to: ", final_score)
                    top_scorers()
                    print("\n")
                    time.sleep(1)
                    # print("Czy chcesz zagrać jeszcze raz? Wprowadź odpowiednią cyfrę.")
                    # time.sleep(1)
                    # print("[1] Tak \n[2] Nie")
                    yes_no()
                else:
                    print("Dobry strzał! Zgaduj dalej!")


def top_scorers():
    final_score = hangman()
    user = str(input("Podaj swoje imię: "))
    file = open("top_scores.txt", "a")
    file.write("\n")
    file.write(user)
    file.write(",")
    file.write(str(final_score))  # (int(x)) can not be written
    file.write("punktów")
    file.write("\n")
    file.close()

    print("\n")
    print("⬇ LISTA WYNIKÓW ⬇")
    f = open('top_scores.txt', 'r')
    winners = [line.replace('\n', '') for line in f.readlines()]
    for i in winners:
        print(i)
    f.close()
    time.sleep(5)
    sys.exit()


def yes_no():
    again = str(input("> "))
    if again == "1":
        hangman()
    elif again == "2":
        print("Dzięki za grę! Miłego dnia!")
        time.sleep(1)
        top_scorers()
        # score
        quit()
    else:
        print("Wprowadź poprawną cyfrę.")
        time.sleep(1)
        yes_no()


def main():
    main_menu()
    time.sleep(1)
    play()
    # if input("\nKliknij ENTER, aby kontynuować lub wpisz 'koniec' by wyjść z gry.") == "koniec":
    #     quit()
    # else:
    #     time.sleep(1)
    #     hangman()
    time.sleep(1)
    hangman()


main()

# Martyna Iwaniec I MA PJN