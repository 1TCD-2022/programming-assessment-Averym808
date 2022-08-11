"""
Filename: maxine_theme_park_project.py
Author: M.Avery
Date: /07/22
Description: This program is to make it more efficient and easier for
my theme park staff to find the cost that each group will pay based
on the amount of rides each person will take within their height group.
"""

#Assign lists and variables necessary
person_cost = 0
total_group_cost = 0

change_rides = ("")
new_group = ("")
new_person = ("")
height_group = ("")
ride_options = ("")

VALID_ANSWER_OPTIONS = ["1", "2"]
VALID_HEIGHT_OPTIONS = ["1", "2", "3"]

VALID_EIGHTY_OPTIONS = ["0","1", "2", "3", "4"]
VALID_HUNDRED_OPTIONS = ["0","1", "2", "3", "4", "5", "6", "7"]
VALID_HUNDRED_THIRTY_OPTIONS = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
 

#Menu with options to choose if they have a new group or not.
#Validate this.
while new_group != "2":

    #Print menu and get user choice, validate user input
    print("""Do you wish to add a new group?

    1  -  Add new group
    2  -  Finish program
    """)

    new_group = input("Please type in one of the options above: ")
    print("")
    while new_group not in VALID_ANSWER_OPTIONS:
            new_group = input("Invalid option. Please type in one of the options above: ")


    #Menu with the options to choose to add a person.
    #Validate this.
    if new_group == "1":
        while new_person != "2":

            #Print menu and get user choice, validate user input
            print("""Do you wish to add a new person to this group?

    1  -  Add new person to group
    2  -  Finish adding people
            """)

            new_person = input("Please type in one of the options above: ")
            print("")
            while new_person not in VALID_ANSWER_OPTIONS:
                    new_person = input("Invalid option. Please type in one of the options above: ")
                
            #Menu with the height options of the customers.
            #Validate this.
            if new_person == "1":
                
                    #Print menu and get user choice, validate user input
                    print("""What height range is this person in?

    1  -  80cm
    2  -  100cm
    3  -  130cm
                    """)

                    height_group = input("Please type in one of the options above: ")
                    print("")
                    while height_group not in VALID_HEIGHT_OPTIONS:
                            height_group = input("Invalid option. Please type in one of the options above: ")

                    #Make sure the height and rides they are allowed on align.
                    #Print menu and get user choice, validate user input
                    while ride_options != "0":

                        if height_group == "1":
                            print("""What rides is this person going on?

    1  -  Toy Park / $4
    2  -  Mirror Town / $3
    3  -  Fantasy Land / $6

    0  -  Finish adding rides
                             
                        """)

                        elif height_group == "2":
                            print("""What rides is this person going on?

    1  -  Toy Park / $4
    2  -  Mirror Town / $3
    3  -  Fantasy Land / $6
    4  -  The Lonely Manor / $8.50
    5  -  The Serpent Plummet / $9
    6  -  Glutton Passage / $8

    0  -  Finish adding rides
                             
                        """)
                                
                        elif height_group == "3":
                            print("""What rides is this person going on?

    1  -  Toy Park / $4
    2  -  Mirror Town / $3
    3  -  Fantasy Land / $6
    4  -  The Lonely Manor / $8.50
    5  -  The Serpent Plummet / $9
    6  -  Glutton Passage / $8
    7  -  The Shift / $13.50
    8  -  The Merry Plunge / $12
    9  -  The Garden / $14.50

    0  -  Finish adding rides
                             
                        """)
                            

                        ride_options = input("Please type in one of the options above: ")
                        print("")
                        while ride_options not in VALID_HUNDRED_THIRTY_OPTIONS:
                            ride_options = input("Invalid option. Please type in one of the options above: ")   

                        if  ride_options == "1":
                            person_cost += 4
                        elif ride_options == "2":
                            person_cost += 3
                        elif ride_options == "3":
                            person_cost += 6                                                                      
                        elif  ride_options == "4":
                            person_cost += 8.5
                        elif  ride_options == "5":
                            person_cost += 9
                        elif  ride_options == "6":
                            person_cost += 8
                        elif  ride_options == "7":
                            person_cost += 13.5
                        elif  ride_options == "8":
                            person_cost += 12
                        elif  ride_options == "9":
                            person_cost += 14.5                                                                    
                                    
                    #Total cost of the individual 
                    print("This person's total ride cost is $",person_cost)
                    print("")

            #Ask if they want to change their rides(-if it costs too much).
            while change_rides != "2":

                #Print menu and get user choice, validate user input
                print("""Do you want to change your rides?

    1  -  Change Rides
    2  -  Continue

                """)
                change_rides = input("Please type in one of the options above: ")
                print("")
                while change_rides not in VALID_ANSWER_OPTIONS:
                    change_rides = input("Invalid option. Please type in one of the options above: ")
                total_group_cost =+ person_cost
                person_cost = 0


    #Total cost of their stay for the day.
    print("This groups's total cost is $",total_group_cost)
    

#Thank them for coming and wish them a lovely time.
print("Goodbye")
