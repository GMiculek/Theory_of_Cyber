#FUNCTIONS WHICH PERFORM FSA OF ACCESS CONTROL ATTACK
#PLEASE VIEW README FILE FOR FURTHER CLARIFICATION

#Primary code and logic of this file by Garrett Miculek,
#additional bug fixes and corrections by Dustin Smith


Yes_or_No = "Enter 'yes' or 'no' to proceed."
Failure = "All possible options have been exhausted. Attack has failed."


Dict_of_State_1_options = {}
Dict_of_State_1_options["Option1"] = ["unattempted"]
Dict_of_State_1_options["Option2"] = ["unattempted"] #global dictionaries to store each option at states with more than one option
Dict_of_State_1_options["Option3"] = ["unattempted"]

Dict_of_State_1_options_exhausted = {}
Dict_of_State_1_options_exhausted["Option1"] = ["attempted"] #global dictionaries that will only be used for comparisons, if they match with the dictionaries we are actively modifying, all options have been exhausted 
Dict_of_State_1_options_exhausted["Option2"] = ["attempted"]
Dict_of_State_1_options_exhausted["Option3"] = ["attempted"]


Dict_of_State_2_options = {}
Dict_of_State_2_options["Option1"] = ["unattempted"]
Dict_of_State_2_options["Option2"] = ["unattempted"]


Dict_of_State_2_options_exhausted = {}
Dict_of_State_2_options_exhausted["Option1"] = ["attempted"]
Dict_of_State_2_options_exhausted["Option2"] = ["attempted"]


Final_Statement = ""

