import random
import time


def main_menu():
    print("\n \t\t ——————————————————————— \n\t\t|    W I S I E L E C    | \n\t\t ———————————————————————\n")
    time.sleep(1)
    print("Witaj w grze!")
    time.sleep(1)
    print("\nCo chcesz zrobić? Wpisz odpowiednią cyfrę!")
    time.sleep(1)
    print("\n[1] Nowa gra \n[2] Zakończ \n[3] Zobacz ranking wyników \n> ")
    time.sleep(1)
    play()


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
        try:
            print_winners()
        except FileNotFoundError:
            print("\nNie ma jeszcze żadnych wyników na liście zwycięzców!\nZagraj w grę, by dostać się na listę!")
            time.sleep(1)
            yes_no()
    else:
        print("\nBłąd! Niepoprawny wybór!")
        main_menu()


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
                          |    O
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
                          |    O
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
                          |    O
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
                          |     O
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
                          |     O
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
                              |     O
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
        print("\nHasło brzmiało: " + answer.upper() + "\n")
        time.sleep(1)
        print("\nPrzegrałeś :( \n")
        yes_no()
        return


pl_animals = ['piesek', 'żyrafa', 'tygrys', 'jaskółka', 'hipopotam', 'tygrys', 'szympans', 'krokodyl', 'delfin',
              'niedźwiedź', 'antylopa', 'gepard', 'pantera', 'wieloryb', 'gepard', 'pszczoła', 'trzmiel', 'pingwin', 'kangur']
pl_fruit = ['jabłko', 'ananas', 'truskawki', 'porzeczki', 'maliny', 'brzoskwinia', 'borówki', 'gruszka', 'cytryna',
            'jagody', 'mandarynki', 'pomarańcza', 'winogrona', 'agrest', 'arbuz']
pl_jobs = ['marynarz', 'nauczyciel', 'sportowiec', 'programista', 'kierowca', 'sprzedawca', 'dziennikarz', 'piosenkarz',
           'architekt', 'piekarz', 'fotograf', 'lekarz', 'anestezjolog', 'dyrektor', 'kierownik', 'profesor', 'kosmonauta']

eng_animals = ['elephant', 'crocodile', 'panther', 'monkey', 'gorilla', 'cheetah', 'chameleon', 'chicken', 'hedgehog',
               'giraffe', 'butterfly', 'rabbit', 'gosling', 'kangaroo', 'dolphin', 'duckling', 'whale', 'python', 'hedgehog']
eng_fruit = ['strawberry', 'raspberry', 'pineapple', 'orange', 'honeydew', 'bananas', 'coconut', 'blueberry', 'grapefruit',
             'watermelon', 'dragonfruit', 'passionfruit', 'elderberry', 'apricots', 'pomegranate', 'tangerine' ]
eng_jobs = ['teacher', 'musician', 'dancer', 'programmer', 'builder', 'firefighter', 'policeman', 'photographer',
            'waitress', 'baker', 'lawyer', 'journalist', 'astronaut', 'mechanic', 'stewardess', 'postman']

ger_animals = ['elefant', 'gorilla', 'gepard', 'krokodil', 'kaninchen', 'schmetterling', 'giraffe', 'schwein', 'frosch',
               'pferde', 'fisch', 'hund', 'vogel', 'schlange']
ger_fruit = ['zitrone', 'wasseermelone', 'orange', 'trauben', 'apfel', 'ananas', 'melone', 'birne', 'erdbeere',
             'blaubeere', 'kirsche', 'limone', 'pflaume']
ger_jobs = ['bauer', 'anwalt', 'ingenieur', 'lehrerin', 'kellner', 'pilot', 'richter', 'bibliothekar', 'politikerin',
            'architektin', 'schriftsteller', 'friseur']


def select_word():
    print("\nCzy chcesz wgrać plik .txt czy użyć jednego z domyślnych słów? Wprowadź odpowiednią cyfrę.\n")
    time.sleep(1)
    user_choice = input("[1] Mój plik .txt \n[2] Gotowe losowe hasło \n> ")
    if user_choice == "wstecz":
        main_menu()
    elif user_choice == "1":
        f = input("\nProszę wpisać ścieżkę lub nazwę pliku, z którego program wylosuje hasło.\n> ")
        try:
            file = open(f, 'r')
            words = file.read().replace('\n', ' ').split(' ')[:-1]
            my_word = 'a'
            while len(my_word) < 4:
                my_word = random.choice(words)
                my_word = str(my_word).strip('[]')
                my_word = str(my_word).strip("''")
                my_word = str(my_word).strip(".")
                my_word = str(my_word).strip('"')
                my_word = str(my_word).strip(",")
                my_word = str(my_word).strip(":")
                my_word = str(my_word).strip("\n")
                my_word = str(my_word).strip("\r")
            my_word = my_word.lower()
            return my_word
        except FileNotFoundError:
            print("\nBłąd!\n")
            select_word()
        except EOFError:
            print("\nBłąd!\n")
            select_word()
        except OSError:
            print("\nBłąd!\n")
            select_word()
        except TypeError:
            print("\nBłąd!\n")
            select_word()
        except AssertionError:
            print("\nBłąd!\n")
            select_word()
    elif user_choice == "2":
        time.sleep(1)
        print("\nJaki język wybierasz?\n")
        time.sleep(1)
        word = None
        language = input("Wprowadź odpowiednią cyfrę.\n [1] Polski \n [2] Angielski \n [3] Niemiecki \n> ")
        if language == "wstecz":
            select_word()
        elif language == "1":
            print("\nUwaga! Pamiętaj, że w przygotowanych hasłach występują polskie znaki!\n")
            time.sleep(1)
            print("Jaką kategorię wybierasz?\n")
            time.sleep(1)
            category = input("Wprowadź odpowiednią cyfrę.\n [1] zwierzątka \n [2] owoce \n [3] zawody\n> ")
            if category == "wstecz":
                select_word()
            elif category == "1":
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
            print("\nJaką kategorię wybierasz?\n")
            time.sleep(1)
            category = input("Wprowadź odpowiednią cyfrę.\n [1] animals \n [2] fruit \n [3] jobs\n> ")
            if category == "wstecz":
                select_word()
            elif category == "1":
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
            print("\nJaką kategorię wybierasz?\n")
            time.sleep(1)
            category = input("Wprowadź odpowiednią cyfrę.\n [1] Tiere\n [2] Obst\n [3] Beruf\n> ")
            if category == "wstecz":
                select_word()
            elif category == "1":
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
            select_word()
    else:
        time.sleep(1)
        print("\nBłąd! Wprowadź swój wybór ponownie!\n")
        select_word()


