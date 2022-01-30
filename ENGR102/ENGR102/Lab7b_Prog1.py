# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   7b-1
# Date:         10/12/2020
#
#pig latin



def isVowel(word): # function that determines whether a string is equivalent to any of the vowels
    if word == "a" or word == "e" or word == "i" or word == "o" or word == "u":
        return True
print("This program converts a word from English to Pig Latin. Enter 'stop' to end the program.")
flag = True
while flag: #flag makes the program loop until stop is entered
    word = input("Please enter a word: ")
    if word == "stop":
        print("You have chosen to stop the program")
        flag = False
        break
    if (" ") in word:
        print("The input contains a space. Please try again with one word.")
        continue
    wordarray = []
    count = 0
    firstVowel = True
    final = ""
    for char in word:
        wordarray.append(char) #creates an array with each element being a letter of the word
    
    if isVowel(wordarray[0]):
        final = word + "yay" #case for starting with vowel
 
    else: #case for starting with consonant
        for letter in wordarray:
            if isVowel(letter):
                firstVowel = False
            if not isVowel(letter) and firstVowel:
                count += 1 #counts the number of consonants from the start of the word
        for num in range(count):
            wordarray.append(wordarray[0])
            del wordarray[0] #moves consonants to the end and removes them from the front
        for letter in wordarray:
            final += letter
        final += "ay" 
    print("Original:",word)
    print("Pig Latin:",final)