def Access_Attack_State1():

    global Final_Statement
    #State 1

    if(Dict_of_State_1_options_exhausted == Dict_of_State_1_options): #if all options have failed, give failure message 
        print("\n"+Final_Statement + Failure)
        

    else: #if options to proceed are still possible 
        print("\nYou are starting the attack.")
        response1 = input("Would you like to attempt to connect to the Home Wi-Fi, attempt to gain access to the user's phone, or attempt to compromise the IoT device directly? Enter '1' for the first option, enter '2' for the second option, or enter '3' for the third option. ")
        #gives you the options on how you would like to proceed 

        if(response1 == "1"): #try to connect to the home wi-fi (option 1 in this case)

            if(Dict_of_State_1_options["Option1"][0] == "attempted"):# if this has been attempted already and it failed, rerun function state1 
                
                input("\nThis option has already been attempted and failed. Please try a new route. Press Enter to continue...")
                Access_Attack_State1()

            else:
                
                Dict_of_State_1_options["Option1"][0] = "attempted" #change unattempted to attempted at current index of list in the dictionary
                Register_Y_or_N= input("\nDid the attacker succeed in connecting to the Home Wi-Fi? " + Yes_or_No + " ") #asks user how to proceed

                if(Register_Y_or_N == "yes" or Register_Y_or_N == "y" or Register_Y_or_N == "Yes" or Register_Y_or_N == "YES" or Register_Y_or_N == "Y"):
                    
                    
                    print("\nThe attacker succeeded in connecting to the Home Wi-Fi.") #moves to state 3
                    Final_Statement= Final_Statement + "The attacker succeeded in connecting to the Home Wi-Fi (State 1 -> State 3 success). "
                    Access_Attack_State3()
                   

                elif(Register_Y_or_N == "no" or Register_Y_or_N == "NO" or Register_Y_or_N == "n" or Register_Y_or_N == "No" or Register_Y_or_N == "N"):
                    
                    Final_Statement= Final_Statement+  "The attacker failed in connecting to the Home Wi-Fi (State 1 -> State 3 fail). "
                    response2 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                    if (response2 == "yes" or response2 == "y" or response2 == "Yes" or response2 == "YES" or response2 == "Y"):
                        Access_Attack_State1() #if they want to retry, rerun function

                    elif (response2 == "no" or response2 == "NO" or response2 == "n" or response2 == "No" or response2 == "N"):
                        print("\nBreak down of path taken: \n")
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

                Access_Y_or_N= input("\nDid the attacker succeed in gaining access to a user's phone (via malware or a phishing attempt)? " + Yes_or_No + " ") #asks user how to proceed

                if(Access_Y_or_N == "yes" or Access_Y_or_N == "y" or Access_Y_or_N == "Yes" or Access_Y_or_N == "YES" or Access_Y_or_N == "Y"):
                    
                    print("\nThe attacker attempted to gain access to a user's phone and succeeded.") #moves to state 2
                    
                    Final_Statement= Final_Statement + "The attacker attempted to gain access to a user's phone and succeeded (State 1 -> State 2 success). "
                   
                    Access_Attack_State2()
                    

                elif(Access_Y_or_N == "no" or Access_Y_or_N == "NO" or Access_Y_or_N == "n" or Access_Y_or_N == "No" or Access_Y_or_N == "N"):
                    
                    Final_Statement= Final_Statement + "The attacker attempted to gain access to a user's phone and failed (State 1 -> State 2 fail). "
                    response3 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                    if (response3 == "yes" or response3 == "y" or response3 == "Yes" or response3 == "YES" or response3 == "Y"):
                        Access_Attack_State1() #if they want to retry, rerun function

                    elif (response3 == "no" or response3 == "NO" or response3 == "n" or response3 == "No" or response3 == "N"):
                        print("\nBreak down of path taken: \n")
                        print("\n"+Final_Statement+Failure) #State 1 to Fail

                    else:
                        
                        input("\nPlease enter only the provided options. Press Enter to continue...")
                        Access_Attack_State1() #reruns function if what was inputted was not an answer choice


                else:
                    Dict_of_State_1_options["Option2"][0] = "unattempted"
                    input("\nPlease enter only the provided options. Press Enter to continue...")
                    Access_Attack_State1() #if user fails to give an appropriate response to the question, change attempted to unattempt at current index of list in the dictionary to prevent a situation where we can't adavnce/fail         



        elif(response1 == "3"): #try to compromise the IoT device

            if(Dict_of_State_1_options["Option3"][0] == "attempted"): #if this has been attempted already and it failed, rerun function state1 
                
                input("\nThis option has already been attempted and failed. Please try a new route. Press Enter to continue...")
                Access_Attack_State1()

            else:

            
                Dict_of_State_1_options["Option3"][0] = "attempted" #change unattempted to attempted at current index of list in the dictionary

                Access_Y_or_N= input("\nDid the attacker succeed in compromising the IoT device directly? " + Yes_or_No + " ") #asks user how to proceed

                if(Access_Y_or_N == "yes" or Access_Y_or_N == "y" or Access_Y_or_N == "Yes" or Access_Y_or_N == "YES" or Access_Y_or_N == "Y"):
                   
                    print("\nThe attacker succeeded in compromising the IoT device directly.") #moves to SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4)
                    
                    Final_Statement= Final_Statement + "The attacker succeeded in compromising the IoT device directly (State 1 -> SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4) success). "
                    
                    SUCCESSFULLY_COMPROMISED_IoT_DEVICE()
                    

                elif(Access_Y_or_N == "no" or Access_Y_or_N == "NO" or Access_Y_or_N == "n" or Access_Y_or_N == "No" or Access_Y_or_N == "N"):
                    
                    Final_Statement= Final_Statement + "The attacker failed in compromising the IoT device directly (State 1 -> SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4) fail). "
                    response3 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                    if (response3 == "yes" or response3 == "y" or response3 == "Yes" or response3 == "YES" or response3 == "Y"):
                        Access_Attack_State1() #if they want to retry, rerun function

                    elif (response3 == "no" or response3 == "NO" or response3 == "n" or response3 == "No" or response3 == "N"):
                        print("\nBreak down of path taken: \n")
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
    
    global Final_Statement

    if(Dict_of_State_2_options_exhausted == Dict_of_State_2_options): #if all options have failed, give failure message 
        print("\n"+Final_Statement+Failure)

    else:

        response1 = input("Would you like to attempt to connect to the Home Wi-Fi or attempt to compromise the IoT device? Enter '1' for the former option, or enter '2' for the latter option. ")  


        if(response1 == "1"): #attempt to connect to the home wifi
            if(Dict_of_State_2_options["Option1"][0] == "attempted"):# if this has been attempted already and it failed, rerun state2 function 
                
                input("\nThis option has already been attempted and failed. Please try a new route. Press Enter to continue...")
                Access_Attack_State2()

            else:
                
                Dict_of_State_2_options["Option1"][0] = "attempted" #change unattempted to attempted at current index of list in the dictionary
                Register_Y_or_N= input("\nDid the attacker succeed in connecting to the Home Wi-Fi? " + Yes_or_No + " ") #asks user how to proceed

                if(Register_Y_or_N == "yes" or Register_Y_or_N == "y" or Register_Y_or_N == "Yes" or Register_Y_or_N == "YES" or Register_Y_or_N == "Y"):
                    
                   
                  
                    Final_Statement= Final_Statement + "The attacker succeeded in connecting to the Home Wi-Fi. (State 2 -> State 3 success). "
                    print("\nThe attacker succeeded in connecting to the Home Wi-Fi.") #moves to state 3
                    Access_Attack_State3()
                   

                elif(Register_Y_or_N == "no" or Register_Y_or_N == "NO" or Register_Y_or_N == "n" or Register_Y_or_N == "No" or Register_Y_or_N == "N"):
                    
                    Final_Statement= Final_Statement + "The attacker failed in connecting to the Home Wi-Fi (State 2 -> State 3 fail). "
                    response2 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                    if (response2 == "yes"):
                        Access_Attack_State2() #if they want to retry, rerun function

                    elif (response2 == "no"):
                        print("\nBreak down of path taken: \n")
                        print("\n"+Final_Statement+Failure) #State 2 to Fail

                    else:
                        
                        input("\nPlease enter only the provided options. Press Enter to continue...")
                        Access_Attack_State2() #reruns function if what was inputted was not an answer choice
                        
                else:
                    Dict_of_State_2_options["Option1"][0] = "unattempted" #if user fails to give an appropriate response to the question, change attempted to unattempt at current index of list in the dictionary to prevent a situation where we can't adavnce/fail
                    input("\nPlease enter only the provided options. Press Enter to continue...")
                    Access_Attack_State2()

            
        elif(response1 == "2"): #attempt to compromise the IoT device
            if(Dict_of_State_2_options["Option2"][0] == "attempted"):# if this has been attempted already and it failed, rerun state2 function 
                
                input("\nThis option has already been attempted and failed. Please try a new route. Press Enter to continue...")
                Access_Attack_State2()

            else:

                        
                Dict_of_State_2_options["Option2"][0] = "attempted" #change unattempted to attempted at current index of list in the dictionary

                Access_Y_or_N= input("\nDid the attacker succeed in compromising the IoT device from the privileges gained from the access of the user's phone? " + Yes_or_No + " ") #asks user how to proceed

                if(Access_Y_or_N == "yes" or Access_Y_or_N == "y" or Access_Y_or_N == "Yes" or Access_Y_or_N == "YES" or Access_Y_or_N == "Y"):
                    
                    print("\nThe attacker succeeded in compromising the IoT device.") #moves to SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4)
                   
                    Final_Statement= Final_Statement + "The attacker succeeded in compromising the IoT device (State 2 -> SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4) success). "
                    
                    SUCCESSFULLY_COMPROMISED_IoT_DEVICE()
                    

                elif(Access_Y_or_N == "no" or Access_Y_or_N == "NO" or Access_Y_or_N == "n" or Access_Y_or_N == "No" or Access_Y_or_N == "N"):
                    
                    Final_Statement= Final_Statement + "The attacker failed in compromising the IoT device (State 2 -> SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4) fail). "
                    response3 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                    if (response3 == "yes"):
                        Access_Attack_State2() #if they want to retry, rerun function

                    elif (response3 == "no"):
                        print("\nBreak down of path taken: \n")
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



