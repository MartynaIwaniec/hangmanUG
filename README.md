# wisielecUG
The program is for Python programming course. 
Documentation is for technical writing task.

# Overview
This document will explain step-by-step how to run the program game.py on **Linux Ubuntu** in 4 simple steps.

If you know how to run Python scripts on Linux, go straight to **Step 4**!

**Step 1** Make sure Python 3 is installed on your computer or install it.
**Step 2** Download the source code from a GitHub repository.
**Step 3** Run the program.
**Step 4** Play hangman.

# Step 1

Linux distributions may include an outdated version of Python (Python 2), but you should install an updated one (Python 3)

*Remember to be careful while using the command line, because you may accidentely damage or remove your data. Write only commands that you known exactly what is their purpose.*

**Access to a command-line/terminal window on Linux:**

                   Ctrl-Alt-T
    
**To find out if Python3 is installed, type the command:** 

                    python3

        
- If your version is Python 3.7.x (x stands for the revision level and could change as new releases come out), go to **Step 2**.

- To **install** Python 3 by writing **sudo apt-get install python3** in the terminal or go to https://www.python.org/downloads/ 
If you are a beginner, I reccomend reading the guide https://wiki.python.org/moin/BeginnersGuide as well.

More details on Python can be found on the [official Python page](https://www.python.org/about/)
and on its [Wikipedia page](https://en.wikipedia.org/wiki/Python_(programming_language)).


# Step 2
Now, you need to download the source code of the Python program you want to run from Github.

##### [Click to go to the Github repository.](https://github.com/MartynaIwaniec/wisielecUG)

You can **download** either:
- **a single Python source code** file
(with extension ".py")
First, click on **wisielec.py** to go to the specific file. Then, click on **Raw** to open the raw source code. Then, you can copy and save it into a new file.
![alt text](https://i.imgur.com/3KUxp5e.png "pic1")

- or **a ZIP file containing the Python file
and the documentation** (which you are currently reading).
![alt text](https://i.imgur.com/HKukWP5.png "pic2")


- It is also possible to access the source code with **git** command. To find out more, go to [Github page]( https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository )!

When you have cloned the .py file, go to the next step.

# Step 3
- Locate where the dowloaded file is located. You may have to unpack it. When you find out the path to the .py file, open up the terminal.

- You can write **ls** in which directory you are. Use the **cd** command to get to the directory with the .py file in it.

- You have to make the script executable first.
Write **chmod a+x in the terminal).

- To run the program, write **./wisielec.py**

Now you can finally play the game!

# Step 4
When you've sucessfully run the program, you should see the main manu:
![alt text](https://i.imgur.com/VUsnxXw.png "pic3")

Please make sure to follow the instructions displayed on the screen throughout the game.

If you want to **play a new game**, choose **1**.
![alt text](https://i.imgur.com/Y6Dzv8X.png
 "pic12")
If you want to *exit the game**, choose **2**.
 ![alt text]( https://i.imgur.com/AADiqOw.png
 "pic11")

If you want to **see the winners**, choose **3**.
- If you haven't won yet, you the program will inform you that the list is empty. To get on the winners list, you have to win a game.
- If you won before, you should see your name on the list.
- Then you  will be asked if you want to start a new game. If you choose **1**, a new game will start by asking you where do you want to get the word from. If you choose **2**, the program will stop.
![alt text](https://i.imgur.com/D8u9kL3.png)


## If you choose **1** to play the game:
- Choose **1** if you want to get a word from your own .txt file.
- Choose **2** if you wan to get a random word from the program.

#### If you choose 1 to get a word from a .txt file, the program will ask you to enter the full path to the .txt file.
After you enter it, you can start guessing!
![alt text](https://i.imgur.com/Hw5xhLZ.png
 "pic5")
 
 Now, you need to enter one letter to check if it is in the word.
 - If you guess corretly, you should see congratulations:
 
![alt text](https://i.imgur.com/ql7o4xe.png
 "pic6")
 
- However, if you guess wrong you will see **Zgaduj dalej!**.
 
- If you enter a letter which you have already guessed, you will see **Już użyłeś tej litery! Wpisz nową!** as well as a list of the letters that you have already tried.

- If you enter more than 1 letter, you will get a message saying **Wpisz tylko jedną literę.**.
 
 Continue to enter letters until you will see the complete world. The program will congratulate you on your win by printing **Brawo! Wygrałeś!**.

Then, the program will ask you to enter your name in order to save it to the winners list.
 ![alt text](https://i.imgur.com/WS5lz7I.png "pic7")

- If you have problems with guessing the right letters, you can always use a lifeline by typing **pomoc**.
Then, the program will give you one of the letters that you need.
You can use the lifeline as many times as you need.

The program will remind you about the lifeline if it notices that you are struggling with guessing the correct letters.
 ![alt text](https://i.imgur.com/VNF2xHF.png "pic8")

 
 - You should remember than every time you are wrong, the game will add a portion of the hangman. 
 You have 8 tries, until the hangman in completed.

In the picure, first stages of the hangman are being added:
 ![alt text](https://i.imgur.com/6a9izYm.png "pic9")

- When the whole hangman is completed, the game is over and you lose.
After your 8th wrong entry, the proram will inform you that you lost and display the word that you haven't guessed.

- After every game, you will be asked if you want to play again. Choose **1** to play again or **2** to exit the game.
![alt text](https://i.imgur.com/pDHh2Kb.png "pic10")

#### You can also get a random word form the game and not use your own .txt file.
If you choose this option, you will have to select a language:
- Enter **1** to choose Polish, **2** to choose English or **3** to choose German.

![alt text](https://i.imgur.com/af1LHP4.png "pic13")

 After that, you will have to choose a category:
- Enter **1** to choose animals, **2** to choose fruit or **3** to choose jobs.

![alt text](https://i.imgur.com/xfgC7mB.png "pic14")

After you choose a category, you can start guessing! Good luck!

Last thing you should know is that if you choose a wrong option by mistake, you can always go back by typing **wstecz**!
