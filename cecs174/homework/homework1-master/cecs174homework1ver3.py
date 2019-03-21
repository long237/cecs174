import math
menu= 0
LIGHT_SPEED = 299_792_458
WARP_EXPO = 10/3
velocity = 0
ULA_RATE = 14_830
SPACEX_RATE= 2720
INSURANCE = 0.3
LIGHT_YEAR = 9.461e15
SEC_IN_HR = 3600
HR_IN_DAY = 24
DAY_IN_YEAR = 365
while menu!= 4:
    print("1. Warp Speed")
    print("2. Cost to launch")
    print("3. Time Dilation")
    print("4. Quit")
    menu= float(input("Choose a function: "))
    print()
    #Warp speed
    if menu == 1:
        warp_factor = -1
        while warp_factor <= 0:
            warp_factor = float(input("Enter warp factor: "))
            if warp_factor >0:
                #Speed function
                velocity = ((warp_factor)**(WARP_EXPO))* LIGHT_SPEED
                print("Warp factor:",int(warp_factor)) #I'm not sure if you want this in float or interger
                print("Your current speed: {0:,.2f}".format(velocity),"m/s")
                print()
     # Cost to launch
    if menu == 2:
        mass = -1
        #mass input
        while mass <= 0:
            mass = float(input("Enter mass of your spaceship in kilogram: "))
        manu_cost = -1
        #manufactur input
        while manu_cost <= 0:
            manu_cost = float(input("Enter the cost to make your space ship: $"))

        #cost calculation and comparison
        cost_ULA= mass * ULA_RATE
        cost_spaceX= mass * SPACEX_RATE + (manu_cost * INSURANCE)
        if cost_ULA > cost_spaceX:
            difference= cost_ULA - cost_spaceX
            print("Elon Musk will save you: $ {0:,.2f}".format(difference))
            print()
        elif cost_spaceX > cost_ULA:
            difference2= cost_spaceX - cost_ULA
            print("United Launch Alliance will save you: $ {0:,.2f}".format(difference2))
            print()
        else:
            print("They both cost you the same amount")
            print()
    # Time dilation fuction
    if menu == 3:
        #speed input
        speed = -1
        while speed <= 0 or speed > 1:
            speed = float(input("Enter your speed as a fraction of light speed:"))
        distance = -1
        #distance input
        while distance <= 0:
            distance = float(input("Enter a ridiculous distance here:"))
        #conversion to meter
        dis_in_m = distance * LIGHT_YEAR
        speed_in_m = speed * LIGHT_SPEED
        #traveling time in seconds
        time_earth_s = dis_in_m / speed_in_m
        #total day on earth of traveling
        day_earth = time_earth_s / SEC_IN_HR / HR_IN_DAY

        #year conversion
        year_earth = day_earth // DAY_IN_YEAR
        #left over days conversion
        day_earth_left = day_earth % DAY_IN_YEAR
        print("An observer on ages",end=' ')
        if year_earth > 0:
            print(int(year_earth), "years", end=" ")
        print(int(day_earth_left), "days")    


        #dilation fuction
        dilation = math.sqrt(1 - (speed_in_m**2 / LIGHT_SPEED**2))
        time_on_ship = time_earth_s * dilation
        #day conversion
        day_on_ship = time_on_ship / SEC_IN_HR / HR_IN_DAY
        #year conversion
        year_on_ship = day_on_ship // DAY_IN_YEAR
        #left over day on ship conversion
        day_left_ship= day_on_ship % DAY_IN_YEAR
        print("A passenger on the ship ages",end=" ")
        if year_on_ship > 0:
            print(int(year_on_ship), "years", end=" ")
        print(int(day_left_ship), "days")
        print()
        

        
        
        
        
                        
                          
    
            
            
                                
                
            
            
        