def hangman():
    guesses = 0
    try:
        w = select_word()
        w_list = list(w)
        blanks = "_" * len(w)
        blanks_list = list(blanks)
        new_blanks_list = list(blanks)
        guess_list = []
        print("Zaczynamy grę!\n")
        time.sleep(1)
        print("*** Pamiętaj, że w każdej chwili możesz poprosić o podpowiedź wpisując 'pomoc' ***\n")
        graphics(guesses, w)
        print("\n" + "" + ' '.join(blanks_list) + "\n")
        time.sleep(1)
        print("Wpisz literę!\n")

        while guesses < 8:
            guess = str(input("\n> "))
            guess = guess.lower()
            if guess == "pomoc":
                if w[0] not in guess_list:
                    print("\n\t\tPierwsza litera to: " + w[0])
                elif w[1] not in guess_list:
                    print("\n\t\tDruga litera to: " + w[1])
                elif w[2] not in guess_list:
                    print("\n\t\tTrzecia litera to: " + w[2])
                elif w[3] not in guess_list:
                    print("\n\t\tCzwarta litera to: " + w[3])
                elif w[4] not in guess_list:
                    print("\n\t\tPiąta litera to: " + w[4])
                elif w[5] not in guess_list:
                    print("\n\t\tSzósta litera to: " + w[5])
                elif w[6] not in guess_list:
                    print("\n\t\tSiódma litera to: " + w[6])
                elif w[3] not in guess_list:
                    print("\n\t\tÓsma litera to: " + w[7])
                elif w[4] not in guess_list:
                    print("\n\t\tDziewiąta litera to: " + w[8])
                elif w[-2] not in guess_list:
                    print("\n\t\tPrzedostatnia litera to: " + w[-2])
                elif w[-1] not in guess_list:
                    print("\n\t\tOstatnia litera to: " + w[-1])
            elif len(guess) > 1:
                print("\t\tWpisz tylko jedną literę!\n")
            elif guess == "":
                print("\t\tWpisz literę!")
            elif guess in guess_list:
                print("\t\tJuż użyłeś tej litery! Wpisz nową!\n")
                print(' '.join(guess_list)) #used letters
            else:
                guess_list.append(guess)
                i = 0
                while i < len(w):
                    if guess == w[i]:
                        new_blanks_list[i] = w_list[i]
                    i = i + 1
                if new_blanks_list == blanks_list:
                    print("\n\t\tTej litery nie ma w haśle.\n")
                    guesses = guesses + 1
                    graphics(guesses, w)
                    if guesses < 8:
                        x = ["Nie poddawaj się!", "Zgaduj dalej!", "Nie tym razem!"]
                        print("\n\t\t", random.choice(x), "\n")
                        print(' '.join(blanks_list)) #blanks and guessed

                elif w_list != blanks_list:
                    blanks_list = new_blanks_list[:]
                    print(' '.join(blanks_list)) #blanks and guessed

                    if w_list == blanks_list:
                        print("\n\t\tBrawo! Wygrałeś!")
                        time.sleep(1)
                        name = str(input("\nPodaj swoje imię: "))
                        get_winner(name)
                        print("\n")
                        time.sleep(1)
                    else:
                        x = ["Dobry strzał! Zgaduj dalej!", "Oby tak dalej!", "Wyśmienicie :)",
                             "Super! Jesteś już blisko zwycięstwa!"]
                        print("\n\n\t\t", random.choice(x))
    except TypeError:
        hangman()


def get_winner(name):
    file = open("top_winners.txt", "a")
    file.write("\n")
    file.write(name)
    file.write("\n")
    file.close()
    print_winners()


def print_winners():
    print("\n")
    print("⬇ LISTA ZWYCIĘZCÓW ⬇")
    f = open('top_winners.txt', 'r')
    winners = [line.replace('\n', '') for line in f.readlines()]
    for i in winners:
        print(i)
    f.close()
    time.sleep(2)
    yes_no()


def yes_no():
    print("\nCzy chcesz zagrać nową rozgrywkę? Wybierz odpowiednią cyfrę.")
    time.sleep(1)
    print("\n[1] Tak \n[2] Nie \n> ")
    time.sleep(1)
    again = str(input())
    if again == "1":
        hangman()
    elif again == "2":
        time.sleep(1)
        print("Dzięki za grę! Miłego dnia!")
        time.sleep(1)
        quit()
    else:
        time.sleep(1)
        print("Wprowadź poprawną cyfrę.")
        time.sleep(1)
        yes_no()


def main():
    main_menu()
    time.sleep(1)
    hangman()


main()
