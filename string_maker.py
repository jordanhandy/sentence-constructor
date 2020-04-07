##################################################################
# Map Renderer 
# Description:
# This program takes a set of strings.  It concatenates these 
# strings to form sentences.
# Once the user enters an exit command, the program exits, 
# and the final String is output to the screen
##################################################################

# Variables
user_input = ""
# to hold concatenated string
stringList = []
# interrogatives to change sentence ending
interrogatives = ("who","what","where","when","why","how")

def sentenceMaker(phrase):
    # if the phrase starts with an interrogative, captialize
    # the phrase, and end the sentene with a ? 
    if (phrase.startswith(interrogatives)):
        return "{}?".format(phrase.capitalize())
    else:
        return "{}.".format(phrase.capitalize())

# the user enters string until they specify "\end" 
# these strings are concatenated and sent to the SentenceMaker
# function

# add the string to the stringList list variable
while (user_input != "\end"):
    user_input = input("Say something:  ")
    if(user_input == "\end"):
        break
    else:
        stringList.append(sentenceMaker(user_input))
# at the end of the loop, print the entire list as a sentence
print(" ".join(stringList))   