print("Welcome to Agile Agile Agile")
player_1_name = input("Please enter the first player's name  ").capitalize()
player_2_name = input("Please enter the second player's name  ").capitalize()

print("Objective: Your goal is to build a city that has a greater overall business value than ")
print("your opponent. You are constrained by an allotted time for each sprint and how ")
print("many times you are able to communicate with your client.")
print("For the best user experience, we recommend you make your console screen as big as possible.")

# Simple loop to insure screen doesn't get too cluttered
i = 2
while i < 2.1:
    if(str(input("Continue? (y/n) ")).lower()) == "y":
        i += 1.2
    else:
        i = 2
        continue
    i += 1

# Defining my dictionaries
School = {"Name": "School",
          "Epic": "A place of learning for children and young adults",
          "User Story": "As a parent, I need a place I can take my children to learn",
          "Business Value": 240,
          "Time to build": 7}
Hospital = {"Name": "Hospital",
            "Epic": "A location to treat the sick and injured",
            "User Story": "As an elderly person with health conditions, I need a place where I can undergo treatment",
            "Business Value": 300,
            "Time to build": 11}
Supermarket = {"Name": "Supermarket",
               "Epic": "A location whereby goods can be purchased by citizens",
               "User Story": "As a citizen, I don't want to have to travel to another town for food",
               "Business Value": 180,
               "Time to build": 9}
Factory = {"Name": "Factory",
               "Epic": "A place whereby we can produce further structures",
               "User Story": "As a contractor, I need a factory to produce additional housing",
               "Business Value": 160,
               "Time to build": 8}
Housing = {"Name": "Housing",
               "Epic": "A place in which citizens can live",
               "User Story": "As a citizen, I don't want to have to live on the street",
               "Business Value": 450,
               "Time to build": 13}
Train_Station = {"Name": "Train Station",
               "Epic": "A railway station linking our town to others",
               "User Story": "As a commuter, a railway system would cut my commute in half",
               "Business Value": 135,
               "Time to build": 7}

print("Available Structures: School (", School["Time to build"], "days), Hospital (", Hospital["Time to build"], "days), Supermarket (", Supermarket["Time to build"], "days), Factory (", Factory["Time to build"], "days), Housing (", Housing["Time to build"], "days), Train Station (", Train_Station["Time to build"], "days)")
print(f"{player_1_name} , you have been given the oppurtunity to enquire about one structure")

# While loops: allow for each player to enquire to the client about one and only one structure
x = 0.5
while x < 1:
    player_1_1st_enquiry = input("What structure would you like to enquire about to the client?  ").lower()
    if player_1_1st_enquiry == "school":
        print("School")
        print("Epic -", School["Epic"])
        print("User Story -", School["User Story"])
        print("Business Value -", School["Business Value"])
        x += 1
        # print("Time to build - ", School["Time to build"], "days")

    elif player_1_1st_enquiry == "hospital":
        print("Hospital")
        print("Epic -", Hospital["Epic"])
        print("User Story -", Hospital["User Story"])
        print("Business Value -", Hospital["Business Value"])
        x += 1
    elif player_1_1st_enquiry == "supermarket":
        print("Supermarket")
        print("Epic -", Supermarket["Epic"])
        print("User Story -", Supermarket["User Story"])
        print("Business Value -", Supermarket["Business Value"])
        x += 1
    elif player_1_1st_enquiry == "factory":
        print("Factory")
        print("Epic -", Factory["Epic"])
        print("User Story -", Factory["User Story"])
        print("Business Value -", Factory["Business Value"])
        x += 1
    elif player_1_1st_enquiry == "housing":
        print("Housing")
        print("Epic -", Housing["Epic"])
        print("User Story -", Housing["User Story"])
        print("Business Value -", Housing["Business Value"])
        x += 1
    elif player_1_1st_enquiry == "train station":
        print("Train Station")
        print("Epic -", Train_Station["Epic"])
        print("User Story -", Train_Station["User Story"])
        print("Business Value -", Train_Station["Business Value"])
        x += 1
    else:
        continue
