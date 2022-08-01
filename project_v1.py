"""
Filename: maxine_theme_park_project.py
Author: M.Avery
Date: /07/22
Description: This program is to make it more efficient and easier for
my theme park staff to find the cost that each group will pay based
on the amount of rides each person will take based on their height.
"""

#Assign lists and variables necessary

new_group = ("")
new_person = ("")
height_group = ("")
eighty_ride_options = ("")
hundred_ride_options = ("")
hundred_thirty_ride_options = ("")

VALID_ANSWER_OPTIONS = ["1", "2"]
VALID_HEIGHT_OPTIONS = ["1", "2", "3", "4"]

VALID_EIGHTY_OPTIONS = ["1", "2", "3", "4"]
VALID_HUNDRED_OPTIONS = ["1", "2", "3", "4", "5", "6", "7"]
VALID_HUNDRED_THIRTY_OPTIONS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
 

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
            height_group = ("")
                
    #Menu with the height options of the customers.
    #Validate this.
            if new_person == "1":
                while height_group != "4":

                    #Print menu and get user choice, validate user input
                    print("""What height range is this person in?

  1  -  80cm
  2  -  100cm
  3  -  130cm
  4  -  Done 
                    """)

                    height_group = input("Please type in one of the options above: ")
                    print("")
                    while height_group not in VALID_HEIGHT_OPTIONS:
                            height_group = input("Invalid option. Please type in one of the options above: ")

                    #Make sure the height and rides they are allowed on align.

                    if height_group == "1":
                        height_group = "4"

                    #Menu with the rides that 80cm group range people are allowed to go on & how much they cost.
                    #Validate this.
                        while eighty_ride_options != "4":

                            #Print menu and get user choice, validate user input
                            print("""What rides is this person going on?

  1  -  Toy Park / $4
  2  -  Mirror Town / $3
  3  -  Fantasy Land / $6
          
  4  -  Finish adding rides
                              
                            """)

                            eighty_ride_options = input("Please type in one of the options above: ")
                            print("")
                            while eighty_ride_options not in VALID_EIGHTY_OPTIONS:
                                eighty_ride_options = input("Invalid option. Please type in one of the options above: ")


                    elif height_group == "2":
                        height_group = "4"

                    #Menu with the rides that 100cm group range people are allowed to go on & how much they cost.
                    #Validate this.
                        while hundred_ride_options != "7":

                            #Print menu and get user choice, validate user input
                            print("""What rides is this person going on?

  1  -  Toy Park / $4
  2  -  Mirror Town / $3
  3  -  Fantasy Land / $6
  4  -  The Lonely Manor / $8.50
  5  -  The Serpent Plummet / $9
  6  -  Glutton Passage / $8
          
  7  -  Finish adding rides
                         
                            """)

                            hundred_ride_options = input("Please type in one of the options above: ")
                            print("")
                            while hundred_ride_options not in VALID_HUNDRED_OPTIONS:
                                hundred_ride_options = input("Invalid option. Please type in one of the options above: ")
                                

                    elif height_group == "3":
                        height_group = "4"

                    #Menu with the rides that 130cm group range people are allowed to go on & how much they cost.
                    #Validate this.
                        while hundred_thirty_ride_options != "10":

                            #Print menu and get user choice, validate user input
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

   10  -  Finish adding rides
                         
                            """)

                            hundred_thirty_ride_options = input("Please type in one of the options above: ")
                            print("")
                            while hundred_thirty_ride_options not in VALID_HUNDRED_THIRTY_OPTIONS:
                                hundred_thirty_ride_options = input("Invalid option. Please type in one of the options above: ")


print("Goodbye")

#Total cost of the individual
#Ask if they want to change their rides(-if it costs too much).


#Total cost of their stay for the day.

#Thank them for coming and wish them a lovely time.
