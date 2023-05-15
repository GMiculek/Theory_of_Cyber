def AccessAttack():
    Yes_or_No = "Enter 'yes' or 'no' to proceed."
    Failure = "All possible options have been exhausted. Attack has failed."

    list_of_dictionaries = []

    Dict_of_State_1_options = {}
    Dict_of_State_1_options["Option1"] = ["unattempted", "unattempted"]
    Dict_of_State_1_options["Option2"] = ["unattempted", "unattempted"] #global dictionaries to store each option at each state and store if the options have been attempted and if they have been successful or not
    Dict_of_State_1_options["Option3"] = ["unattempted", "unattempted"]

    Dict_of_State_1_options_exhausted = {}
    Dict_of_State_1_options_exhausted["Option1"] = ["attempted", "unsuccessful"] #global dictionaries that will only be used for comparisons, if they match with the dictionaries we are actively modifying, all options have been exhausted 
    Dict_of_State_1_options_exhausted["Option2"] = ["attempted", "unsuccessful"]
    Dict_of_State_1_options_exhausted["Option3"] = ["attempted", "unsuccessful"]


    Dict_of_State_2_options = {}
    Dict_of_State_2_options["Option1"] = ["unattempted", "unattempted"]
    Dict_of_State_2_options["Option2"] = ["unattempted", "unattempted"]


    Dict_of_State_2_options_exhausted = {}
    Dict_of_State_2_options_exhausted["Option1"] = ["attempted", "unsuccessful"]
    Dict_of_State_2_options_exhausted["Option2"] = ["attempted", "unsuccessful"]


    Dict_of_State_3_options = {}
    Dict_of_State_3_options["Option1"] = ["unattempted", "unattempted"]

    Dict_of_State_4_options = {}
    Dict_of_State_4_options["Option1"] = ["unattempted", "unattempted"]


    global Final_Statement
    Final_Statement = ""

    def Access_Attack_State1():

        global Final_Statement
        print("\nYou are starting your attack.") #State 1

        if(Dict_of_State_1_options_exhausted == Dict_of_State_1_options): #if all options have failed, give failure message 
            print("\n"+Final_Statement + Failure)
            

        else: #if options to proceed are still possible 

            response1 = input("Would you like to attempt to connect to the Home Wi-Fi, see if you have access to the user's phone, or attempt to compromise the IoT device directly? Enter '1' for the first option, enter '2' for the second option, or enter '3' for the third option. ")
            #gives you the options on how you would like to proceed 

            if(response1 == "1"): #try to connect to the home wi-fi (option 1 in this case)

                if(Dict_of_State_1_options["Option1"][0] == "attempted"):# if this has been attempted already and it failed, rerun function state1 
                    
                    input("\nThis option has already been attempted and failed. Please try a new route. Press Enter to continue...")
                    Access_Attack_State1()

                else:
                    
                    Dict_of_State_1_options["Option1"][0] = "attempted" #change unattempted to attempted at current index of list in the dictionary
                    Register_Y_or_N= input("\nCan you connect to the Home Wi-fi? " + Yes_or_No + " ") #asks user how to proceed

                    if(Register_Y_or_N == "yes"):
                        Dict_of_State_1_options["Option1"][1] = "successful" #change unattempted to successful at current index of list in the dictionary
                        #list_of_dictionaries.append("State_1: " + str(Dict_of_State_1_options) + " ")
                        list_of_dictionaries.append("State_1")
                        print("\nYou are now connected with the Home Wi-Fi.") #moves to state 3
                        Final_Statement= Final_Statement + "Attacker attempted to connect with Home Wi-Fi and succeeded (State 1 -> State 3 success). "
                        SUCCESSFULLY_COMPROMISED_IoT_DEVICE()
                    

                    elif(Register_Y_or_N == "no"):
                        Dict_of_State_1_options["Option1"][1] = "unsuccessful" #change unattempted to unsuccessful at current index of list in the dictionary
                        Final_Statement= Final_Statement+  "Attacker attempted to connect with Home Wi-Fi and failed (State 1 -> State 3 fail). "
                        response2 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                        if (response2 == "yes"):
                            Access_Attack_State1() #if they want to retry, rerun function

                        elif (response2 == "no"):
                            print("\n"+Final_Statement+Failure) #State 1 to Fail

                        else:
                            
                            input("\nPlease enter only the provided options. Press Enter to continue...")
                            Access_Attack_State1() #reruns function if what was inputted was not an answer choice
                            
                    else:
                        Dict_of_State_1_options["Option1"][0] = "unattempted" #if user fails to give an appropriate response to the question, change attempted to unattempt at current index of list in the dictionary to prevent a situation where we can't adavnce/fail
                        input("\nPlease enter only the provided options. Press Enter to continue...")
                        Access_Attack_State1()
                    

                

            elif(response1 == "2"): #try to access user's phone

                if(Dict_of_State_1_options["Option2"][0] == "attempted"): #if this has been attempted already and it failed, rerun function state1 
                    
                    input("\nThis option has already been attempted and failed. Please try a new route. Press Enter to continue...")
                    Access_Attack_State1()

                else:

                

                
                    Dict_of_State_1_options["Option2"][0] = "attempted" #change unattempted to attempted at current index of list in the dictionary

                    Access_Y_or_N= input("\nDo you have access to user's phone? " + Yes_or_No + " ") #asks user how to proceed

                    if(Access_Y_or_N == "yes"):
                        Dict_of_State_1_options["Option2"][1] = "successful" #change unattempted to successful at current index of list in the dictionary
                        print("\nYou now have access to the user's phone.") #moves to state 2
                        #list_of_dictionaries.append("State_1: " + str(Dict_of_State_1_options) + " ")
                        Final_Statement= Final_Statement + "Attacker attempted to gain access to user's phone and succeeded (State 1 -> State 2 success). "
                        list_of_dictionaries.append("State_1")
                        Access_Attack_State2()
                        

                    elif(Access_Y_or_N == "no"):
                        Dict_of_State_1_options["Option2"][1] = "unsuccessful" #change unattempted to unsuccessful at current index of list in the dictionary
                        Final_Statement= Final_Statement + "Attacker attempted to gain access to user's phone and failed (State 1 -> State 2 fail). "
                        response3 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                        if (response3 == "yes"):
                            Access_Attack_State1() #if they want to retry, rerun function

                        elif (response3 == "no"):
                            print("\n"+Final_Statement+Failure) #State 1 to Fail

                        else:
                            
                            input("\nPlease enter only the provided options. Press Enter to continue...")
                            Access_Attack_State1() #reruns function if what was inputted was not an answer choice


                    else:
                        Dict_of_State_1_options["Option2"][0] = "unattempted"
                        input("\nPlease enter only the provided options. Press Enter to continue...")
                        Access_Attack_State1() #if user fails to give an appropriate response to the question, change attempted to unattempt at current index of list in the dictionary to prevent a situation where we can't adavnce/fail         






            elif(response1 == "3"): #try to access user's phone

                if(Dict_of_State_1_options["Option3"][0] == "attempted"): #if this has been attempted already and it failed, rerun function state1 
                    
                    input("\nThis option has already been attempted and failed. Please try a new route. Press Enter to continue...")
                    Access_Attack_State1()

                else:

                

                
                    Dict_of_State_1_options["Option3"][0] = "attempted" #change unattempted to attempted at current index of list in the dictionary

                    Access_Y_or_N= input("\nAre you able to compromise the IoT device? " + Yes_or_No + " ") #asks user how to proceed

                    if(Access_Y_or_N == "yes"):
                        Dict_of_State_1_options["Option3"][1] = "successful" #change unattempted to successful at current index of list in the dictionary
                        print("\nYou now have access to the user's phone.") #moves to state 4
                        #list_of_dictionaries.append("State_1: " + str(Dict_of_State_1_options) + " ")
                        Final_Statement= Final_Statement + "Attacker attempted to compromise the IoT device and succeeded (State 1 -> SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4) success). "
                        list_of_dictionaries.append("State_1")
                        Access_Attack_State4()
                        

                    elif(Access_Y_or_N == "no"):
                        Dict_of_State_1_options["Option3"][1] = "unsuccessful" #change unattempted to unsuccessful at current index of list in the dictionary
                        Final_Statement= Final_Statement + "Attacker attempted to compromise the IoT device and failed (State 1 -> SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4) fail). "
                        response3 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                        if (response3 == "yes"):
                            Access_Attack_State1() #if they want to retry, rerun function

                        elif (response3 == "no"):
                            print("\n"+Final_Statement+Failure) #State 1 to Fail

                        else:
                            
                            input("\nPlease enter only the provided options. Press Enter to continue...")
                            Access_Attack_State1() #reruns function if what was inputted was not an answer choice


                    else:
                        Dict_of_State_1_options["Option3"][0] = "unattempted"
                        input("\nPlease enter only the provided options. Press Enter to continue...")
                        Access_Attack_State1() #if user fails to give an appropriate response to the question, change attempted to unattempt at current index of list in the dictionary to prevent a situation where we can't adavnce/fail






            else:

                input("\nPlease enter only the provided options. Press Enter to continue...")
                Access_Attack_State1() #reruns function if what was inputted was not an answer choice

        



    def Access_Attack_State2():
        #print(list_of_dictionaries)
        global Final_Statement

        if(Dict_of_State_2_options_exhausted == Dict_of_State_2_options): #if all options have failed, give failure message 
            print("\n"+Final_Statement+Failure)

        else:

            response1 = input("Would you like to attempt to connect to the Home Wi-Fi, or attempt to compromise the IoT device directly? Enter '1' for the former option, or enter '2' for the latter option. ")  


            if(response1 == "1"):
                if(Dict_of_State_2_options["Option1"][0] == "attempted"):# if this has been attempted already and it failed, rerun state2 function 
                    
                    input("\nThis option has already been attempted and failed. Please try a new route. Press Enter to continue...")
                    Access_Attack_State2()

                else:
                    
                    Dict_of_State_2_options["Option1"][0] = "attempted" #change unattempted to attempted at current index of list in the dictionary
                    Register_Y_or_N= input("\nCan you connect to the Home Wi-fi? " + Yes_or_No + " ") #asks user how to proceed

                    if(Register_Y_or_N == "yes"):
                        
                        Dict_of_State_2_options["Option1"][1] = "successful" #change unattempted to successful at current index of list in the dictionary
                        #list_of_dictionaries.append("State_2: " + str(Dict_of_State_2_options) + " ")
                        list_of_dictionaries.append("State_2")
                        Final_Statement= Final_Statement + "Attacker attempted to connect with Home Wi-Fi and succeeded (State 2 -> State 3 success). "
                        print("\nYou are now registered with the Home Wi-Fi.") #moves to state 3
                        SUCCESSFULLY_COMPROMISED_IoT_DEVICE()
                    

                    elif(Register_Y_or_N == "no"):
                        Dict_of_State_2_options["Option1"][1] = "unsuccessful" #change unattempted to unsuccessful at current index of list in the dictionary
                        Final_Statement= Final_Statement + "Attacker attempted to register with Home Wi-Fi and failed (State 2 -> State 3 fail). "
                        response2 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                        if (response2 == "yes"):
                            Access_Attack_State2() #if they want to retry, rerun function

                        elif (response2 == "no"):
                            print("\n"+Final_Statement+Failure) #State 2 to Fail

                        else:
                            
                            input("\nPlease enter only the provided options. Press Enter to continue...")
                            Access_Attack_State2() #reruns function if what was inputted was not an answer choice
                            
                    else:
                        Dict_of_State_2_options["Option1"][0] = "unattempted" #if user fails to give an appropriate response to the question, change attempted to unattempt at current index of list in the dictionary to prevent a situation where we can't adavnce/fail
                        input("\nPlease enter only the provided options. Press Enter to continue...")
                        Access_Attack_State2()

                

                


            elif(response1 == "2"):
                if(Dict_of_State_2_options["Option2"][0] == "attempted"):# if this has been attempted already and it failed, rerun state2 function 
                    
                    input("\nThis option has already been attempted and failed. Please try a new route. Press Enter to continue...")
                    Access_Attack_State2()

                else:

                

                
                    Dict_of_State_2_options["Option2"][0] = "attempted" #change unattempted to attempted at current index of list in the dictionary

                    Access_Y_or_N= input("\nAre you able to compromise the IoT device? " + Yes_or_No + " ") #asks user how to proceed

                    if(Access_Y_or_N == "yes"):
                        Dict_of_State_2_options["Option2"][1] = "successful" #change unattempted to successful at current index of list in the dictionary
                        print("\nYou now have access to the user's phone.") #moves to state 4
                        #list_of_dictionaries.append("State_1: " + str(Dict_of_State_1_options) + " ")
                        Final_Statement= Final_Statement + "Attacker attempted to compromise the IoT device and succeeded (State 2 -> SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4) success). "
                        list_of_dictionaries.append("State_2")
                        Access_Attack_State4()
                        

                    elif(Access_Y_or_N == "no"):
                        Dict_of_State_2_options["Option2"][1] = "unsuccessful" #change unattempted to unsuccessful at current index of list in the dictionary
                        Final_Statement= Final_Statement + "Attacker attempted to compromise the IoT device and failed (State 2 -> SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4) fail). "
                        response3 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                        if (response3 == "yes"):
                            Access_Attack_State2() #if they want to retry, rerun function

                        elif (response3 == "no"):
                            print("\n"+Final_Statement+Failure) #State 1 to Fail

                        else:
                            
                            input("\nPlease enter only the provided options. Press Enter to continue...")
                            Access_Attack_State2() #reruns function if what was inputted was not an answer choice


                    else:
                        Dict_of_State_2_options["Option2"][0] = "unattempted"
                        input("\nPlease enter only the provided options. Press Enter to continue...")
                        Access_Attack_State1() #if user fails to give an appropriate response to the question, change attempted to unattempt at current index of list in the dictionary to prevent a situation where we can't adavnce/fail



            else:
                input("\nPlease enter only the provided options. Press Enter to continue...")
                Access_Attack_State2() #reruns function if what was inputted was not an answer choice

            
    def SUCCESSFULLY_COMPROMISED_IoT_DEVICE():
        global Final_Statement
        response1 = input("Are you able to compromise the IoT device? " + Yes_or_No + " ")

        if (response1 == "yes"):
            Dict_of_State_3_options["Option1"][0] = "attempted"
            Dict_of_State_3_options["Option1"][1] = "successful"
            list_of_dictionaries.append("State_3")
            #list_of_dictionaries.append("State_3: " + str(Dict_of_State_3_options) + " ")
            Final_Statement= Final_Statement + "Attacker attempted to compromise the IoT device and succeeded (State 3 -> SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4) success). "
            print("\nThe IoT device was successfully compromised.") #moves to state 4
            Access_Attack_State4()

        elif (response1 == "no"):
            Dict_of_State_3_options["Option1"][0] = "attempted"
            Dict_of_State_3_options["Option1"][1] = "unsuccessful"
            Final_Statement= Final_Statement + "Attacker attempted to connect to the IoT App and failed (State 3 -> SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4) fail). " 
            print("\n"+Final_Statement + Failure) #State 3 to Fail

        else:
            input("\nPlease enter only the provided options. Press Enter to continue...")
            SUCCESSFULLY_COMPROMISED_IoT_DEVICE() #reruns function if what was inputted was not an answer choice

            
    def Access_Attack_State4():
        global Final_Statement
        response1 = input("Are you able to compromise the Home Network " + Yes_or_No + " ")
        
        if (response1 == "yes"):
            Dict_of_State_4_options["Option1"][0] = "attempted"
            Dict_of_State_4_options["Option1"][1] = "successful"
            list_of_dictionaries.append("State_7")
            
            Final_Statement= Final_Statement + "Attacker attempted to compromsing the Home Network and succeeded. Compromise Successful. Attack Complete. (SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4) -> SUCCESSFULLY COMPROMISED HOME NETWORK (state 5) success). "
            
            Access_Attack_closing()

        elif (response1 == "no"):
            Dict_of_State_4_options["Option1"][0] = "attempted"
            Dict_of_State_4_options["Option1"][1] = "unsuccessful"
            Final_Statement= Final_Statement + "While the attacker failed to compromise the Home Network, the attacker was successful in compromising the IoT device Compromise Successful. Attack Complete. (SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4) -> SUCCESSFULLY COMPROMISED HOME NETWORK (state 5) fail). "
            Access_Attack_closing()

        else:
            input("\nPlease enter only the provided options. Press Enter to continue...")
            Access_Attack_State4() #reruns function if what was inputted was not an answer choice  
            
            
            
    def Access_Attack_closing():
        global Final_Statement
        print(list_of_dictionaries)
        print("\n" + Final_Statement + "\n")

        print("Complete model of all pathways:\n")
        





        print("                                                                                                                     SUCCESSFULLY COMPROMISED HOME NETWORK")
        print("                                                                                                                                                         ^")
        print("                                                - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                                  |")
        print("                                               |                                                                       |                                 |")
        print("                                               |                                                                       |                                 |")
        print("                                               |                                       - - - - - > FAIL                |                                 |")
        print("                                               |                                      |                                |                                 |")
        print("                                               |                                      |  A                             |                                 |")
        print("                                               |                                      |  L                             |                                 |")
        print("                                               |                                      |  L                             |                                 |")
        print("                                               |                                      |                                |                                 |")
        print("                                               |                                      |  P                             |                                 |")
        print("                                            C  |                                      |  A                             |                            C    |")
        print("                                            O  |                                      |  T                             |                            O    |")
        print("                                            M  |                                      |  H                             |                            M    |")
        print("                                            P  |                                      |  S                             |                            P    |")
        print("                                            R  |                                      |                                |                            R    |")
        print("                                            I  |                                      |  F                             |                            O    |")
        print("                                            S  |                                      |  A                             |                            M    |")
        print("                                            E  |                                      |  I                             |                            I    |")
        print("                                               |                                      |  L                             |                            S    |")
        print("                                               |                                      |                                |                            E    |")
        print("                                               |                                      |                                |                                 |")
        print("          A L L   P A T H S   F A I L          |      C O N N E C T                   |      C O M P R O M I S E       v                                 |")  
        print("FAIL < - - - - - - - - - - - - - - - - - - - - S1 - - - - - - - - - - - - - - - - - > S3 - - - - - - - - - - - - - - > SUCCESSFULLY COMPROMISED IoT DEVICE")
        print("                                               |                                      ^                                ^              ^                  |")
        print("                                               |                                      |                                |              |               A  |")
        print("                                               |                                      |                                |              |               L  |")
        print("                                            A  |                                      |                                |              |               L  |")
        print("                                            C  |                                      |                                |              |                  |")
        print("                                            C  |                                      |                                |              |               P  |")
        print("                                            E  |                                      |                                |              |               A  |")
        print("                                            S  |                                      |                                |              |               T  |")
        print("                                            S  |                                      |                                |              |               H  |")
        print("                                               |                                      |                                |              |               S  |")
        print("                                               |                                      |                                |              |                  |")
        print("                                               |                                      |                                |              |               F  |")
        print("                                               |                                      |                                |              |               A  |")
        print("          A L L   P A T H S   F A I L          V      C O N N E C T                   |                                |              |               I  |")
        print("FAIL < - - - - - - - - - - - - - - - - - - - - S2 - - - - - - - - - - - - - - - - - -                                  |              |               L  |")
        print("                                               |                                                                       |              |                  |")
        print("                                               |                                                                       |              |                  |")
        print("                                            C  |                                                                       |               - - - - - - - - - ")
        print("                                            O  |                                                                       |")
        print("                                            M  |                                                                       |")
        print("                                            P  |                                                                       |")
        print("                                            R  |                                                                       |")
        print("                                            I  |                                                                       |")
        print("                                            S  |                                                                       |")
        print("                                            E  |                                                                       |")
        print("                                               |                                                                       |")
        print("                                                - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print()

        print("Key: S1-> Attacker, S2 -> User Phone, S3 -> Home Wi-Fi")
        print("FAIL -> Attemped attack failed, SUCCESSFULLY COMPROMISED IoT DEVICE -> IoT Device was successfully compromised, SUCCESSFULLY COMPROMISED HOME NETWORK -> Home Network was successfully compromised ")    


        

    Access_Attack_State1()
    







