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
        Access_Attack.AccessAttack()
    elif(userSelection == 2):
        Authentication_Attack.AuthenticationAttack()
    elif(userSelection == 3):
        Confidentiality_Attack.ConfidentialityAttack()
    
    userExit = input("\n\nAttack complete. Would you like to run another attack?\n\
                     \rEnter y to rerun, or enter anything else to exit: ")
    if (userExit == "y"):
        print("Rerunning program...")
        main()
    else:
        print("Exiting program...")
        exit(0)

main()