import pickle
#a function to retrieve the words from the text file, save them to a list of lists, and store it in pickle
def get_word(file_name, l_name):
    #open the text file at the address of file_name
    with open(file_name, "r+") as l_name:

        #read the text file
        whole = l_name.read()

        #create a list of each word that is seperated by a comma on text file
        l_name = [x.strip() for x in whole.split(',')]

        word_list = pickle.load(open("save.p", "rb"))

        #add the list of words from text file to a list of all the lists
        word_list.append(l_name)

        #save the list of lists of words to a pickle, to store words outside program
        pickle.dump(word_list, open("save.p", "wb"))
