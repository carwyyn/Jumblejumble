# Jumble the words game
import random
import get_words
import time
import pickle


def play(word_list):
    # set the count, as to only give the user 10 words to decrypt
    count = 0
    # keep note of the score
    score = 0

    new_list = word_list
    while count < 10:
        # pick a random word from the list
        word = random.choice(new_list)

        correct = word
        # to put the jumbled word in
        jumble = ""
        # REFERENCE: code from lecture booklet, chapter 4, jumble game
        while (len(word) > 0):

            position = random.randrange(len(word))

            jumble += word[position]

            word = word[:position] + word[(position + 1):]

        print("jumble word is {}.".format(jumble))

        # Getting the players guess

        guess = str(input("Enter your guess: "))
        if guess == correct:
            print("Congratulations")
            score += 1
        else:
            print("Sorry, you lose, the word was {}".format(correct))
        count += 1

        
    # after they have guessed 10 times   
    else:
        # show overall score
        print("Thanks for playing, your score is %2d." % (score))
        
        # open the scorelist from the pickled file
        scorelist = pickle.load(open("score.p", "rb"))
        
        # append the list with a list with the latest score and time
        scorelist.append([str(score), str(time.strftime("%H:%M  %d-%m-%Y"))])

        # SORTING the score
        for num in range(len(scorelist) - 1, 0, -1):  # go through scorelist
            for i in range(num):  # for every element within list
                # check to see if first element of i item is bigger than 1st
                # element of i+1 item
                
                if scorelist[i][0] < scorelist[i + 1][0]:
                    
                    # if it is bigger, swap them around
                    temp = scorelist[i + 1]
                    
                    scorelist[i + 1] = scorelist[i]
                    
                    scorelist[i] = temp
                    
        # re-pickle the list of scores
        pickle.dump(scorelist, open("score.p", "wb"))
