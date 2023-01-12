#Created by Alon R. for CIS 261 - Hotel Reservation

from datetime import datetime, date

PlayAgain = "y"

while PlayAgain.lower() == "y":

    print("\nHotel Reservation \n")

    Arrival = input("Please enter your arrival date: ") 

    Number = Arrival.split("-")

    def ErrorDate():
        global Arrival
        try:
            GivenDate1 = datetime.strptime(Arrival, "%Y-%m-%d")#.strftime('%Y-%m-%d')
            GivenDate1 = "Good"
        except ValueError:
            GivenDate1 = "Bad"
            if GivenDate1 == "Bad":
                  print("\nPlease type in a date like this: YYYY-MM-DD")
                  Arrival = input("\nYour arrival date please: ")
                  ErrorDate()

    ErrorDate()

    def DateGetter():
         global year, month, day
         global date1
         year, month, day = map(int, Arrival.split("-"))
         date1 = date(year, month, day)
        # except ValueError:
           # raise ValueError("Date in not in the correct format")

    DateGetter()


    while date1 <= date.today():
   
        print("\nCan only reserve future rooms.")
        Arrival = input("\nYour arrival date please: ")
        ErrorDate()
        DateGetter()
    
    else:
         print("\nArrival date OK")



    #Year = Number[0]
    #Month = Number[1]
    #Day = Number[2]



    Departure = input("\nPlease enter your depature date: ")

    def ErrorDate2():
        global Departure
        try:
            GivenDat2 = datetime.strptime(Departure, "%Y-%m-%d")#.strftime('%Y-%m-%d')
            GivenDate2 = "Good"
        except ValueError:
            GivenDate2 = "Bad"
            if GivenDate2 == "Bad":
                  print("\nPlease type in a date like this: YYYY-MM-DD")
                  Departure = input("\nYour arrival date please: ")
                  ErrorDate2()

    ErrorDate2()

    def DateGetter2():
         global date2
         year, month, day = map(int, Departure.split("-"))
         date2  = date(year, month, day)

    DateGetter2()

    while date2 <= date1:
   
        print("\nYour departure must be after your arrival.")
        Arrival = input("\nYour departure date please: ")
        ErrorDate2()
        DateGetter2()
    
    else:
         print("\nDeparture date OK")

    Night = date2 - date1
    NightRate = 85.00
    if date1 or date2 != date.month("08"):
        NightRate = 85.00
    else:
        NightRate = 105.00
    TotalCalculate = NightRate * Night.days
    print("\nStaying for", Night.days, "Nights will cost you " +  "$" + str(TotalCalculate))

    PlayAgain =input("\nTry again? (Y/N) ")

    while PlayAgain.lower() != "y" and PlayAgain.lower() != "n":
          print("\nPlease type in only the letters Y or N. (Can be used both in caps lock or without)")
          PlayAgain =input("\nTry again? (Y/N) ")

print("\nThank you, see you again!")