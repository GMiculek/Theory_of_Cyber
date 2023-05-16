Yes_or_No = "Enter 'yes' or 'no' to proceed."
Failure = "All possible options have been exhausted. Attack has failed."

Dict_of_State_1_options = {}
Dict_of_State_1_options["Option1"] = ["unattempted"]
Dict_of_State_1_options["Option2"] = ["unattempted"] #global dictionaries to store each option at states with more than one option

Dict_of_State_1_options_exhausted = {}
Dict_of_State_1_options_exhausted["Option1"] = ["attempted"] #global dictionaries that will only be used for comparisons, if they match with the dictionaries we are actively modifying, all options have been exhausted 
Dict_of_State_1_options_exhausted["Option2"] = ["attempted"]


Final_Statement = ""

def Authentication_Attack_State1():

    global Final_Statement
   
    if(Dict_of_State_1_options_exhausted == Dict_of_State_1_options): #if all options have been attempted, give failure message 
        print("\n"+Final_Statement + Failure)
        
    else: #if options to proceed are still possible 
        print("\nYou are starting the attack.")
        response1 = input("Would you like to attempt to gain access to the Home Wi-Fi or attempt to gain access to the IoT App? Enter '1' for the former option or enter '2' for the latter option. ")
        #gives you the options on how you would like to proceed 

        if(response1 == "1"): #try to gain access to the home Wi-Fi (option 1 in this case)

            if(Dict_of_State_1_options["Option1"][0] == "attempted"):# if this has been attempted already and it failed, rerun function state1 
                
                input("\nThis option has already been attempted and failed. Please try a new route. Press Enter to continue...")
                Authentication_Attack_State1()

            else:
                
                Dict_of_State_1_options["Option1"][0] = "attempted" #change unattempted to attempted 
                Register_Y_or_N= input("\nDid the attacker succeed in gaining access to the Home Wi-Fi (via login attempts)? " + Yes_or_No + " ") #asks user how to proceed

                if(Register_Y_or_N == "yes" or Register_Y_or_N == "y" or Register_Y_or_N == "Yes" or Register_Y_or_N == "YES" or Register_Y_or_N == "Y"):
                    
                    
                    print("\nThe attacker succeeded in gaining access to the Home Wi-Fi.") #moves to state 2
                    Final_Statement= Final_Statement + "The attacker succeed in gaining access to the Home Wi-Fi (State 1 -> State 2 success). "
                    Authentication_Attack_State2()
                   

                elif(Register_Y_or_N == "no" or Register_Y_or_N == "NO" or Register_Y_or_N == "n" or Register_Y_or_N == "No" or Register_Y_or_N == "N"):
                    
                    Final_Statement= Final_Statement+  "The attacker failed in gaining access to the Home Wi-Fi (State 1 -> State 2 fail). "
                    response2 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                    if (response2 == "yes" or response2 == "y" or response2 == "Yes" or response2 == "YES" or response2 == "Y"):
                        Authentication_Attack_State1() #if they want to retry, rerun function

                    elif (response2 == "no" or response2 == "NO" or response2 == "n" or response2 == "No" or response2 == "N"):
                        print("\nBreak down of path taken: \n")
                        print("\n"+Final_Statement+Failure) #State 1 to Fail

                    else:
                        
                        input("\nPlease enter only the provided options. Press Enter to continue...")
                        Authentication_Attack_State1() #reruns function if what was inputted was not an answer choice
                        
                else:
                    Dict_of_State_1_options["Option1"][0] = "unattempted" #if user fails to give an appropriate response to the question, change attempted back to unattempt at current index of list in the dictionary to prevent a situation where we can't adavnce/fail
                    input("\nPlease enter only the provided options. Press Enter to continue...")
                    Authentication_Attack_State1()
                

            
        elif(response1 == "2"): #try to gain access to the IoT  App

            if(Dict_of_State_1_options["Option2"][0] == "attempted"): #if this has been attempted already and it failed, rerun function state1 
                
                input("\nThis option has already been attempted and failed. Please try a new route. Press Enter to continue...")
                Authentication_Attack_State1()

            else:

            
                Dict_of_State_1_options["Option2"][0] = "attempted" #change unattempted to attempted at current index of list in the dictionary

                Access_Y_or_N= input("\nDid the attacker succeed in gaining access to the IoT application (via login attempts)? " + Yes_or_No + " ") #asks user how to proceed

                if(Access_Y_or_N == "yes" or Access_Y_or_N == "y" or Access_Y_or_N == "Yes" or Access_Y_or_N == "YES" or Access_Y_or_N == "Y"):
                    
                    print("\nYou have gained access to the IoT App.") #moves to state 3
                    
                    Final_Statement= Final_Statement + "The attacker succeeded in gaining access to the IoT App (State 1 -> State 3 success). "
                    
                    print("The attacker succeeded in gaining access to the IoT App")
                    Authentication_Attack_State3()
                    

                elif(Access_Y_or_N == "no" or Access_Y_or_N == "NO" or Access_Y_or_N == "n" or Access_Y_or_N == "No" or Access_Y_or_N == "N"):
                   
                    Final_Statement= Final_Statement + "The attacker failed in gaining access to the IoT App (State 1 -> State 3 fail). "
                    response3 = input("\nFailure of current action. Would you like to retry other options? " + Yes_or_No + " ") #asks if user would like to try a different option 

                    if (response3 == "yes" or response3 == "y" or response3 == "Yes" or response3 == "YES" or response3 == "Y"):
                        Authentication_Attack_State1() #if they want to retry, rerun function

                    elif (response3 == "no" or response3 == "NO" or response3 == "n" or response3 == "No" or response3 == "N"):
                        print("\nBreak down of path taken: \n")
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
    response1 = input("Is the attacker able to compromise the home network? " + Yes_or_No + " ")

    if (response1 == "yes" or response1 == "y" or response1 == "Yes" or response1 == "YES" or response1 == "Y"):
        
       
        Final_Statement= Final_Statement + "The attacker succeeded in compromising the home network. Compromise Successful. Attack Complete. (State 2 -> Success). "
        print("The attacker succeeded in compromising the home network.")
        Authentication_Attack_closing() #compromise successful, move to closing function

    elif (response1 == "no" or response1 == "NO" or response1 == "n" or response1 == "No" or response1 == "N"):
        
        Final_Statement= Final_Statement + "The attacker failed in compromising the home network (State 2 -> Fail). " 
        print("\nBreak down of path taken: \n")
        print("\n"+Final_Statement + Failure) #State 2 to Fail

    else:
        input("\nPlease enter only the provided options. Press Enter to continue...")
        Authentication_Attack_State2() #reruns function if what was inputted was not an answer choice


        
