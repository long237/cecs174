def print_menu():
    print("1.Information of an Interstate")
    print("2.Quit")

def get_menu_choice():
    user_input = -1
    while user_input < 1 or user_input > 2:
        user_input = int(input("Enter your choice here: "))
    return user_input

def get_interstate_number():
    user_input = ''
    while len(user_input) < 1:
        user_input = input("Enter a US interstate route:")
    if user_input.startswith('Interstate'):
        num_inter = int(user_input[11:])
    elif user_input[0:2] == "I-":
        num_inter = int(user_input[2:])
    elif user_input.find('I') == 0:
        num_inter = int(user_input[1:])
    else:
        num_inter = int(user_input)
    return num_inter 

def is_primary(number):
    if number < 100:
        return True
    return False

#this function can only be call on primary interstate
def compass_orientation(number):
    if (number % 2) == 0:
        return "east-west"
    return "north-south"

#only on primary interstate
def is_aterial(number):
    if (number % 5) == 0:
        return True
    return False

#only for auxiliary
def auxiliary_type(number):
    if ((number // 100) % 2) == 0:
        return "radial highway"
    return "spur highway"

#only for auxiliary
def parent_highway(number):
    return (number % 100)

def main():
    menu_choice = -1
    while menu_choice != 2:
        print_menu()
        print()
        menu_choice = get_menu_choice()
        if menu_choice == 1:
            user_input = get_interstate_number()
            print()
            if is_primary(user_input) == True:
                if is_aterial(user_input) == True:
                    print("Interstate", user_input, "is a long-distance highway oriented",compass_orientation(user_input))
                    print()
                else:
                    print("Interstate", user_input, "oriented", compass_orientation(user_input))
                    print()
            else:
                print("Interstate", user_input,"is", auxiliary_type(user_input),"of Interstate", parent_highway(user_input))
                print()
        elif menu_choice == 2:
            print("Adios")
        
main()

#Reasearch questions
#1)President Dwight D. Eisenhower
#2)I-405 Los Angeles section
#3)Formed in Bellingham, Washington
    
