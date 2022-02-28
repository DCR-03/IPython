# import sys to quit out of program later
import sys

# the opening statement that tells the user about the different options they have to learn about the car that they selected
userInputInfo = "If you would like to learn about the miles per gallon type 1, if you would like to learn about the base price of the car press 2 and if you would like to learn about the type of engine press 3."


# the function of toyota that is called upon by one of the if statements
def toyota():
    # the dictionary for the Toyota Corolla
    Corolla = {1: "The Corolla gets 40mpg on the highway", 2: "The price of the Corolla starts at 20,000",
               3: "The Corolla has a 2.0L 4 Cylinder Engine"}
    # the dictionary for the Toyota Camry
    Camry = {1: "The Camry gets 39mpg on the highway", 2: "The price of the Camry starts at 26,000",
             3: "The Camry has a 3.5L 4 Cylinder Engine"}
    # the dictionary for the Toyota Sienna
    Sienna = {1: "The Sienna gets 36mpg on the highway", 2: "The price of the Sienna starts at 35,000",
              3: "The Sienna has a 2.5L 4 Cylinder Engine"}
    # the dictionary for the Toyota Tundra
    Tundra = {1: "The Tundra gets 18mpg on the highway", 2: "The price of the Tundra starts at 36,000",
              3: "The Tundra has a 3.5L 4 Cylinder Engine"}

    # opening statement for telling the user that Toyota has four models
    print("Hi here at Toyota we offer four different models:")

    # list of the different models that Toyota offers
    toyotaModel = ["Corolla", "Camry", "Sienna", "Tundra"]

    # a for loop that prints out all of the different Toyota models
    for x in toyotaModel:
        print(x)

    # a question to ask the user which model they are interested in and takes their input
    print("Which model are you interested in?")
    toyotaInput = input()

    # a list of if statements that cycle through the four toyota models
    if toyotaInput == "Corolla":
        # prints the userInputInfo which asks the user what specifically they want to learn more about regarding the car they selected
        print(userInputInfo)
        cor_In = input()
        # a list of different if statements that cycle through the three options that users have to learn more about their car
        if cor_In == "1":
            # print statement for the info that the user requested
            print(Corolla[1])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Corolla.txt", "a")
            f.write(Corolla[1])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Corolla's mpg have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "2":
            # print statement for the info that the user requested
            print(Corolla[2])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Corolla.txt", "a")
            f.write(Corolla[2])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The price of the Corolla have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()

        if cor_In == "3":
            # print statement for the info that the user requested
            print(Corolla[3])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Corolla.txt", "a")
            f.write(Corolla[3])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Corolla's engine have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()

    if toyotaInput == "Camry":
        # prints the userInputInfo which asks the user what specifically they want to learn more about regarding the car they selected
        print(userInputInfo)
        cor_In = input()
        # a list of different if statements that cycle through the three options that users have to learn more about their car
        if cor_In == "1":
            # print statement for the info that the user requested
            print(Camry[1])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Camry.txt", "a")
            f.write(Camry[1])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Camry's mpg have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "2":
            # print statement for the info that the user requested
            print(Camry[2])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Camry.txt", "a")
            f.write(Camry[2])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The price of the Camry have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "3":
            # print statement for the info that the user requested
            print(Camry[3])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Camry.txt", "a")
            f.write(Camry[3])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Camry's engine have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()

    if toyotaInput == "Sienna":
        # prints the userInputInfo which asks the user what specifically they want to learn more about regarding the car they selected
        print(userInputInfo)
        cor_In = input()
        # a list of different if statements that cycle through the three options that users have to learn more about their car
        if cor_In == "1":
            # print statement for the info that the user requested
            print(Sienna[1])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Sienna.txt", "a")
            f.write(Sienna[1])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Sienna's mpg have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "2":
            # print statement for the info that the user requested
            print(Sienna[2])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Camry.txt", "a")
            f.write(Camry[2])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The price of the Sienna have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "3":
            # print statement for the info that the user requested
            print(Sienna[3])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Sienna.txt", "a")
            f.write(Sienna[3])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Sienna's engine have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()

    if toyotaInput == "Tundra":
        # prints the userInputInfo which asks the user what specifically they want to learn more about regarding the car they selected
        print(userInputInfo)
        cor_In = input()
        # a list of different if statements that cycle through the three options that users have to learn more about their car
        if cor_In == "1":
            # print statement for the info that the user requested
            print(Tundra[1])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Tundra.txt", "a")
            f.write(Tundra[1])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Tundra's mpg have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "2":
            # print statement for the info that the user requested
            print(Tundra[2])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Tundra.txt", "a")
            f.write(Tundra[2])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The price of the Tundra have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "3":
            # print statement for the info that the user requested
            print(Tundra[3])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Tundra.txt", "a")
            f.write(Tundra[3])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Tundra's engine have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()