def Authentication_Attack_State3():
    global Final_Statement
    
    response1 = input("Did the attacker succeed in gaining service access to the web services from the IoT application (via hacked authentication credentials)? " + Yes_or_No + " ")

    if (response1 == "yes" or response1 == "y" or response1 == "Yes" or response1 == "YES" or response1 == "Y"):
        
       
        Final_Statement= Final_Statement + "The attacker succeed in gaining service access to the web services from the IoT App (State 3 -> State 4 success). "
        print("\nThe attacker succeed in gaining service access to the web services from the IoT App.") #state 3 to state 4
        Authentication_Attack_State4()

    elif (response1 == "no" or response1 == "NO" or response1 == "n" or response1 == "No" or response1 == "N"):
        
        Final_Statement= Final_Statement + "The attacker failed in gaining service access to the web services from the IoT App (State 3 -> State 4 fail). " 
        print("\nBreak down of path taken: \n")
        print("\n"+Final_Statement + Failure) #State 3 to Fail

    else:
        input("\nPlease enter only the provided options. Press Enter to continue...")
        Authentication_Attack_State3() #reruns function if what was inputted was not an answer choice

        
def Authentication_Attack_State4():
    global Final_Statement
    response1 = input("Did the attacker succeed in gaining router access to the home gateway router (via script and/or command injection)? " + Yes_or_No + " ")

    if (response1 == "yes" or response1 == "y" or response1 == "Yes" or response1 == "YES" or response1 == "Y"):

        Final_Statement= Final_Statement + "The attacker succeed in gaining router access to the home gateway router (State 4 -> State 5 success). "
        print("\nYou now have access to the home gateway router.") #state 4 to 5
        Authentication_Attack_State5()

    elif (response1 == "no" or response1 == "NO" or response1 == "n" or response1 == "No" or response1 == "N"):
       
        Final_Statement= Final_Statement + "The attacker failed in gaining router access to the home gateway router (State 4 -> State 5 fail). " 
        print("\nBreak down of path taken: \n")
        print("\n"+Final_Statement+Failure) #State 4 to Fail

    else:
        input("\nPlease enter only the provided options. Press Enter to continue...")
        Authentication_Attack_State4() #reruns function if what was inputted was not an answer choice 
        
        
def Authentication_Attack_State5():
    global Final_Statement
    response1 = input("Did the attacker succeed in compromsing the IoT device (via the privileges gained from home gateway router access)? " + Yes_or_No + " ")
    
    if (response1 == "yes" or response1 == "y" or response1 == "Yes" or response1 == "YES" or response1 == "Y"):
        
        
        Final_Statement= Final_Statement + "Attacker attempted to compromise the IoT device and succeeded. Compromise Successful. Attack Complete. (State 5 -> Success). "
        Authentication_Attack_closing() #compromise successful, move to closing function

    elif (response1 == "no" or response1 == "NO" or response1 == "n" or response1 == "No" or response1 == "N"):
        
        Final_Statement= Final_Statement + "Attacker attempted to compromise the IoT device and failed (State 5 -> Fail). "
        print("\nBreak down of path taken: \n")
        print("\n"+Final_Statement+Failure) #State 5 to Fail

    else:
        input("\nPlease enter only the provided options. Press Enter to continue...")
        Authentication_Attack_State5() #reruns function if what was inputted was not an answer choice 


def Authentication_Attack_closing():
    global Final_Statement
    print("\nBreak down of path taken: \n")
    print("\n" + Final_Statement + "\n")