z = 0.5
while z < 1:
    player_2_1st_enquiry = input(f"{player_2_name} , what structure would you like to enquire about to the client?  ").lower()
    if player_2_1st_enquiry == "school":
        print("School")
        print("Epic -", School["Epic"])
        print("User Story -", School["User Story"])
        print("Business Value -", School["Business Value"])
        z += 1
        # print("Time to build - ", School["Time to build"], "days")

    elif player_2_1st_enquiry == "hospital":
        print("Hospital")
        print("Epic -", Hospital["Epic"])
        print("User Story -", Hospital["User Story"])
        print("Business Value -", Hospital["Business Value"])
        z += 1
    elif player_2_1st_enquiry == "supermarket":
        print("Supermarket")
        print("Epic -", Supermarket["Epic"])
        print("User Story -", Supermarket["User Story"])
        print("Business Value -", Supermarket["Business Value"])
        z += 1
    elif player_2_1st_enquiry == "factory":
        print("Factory")
        print("Epic -", Factory["Epic"])
        print("User Story -", Factory["User Story"])
        print("Business Value -", Factory["Business Value"])
        z += 1
    elif player_2_1st_enquiry == "housing":
        print("Housing")
        print("Epic -", Housing["Epic"])
        print("User Story -", Housing["User Story"])
        print("Business Value -", Housing["Business Value"])
        z += 1
    elif player_2_1st_enquiry == "train station":
        print("Train Station")
        print("Epic -", Train_Station["Epic"])
        print("User Story -", Train_Station["User Story"])
        print("Business Value -", Train_Station["Business Value"])
        z += 1
    else:
        continue
q = 2
while q < 2.1:
    if(str(input("Continue? (y/n) ")).lower()) == "y":
        q += 1.2
    else:
        q = 2
        continue
    q += 1

print("The clients have grown tired of your questions; it's time to start building")
print("School (", School["Time to build"], "days)")
print("Hospital (", Hospital["Time to build"], "days)")
print("Supermarket (", Supermarket["Time to build"], "days)")
print("Factory (", Factory["Time to build"], "days)")
print("Housing (", Housing["Time to build"], "days)")
print("Train Station (", Train_Station["Time to build"], "days)")

player_2_time = 20
player_1_time = 20
player_1_score = 0
player_2_score = 0

# While loop that adds a score for each structure built and prevents the player from building something they don't have enough time to build
while player_1_time != 0:
    player_1_choice = input(f"{player_1_name}, what would you like to build? (type 'end' to end your turn) ").lower()
    if player_1_choice == "school" and player_1_time >= School["Time to build"]:
        player_1_score += School["Business Value"]
        print("School successfully built")
        player_1_time -= School["Time to build"]
        print("You have", player_1_time, "days remaining")
    elif player_1_choice == "school" and player_1_time < School["Time to build"]:
        print("Unfortunately, we don't have enough time to build a school")

    elif player_1_choice == "hospital" and player_1_time >= Hospital["Time to build"]:
        player_1_score += Hospital["Business Value"]
        print("Hospital successfully built")
        player_1_time -= Hospital["Time to build"]
        print("You have", player_1_time, "days remaining")
    elif player_1_choice == "hospital" and player_1_time < Hospital["Time to build"]:
        print("Unfortunately, we don't have enough time to build a Hospital")

    elif player_1_choice == "supermarket" and player_1_time >= Supermarket["Time to build"]:
        player_1_score += Supermarket["Business Value"]
        print("Supermarket successfully built")
        player_1_time -= Supermarket["Time to build"]
        print("You have", player_1_time, "days remaining")
    elif player_1_choice == "supermarket" and player_1_time < Supermarket["Time to build"]:
        print("Unfortunately, we don't have enough time to build a Supermarket")

    elif player_1_choice == "factory" and player_1_time >= Factory["Time to build"]:
        player_1_score += Factory["Business Value"]
        print("Factory successfully built")
        player_1_time -= Factory["Time to build"]
        print("You have", player_1_time, "days remaining")
    elif player_1_choice == "factory" and player_1_time < Factory["Time to build"]:
        print("Unfortunately, we don't have enough time to build a Factory")

    elif player_1_choice == "housing" and player_1_time >= Housing["Time to build"]:
        player_1_score += Housing["Business Value"]
        print("Housing successfully built")
        player_1_time -= Housing["Time to build"]
        print("You have", player_1_time, "days remaining")
    elif player_1_choice == "housing" and player_1_time < Housing["Time to build"]:
        print("Unfortunately, we don't have enough time to build Housing")

    elif player_1_choice == "train station" and player_1_time >= Train_Station["Time to build"]:
        player_1_score += Train_Station["Business Value"]
        print("Train Station successfully built")
        player_1_time -= Train_Station["Time to build"]
        print("You have", player_1_time, "days remaining")
    elif player_1_choice == "train station" and player_1_time < Train_Station["Time to build"]:
        print("Unfortunately, we don't have enough time to build a Train Station")

    elif player_1_choice == "end":
        player_1_time -= player_1_time
    else:
        continue