# the function of honda that is called upon by one of the if statements
def honda():
    # the dictionary for the Honda Civic
    Civic = {1: "The Civic gets 42mpg on the highway", 2: "The price of the Civic starts at 22,000",
             3: "The Civic has a 2.0L 4 Cylinder Engine"}
    # the dictionary for the Honda CRV
    CRV = {1: "The CRV gets 34mpg on the highway", 2: "The price of the CRV starts at 26,000",
           3: "The CRV has a 1.5L 4 Cylinder Engine"}
    # the dictionary for the Honda Passport
    Passport = {1: "The Passport gets 36mpg on the highway", 2: "The price of the Passport starts at 33,000",
                3: "The Passport has a 3.5L 6 Cylinder Engine"}
    # the dictionary for the Honda Pilot
    Pilot = {1: "The Pilot gets 27mpg on the highway", 2: "The price of the Pilot starts at 33,000",
             3: "The Pilot has a 3.5L 6 Cylinder Engine"}

    # opening statement for telling the user that Honda has four models
    print("Hi here at Honda we offer four different models:")

    # list of the different models that Honda offers
    hondaModel = ["Civic", "CRV", "Passport", "Pilot"]

    # a for loop that prints out all of the different Honda models
    for x in hondaModel:
        print(x)

    # a question to ask the user which model they are interested in and takes their input
    print("Which model are you interested in?")
    hondaInput = input()

    # a list of if statements that cycle through the four Honda models
    if hondaInput == "Civic":
        # prints the userInputInfo which asks the user what specifically they want to learn more about regarding the car they selected
        print(userInputInfo)
        # a list of different if statements that cycle through the three options that users have to learn more about their car
        cor_In = input()
        if cor_In == "1":
            # print statement for the info that the user requested
            print(Civic[1])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Civic.txt", "a")
            f.write(Civic[1])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Civic's mpg have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "2":
            # print statement for the info that the user requested
            print(Civic[2])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Civic.txt", "a")
            f.write(Civic[2])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The price of the Civic have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "3":
            # print statement for the info that the user requested
            print(Civic[3])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Civic.txt", "a")
            f.write(Civic[3])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Civic's engine have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()

    if hondaInput == "CRV":
        # prints the userInputInfo which asks the user what specifically they want to learn more about regarding the car they selected
        print(userInputInfo)
        # a list of different if statements that cycle through the three options that users have to learn more about their car
        cor_In = input()
        if cor_In == "1":
            # print statement for the info that the user requested
            print(CRV[1])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("CRV.txt", "a")
            f.write(CRV[1])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the CRV's mpg have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "2":
            # print statement for the info that the user requested
            print(CRV[2])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("CRV.txt", "a")
            f.write(CRV[2])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The price of the CRV have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "3":
            # print statement for the info that the user requested
            print(CRV[3])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("CRV.txt", "a")
            f.write(CRV[3])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the CRV's engine have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()

    if hondaInput == "Passport":
        # prints the userInputInfo which asks the user what specifically they want to learn more about regarding the car they selected
        print(userInputInfo)
        cor_In = input()
        # a list of different if statements that cycle through the three options that users have to learn more about their car
        if cor_In == "1":
            # print statement for the info that the user requested
            print(Passport[1])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Passport.txt", "a")
            f.write(CRV[1])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Passport's mpg have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "2":
            # print statement for the info that the user requested
            print(Passport[2])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Passport.txt", "a")
            f.write(Passport[2])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The price of the Passport have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "3":
            # print statement for the info that the user requested
            print(Passport[3])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Passport.txt", "a")
            f.write(Passport[3])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Passport's engine have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()

    if hondaInput == "Pilot":
        # prints the userInputInfo which asks the user what specifically they want to learn more about regarding the car they selected
        print(userInputInfo)
        cor_In = input()
        # a list of different if statements that cycle through the three options that users have to learn more about their car
        if cor_In == "1":
            # print statement for the info that the user requested
            print(Pilot[1])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Pilot.txt", "a")
            f.write(Pilot[1])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Pilot's mpg have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "2":
            # print statement for the info that the user requested
            print(Pilot[2])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Pilot.txt", "a")
            f.write(Pilot[2])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The price of the Pilot have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
            # quits out of program when info is given to user
            exit()
        if cor_In == "3":
            # print statement for the info that the user requested
            print(Pilot[3])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Pilot.txt", "a")
            f.write(Pilot[3])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Pilot's engine have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()


