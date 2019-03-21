import EnglishDictionary
import math

def print_menu():
    print("1:Check a palindrome")
    print("2:Check a crossword square")
    print("3:Quit")

def get_menu_choice():
    user_input = -1
    while user_input < 1 or user_input > 3:
        user_input = float(input("Enter your choice here:"))
    return user_input

def get_phrase():
    user_input = ''
    while len(user_input) < 1:
        user_input = input("Enter a phrase:")
    return user_input

def is_palindrome(phrase):
    i = 0
    j = len(phrase) -1
    while i < j:

        #check index i, if it is not a letter, increase by 1
        while phrase[i].isalpha() == False:
            i += 1
        #check index j, if it is not a letter, increase by 1
        while phrase[j].isalpha() == False:
            j -= 1
        #if the pair of letter is different, it is not a palidrome
        if phrase[i].lower() != phrase[j].lower():
            return False
        #increase index for every iteration of the loop
        i += 1
        j -= 1
    return True

def menu_check_palindrome():
    user_input = get_phrase()
    result = is_palindrome(user_input)
    if result == True:
        print("{0}".format(user_input),"is a palindrome")
    else:
        print("{0}".format(user_input),"is not a palindrome")

def get_crossword_square():
    user_input = input("Enter a word here:")
    order_of_square = len(user_input)
    #loop to get the rest of the words
    for i in range(order_of_square - 1):
        user_input_2 = input("Enter a word here:")
        #string concatenation
        user_input += user_input_2
    return user_input

def check_crossword_square(square):
    order_square = math.sqrt(len(get_crossword_square))
    horizontal_word = ''
    for i in range(0,4):    
        pass
print(get_crossword_square())
    
    