def Access_Attack_State3():
    global Final_Statement
    response1 = input("Did the attacker succeed in compromising the IoT device from the privileges gained from the Home Wi-Fi? " + Yes_or_No + " ")
    
    if (response1 == "yes" or response1 == "y" or response1 == "Yes" or response1 == "YES" or response1 == "Y"):

        Final_Statement= Final_Statement + "The attacker succeeded in compromising the IoT device (State 3 -> SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4) success). "
        print("\nThe attacker succeeded in compromising the IoT device.") #moves to SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4)
        SUCCESSFULLY_COMPROMISED_IoT_DEVICE()

    elif (response1 == "no" or response1 == "NO" or response1 == "n" or response1 == "No" or response1 == "N"):
       
        Final_Statement= Final_Statement + "The attacker failed in compromising the IoT device (State 3 -> SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4) fail). " 
        print("\nBreak down of path taken: \n")
        print("\n"+Final_Statement+Failure) #State 3 to Fail

    else:
        input("\nPlease enter only the provided options. Press Enter to continue...")
        Access_Attack_State3() #reruns function if what was inputted was not an answer choice 


        
def SUCCESSFULLY_COMPROMISED_IoT_DEVICE():
    global Final_Statement
    response1 = input("Did the attacker succeed in compromising the Home Network from the already compromised IoT device? " + Yes_or_No + " ") #while IoT device was compromised, we can go further and see if we can compromise the home network
    
    if (response1 == "yes" or response1 == "y" or response1 == "Yes" or response1 == "YES" or response1 == "Y"):
        
        
        Final_Statement= Final_Statement + "Attacker attempted to compromse the home network and succeeded. Compromise Successful. Attack Complete. (SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4) -> SUCCESSFULLY COMPROMISED HOME NETWORK (state 5) success). "
        
        Access_Attack_closing() 

    elif (response1 == "no" or response1 == "NO" or response1 == "n" or response1 == "No" or response1 == "N"):
        
        Final_Statement= Final_Statement + "While the attacker failed to compromise the home network, the attacker was successful in compromising the IoT device. Compromise Successful. Attack Complete. (SUCCESSFULLY_COMPROMISED_IoT_DEVICE (state 4) -> SUCCESSFULLY_COMPROMISED_HOME_NETWORK (state 5) fail). "
        Access_Attack_closing()

    else:
        input("\nPlease enter only the provided options. Press Enter to continue...")
        Access_Attack_closing() #reruns function if what was inputted was not an answer choice  
        

                
        
def Access_Attack_closing():
    global Final_Statement
    print("\nBreak down of path taken: \n")
    print("\n" + Final_Statement + "\n")



