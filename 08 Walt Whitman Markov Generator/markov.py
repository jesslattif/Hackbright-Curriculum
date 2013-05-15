#!/usr/bin/env python

import sys
import random
#import twitter
#http://inventwithpython.com/blog/2012/03/25/how-to-code-a-twitter-bot-in-python-on-dreamhost/

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    # split text into a list of words
    text_list = read_text.split() #splitting text into a list of words
    
    global text_dict
    text_dict = {} #creating empty dictionary

    i = 0 #setting index count to zero

    for word in text_list: #create variable word in list
        # we want the key to be two words
        if i == (len(text_list) - 2):  #prevents from breaking at the end of the list
            break
        else:
            key = (text_list[i],text_list[i + 1])
            if key not in text_dict: # if word isn't in the dictionary,
                text_dict[key] = [text_list[i+2]] # for the word in "i" position which is the dict key, create a value for that key which is a list of the word that follows that key
                
            else: # if the word is already a key in the text dictionary DON'T OVERWRITE PREVIOUS VALUE -- instead, append the word that follows to the value list for that key
                text_dict[key].append(text_list[i+2])
        i += 1 # then move to the next place

    return text_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    
    key_list = []

    for i in text_dict.keys(): # creates a list of all keys in text_dict that start with capital letters
        if i[0][0].istitle() == True:
            key_list.append(i)

    markov_list = []

    first_half = random.choice(key_list) #choose a random key from the new keys list
    markov_list.append(first_half[0])
    markov_list.append(first_half[1])
    
    punct = [".", "!", "?"]

    while not markov_list[-1][-1] in punct or len(markov_list) < 15:
        tuple_key = (markov_list[-2], markov_list[-1])
        next_value = random.choice(text_dict[tuple_key])
        markov_list.append(next_value)

    return " ".join(markov_list) 
    
def write_text(random_text):
    output_file = str(raw_input("File to save output: "))
    if output_file == "":
        return
    target = open(output_file, "a+") #"a+" prevents overwrite, writes to the end of the file
    target.write(random_text+'\n\n')
    target.close()    

def main():
    args = sys.argv
    global read_text

    # Change this to read input_text from a file
    input_text = open(args[1])
    
    read_text = input_text.read()
    input_text.close()

    """Call the functions and make them run"""

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    write_text(random_text)
    print random_text

if __name__ == "__main__":
    main()
