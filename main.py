#MAIN PROGRAM / FUNCTION CALLER
#PLEASE VIEW README FILE FOR FURTHER CLARIFICATION,
#BUT FOR STANDARD PROCEDURE SIMPLY RUN THIS FILE
#BY ITSELF WITH NO ADDITIONAL ARGUMENTS AT CALL

#Primary code and logic of this file by Dustin Smith,
#additional bug fixes and corrections by Garrett Miculek

#Import attacks from other files
import Authentication_Attack, Access_Attack, Confidentiality_Attack

#main function for possible reruns
def main():
    #Get user selection
    print("\n#####################\n\
            \r# BEGINNING PROGRAM #\n\
            \r#####################\n")
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
        print("\n###################################\n\
              \r# BEGINNING ACCESS CONTROL ATTACK #\n\
              \r###################################\n")
        Access_Attack.Access_Attack_State1()
        print("\n################################\n\
              \r# ENDING ACCESS CONTROL ATTACK #\n\
              \r################################\n")
    elif(userSelection == 2):
        print("\n###################################\n\
              \r# BEGINNING AUTHENTICATION ATTACK #\n\
              \r###################################\n")
        Authentication_Attack.Authentication_Attack_State1()
        print("\n################################\n\
              \r# ENDING AUTHENTICATION ATTACK #\n\
              \r################################\n")
    elif(userSelection == 3):
        print("\n####################################\n\
              \r# BEGINNING CONFIDENTIALITY ATTACK #\n\
              \r####################################\n")
        Confidentiality_Attack.Confidentiality_Attack_State1()
        print("\n#################################\n\
              \r# ENDING CONFIDENTIALITY ATTACK #\n\
              \r#################################\n")
    
    #queries user on if they wish to run another attack
    userExit = input("Action complete. Would you like to run another attack?\n\
                     \rEnter yes to rerun, or enter anything else to exit: ")
    userExit = userExit.lower()

    #if they wish to rerun, reset all status variables for the attacks inorder to reset the state
    if (userExit == "yes" or userExit == "y"):
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
        print("\n#####################\n\
                \r# RERUNNING PROGRAM #\n\
                \r#####################")
        main()
    else:
        print("\n###################\n\
                \r# EXITING PROGRAM #\n\
                \r###################\n")
        exit(0)

main()
