
Word Guessing Game
This is a simple word-guessing game where the player has to guess the letters of a randomly chosen secret word. The player has a limited number of chances based on the length of the word. The game ends when the player either guesses the entire word or runs out of chances.

How it works
Word Selection:
A word is randomly selected from the file palavras.txt, which contains a list of words, each on a new line. You can add more words to this file if you like.

Gameplay:

The player guesses letters one by one.
Correct guesses reveal the positions of those letters in the word.
Incorrect guesses reduce the player's available chances.
The game ends when the player guesses all the letters correctly or runs out of chances.
Winning/Losing:

Win: The player wins if they guess all the letters of the secret word before their chances run out.
Lose: The player loses if they run out of chances without guessing the word.
Installation and Setup
Ensure you have Python installed on your machine.
Clone or download this repository.
Add your word list to the palavras.txt file, if desired. Each word should be on a new line.
Example:
bash
Copiar código
limao
abacaxi
uva
How to Run the Game
Open a terminal or command prompt in the directory where the script is located.
Run the following command:
bash
Copiar código
python3 game.py
or
bash
Copiar código
python game.py
How to Add Words to the Game
You can add new words to the game by appending them to the palavras.txt file. Each word should be on a new line. Example of adding a word in Python:

python
Copiar código
adc_palavra = open("palavras.txt", "a")
adc_palavra.write("manga \n")
adc_palavra.close()
Features
Random word selection from a text file.
Tracks letters guessed by the player.
Limits the number of incorrect guesses based on word length.
Simple win/lose messages displayed at the end of the game.
Requirements
Python 3.x
A text file (palavras.txt) containing the list of words.
Example of Gameplay
bash
Copiar código
_ _ _ _ _ _ 
Você tem 6 chances

Escolha uma letra: A
_ A _ A _ A 
Você tem 6 chances

Escolha uma letra: B
_ A _ A _ A 
Você tem 5 chances

Escolha uma letra: C
A palavra secreta era: BANANA
Parabéns, você ganhou!
