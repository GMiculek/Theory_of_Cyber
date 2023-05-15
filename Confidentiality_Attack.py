def ConfidentialityAttack():
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
    Dict_of_State_2_options["Option2"] = ["unattempted", "unattempted"]
    Dict_of_State_2_options["Option3"] = ["unattempted", "unattempted"]

    Dict_of_State_2_options_exhausted = {}
    Dict_of_State_2_options_exhausted["Option1"] = ["attempted", "unsuccessful"]
    Dict_of_State_2_options_exhausted["Option2"] = ["attempted", "unsuccessful"]
    Dict_of_State_2_options_exhausted["Option3"] = ["attempted", "unsuccessful"]

    Dict_of_State_3_options = {}
    Dict_of_State_3_options["Option1"] = ["unattempted", "unattempted"]

    Dict_of_State_4_options = {}
    Dict_of_State_4_options["Option1"] = ["unattempted", "unattempted"]

    Dict_of_State_5_options = {}
    Dict_of_State_5_options["Option1"] = ["unattempted", "unattempted"]

    Dict_of_State_6_options = {}
    Dict_of_State_6_options["Option1"] = ["unattempted", "unattempted"]

    Dict_of_State_7_options = {}
    Dict_of_State_7_options["Option1"] = ["unattempted", "unattempted"]

    global Final_Statement
    Final_Statement = ""

    def Confidentiality_Attack_State1():

        global Final_Statement
        print("\nYou are currently attempting to access the Public Wi-Fi.") #State 1

        if(Dict_of_State_1_options_exhausted == Dict_of_State_1_options): #if all options have failed, give failure message 
            print("\n"+Final_Statement + Failure)
            

        else: #if options to proceed are still possible 

            response1 = input("Would you like to attempt to register to the Public Wi-Fi or see if you have access to the user's phone? Enter '1' for the former option or enter '2' for the latter option. ")
            #gives you the options on how you would like to proceed 

            if(response1 == "1"): #try to register to the public wi-fi (option 1 in this case)

                if(Dict_of_State_1_options["Option1"][0] == "attempted"):# if this has been attempted already and it failed, rerun function state1 
                    
                    input("\nThis option has already been attempted and failed. Please try a new route. Press Enter to continue...")
                    Confidentiality_Attack_State1()

                else:
                    
                    Dict_of_State_1_options["Option1"][0] = "attempted" #change unattempted to attempted at current index of list in the dictionary
                    Register_Y_or_N= input("\nCan you register on the Public Wi-fi? " + Yes_or_No + " ") #asks user how to proceed

                    if(Register_Y_or_N == "yes"):
                        Dict_of_State_1_options["Option1"][1] = "successful" #change unattempted to successful at current index of list in the dictionary
                        #list_of_dictionaries.append("State_1: " + str(Dict_of_State_1_options) + " ")
                        list_of_dictionaries.append("State_1")
                        print("\nYou are now registered with the Public Wi-Fi.") #moves to state 3
                        Final_Statement= Final_Statement + "Attacker attempted to register with Public Wi-Fi and succeeded (State 1 -> State 3 success). "
                        Confidentiality_Attack_State3()
                    

                    elif(Register_Y_or_N == "no"):
                        Dict_of_State_1_options["Option1"][1] = "unsuccessful" #change unattempted to unsuccessful at current index of list in the dictionary
                        Final_Statement= Final_Statement+  "Attacker attempted to register with Public Wi-Fi and failed (State 1 -> State 3 fail). "
                        response2 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                        if (response2 == "yes"):
                            Confidentiality_Attack_State1() #if they want to retry, rerun function

                        elif (response2 == "no"):
                            print("\n"+Final_Statement+Failure) #State 1 to Fail

                        else:
                            
                            input("\nPlease enter only the provided options. Press Enter to continue...")
                            Confidentiality_Attack_State1() #reruns function if what was inputted was not an answer choice
                            
                    else:
                        Dict_of_State_1_options["Option1"][0] = "unattempted" #if user fails to give an appropriate response to the question, change attempted to unattempt at current index of list in the dictionary to prevent a situation where we can't adavnce/fail
                        input("\nPlease enter only the provided options. Press Enter to continue...")
                        Confidentiality_Attack_State1()
                    

                

            elif(response1 == "2"): #try to access user's phone

                if(Dict_of_State_1_options["Option2"][0] == "attempted"): #if this has been attempted already and it failed, rerun function state1 
                    
                    input("\nThis option has already been attempted and failed. Please try a new route. Press Enter to continue...")
                    Confidentiality_Attack_State1()

                else:

                

                
                    Dict_of_State_1_options["Option2"][0] = "attempted" #change unattempted to attempted at current index of list in the dictionary

                    Access_Y_or_N= input("\nDo you have access to user's phone? " + Yes_or_No + " ") #asks user how to proceed

                    if(Access_Y_or_N == "yes"):
                        Dict_of_State_1_options["Option2"][1] = "successful" #change unattempted to successful at current index of list in the dictionary
                        print("\nYou now have access to the user's phone.") #moves to state 2
                        #list_of_dictionaries.append("State_1: " + str(Dict_of_State_1_options) + " ")
                        Final_Statement= Final_Statement + "Attacker attempted to gain access to user's phone and succeeded (State 1 -> State 2 success). "
                        list_of_dictionaries.append("State_1")
                        Confidentiality_Attack_State2()
                        

                    elif(Access_Y_or_N == "no"):
                        Dict_of_State_1_options["Option2"][1] = "unsuccessful" #change unattempted to unsuccessful at current index of list in the dictionary
                        Final_Statement= Final_Statement + "Attacker attempted to gain access to user's phone and failed (State 1 -> State 2 fail). "
                        response3 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                        if (response3 == "yes"):
                            Confidentiality_Attack_State1() #if they want to retry, rerun function

                        elif (response3 == "no"):
                            print("\n"+Final_Statement+Failure) #State 1 to Fail

                        else:
                            
                            input("\nPlease enter only the provided options. Press Enter to continue...")
                            Confidentiality_Attack_State1() #reruns function if what was inputted was not an answer choice


                    else:
                        Dict_of_State_1_options["Option2"][0] = "unattempted"
                        input("\nPlease enter only the provided options. Press Enter to continue...")
                        Confidentiality_Attack_State1() #if user fails to give an appropriate response to the question, change attempted to unattempt at current index of list in the dictionary to prevent a situation where we can't adavnce/fail         

            else:

                input("\nPlease enter only the provided options. Press Enter to continue...")
                Confidentiality_Attack_State1() #reruns function if what was inputted was not an answer choice

        



    def Confidentiality_Attack_State2():
        #print(list_of_dictionaries)
        global Final_Statement

        if(Dict_of_State_2_options_exhausted == Dict_of_State_2_options): #if all options have failed, give failure message 
            print("\n"+Final_Statement+Failure)

        else:

            response1 = input("Would you like to attempt to register to the Public Wi-Fi, attempt to register to the Dongle/portable router, or attempt to connect directly to the IoT App? Enter '1' to attempt to register to the Public Wi-Fi, enter '2' to attempt to register to Dongle/portable router, or enter '3' to attempt to connect directly to the IoT App. ")  


            if(response1 == "1"):
                if(Dict_of_State_2_options["Option1"][0] == "attempted"):# if this has been attempted already and it failed, rerun state2 function 
                    
                    input("\nThis option has already been attempted and failed. Please try a new route. Press Enter to continue...")
                    Confidentiality_Attack_State2()

                else:
                    
                    Dict_of_State_2_options["Option1"][0] = "attempted" #change unattempted to attempted at current index of list in the dictionary
                    Register_Y_or_N= input("\nCan you register on the Public Wi-fi? " + Yes_or_No + " ") #asks user how to proceed

                    if(Register_Y_or_N == "yes"):
                        
                        Dict_of_State_2_options["Option1"][1] = "successful" #change unattempted to successful at current index of list in the dictionary
                        #list_of_dictionaries.append("State_2: " + str(Dict_of_State_2_options) + " ")
                        list_of_dictionaries.append("State_2")
                        Final_Statement= Final_Statement + "Attacker attempted to register with Public Wi-Fi and succeeded (State 2 -> State 3 success). "
                        print("\nYou are now registered with the Public Wi-Fi.") #moves to state 3
                        Confidentiality_Attack_State3()
                    

                    elif(Register_Y_or_N == "no"):
                        Dict_of_State_2_options["Option1"][1] = "unsuccessful" #change unattempted to unsuccessful at current index of list in the dictionary
                        Final_Statement= Final_Statement + "Attacker attempted to register with Public Wi-Fi and failed (State 2 -> State 3 fail). "
                        response2 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                        if (response2 == "yes"):
                            Confidentiality_Attack_State2() #if they want to retry, rerun function

                        elif (response2 == "no"):
                            print("\n"+Final_Statement+Failure) #State 2 to Fail

                        else:
                            
                            input("\nPlease enter only the provided options. Press Enter to continue...")
                            Confidentiality_Attack_State2() #reruns function if what was inputted was not an answer choice
                            
                    else:
                        Dict_of_State_2_options["Option1"][0] = "unattempted" #if user fails to give an appropriate response to the question, change attempted to unattempt at current index of list in the dictionary to prevent a situation where we can't adavnce/fail
                        input("\nPlease enter only the provided options. Press Enter to continue...")
                        Confidentiality_Attack_State2()

                

                


            elif(response1 == "2"):
                if(Dict_of_State_2_options["Option2"][0] == "attempted"):# if this has been attempted already and it failed, rerun state2 function 
                    
                    input("\nThis option has already been attempted and failed. Please try a new route. Press Enter to continue...")
                    Confidentiality_Attack_State2()

                else:
                    
                    Dict_of_State_2_options["Option2"][0] = "attempted" #change unattempted to attempted at current index of list in the dictionary
                    Register_Y_or_N= input("\nCan you register to the Dongle/portable router? " + Yes_or_No + " ") #asks user how to proceed

                    if(Register_Y_or_N == "yes"):
                        Dict_of_State_2_options["Option2"][1] = "successful" #change unattempted to successful at current index of list in the dictionary
                        list_of_dictionaries.append("State_2")
                        #list_of_dictionaries.append("State_2: " + str(Dict_of_State_2_options) + " ")
                        Final_Statement= Final_Statement + "Attacker attempted to register with the Dongle/portable router and succeeded (State 2 -> State 4 success). "
                        print("\nYou are now registered with the Dongle/portable router.") #moves to state 4
                        Confidentiality_Attack_State4()
                    

                    elif(Register_Y_or_N == "no"):
                        Dict_of_State_2_options["Option2"][1] = "unsuccessful" #change unattempted to unsuccessful at current index of list in the dictionary
                        Final_Statement= Final_Statement + "Attacker attempted to register with the Dongle/portable router and failed (State 2 -> State 4 fail). "
                        response3 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                        if (response3 == "yes"):
                            Confidentiality_Attack_State2() #if they want to retry, rerun function

                        elif (response3 == "no"):
                            print("\n"+Final_Statement+Failure) #State 2 to Fail

                        else:
                            
                            input("\nPlease enter only the provided options. Press Enter to continue...")
                            Confidentiality_Attack_State2() #reruns function if what was inputted was not an answer choice
                            
                    else:
                        Dict_of_State_2_options["Option2"][0] = "unattempted" #if user fails to give an appropriate response to the question, change attempted to unattempt at current index of list in the dictionary to prevent a situation where we can't adavnce/fail
                        input("\nPlease enter only the provided options. Press Enter to continue...")
                        Confidentiality_Attack_State2()


            elif(response1 == "3"):
                if(Dict_of_State_2_options["Option3"][0] == "attempted"):# if this has been attempted already and it failed, rerun state2 function 
                    
                    input("\nThis option has already been attempted and failed. Please try a new route. Press Enter to continue...")
                    Confidentiality_Attack_State2()

                else:
                    
                    Dict_of_State_2_options["Option3"][0] = "attempted" #change unattempted to attempted at current index of list in the dictionary
                    Register_Y_or_N= input("\nCan you connect to the IoT App? " + Yes_or_No + " ") #asks user how to proceed

                    if(Register_Y_or_N == "yes"):
                        Dict_of_State_2_options["Option3"][1] = "successful" #change unattempted to successful at current index of list in the dictionary
                        list_of_dictionaries.append("State_2")
                        Final_Statement= Final_Statement + "Attacker attempted to connect to the IoT App and succeeded (State 2 -> State 5 success). "
                        #list_of_dictionaries.append("State_2: " + str(Dict_of_State_2_options) + " ")
                        print("\nYou are now connected to the IoT App.") #moves to state 5
                        Confidentiality_Attack_State5()
                    

                    elif(Register_Y_or_N == "no"):
                        Dict_of_State_2_options["Option3"][1] = "unsuccessful" #change unattempted to unsuccessful at current index of list in the dictionary
                        Final_Statement= Final_Statement + "Attacker attempted to connect to the IoT App and failed (State 2 -> State 5 fail) ." 
                        response4 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                        if (response4 == "yes"):
                            Confidentiality_Attack_State2() #if they want to retry, rerun function

                        elif (response4 == "no"):
                            print("\n"+ Final_Statement + Failure) #State 2 to Fail

                        else:
                            
                            input("\nPlease enter only the provided options. Press Enter to continue...")
                            Confidentiality_Attack_State2() #reruns function if what was inputted was not an answer choice
                            
                    else:
                        Dict_of_State_2_options["Option3"][0] = "unattempted" #if user fails to give an appropriate response to the question, change attempted to unattempt at current index of list in the dictionary to prevent a situation where we can't adavnce/fail
                        input("\nPlease enter only the provided options. Press Enter to continue...")
                        Confidentiality_Attack_State2()


            else:
                input("\nPlease enter only the provided options. Press Enter to continue...")
                Confidentiality_Attack_State2() #reruns function if what was inputted was not an answer choice

            
    def Confidentiality_Attack_State3():
        global Final_Statement
        response1 = input("Would you like to attempt to connect directly to the IoT App? " + Yes_or_No + " ")

        if (response1 == "yes"):
            Dict_of_State_3_options["Option1"][0] = "attempted"
            Dict_of_State_3_options["Option1"][1] = "successful"
            list_of_dictionaries.append("State_3")
            #list_of_dictionaries.append("State_3: " + str(Dict_of_State_3_options) + " ")
            Final_Statement= Final_Statement + "Attacker attempted to connect to the IoT App and succeeded (State 3 -> State 5 success). "
            print("\nYou are now connected to the IoT App.") #moves to state 5
            Confidentiality_Attack_State5()

        elif (response1 == "no"):
            Dict_of_State_3_options["Option1"][0] = "attempted"
            Dict_of_State_3_options["Option1"][1] = "unsuccessful"
            Final_Statement= Final_Statement + "Attacker attempted to connect to the IoT App and failed (State 3 -> State 5 fail) ." 
            print("\n"+Final_Statement + Failure) #State 3 to Fail

        else:
            input("\nPlease enter only the provided options. Press Enter to continue...")
            Confidentiality_Attack_State3() #reruns function if what was inputted was not an answer choice

            
    def Confidentiality_Attack_State4():
        global Final_Statement
        response1 = input("Would you like to attempt to connect directly to the IoT App? " + Yes_or_No + " ")

        if (response1 == "yes"):
            Dict_of_State_4_options["Option1"][0] = "attempted"
            Dict_of_State_4_options["Option1"][1] = "successful"
            #list_of_dictionaries.append("State_4: " + str(Dict_of_State_4_options) + " ")
            list_of_dictionaries.append("State_4")
            Final_Statement= Final_Statement + "Attacker attempted to connect to the IoT App and succeeded (State 4 -> State 5 success). "
            print("\nYou are now connected to the IoT App.") #moves to state 5
            Confidentiality_Attack_State5()

        elif (response1 == "no"):
            Dict_of_State_4_options["Option1"][0] = "attempted"
            Dict_of_State_4_options["Option1"][1] = "unsuccessful"
            Final_Statement= Final_Statement + "Attacker attempted to connect to the IoT App and failed (State 4 -> State 5 fail) ." 
            print("\n"+Final_Statement+Failure) #State 4 to Fail

        else:
            input("\nPlease enter only the provided options. Press Enter to continue...")
            Confidentiality_Attack_State4() #reruns function if what was inputted was not an answer choice 
            
            
            



    def Confidentiality_Attack_State5():
        global Final_Statement
        response1 = input("Are you able to get service access to the web services? " + Yes_or_No + " ")
        
        if (response1 == "yes"):
            Dict_of_State_5_options["Option1"][0] = "attempted"
            Dict_of_State_5_options["Option1"][1] = "successful"
            #list_of_dictionaries.append("State_5: " + str(Dict_of_State_5_options) + " ")
            list_of_dictionaries.append("State_5")
            Final_Statement= Final_Statement + "Attacker attempted to get service access to the web services and succeeded (State 5 -> State 6 success). "
            print("\nWeb services access gained.") #moves to state 6
            Confidentiality_Attack_State6()

        elif (response1 == "no"):
            Dict_of_State_5_options["Option1"][0] = "attempted"
            Dict_of_State_5_options["Option1"][1] = "unsuccessful"
            Final_Statement= Final_Statement + "Attacker attempted to get service access to the web services and failed (State 5 -> State 6 fail). "
            print("\n"+Final_Statement+Failure) #State 5 to Fail

        else:
            input("\nPlease enter only the provided options. Press Enter to continue...")
            Confidentiality_Attack_State5() #reruns function if what was inputted was not an answer choice


    def Confidentiality_Attack_State6():
        global Final_Statement
        response1 = input("Are you able to get router access to the home gateway router? " + Yes_or_No + " ")
        
        if (response1 == "yes"):
            Dict_of_State_6_options["Option1"][0] = "attempted"
            Dict_of_State_6_options["Option1"][1] = "successful"
            list_of_dictionaries.append("State_6")
            #list_of_dictionaries.append("State_6: " + str(Dict_of_State_6_options) + " ")
            Final_Statement= Final_Statement + "Attacker attempted to get router access to the home gateway router and succeeded (State 6 -> State 7 success). "
            print("\nHome gateway router accessed.") #moves to state 7
            Confidentiality_Attack_State7()

        elif (response1 == "no"):
            Dict_of_State_6_options["Option1"][0] = "attempted"
            Dict_of_State_6_options["Option1"][1] = "unsuccessful"
            Final_Statement= Final_Statement + "Attacker attempted to get router access to the home gateway router and failed (State 6 -> State 7 fail). "
            print("\n"+Final_Statement+Failure) #State 6 to Fail

        else:
            input("\nPlease enter only the provided options. Press Enter to continue...")
            Confidentiality_Attack_State6() #reruns function if what was inputted was not an answer choice

    def Confidentiality_Attack_State7():
        global Final_Statement
        response1 = input("Is compromsing the IoT device possible now? " + Yes_or_No + " ")
        
        if (response1 == "yes"):
            Dict_of_State_7_options["Option1"][0] = "attempted"
            Dict_of_State_7_options["Option1"][1] = "successful"
            list_of_dictionaries.append("State_7")
            #list_of_dictionaries.append("State_7: " + str(Dict_of_State_7_options) + " ")
            Final_Statement= Final_Statement + "Attacker attempted to compromsing the IoT device and succeeded. Compromise Successful. Attack Complete. (State 7 -> Success). "
            #print("\nCompromise Successful. Attack Complete") #compromise successful
            #print(list_of_dictionaries)
            Confidentiality_Attack_closing()

        elif (response1 == "no"):
            Dict_of_State_7_options["Option1"][0] = "attempted"
            Dict_of_State_7_options["Option1"][1] = "unsuccessful"
            Final_Statement= Final_Statement + "Attacker attempted to compromsing the IoT device and failed (State 7 -> Fail). "
            print("\n"+Final_Statement+Failure) #State 7 to Fail

        else:
            input("\nPlease enter only the provided options. Press Enter to continue...")
            Confidentiality_Attack_State7() #reruns function if what was inputted was not an answer choice 
        


    def Confidentiality_Attack_closing():
        global Final_Statement
        print(list_of_dictionaries)
        print("\n" + Final_Statement + "\n")

        print("Complete model of all pathways:\n")
        





        print("  A L L   P A T H S   F A I L")
        print(" - - - - - - - - - - - - - - - > FAIL       - - - - - > FAIL             COMPROMISE SUCCESSFUL  < - - - - - - ")
        print("|                                          |                                                                 |")
        print("|                                          |  A                                                              |")
        print("|                                          |  L                                                              |")
        print("|                                          |  L                                                            C |")
        print("|                                          |                                                               O |")
        print("|                                          |  P                                                            M |")
        print("|                                          |  A                                                            P |")
        print("|                                          |  T                                                            R |")
        print("|                                          |  H                                                            O |")
        print("|                                          |  S                                                            M |")
        print("|                                          |                                                               I |")
        print("|                                          |  F                                                            S |")
        print("|                                          |  A                                                            E |")
        print("|                                          |  I                                                              |")
        print("|                                          |  L                                                              |   A L L   P A T H S   F A I L")
        print("|                                          |                                                                 S7 - - - - - - - - - - - - - - - - > FAIL ")
        print("|                                          |                                                                 ^")
        print("|     R E G I S T E R                      |      C O N N E C T                                              | ")
        print("S1 - - - - - - - - - - - - - - - - - - - ->S3 - - - - - - - - - - - - -                                      | R")
        print("|                                          ^                            |                                    | E")
        print("|                                          |                            |                                    | M")
        print("|                                          |                            |                                    | O")
        print("|                                       R  |                            |                                    | T")
        print("|                                       E  |                            |                                    | E")
        print("|                                       G  |                            |                                    | ")
        print("|                                       I  |                            |                                    | A")
        print("|                                       S  |                            |                                    | C")
        print("|                                       T  |                            |                                    | C")
        print("|                                       E  |                            |                                    | E")
        print("|                                       R  |                            |                                    | S")
        print("|                                          |                            |                                    | S")
        print("|                                          |                            |                                    |")
        print("|     A C C E S S                          |      C O N N E C T         V    S E R V I C E   A C C E S S     |   A L L   P A T H S   F A I L")
        print(" - - - - - - - - - - - - - - - - - - - - > S2 - - - - - - - - - - - - > S5 - - - - - - - - - - - - - - - - > S6 - - - - - - - - - - - - - - - - > FAIL ")
        print("                                          /|                            ^\\")
        print("                                         / |  C                         | \\")
        print("                                        /  |  O                         |  \\")
        print("FAIL <- - - - - - - - - - - - - - - - -    |  N                         |   - - - - - - - - - - - - - - - - > FAIL ")
        print("          A L L   P A T H S   F A I L      |  N                         |     A L L   P A T H S   F A I L")
        print("                                           |  E                         |")
        print("                                           |  C                         |")
        print("                                           |  T                         |")
        print("                                           |                            |")
        print("                                           V      C O N N E C T         |")
        print("FAIL <- - - - - - - - - - - - - - - - - - S4 - - - - - - - - - - - - - - ")
        print("          A L L   P A T H S   F A I L")

        print()
        print("Key: S1-> Attacker, S2 -> User Phone, S3 -> Public Wi-Fi, S4 -> Dongle/Portable Router, S5 -> Iot App, S6 -> Web Services, S7 -> Home Gateway Router")
        print("FAIL -> Attemped attack failed, Compromise Successful -> IoT Device was successfully compromised")    


        

    Confidentiality_Attack_State1()
    
