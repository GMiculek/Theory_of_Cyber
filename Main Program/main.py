#Import attacks from other files
import Authentication_Attack, Access_Attack, Confidentiality_Attack

#main function for possible reruns
def main():
    #Get user selection
    userSelection = input("Please select an attack to perform. Options are:\n\
    \r\t1:\tAccess Attack\n\
    \r\t2:\tAuthentication Attack\n\
    \r\t3:\tConfidentiality Attack\n\
    \rAttack Selection: ")
    #input validation loop
    while(1):
        try:
            userSelection = int(userSelection)
            if userSelection in [1,2,3]:
                break
            else:
                print("Invalid option selected! Please select an existing attack.")
                userSelection = input("Please select an attack to perform. Options are:\n\
                \r\t1:\tAccess Attack\n\
                \r\t2:\tAuthentication Attack\n\
                \r\t3:\tConfidentiality Attack\n\
                \rAttack Selection: ")
        except Exception:
            print("Invalid input entered! Please use a number to select your attack.")
            userSelection = input("Please select an attack to perform. Options are:\n\
            \r\t1:\tAccess Attack\n\
            \r\t2:\tAuthentication Attack\n\
            \r\t3:\tConfidentiality Attack\n\
            \rAttack Selection: ")

    #attack selection
    if(userSelection == 1):
        Access_Attack.Access_Attack_State1()
    elif(userSelection == 2):
        Authentication_Attack.Authentication_Attack_State1()
    elif(userSelection == 3):
        Confidentiality_Attack.Confidentiality_Attack_State1()
    
    userExit = input("\n\nAction complete. Would you like to run another attack?\n\
                     \rEnter y to rerun, or enter anything else to exit: ")
    if (userExit == "yes" or userExit == "y" or userExit == "Yes" or userExit == "YES" or userExit == "Y"):
        Access_Attack.Dict_of_State_1_options["Option1"] = ["unattempted"]
        Access_Attack.Dict_of_State_1_options["Option2"] = ["unattempted"] 
        Access_Attack.Dict_of_State_1_options["Option3"] = ["unattempted"]
        Access_Attack.Dict_of_State_2_options["Option1"] = ["unattempted"]
        Access_Attack.Dict_of_State_2_options["Option2"] = ["unattempted"]
        Authentication_Attack.Dict_of_State_1_options["Option1"] = ["unattempted"]
        Authentication_Attack.Dict_of_State_1_options["Option2"] = ["unattempted"]
        Confidentiality_Attack.Dict_of_State_1_options["Option1"] = ["unattempted"]
        Confidentiality_Attack.Dict_of_State_1_options["Option2"] = ["unattempted"]
        Confidentiality_Attack.Dict_of_State_2_options["Option1"] = ["unattempted"]
        Confidentiality_Attack.Dict_of_State_2_options["Option2"] = ["unattempted"]
        Confidentiality_Attack.Dict_of_State_2_options["Option3"] = ["unattempted"]
        Access_Attack.Final_Statement = ""
        Authentication_Attack.Final_Statement = ""
        Confidentiality_Attack.Final_Statement = ""
        print("Rerunning program...")
        main()
    else:
        print("Exiting program...")
        exit(0)

main()