while player_2_time != 0:
    player_2_choice = input(f"{player_2_name}, what would you like to build? (type 'end' to end your turn) ").lower()
    if player_2_choice == "school" and player_2_time >= School["Time to build"]:
        player_2_score += School["Business Value"]
        print("School successfully built")
        player_2_time -= School["Time to build"]
        print("You have", player_2_time, "days remaining")
    elif player_2_choice == "school" and player_2_time < School["Time to build"]:
        print("Unfortunately, we don't have enough time to build a school")

    elif player_2_choice == "hospital" and player_2_time >= Hospital["Time to build"]:
        player_2_score += Hospital["Business Value"]
        print("Hospital successfully built")
        player_2_time -= Hospital["Time to build"]
        print("You have", player_2_time, "days remaining")
    elif player_2_choice == "hospital" and player_2_time < Hospital["Time to build"]:
        print("Unfortunately, we don't have enough time to build a Hospital")

    elif player_2_choice == "supermarket" and player_2_time >= Supermarket["Time to build"]:
        player_2_score += Supermarket["Business Value"]
        print("Supermarket successfully built")
        player_2_time -= Supermarket["Time to build"]
        print("You have", player_2_time, "days remaining")
    elif player_2_choice == "supermarket" and player_2_time < Supermarket["Time to build"]:
        print("Unfortunately, we don't have enough time to build a Supermarket")

    elif player_2_choice == "factory" and player_2_time >= Factory["Time to build"]:
        player_2_score += Factory["Business Value"]
        print("Factory successfully built")
        player_2_time -= Factory["Time to build"]
        print("You have", player_2_time, "days remaining")
    elif player_2_choice == "factory" and player_2_time < Factory["Time to build"]:
        print("Unfortunately, we don't have enough time to build a Factory")

    elif player_2_choice == "housing" and player_2_time >= Housing["Time to build"]:
        player_2_score += Housing["Business Value"]
        print("Housing successfully built")
        player_2_time -= Housing["Time to build"]
        print("You have", player_2_time, "days remaining")
    elif player_2_choice == "housing" and player_2_time < Housing["Time to build"]:
        print("Unfortunately, we don't have enough time to build Housing")

    elif player_2_choice == "train station" and player_2_time >= Train_Station["Time to build"]:
        player_2_score += Train_Station["Business Value"]
        print("Train Station successfully built")
        player_2_time -= Train_Station["Time to build"]
        print("You have", player_2_time, "days remaining")
    elif player_2_choice == "train station" and player_2_time < Train_Station["Time to build"]:
        print("Unfortunately, we don't have enough time to build a Train Station")

    elif player_2_choice == "end":
        player_2_time -= player_2_time
    else:
        continue

print(f"{player_1_name} 's accumulated business value is {player_1_score}")
print(f"{player_2_name} 's accumulated business value is {player_2_score}")
if player_1_score > player_2_score:
    print(f"so {player_1_name} beats {player_2_name} by {player_1_score} to {player_2_score}")
elif player_2_score > player_1_score:
    print(f"so {player_2_name} beats {player_1_name} by {player_2_score} to {player_1_score}")
else:
    print(f"The scores are tied at {player_1_score}. Unbelievable!")

w = 2
while w < 2.1:
    if(str(input("Continue? (y/n) ")).lower()) == "y":
        w += 1.2
    else:
        w = 2
        continue
    w += 1

print("Made by Khanhi Ramraj")
print("I am very proud of my game, but if i had more time I would add a second")
print("sprint where the players are able to build a new set of structures.")




