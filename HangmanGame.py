#Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess.
#This starts up an interactive game of Hangman between the user and the computer. 
#Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, 
#that you've defined in the previous part.

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    import string
   
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    lettersGuessed = [] 
    guessLeft = 8
    while (guessLeft > 0) :
        print ("-------------")
        print ("You have " + str(guessLeft) + " guesses left.")
        availableLetters = getAvailableLetters(lettersGuessed)
        print ("Available letters :" + str(availableLetters))
        guess = input("Please guess a letter:")
        guessLower = guess.lower()
        if guessLower in lettersGuessed :
            print("Oops! You've already guessed that letter: " + str(wordGuessed))
        else:
            lettersGuessed.append(guessLower)
            wordGuessed = getGuessedWord(secretWord, lettersGuessed)
            if guessLower in secretWord :
                print("Good guess: " + str(wordGuessed))
                if(isWordGuessed(secretWord, lettersGuessed)):
                    print ("-------------")
                    print ("Congratulations, you won!")
                    return None
            else:
                print("Oops! That letter is not in my word: " + str(wordGuessed))
                guessLeft -= 1
    
    if(guessLeft == 0):
        print ("-------------")
        print("Sorry, you ran out of guesses. The word was " + str(secretWord) + ".")
                
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    all_letters = string.ascii_lowercase
    avail_letters = []
    for char in all_letters:
        if char not in lettersGuessed:
            avail_letters.append(char)
        
    return ("".join(avail_letters))

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guess_elem = '_ '
    guessList = []
    for i in range(len(secretWord)) :
        guessList.append(guess_elem)
    index = 0
    for char in secretWord :
        if char in lettersGuessed :
            guessList[index] = char
        index += 1
    GuessedWord = "".join(guessList) 
    return GuessedWord
     
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    for char in secretWord :
        if char not in lettersGuessed :
            return False
    return True
        
        

