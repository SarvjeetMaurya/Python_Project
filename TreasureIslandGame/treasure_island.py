print(""" __      __       .__                               
/  \    /  \ ____ |  |   ____  ____   _____   ____  
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \ 
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ 
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >
       \/       \/          \/            \/     \/ 
""")
print("""                  __          
                 /  |_  ____  
                \   __\/  _ \ 
                 |  | (  <_> )
                 |__|  \____/ 
                              """)
print(""" _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_| """)

print("Your mission to find the treasutre....\n")
start = input("Do you want the play the game? 'Y' or 'N' \n")
if start == "y" or start=="Y":
    print (" All the best Dear!")
    side=input("Where are you want to go?(left or right) 'L' or 'R'\n ")
    if side == "l" or side == "L":
        print("Okey..")
        swim_wait=input("Swim or Wait 'S' or 'W'?\n")
        if swim_wait == "W" or swim_wait=="w":
            print("Okey..")
            door=input("Which door you want to open? red: 'R',blue:'B' or Yellow:'Y'\n ")
            if door=="r" or door=="R":
                print("Sorry, you miss the treasure ")
                print("Game over....")
            elif door=="Y" or door=="y":
                print("You are almost near to the treasure..")
                tranvel= input("Ship:'S' or Boat:'B'")
                if tranvel =="s" or tranvel=="S":
                    print("Sorry, you miss the treasure ")
                    print("Game over....")
                elif tranvel== "b" or tranvel=="B":
                    print("Hurry, You won the Game...")
                    print(""" _______________
|@@@@|     |####|
|@@@@|     |####|
|@@@@|     |####|
\@@@@|     |####/
 \@@@|     |###/
  `@@|_____|##'
       (O)
    .-'''''-.
  .'  * * *  `.
 :  *       *  :.
: ~ TREASURE  ~ :
: ~ A W A R D ~ :
 :  *       *  :
  `.  * * *  .'
    `-.....-'""")
                else:
                    print(f"{tranvel} is an invailed input.")
            elif door=="b" or door=="B":
                 print("Sorry, you miss the tresure\n")
                 print("Game over....")
            else:
                print(f"{door}")
        elif swim_wait=="s" or swim_wait=="S":
            print("Sorry, you miss the treasure\n")
            print("Game over....")
        else:
            print(f"{swim_wait} is an invailed input.")
    elif side == "r" or side == "R":
        print("Sorry, you miss the treasure ")
        print("Game over....")
    else:
        print(f"{side} is an invailed input.")
elif start == "n" or start == "N":
    print("Thank you so much.\n")
else:
    print(f"{start},is an invailed input.")