# the function of Chevy that is called upon by one of the if statements
def chevy():
    # the dictionary for the Chevy Malibu
    Malibu = {1: "The Malibu gets 36mpg on the highway", 2: "The price of the Malibu starts at 24,000",
              3: "The Malibu has a 1.5L 4 Cylinder Engine"}

    # the dictionary for the Chevy Camaro
    Camaro = {1: "The Camaro gets 30mpg on the highway", 2: "The price of the Camaro starts at 25,000",
              3: "The Camaro has a 2.0L 4 Cylinder Engine"}

    # the dictionary for the Chevy Equinox
    Equinox = {1: "The Equinox gets 31mpg on the highway", 2: "The price of the Equinox starts at 26,000",
               3: "The Equinox has a 1.5L 4 Cylinder Engine"}

    # the dictionary for the Chevy Silverado
    Silverado = {1: "The Silverado gets 31mpg on the highway", 2: "The price of the Silverado starts at 31,000",
                 3: "The Silverado has a 2.7L 4 Cylinder Engine"}

    print("Hi here at Chevy we offer four different models:")

    # list of the different models that Chevy offers
    chevyModel = ["Malibu", "Camaro", "Equinox", "Silverado"]

    # a for loop that prints out all of the different Honda models
    for x in chevyModel:
        print(x)

    # a question to ask the user which model they are interested in and takes their input
    print("Which model are you interested in?")

    chevyInput = input()
    # a list of if statements that cycle through the four Chevy models
    if chevyInput == "Malibu":
        # prints the userInputInfo which asks the user what specifically they want to learn more about regarding the car they selected
        print(userInputInfo)
        cor_In = input()
        # a list of different if statements that cycle through the three options that users have to learn more about their car
        if cor_In == "1":
            # print statement for the info that the user requested
            print(Malibu[1])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Malibu.txt", "a")
            f.write(Malibu[1])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Malibu's mpg have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "2":
            # print statement for the info that the user requested
            print(Malibu[2])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Malibu.txt", "a")
            f.write(Malibu[2])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The price of the Malibu have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "3":
            # print statement for the info that the user requested
            print(Malibu[3])
            f = open("Malibu.txt", "a")
            f.write(Malibu[3])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Malibu's engine have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()

    if chevyInput == "Camaro":
        # prints the userInputInfo which asks the user what specifically they want to learn more about regarding the car they selected
        print(userInputInfo)
        cor_In = input()
        # a list of different if statements that cycle through the three options that users have to learn more about their car
        if cor_In == "1":
            # print statement for the info that the user requested
            print(Camaro[1])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Camaro.txt", "a")
            f.write(Camaro[1])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Camaro's mpg have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "2":
            # print statement for the info that the user requested
            print(Camaro[2])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Camaro.txt", "a")
            f.write(Camaro[2])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The price of the Camaro have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "3":
            # print statement for the info that the user requested
            print(Camaro[3])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Camaro.txt", "a")
            f.write(Camaro[3])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Camaro's engine have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()

    if chevyInput == "Equinox":
        # prints the userInputInfo which asks the user what specifically they want to learn more about regarding the car they selected
        print(userInputInfo)
        cor_In = input()
        # a list of different if statements that cycle through the three options that users have to learn more about their car
        if cor_In == "1":
            # print statement for the info that the user requested
            print(Equinox[1])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Equinox.txt", "a")
            f.write(Equinox[1])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Equinox's mpg have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "2":
            # print statement for the info that the user requested
            print(Equinox[2])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Equinox.txt", "a")
            f.write(Equinox[2])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The price of the Equinox have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "3":
            # print statement for the info that the user requested
            print(Equinox[3])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Equinox.txt", "a")
            f.write(Equinox[3])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Equinox's engine have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()

    if chevyInput == "Silverado":
        # prints the userInputInfo which asks the user what specifically they want to learn more about regarding the car they selected
        print(userInputInfo)
        cor_In = input()
        # a list of different if statements that cycle through the three options that users have to learn more about their car
        if cor_In == "1":
            # print statement for the info that the user requested
            print(Silverado[1])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Silverado.txt", "a")
            f.write(Silverado[1])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Silverado's mpg have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "2":
            # print statement for the info that the user requested
            print(Silverado[2])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Silverado.txt", "a")
            f.write(Silverado[2])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The price of the Silverado have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "3":
            # print statement for the info that the user requested
            print(Silverado[3])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Silverado.txt", "a")
            f.write(Silverado[3])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Silverado's engine have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()


