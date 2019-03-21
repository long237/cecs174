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
        while phrase[i].isalpha() == False and i < j:
            i += 1
        #check index j, if it is not a letter, increase by 1
        while phrase[j].isalpha() == False and i < j:
            j -= 1
        #if the pair of letter is different, it is not a palidrome
        if phrase[i].lower() != phrase[j].lower():
            return False
        #increase index for every iteration of the loop
        i += 1
        j -= 1
    return True

#main function for checking a palidrome
def menu_check_palindrome():
    user_input = get_phrase()
    result = is_palindrome(user_input)
    if result == True:
        print()
        print("\"{0}\"".format(user_input),"is a palindrome")
    else:
        print()
        print("\"{0}\"".format(user_input),"is not a palindrome")

def get_crossword_square():
    user_input = input("Enter a word here:")
    order_of_square = len(user_input)
    #loop to get the rest of the words
    for i in range(order_of_square - 1):
        #User validation(user has to enter following words as the same lenth of the first word)
        #keep looping until the length of follwoing words equal the first one.
        user_input_2 = ""
        while len(user_input_2) != order_of_square:
            user_input_2 = input("Enter a word here:")
        #string concatenation
        user_input += user_input_2
    return user_input

def check_crossword_square(square):
    user_input = square.lower()
    order_square = int(math.sqrt(len(user_input)))

    #horizontal words check
    for i in range(order_square):
        horizontal_result = EnglishDictionary.is_word(user_input[(order_square * i):((order_square * i) + order_square)])
        #the very first word in the horizontal line that is not an English word will return False
        if horizontal_result == False:
            return False

    #vertical words check
    for j in range(order_square):
        vertical_result = EnglishDictionary.is_word(user_input[j::order_square])
        #the very first word in the column that is not an English word will return False
        if vertical_result == False:
            return False
    #return true if all words are English words
    return True

#main function to check a crosword square
def menu_check_crossword_square():
    user_input = get_crossword_square()
    bool_result = check_crossword_square(user_input)

    #same logic as horizontal words
    order_square = int(math.sqrt(len(user_input)))
    if bool_result == True:
        print()
        for i in range(order_square):
            #print every words on its own line
            print(user_input[(order_square * i):((order_square * i) + order_square)])
        print()
        print("is a crossword square!")
    else:
        print()
        for i in range(order_square):
            #print every words on its own line
            print(user_input[(order_square * i):((order_square * i) + order_square)])
        print()
        print("is not a crossword square")

def main():
    user_input = 0
    while user_input != 3:
        print_menu()
        print()
        user_input = int(input("Enter your choice here:"))
        if user_input == 1:
            menu_check_palindrome()
            print()
        elif user_input == 2:
            menu_check_crossword_square()
            print()
        else:
            print("Bye")

main()
      

    
    


