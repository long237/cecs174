vehicle_price = -1
year = -1
depri_rate = 0.18
#Input validation
while vehicle_price <= 0:
    vehicle_price = float(input("Enter your vehicle "\
                                +"price here:$"))
while year <= 0:
    year = int(input("Enter number of years:"))
    
#vehicle price calculation
for counter in range(year):

    #yearly price depricition calculation
    vehicle_price = vehicle_price - vehicle_price * depri_rate
    print("Year", counter+1 , "value",
          "$ {0:.2f}".format(vehicle_price))
    

