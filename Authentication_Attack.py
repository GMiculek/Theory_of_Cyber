def AuthenticationAttack():
    Yes_or_No = "Enter 'yes' or 'no' to proceed."
    Failure = "All possible options have been exhausted. Attack has failed."

    list_of_dictionaries = []

    Dict_of_State_1_options = {}
    Dict_of_State_1_options["Option1"] = ["unattempted", "unattempted"]
    Dict_of_State_1_options["Option2"] = ["unattempted", "unattempted"] #global dictionaries to store each option at each state and store if the options have been attempted and if they have been successful or not

    Dict_of_State_1_options_exhausted = {}
    Dict_of_State_1_options_exhausted["Option1"] = ["attempted", "unsuccessful"] #global dictionaries that will only be used for comparisons, if they match with the dictionaries we are actively modifying, all options have been exhausted 
    Dict_of_State_1_options_exhausted["Option2"] = ["attempted", "unsuccessful"]


    Dict_of_State_2_options = {}
    Dict_of_State_2_options["Option1"] = ["unattempted", "unattempted"]


    Dict_of_State_3_options = {}
    Dict_of_State_3_options["Option1"] = ["unattempted", "unattempted"]

    Dict_of_State_4_options = {}
    Dict_of_State_4_options["Option1"] = ["unattempted", "unattempted"]

    Dict_of_State_5_options = {}
    Dict_of_State_5_options["Option1"] = ["unattempted", "unattempted"]


    global Final_Statement
    Final_Statement = ""

    def Authentication_Attack_State1():

        global Final_Statement
        print("\nYou are currently attempting to gain access to either the home Wi-Fi or the IoT App.") #State 1

        if(Dict_of_State_1_options_exhausted == Dict_of_State_1_options): #if all options have failed, give failure message 
            print("\n"+Final_Statement + Failure)
            

        else: #if options to proceed are still possible 

            response1 = input("Would you like to attempt to gain access to the home Wi-Fi or attempt to gain access to the IoT App? Enter '1' for the former option or enter '2' for the latter option. ")
            #gives you the options on how you would like to proceed 

            if(response1 == "1"): #try to gain access to the home Wi-Fi (option 1 in this case)

                if(Dict_of_State_1_options["Option1"][0] == "attempted"):# if this has been attempted already and it failed, rerun function state1 
                    
                    input("\nThis option has already been attempted and failed. Please try a new route. Press Enter to continue...")
                    Authentication_Attack_State1()

                else:
                    
                    Dict_of_State_1_options["Option1"][0] = "attempted" #change unattempted to attempted at current index of list in the dictionary
                    Register_Y_or_N= input("\nCan you gain access to the home Wi_Fi? " + Yes_or_No + " ") #asks user how to proceed

                    if(Register_Y_or_N == "yes"):
                        Dict_of_State_1_options["Option1"][1] = "successful" #change unattempted to successful at current index of list in the dictionary
                        #list_of_dictionaries.append("State_1: " + str(Dict_of_State_1_options) + " ")
                        list_of_dictionaries.append("State_1")
                        print("\nYou have gained access to the home Wi-Fi.") #moves to state 2
                        Final_Statement= Final_Statement + "Attacker attempted to gain acess to the home Wi-Fi and succeeded (State 1 -> State 2 success). "
                        Authentication_Attack_State2()
                    

                    elif(Register_Y_or_N == "no"):
                        Dict_of_State_1_options["Option1"][1] = "unsuccessful" #change unattempted to unsuccessful at current index of list in the dictionary
                        Final_Statement= Final_Statement+  "Attacker attempted to gain access to the home Wi-Fi and failed (State 1 -> State 2 fail). "
                        response2 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                        if (response2 == "yes"):
                            Authentication_Attack_State1() #if they want to retry, rerun function

                        elif (response2 == "no"):
                            print("\n"+Final_Statement+Failure) #State 1 to Fail

                        else:
                            
                            input("\nPlease enter only the provided options. Press Enter to continue...")
                            Authentication_Attack_State1() #reruns function if what was inputted was not an answer choice
                            
                    else:
                        Dict_of_State_1_options["Option1"][0] = "unattempted" #if user fails to give an appropriate response to the question, change attempted to unattempt at current index of list in the dictionary to prevent a situation where we can't adavnce/fail
                        input("\nPlease enter only the provided options. Press Enter to continue...")
                        Authentication_Attack_State1()
                    

                

            elif(response1 == "2"): #try to gain access to the IoT  App

                if(Dict_of_State_1_options["Option2"][0] == "attempted"): #if this has been attempted already and it failed, rerun function state1 
                    
                    input("\nThis option has already been attempted and failed. Please try a new route. Press Enter to continue...")
                    Authentication_Attack_State1()

                else:

                

                
                    Dict_of_State_1_options["Option2"][0] = "attempted" #change unattempted to attempted at current index of list in the dictionary

                    Access_Y_or_N= input("\nCan you gain access to the IoT App? " + Yes_or_No + " ") #asks user how to proceed

                    if(Access_Y_or_N == "yes"):
                        Dict_of_State_1_options["Option2"][1] = "successful" #change unattempted to successful at current index of list in the dictionary
                        print("\nYou have gained access to the IoT App.") #moves to state 3
                        #list_of_dictionaries.append("State_1: " + str(Dict_of_State_1_options) + " ")
                        Final_Statement= Final_Statement + "Attacker attempted to gain access to the IoT App and succeeded (State 1 -> State 3 success). "
                        list_of_dictionaries.append("State_1")
                        Authentication_Attack_State3()
                        

                    elif(Access_Y_or_N == "no"):
                        Dict_of_State_1_options["Option2"][1] = "unsuccessful" #change unattempted to unsuccessful at current index of list in the dictionary
                        Final_Statement= Final_Statement + "Attacker attempted to gain access to the IoT App and failed (State 1 -> State 3 fail). "
                        response3 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                        if (response3 == "yes"):
                            Authentication_Attack_State1() #if they want to retry, rerun function

                        elif (response3 == "no"):
                            print("\n"+Final_Statement+Failure) #State 1 to Fail

                        else:
                            
                            input("\nPlease enter only the provided options. Press Enter to continue...")
                            Authentication_Attack_State1() #reruns function if what was inputted was not an answer choice


                    else:
                        Dict_of_State_1_options["Option2"][0] = "unattempted"
                        input("\nPlease enter only the provided options. Press Enter to continue...")
                        Authentication_Attack_State1() #if user fails to give an appropriate response to the question, change attempted to unattempt at current index of list in the dictionary to prevent a situation where we can't adavnce/fail         

            else:

                input("\nPlease enter only the provided options. Press Enter to continue...")
                Authentication_Attack_State1() #reruns function if what was inputted was not an answer choice

        



    def Authentication_Attack_State2():
        global Final_Statement
        response1 = input("Are you able to compromise the Home Wi-Fi? " + Yes_or_No + " ")

        if (response1 == "yes"):
            Dict_of_State_2_options["Option1"][0] = "attempted"
            Dict_of_State_2_options["Option1"][1] = "successful"
            list_of_dictionaries.append("State_2")
            Final_Statement= Final_Statement + "Attacker attempted to compromise the Home Wi-Fi and succeeded. Compromise Successful. Attack Complete. (State 2 -> Success). "
            Authentication_Attack_closing()

        elif (response1 == "no"):
            Dict_of_State_2_options["Option1"][0] = "attempted"
            Dict_of_State_2_options["Option1"][1] = "unsuccessful"
            Final_Statement= Final_Statement + "Attacker attempted to compromise the Home Wi-Fi and failed (State 2 -> Fail). " 
            print("\n"+Final_Statement + Failure) #State 2 to Fail

        else:
            input("\nPlease enter only the provided options. Press Enter to continue...")
            Authentication_Attack_State2() #reruns function if what was inputted was not an answer choice






            
    def Authentication_Attack_State3():
        global Final_Statement
        response1 = input("Are you able to gain service access to the web services from the IoT App? " + Yes_or_No + " ")

        if (response1 == "yes"):
            Dict_of_State_3_options["Option1"][0] = "attempted"
            Dict_of_State_3_options["Option1"][1] = "successful"
            list_of_dictionaries.append("State_3")
            Final_Statement= Final_Statement + "Attacker attempted to gain service access to the web services from the IoT App and succeeded (State 3 -> State 4 success). "
            print("\nYou now have access to the web services from the IoT App.") #moves to state 4
            Authentication_Attack_State4()

        elif (response1 == "no"):
            Dict_of_State_3_options["Option1"][0] = "attempted"
            Dict_of_State_3_options["Option1"][1] = "unsuccessful"
            Final_Statement= Final_Statement + "Attacker attempted to gain service access to the web services from the IoT App and failed (State 3 -> State 4 fail). " 
            print("\n"+Final_Statement + Failure) #State 3 to Fail

        else:
            input("\nPlease enter only the provided options. Press Enter to continue...")
            Authentication_Attack_State3() #reruns function if what was inputted was not an answer choice

            
    def Authentication_Attack_State4():
        global Final_Statement
        response1 = input("Are you able to gain router access to the home gateway router from the IoT App? " + Yes_or_No + " ")

        if (response1 == "yes"):
            Dict_of_State_4_options["Option1"][0] = "attempted"
            Dict_of_State_4_options["Option1"][1] = "successful"
        
            list_of_dictionaries.append("State_4")
            Final_Statement= Final_Statement + "Attacker attempted to gain router access to the home gateway router from the IoT App and succeeded (State 4 -> State 5 success). "
            print("\nYou now have access to the home gateway router.") #moves to state 5
            Authentication_Attack_State5()

        elif (response1 == "no"):
            Dict_of_State_4_options["Option1"][0] = "attempted"
            Dict_of_State_4_options["Option1"][1] = "unsuccessful"
            Final_Statement= Final_Statement + "Attacker attempted to gain router access to the home gateway router from the IoT App and failed (State 4 -> State 5 fail). " 
            print("\n"+Final_Statement+Failure) #State 4 to Fail

        else:
            input("\nPlease enter only the provided options. Press Enter to continue...")
            Authentication_Attack_State4() #reruns function if what was inputted was not an answer choice 
            
            
            



    def Authentication_Attack_State5():
        global Final_Statement
        response1 = input("Is compromsing the IoT device possible now? " + Yes_or_No + " ")
        
        if (response1 == "yes"):
            Dict_of_State_5_options["Option1"][0] = "attempted"
            Dict_of_State_5_options["Option1"][1] = "successful"
            list_of_dictionaries.append("State_5")
            Final_Statement= Final_Statement + "Attacker attempted to compromsing the IoT device and succeeded. Compromise Successful. Attack Complete. (State 5 -> Success). "
            Authentication_Attack_closing()

        elif (response1 == "no"):
            Dict_of_State_5_options["Option1"][0] = "attempted"
            Dict_of_State_5_options["Option1"][1] = "unsuccessful"
            Final_Statement= Final_Statement + "Attacker attempted to compromsing the IoT device and failed (State 5 -> Fail). "
            print("\n"+Final_Statement+Failure) #State 5 to Fail

        else:
            input("\nPlease enter only the provided options. Press Enter to continue...")
            Authentication_Attack_State5() #reruns function if what was inputted was not an answer choice 


        


    def Authentication_Attack_closing():
        global Final_Statement
        print(list_of_dictionaries)
        print("\n" + Final_Statement + "\n")

        print("Complete model of all pathways:\n")
        





        print("  A L L   P A T H S   F A I L")
        print(" - - - - - - - - - - - - - - - > FAIL       - - - - - > FAIL                         COMPROMISE SUCCESSFUL  < - - - - - - ")
        print("|                                          |                                                                             |")
        print("|                                          |  A                                                                          |")
        print("|                                          |  L                                                                          |")
        print("|                                          |  L                                                                        C |")
        print("|                                          |                                                                           O |")
        print("|                                          |  P                                                                        M |")
        print("|                                          |  A                                                                        P |")
        print("|                                          |  T                                                                        R |")
        print("|                                          |  H                                                                        O |")
        print("|                                          |  S                                                                        M |")
        print("|                                          |                                                                           I |")
        print("|                                          |  F                                                                        S |")
        print("|                                          |  A                                                                        E |")
        print("|                                          |  I                                                                          |")
        print("|                                          |  L                                                                          |")
        print("|                                          |                                                                             |")
        print("|                                          |                                                                             |")
        print("|     A C C E S S                          |      S E R V I C E   A C C E S S             R O U T E R   A C C E S S      |")
        print("S1 - - - - - - - - - - - - - - - - - - - ->S3 - - - - - - - - - - - - - - - - - - - >S4 - - - - - - - - - - - - - - - - >S5")
        print("|                                                                                  A |                                 A | ")
        print("|                                                                                  L |                                 L |")
        print("|                                                                                  L |                                 L |")
        print("|                                                                                    |                                   |")
        print("|                                                                                  P |                                 P |")
        print("|                                                                                  A |                                 A |")
        print("|                                                                                  T |                                 T |")
        print("|                                                                                  H |                                 H |")
        print("|                                                                                  S |                                 S |")
        print("|                                                                                    |                                   |")
        print("|                                                                                  F |                                 F |")
        print("|                                                                                  A |                                 A |")
        print("|                                                                                  I |                                 I |")
        print("|     A C C E S S                                 C O M P R O M I S E              L |                                 L |")
        print(" - - - - - - - - - - - - - - - - - - - - > S2 - - - - - - - - - - - - - - -           - - - > FAIL                        - - - > FAIL ")
        print("                                                                           |")
        print("                                                                           |")
        print("                                                                           |")
        print("                                                                           |")
        print("                                                                           |")
        print("                                                                           |")
        print("                                                                            - - - - - - >  COMPROMISE SUCCESSFUL")
        print()
        print("Key: S1-> Attacker, S2 -> Home Wi-Fi, S3 -> IoT App, S4 -> Web Services, S5 -> Home Gateway Router")
        print("FAIL -> Attemped attack failed, Compromise Successful -> Either IoT Device or Home Wi-Fi network was successfully compromised")    


        

    Authentication_Attack_State1()
    







