def get_word():
    u_input = input("Enter a word here:")
    return u_input

def is_vowel(letter):
    vowel = ['a', 'i', 'e', 'o' , 'u']
    if letter in vowel:
        return True
    return False

def calculate_measure(word):
    measure_count = 0
    for i in range(len(word)-1):
        previous_result = is_vowel(word[i])
        current_result = is_vowel(word[i+1])
        #increase measure if result is different than previous result and previous result must be true
        if current_result != previous_result and previous_result == True:
            measure_count += 1
    return measure_count

#extra function for easier testing
def stop():
    user_input = int(input("Enter 0 to stop:"))
    if user_input == 0:
        return True
    return False

def main():
    run = True
    while run:
        user_input = get_word()
        measure = calculate_measure(user_input)
        print(user_input, 'has a measure of', measure)
        run = not(stop())
    
main()
