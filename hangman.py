import time
import re
import random

play_again='y'
while play_again=='y':

    guess=[] 
    flag=False
    user_guessed_letters=[] #keep track of already guessed words to avoid repetition

    #chooses a random word from the words_list file
    with open("words_list.txt","r") as words_file:
        lines=words_file.readlines()
        list_of_words=[]
        for word in lines:
            #print(word.strip())
            list_of_words.append(word.strip())
    #print(list_of_words)
    words_to_find=random.choice(list_of_words)
    #print(words_to_find)


    hangman=[''' 
    +---+
        |
        |
        |
        |
       --- ''',
       ''' 
    +---+
    |   |
        |
        |
        |
       ---''',
       ''' 
    +---+
    |   |
    O   |
        |
        |
       ---''',
       ''' 
    +---+
    |   |
    O   |
    |   |
        |
       ---''',
       
      '''
    +---+
    |   |
    O   |
    |\  |
        |
       ---  ''',
       ''' 
     +---+
     |   |
     O   |
    /|\  |
         |
       ---''',
       ''' 
     +---+
     |   |
     O   |
    /|\  |
     |   |
       ---''',
       ''' 
     +---+
     |   |
     O   |
    /|\  |
     |\  |
       ---''',
       ''' 
     +---+
     |   |
     O   |
    /|\  |
    /|\  |
       ---'''
    ]
    #print(len(hangman))

    #Initial prompt
    print("---------------------------------HANGMAN--------------------------------------")
    user_name=input("Enter your name : ")
    print("\n")
    print("Welcome {} !!! Lets play !!!".format(user_name))
    print("Game loading...")
    time.sleep(1)
    print("\n")
    print("Here you go!")
    hangman_index_position=0
    hangman_position=hangman[0]
    print(hangman_position)
    print("Don't get hanged ! Good luck !")
    time.sleep(2)



    #initially fill the list with blanks
    for char in words_to_find:
        guess.append("_")
    print("\n")
    print("A {} letter word".format(len(words_to_find)))
    print("\n")
    print(guess)
    print("\n")


    while hangman_index_position<len(hangman)-1: #loop until the last picture (hanged) occurs in hangman list
        print("\n")
        time.sleep(1)
        user_input=input("Guess a character : ")
        user_input=user_input.lower()
        count=words_to_find.count(user_input) 
        
        #Accept only letters 'a' to 'z'
        if not re.match("^[a-z][A-Z]*$",user_input):
            print("Only letters are accepted")
            user_input=input("Try a letter (a-z) : ")
        
        
        
        #To handle repeated guesses of same letter by the user
        if user_input in user_guessed_letters:
            print("Already guessed ! You have guessed these letters so far : {}".format(user_guessed_letters))
            user_input=input("Try another letter : ")
        else:
            user_guessed_letters.append(user_input)
       
            
        
        #if user_input character is in the word_to_find replace blank with the guessed letter
        if user_input in words_to_find: 
            if count==1:   #if the character occurs only once in words_to_find
                idx=words_to_find.index(user_input)
                guess[idx]=user_input
           
            else:          #if character occurs more than once in words_to_find
                index=[idx for idx,word in enumerate(words_to_find) if word==user_input]
                #print(index)
                for idx in index:
                    guess[idx]=user_input
            
            
            if hangman_index_position!=8 and "_" in guess: #if its not the last but one turn and still there are letters to be found
                print("\n")
                print("Wohoooo! That's a correct guess. Go on !")
                print(guess)
                print("--------------------------------------------------")
            elif "_" not in guess: #if all letters are found
                print("\n")
                print(guess)
                print("Well done !You Won !!!")
                flag=True
                print("\n")
                print("---------------------------------Game Over--------------------------------------")
                turns=0
                break
            else: #if its the last but one turn
                print("\n")
                print(guess)
        
        #if the guessed character is wrong 
        else:
            #increment hangman position for every wrong answer
            hangman_position=hangman[hangman_index_position+1]
            hangman_index_position+=1
            print(hangman_position)
            time.sleep(1)
            
            if hangman_index_position!=8: #not the last but one turn
                print("\n")
                print("NAH ! Give it another shot !")
                print(guess)
                print("--------------------------------------------------")
            else: #if it is the last but one turn
                print("\n")
                print(guess)
                
        
    if flag==False:
        print("\n")
        print("You lost !!! :( ")
        print("THE WORD IS : ",words_to_find)
        print("\n")
        print("---------------------------------Game Over--------------------------------------")
    play_again=input("Do you want to play again ? (y/n) : ")       