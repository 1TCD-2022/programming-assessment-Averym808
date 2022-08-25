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
people_group_number = 0

change_rides = ("")
new_group = ("")
new_person = ("")
height_group = ("")
ride_options = ("")

rides_chosen = []

VALID_ANSWER_OPTIONS = ["1", "2"]
VALID_HEIGHT_OPTIONS = ["1", "2", "3"]

VALID_EIGHTY_OPTIONS = ["0", "1", "2", "3"]
VALID_HUNDRED_OPTIONS = ["0", "1", "2", "3", "4", "5", "6"]
VALID_HUNDRED_THIRTY_OPTIONS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("""This program is for you to help find the cost
a group will pay based on the amount of rides
each individual person in their group will
take- within their height group.

I hope this program makes it easier and more
efficent for you and your family to visit this
amaxing theme park ☜(⌒▽⌒)☞ ~! """)
print("")

while new_person != "2":

    #Print menu and get user choice, validate user input
    print("""Do you wish to add a new person to this group?

    1  -  Add new person to group
    2  -  Finish adding people
            """)

    new_person = input("Please type in one of the options above: ").strip()
    print("")
    while new_person not in VALID_ANSWER_OPTIONS:
        new_person = input("Invalid option. Please type in one of the options above: ").strip()
    #Menu with the height options of the customers.
    #Validate this.
    if new_person == "1":
        people_group_number += 1

        #Print menu and get user choice, validate user input
        print("""What height range is this person in?

    1  -  80cm
    2  -  100cm
    3  -  130cm
                """)

        height_group = input("Please type in one of the options above: ").strip()
        print("")
        while height_group not in VALID_HEIGHT_OPTIONS:
            height_group = input("Invalid option. Please type in one of the options above: ").strip()

        #Make sure the height and rides they are allowed on align.
        #Print menu and get user choice, validate user input
        ride_options = ("")
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

            ride_options = input("Please type in one of the options above: ").strip()
            print("")

            if height_group == "1":
                while ride_options not in VALID_EIGHTY_OPTIONS:
                    ride_options = input("Invalid option. Please type in one of the options above: ").strip()
            elif height_group == "2":
                while ride_options not in VALID_HUNDRED_OPTIONS:
                    ride_options = input("Invalid option. Please type in one of the options above: ").strip()
            elif height_group == "3":
                while ride_options not in VALID_HUNDRED_THIRTY_OPTIONS:
                    ride_options = input("Invalid option. Please type in one of the options above: ").strip()

            #Total cost of the individual
            if ride_options == "1":
                person_cost += 4
                rides_chosen.append("Toy Park")
            elif ride_options == "2":
                person_cost += 3
                rides_chosen.append("Mirror Town")
            elif ride_options == "3":
                person_cost += 6
                rides_chosen.append("Fantasy Land")
            elif ride_options == "4":
                person_cost += 8.5
                rides_chosen.append("The Lonely Manor")
            elif ride_options == "5":
                person_cost += 9
                rides_chosen.append("The Serpent Plummet")
            elif ride_options == "6":
                person_cost += 8
                rides_chosen.append("Glutton Passage")
            elif ride_options == "7":
                person_cost += 13.5
                rides_chosen.append("The Shift")
            elif ride_options == "8":
                person_cost += 12
                rides_chosen.append("The Merry Plunge")
            elif ride_options == "9":
                person_cost += 14.5
                rides_chosen.append("The Garden")
            print("")
                    
            if ride_options == "0":

                #Total cost of the individual
                print("This person's total ride cost is $", person_cost)
                print("")
                print("The rides you have chosen are: ")
                print(", ".join(rides_chosen) + ".")
                print("")

                #Ask if they want to change their rides(-if it costs too much).
                #Print menu and get user choice, validate user input
                print("""Do you want to change your rides?

    1  -  Change rides
    2  -  Continue
                    """)

                change_rides = input("Please type in one of the options above: ").strip()
                print("")
                while change_rides not in VALID_ANSWER_OPTIONS:
                    change_rides = input("Invalid option. Please type in one of the options above: ").strip()
                if change_rides == "1":
                    person_cost = 0
                    rides_chosen = []
                    ride_options = ("")
                    print("Select new rides here.")
                    print("")
                        
                total_group_cost += person_cost
                person_cost = 0
                rides_chosen = []

#Total cost of their stay for the day.
print("This groups's total cost is $", total_group_cost)
print("")

#Thank them for coming and wish them a lovely time.
print("Thank you for coming to are Amaxing theme park!")
print("Please come again ~!")