def ford():
    # the dictionary for the Ford Mustang
    Mustang = {1: "The Mustang gets 32mpg on the highway", 2: "The price of the Mustang starts at 27,000",
               3: "The Mustang has a 2.3L 4 Cylinder Engine"}

    # the dictionary for the Ford Escape
    Escape = {1: "The Escape gets 37mpg on the highway", 2: "The price of the Escape starts at 25,000",
              3: "The Escape has a 1.5L 3 Cylinder Engine"}

    # the dictionary for the Ford Bronco
    Bronco = {1: "The Bronco gets 22mpg on the highway", 2: "The price of the Bronco starts at 30,000",
              3: "The Bronco has a 2.3L 4 Cylinder Engine"}

    # the dictionary for the Ford F-250
    ford_Truck = {1: "The F-250 gets 15mpg on the highway", 2: "The price of the F-250 starts at 36,000",
                  3: "The F-250 has a 6.2L 8 Cylinder Engine"}

    print("Hi here at Ford we offer four different models:")

    # list of the different models that Ford offers
    fordModel = ["Mustang", "Escape", "Bronco", "F-250"]

    # a for loop that prints out all of the different Honda models
    for x in fordModel:
        print(x)

    # a question to ask the user which model they are interested in and takes their input
    print("Which model are you interested in?")
    fordInput = input()

    # a list of if statements that cycle through the four ford models
    if fordInput == "Mustang":
        # prints the userInputInfo which asks the user what specifically they want to learn more about regarding the car they selected
        print(userInputInfo)
        cor_In = input()
        # a list of different if statements that cycle through the three options that users have to learn more about their car
        if cor_In == "1":
            # print statement for the info that the user requested
            print(Mustang[1])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Mustang.txt", "a")
            f.write(Mustang[1])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Mustang's mpg have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "2":
            # print statement for the info that the user requested
            print(Mustang[2])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Mustang.txt", "a")
            f.write(Mustang[1])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The price of the Mustang have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "3":
            # print statement for the info that the user requested
            print(Mustang[3])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Mustang.txt", "a")
            f.write(Mustang[3])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Mustang's engine have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()

    if fordInput == "Escape":
        # prints the userInputInfo which asks the user what specifically they want to learn more about regarding the car they selected
        print(userInputInfo)
        cor_In = input()
        # a list of different if statements that cycle through the three options that users have to learn more about their car
        if cor_In == "1":
            # print statement for the info that the user requested
            print(Escape[1])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Escape.txt", "a")
            f.write(Escape[1])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Escape's mpg have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "2":
            # print statement for the info that the user requested
            print(Escape[2])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Escape.txt", "a")
            f.write(Escape[2])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The price of the Escape have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "3":
            # print statement for the info that the user requested
            print(Escape[3])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Escape.txt", "a")
            f.write(Escape[3])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Escape's engine have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()

    if fordInput == "Bronco":
        # prints the userInputInfo which asks the user what specifically they want to learn more about regarding the car they selected
        print(userInputInfo)
        cor_In = input()
        # a list of different if statements that cycle through the three options that users have to learn more about their car
        if cor_In == "1":
            # print statement for the info that the user requested
            print(Bronco[1])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Bronco.txt", "a")
            f.write(Bronco[1])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Bronco's mpg have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "2":
            # print statement for the info that the user requested
            print(Bronco[2])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Bronco.txt", "a")
            f.write(Bronco[2])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The price of the Bronco have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "3":
            # print statement for the info that the user requested
            print(Bronco[3])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("Bronco.txt", "a")
            f.write(Bronco[3])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the Bronco's engine have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()

    if fordInput == "F-250":
        # prints the userInputInfo which asks the user what specifically they want to learn more about regarding the car they selected
        print(userInputInfo)
        cor_In = input()
        # a list of different if statements that cycle through the three options that users have to learn more about their car
        if cor_In == "1":
            # print statement for the info that the user requested
            print(ford_Truck[1])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("F-250.txt", "a")
            f.write(ford_Truck[1])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the F-250's mpg have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "2":
            # print statement for the info that the user requested
            print(ford_Truck[2])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("F-250.txt", "a")
            f.write(ford_Truck[2])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The price of the F-250 have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()
        if cor_In == "3":
            # print statement for the info that the user requested
            print(ford_Truck[3])
            # creating a file that inputs the data from the list that the user requested and closes it
            f = open("F-250.txt", "a")
            f.write(ford_Truck[3])
            f.close()
            # printing a statement that tells the user about the file that has been created and saved
            print("The statistics of the F-250's engine have the been saved in text file for you to view.")
            # quits out of program when info is given to user
            exit()


# the start of the main function that asks the user about their interest
def main():
    print(
        "Welcome to our Auto Body mall here we have Toyota, Honda, Chevy, and Ford which of these Auto Body shops would you like to check out?")

    # takes the input of what the customer is interested in
    customerChoice = input()

    # cycles through if statements that correlate with different car companies I have listed
    if customerChoice == "Toyota":
        toyota()
    if customerChoice == "Honda":
        honda()
    if customerChoice == "Chevy":
        chevy()
    if customerChoice == "Ford":
        ford()
    # if the correct answers isn't given at any point in the code it will tell the user to try again and runs the main function again starting the user at the beginning
    elif customerChoice != "":
        print("Your entry didn't work please try again")
        main()


# runs the main function
main()
