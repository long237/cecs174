def main():
    placings = ["United States", 'Sweden', 'Switzerland', 'Canada',
               'Great Britain', 'Norway', 'South Korea', 'Japan',
               'Italy', 'Denmark']
    user_input = ''
    while user_input != 'quit':
        user_input = input("Enter a name of a country here, enter 'quit' exit: ")
        if user_input == 'quit':
            print("Bye")
        country_index = -1
        for index in range(len(placings)):
            if placings[index] == user_input:
                country_index = index
        if country_index == -1:
            print(user_input,"did not compete")
            print()
            continue
        print(user_input, 'placed' , country_index + 1,'in curling', end='')
        if country_index == 0:
            print('(Gold medal)',end = '')
        elif country_index == 1:
            print('(Silver medal)',end = '')
        elif country_index == 2:
            print('(Bronze medal)',end = '')
        print()
        print()
        



main()
        
    
#Research question
#1) #Granite rock that weight between 38 and 44 pounds
    #The rings or circles toward which play is directed consisting of a 12-foot ring, 8-foot ring, 4-foot ring and a button.
    #The circle at the centre of the house
    #The person who pushes the stone
    #The player who determines the strategy, and directs play for the team. The skip delivers the last pair of stones for his/her team in each end.
#2)Norway has won the most all time medal in Winter Olympics.
#3)Biathlon is the sport the US has no medal.
