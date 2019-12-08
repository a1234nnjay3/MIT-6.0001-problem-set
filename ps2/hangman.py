# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import time

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
#print("secret_word = "+"'"+ secret_word+"'")

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    check = 0
    for word in secret_word:
        if word in letters_guessed:
            check+=1
    return check==len(secret_word)

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guess_words = "'"+ "_"*len(secret_word)+"'"
    guess_word = list(guess_words)
    for char1 in letters_guessed:
        n=1
        for char2 in secret_word:
            if char1 == char2:
                guess_word[n] = char1
            n+=1
    guess_words = ''.join(guess_word)
    return guess_words

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = string.ascii_lowercase
    available_letters_list = list(available_letters)
    for char1 in letters_guessed:
        for char2 in available_letters_list:
            if char1 == char2:
                available_letters_list.remove(char2)
    available_letters = ''.join(available_letters_list)
    return available_letters

def check_warning(number_of_warning,letters_guessed,guessing_letter,num_of_guesses):
    if number_of_warning >=0:
        if guessing_letter.isalpha() == False or len(guessing_letter)>1:
            print("Oops! That is a valid letter.")
            number_of_warning-=1
            print("You have ", number_of_warning , 
                  "warnings left:", get_guessed_word(secret_word, letters_guessed))
    else:
        print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", 
              get_guessed_word(secret_word, letters_guessed))
        num_of_guesses-=1
        number_of_warning = 3
    return number_of_warning

def unique_letters(secret_word):
    count = 0
    for i in string.ascii_lowercase:
        if i in secret_word:
            count+=1
    return count

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    num_of_guesses = 6
    number_of_warning = 3
    letters_guessed = []
    print("Welcome to the game HangMan! \nI'm thinking of a word that is", len(secret_word), "letters long!")
    print("You have ", number_of_warning , "warnings left!")
    while is_word_guessed(secret_word, letters_guessed)==False and num_of_guesses>0:
        print("-----------------")
        print("You have", num_of_guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guessing_letter = str(input("Please guess a letter: "))
        if guessing_letter in string.ascii_uppercase:
            guessing_letter=guessing_letter.lower()
        #Input Check(alphabet or non-alphabet)
        if guessing_letter.isalpha() == False or len(guessing_letter)>1:
            if number_of_warning >0:
                print("Oops! That is not a valid letter.")
                number_of_warning-=1
                print("You have ", number_of_warning , 
                      "warnings left:", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! You have no warnings left so you lose one guess:", 
                      get_guessed_word(secret_word, letters_guessed))
                num_of_guesses-=1
                number_of_warning = 3
        
        #Check Repeat or Right or Wrong
        if guessing_letter.isalpha() == True and len(guessing_letter)==1:
            if guessing_letter in letters_guessed:
                number_of_warning-=1
                if number_of_warning < 0:
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", 
                      get_guessed_word(secret_word, letters_guessed))
                    num_of_guesses-=1
                    number_of_warning = 3
                else:
                    print("Oops! You've already guessed that letter. You have",
                      number_of_warning, "warnings left:", get_guessed_word(secret_word, letters_guessed))
            elif guessing_letter in secret_word:
                letters_guessed.append(guessing_letter)
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                letters_guessed.append(guessing_letter)
                if guessing_letter in ['a','e','i','o']:
                    num_of_guesses-=2
                else:
                    num_of_guesses-=1
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        time.sleep(1)
        
    if is_word_guessed(secret_word, letters_guessed)==True:
        print("-----------------")
        print("Congratulations, you won!")
        print("Your total score for this game is:", num_of_guesses*unique_letters(secret_word))
        print("Let's have sex!")
    else:
        print("Sorry, you ran out of guesses. The word was",secret_word,".")
        
    return



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    other_word.replace(" ", "")
    my_word.replace(" ", "")
    
    check  = False
    if len(my_word) == len(other_word):
        check = True
        for i in range(len(my_word)):
            if my_word[i] == "_":
                pass
            elif my_word[i] != other_word[i]:
                check = False
    return check



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    a = 0
    b = my_word.strip(" ' ")
    for word in wordlist:
        if match_with_gaps(b, word) == True:
            print(word, end=' ')
            a+=1
    if a == 0:
        print("No matches found", end='')
    return
#show_possible_matches(get_guessed_word(secret_word, letters_guessed))


def hangman_with_hints(secret_word):
    
    num_of_guesses = 6
    number_of_warning = 3
    letters_guessed = []
    print("Welcome to the game HangMan! \nI'm thinking of a word that is", len(secret_word), "letters long!")
    print("You have ", number_of_warning , "warnings left!")
    while is_word_guessed(secret_word, letters_guessed)==False and num_of_guesses>0:
        print("-----------------")
        print("You have", num_of_guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guessing_letter = str(input("Please guess a letter: "))
        
        if guessing_letter in string.ascii_uppercase:
            guessing_letter=guessing_letter.lower()
        #Input Check(alphabet or non-alphabet)
        if guessing_letter.isalpha() == False or len(guessing_letter)>1:
            if guessing_letter == "*":
                print("Possible word matches are:")
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
                print("\n")
            elif number_of_warning >0:
                print("Oops! That is not a valid letter.")
                number_of_warning-=1
                print("You have ", number_of_warning , 
                      "warnings left:", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! You have no warnings left so you lose one guess:", 
                      get_guessed_word(secret_word, letters_guessed))
                num_of_guesses-=1
                number_of_warning = 3
        
        #Check Repeat or Right or Wrong
        if guessing_letter.isalpha() == True and len(guessing_letter)==1:
            if guessing_letter in letters_guessed:
                number_of_warning-=1
                if number_of_warning < 0:
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", 
                      get_guessed_word(secret_word, letters_guessed))
                    num_of_guesses-=1
                    number_of_warning = 3
                else:
                    print("Oops! You've already guessed that letter. You have",
                      number_of_warning, "warnings left:", get_guessed_word(secret_word, letters_guessed))
            elif guessing_letter in secret_word:
                letters_guessed.append(guessing_letter)
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                letters_guessed.append(guessing_letter)
                if guessing_letter in ['a','e','i','o']:
                    num_of_guesses-=2
                else:
                    num_of_guesses-=1
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        time.sleep(1)
        
    if is_word_guessed(secret_word, letters_guessed)==True:
        print("-----------------")
        print("Congratulations, you won!")
        print("Your total score for this game is:", num_of_guesses*unique_letters(secret_word))
        print("Let's have a marathon sex!")
        time.sleep(1)
        print("Plz.......")
    else:
        print("Sorry, you ran out of guesses. The word was",secret_word,".")
    return



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
