def get_magnitude(num):
    magnitude = -1
    while magnitude < 0:
        magnitude = float(input("Enter the magnitude of the earthquake {0}: ".format(num)))
    return magnitude
def compare_magnitudes(magnitude1,magnitude2):
    f = 10**(1.5*(magnitude1-magnitude2))
    return f
def get_run_again():
    u_int = int(input("Enter 1 to do it again: "))
    if u_int == 1:
        return True
    else:
        return False

def main():
    run = True
    while run:
        magnitude_1 = get_magnitude(1)
        magnitude_2 = get_magnitude(2)
        if magnitude_1 > magnitude_2:
            mag_1 = magnitude_1
            mag_2 = magnitude_2
        else:
            mag_1 = magnitude_2
            mag_2 = magnitude_1
        
        value_f = compare_magnitudes(mag_1, mag_2)
        print()
        print("An earthquake of magnitude {0:.1f} is {1:.1f} times more powerful than an earth quake {2:.1f}".format(mag_1,value_f,mag_2))
        run = get_run_again()
    print("Bye")


main()

#research
#1) a)The magnitude of 2011 TohoKu Earthquake was 9.0
#   b)The magnitude of 1989 Loma Prieta was 6.9
#   c)The magnitude of 2010 Haiti earthquake was 7.0
#2) The 2011 earthquake is 1000 times more powerful than the 2010 Haiti earthquake
#3) 230,000 people died in the Haiti earthquake
#   15,894 people died in the 2011 Tohoku earthquake
#   Yes, definitely but also becaue Japan is more well prepared since they have to deal with earthquake a lot.
