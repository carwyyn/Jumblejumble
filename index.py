# 1327289
# Import other modules
from get_words import *
import game


# greet the player
print ("""
Welcome to word jumble!
""")

# set answer to 0 as the starting point for where to take user
answer = 0

# if exit has not been executed, give user options
while answer != 6:
    print("""
Pick an option:
1 -- Play the game
2-- Browse a word set
3-- Add a new word set
4-- Delete a word set
5-- My sorted scores
6-- Exit
""")

    # The user's choices

    # ensure user's answer is valid and an option
    answer = int(input("Please select:"))

    # if its an invalid option, give the user another go, otherwise
    # program would come to an error
    while answer not in (1, 2, 3, 4, 5, 6):
        input("Please select a number from the list above: ")

    # playing the game
    if answer == 1:
        print ("""
        Which word set would you like?
        """ )
        # loads the word lists available, and gives an option to which one the user
        # wants to pick based on the index
        word_list = pickle.load(open("save.p", "rb"))
        notin = []
        for t in word_list:
            notin.append(word_list.index(t))
            print(word_list.index(t), t[0])

        answer1 = int(input())
        # again, ensure user's choice is valid
        while answer1 not in notin:
            answer1 = int(input("Please select a number from the list: "))
        notin.clear

        # execute the game using the wordlist they chose
        # game is defined in another module, so imports the play element
        game.play(word_list[answer1])

    # browsing word sets
    elif answer == 2:
        print("Which word set would you like to browse?")
        word_list = pickle.load(open("save.p", "rb"))
        notin = []
        for t in word_list:
            notin.append(word_list.index(t))
            print(word_list.index(t), t[0])

        answer2 = int(input())

        while answer2 not in notin:
            answer2 = int(input("Please select a number from the list: "))
        notin.clear()

        # prints the first word in list as the list title
        print("******")
        print(word_list[answer2][0])
        print("******")
        for l in word_list[answer2]:
            # print the whole list, without starting a new line each time
            print(l, end="  ")

    # Add a new word file to the program
    elif answer == 3:
        file_name = input("Name of file: ")
        l_name = input("Name of list: ")
        # confirms to the user of the procedure
        print(l_name, "added")

        # puts the user's information into a defined function from another
        # module
        get_word(file_name, l_name)

    # Delete a wordset
    elif answer == 4:
        print("Which word set would you like to delete?")
        word_list = pickle.load(open("save.p", "rb"))
        notin = []
        for t in word_list:
            notin.append(word_list.index(t))
            print(word_list.index(t), t[0])

        answer3 = int(input())

        while answer3 not in notin:
            answer2 = int(input("Please select a number from the list: "))
        notin.clear()

        print(word_list[answer3][0], "deleted")
        # deletes word from the updated file from pickle
        del word_list[answer3]
        # re-saves the updated file without the deleted word list
        pickle.dump(word_list, open("save.p", "wb"))

    elif answer == 5:
        # gives the score list a title
        print(("{:6s} {:13s}").format('Score', 'Date'))
        # load the scores from pickle
        scores=pickle.load(open("score.p", "rb"))

        # show the scores without the list brackets
        for s in scores:
            print(s[0], s[1])

    # Quit the program
    else:
        # ensure the user is sure they want to exot
        qu=input("Are you sure you want to quit? (Y/N)")
        while qu not in ["Y", "y", "N", "n"]:
            qu=input("Please select Y or N")
        if qu in ["Y", "y"]:
            quit()
        # otherwise go back to main pick options
        else:
            answer=0
