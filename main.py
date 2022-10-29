from random import randint
import os
import time

#Clear function
platform = "d"
def clear():
    if platform == "c":
        os.system('cls')
    elif platform == "u":
        os.system('clear')
    else:
        print()
        print("ERR_Invalid_Setup: Complete installation or reinstall program")
        print()

#Establish pin
try:
    pint = open("pint.txt", "rt")
    pin = pint.read()
    pint.close()
except:
    pint = open("pint.txt", "wt")
    print("Setup started!")
    pint.write(input("Please enter admin password: "))
    print("Admin password set!")
    pint.close()
    pint = open("pint.txt", "rt")
    pin = pint.read()
    pint.close()

#Admin actions menu
def adminmenu():
    password = input("Please enter dealer password ")
    clear()
    if password == pin:
        print("Password entered is valid, welcome dealer!")
        print("Option 1: Reset high score")
        print("Option 2: Reset last score")
        print("Option 3: Reset user")
        print("Option 4: Change user funds")
        print("Option 5: Change admin password")
        choice = input("Choice: ")
        if choice == "1":
            high = open("highscore.txt", "wt")
            high.write("0")
            high.close()
        elif choice == "2":
            last = open("lastwin.txt", "wt")
            last.write("0")
            last.close()
        elif choice == "3":
            username = input("Enter user's username to reset score: ")
            score = open(username + ".txt", "wt")
            score.write("0")
            score.close()
        elif choice == "4":
            username = input("Enter user's username to reset score: ")
            score = open(username + ".txt", "wt")
            newscore = input("Enter a new score for user ")
            score.write(newscore)
            score.close()
        elif choice == "5":
            print("no.")
        clear()
    else:
        print("Invalid password")

on = 1

while on == 1:
    clear()
    # Try to display scores
    try:
        high = open("highscore.txt", "rt")
        last = open("lastwin.txt", "rt")
        user = open("highuser.txt", "rt")
        count = open("count.txt", "rt")
        print("Last big win was: ", last.read())
        last.close()
        print("High score is:    ", high.read(), "by", user.read())
        high.close()
        plat = open("plat.txt", "rt")
        platform = plat.read()
        count.close
    except:
        high = open("highscore.txt", "wt")
        last = open("lastwin.txt", "wt")
        user = open("highuser.txt", "wt")
        count = open("count.txt", "wt")
        print("This machine is fresh!")
        high.write("0")
        last.write("0")
        user.write("0")
        count.write("0")
        high.close()
        last.close()
        user.close()
        count.close
        platform = input("Please Enter 'c' for CMD terminal (Windows), and use 'u' for unix terminal(MacOS or Linux) ")
        plat = open("plat.txt", "wt")
        plat.write(platform)
        plat.close()

    # Print potential wins
    print("Cost to play:      10")
    print("x x y = 10    6 6 6 = 700")
    print("x x x = 400   6 9 6 = 1000")
    print("3 4 3 = 500   7 7 7 = 2000")
    print()

    # Set username and display current funds
    username = input("Enter your username to play! ")
    clear()
    if username == "Exit":
        on = 0
        quit()
    elif username == "Admin":
        adminmenu()
    elif username == "plat" or username == "pint" or username == "lastwin" or username == "highuser" or username == "highscore":
        print("You know how this works, fuck you.")
    else:
        try:
            userscore = open(username + ".txt", "xt")
            userscore.close()
            userscore = open(username + ".txt", "wt")
            userscore.write("0")
            userscore.close()
        except:
            print("Welcome back")
        userscore = open(username + ".txt", "rt")
        balancetxt = userscore.read()
        userscore.close()
        print("You currently have", balancetxt)
        balance = int(balancetxt)


        # Verify that user has funds
        if balance < 10:
            x = 1
            while x == 1:
                print("Please pay dealer 10 token")
                pinput = (input("Please enter dealer PIN "))
                if pinput == pin:
                    balance = 10
                    x = 0
                else:
                    clear()
                    print("Try again")
            clear()
        else:
            nonsense = input("Enter 'c' to continue... ")
        clear()
        if balance >= 20:
            print("would you like to multiply bet?")
            multis = input("Enter multiplier '1' or '2' for 1x and 2x multiplier: ")
            try:
                multi = int(multis)
            except:
                print("You have not entered a digit!")
                multi = 1
            if multi == 1:
                print("10 tokens removed")
            elif multi == 2:
                print("20 tokens removed")
            else:
                "You're gonna go broke."
                multi = 2
        else:
            multi = 1
        clear()

        # Roll the "dice"
        for i in range(20):
            var1 = randint(1, 9)
            var2 = randint(1, 9)
            var3 = randint(1, 9)
            print("You roll:", var1, var2, var3)
            time.sleep(0.15)
            clear()
        print()
        var1 = randint(1, 9)
        var2 = randint(1, 9)
        var3 = randint(1, 9)
        print("You roll:", var1, var2, var3)
        payout = 0
        count = open("count.txt", "rt")
        countmsg = count.read()
        count.close()
        countint = int(countmsg)
        countint += 1
        countmsg = str(countint)
        count = open("count.txt", "wt")
        count.write(countmsg)
        count.close()




        # Assign payouts
        if var1 == 3 and var2 == 4 and var3 == 3:
            payout = 400
        elif var1 == 6 and var2 == 6 and var3 == 6:
            payout = 600
        elif var1 == 6 and var2 == 9 and var3 == 6:
            payout = 1000
        elif var1 == 7 and var2 == 7 and var3 == 7:
            payout = 2000
        elif var1 == 3 and var2 == 1 and var3 == 4:
            payout = 1000
        elif var1 == var2 == var3:
            payout = 400
        elif var1 == var2:
            payout = 20
        elif var2 == var3:
            payout = 20
        elif var1 == var3:
            payout = 10
        elif var1 == 7:
            payout = 20
        elif var2 == 7:
            payout = 20
        elif var3 == 7:
            payout = 20
        print("Your payout is:", payout)
        if multi > 1:
            print(str(multi)+"x Multiplier enabled, score doubled!")
            payout *= multi
            print("Multiplied score is", payout)

        # Set balance to user
        print("Balance was:", balance)
        newbal = balance + payout - 10*multi
        print("New balance is:", newbal)
        userscore = open(username+".txt", "wt")
        userscoremsg = str(newbal)
        userscore.write(userscoremsg)
        userscore.close()

        # Set last win
        if payout > 5:
            last = open("lastwin.txt", "wt")
            lastmsg = str(payout) + " by " + username + " " +str(multi) + "x"
            last.write(lastmsg)
            last.close()
            try:
                record = open("winrecord.txt", "at")
                record.write(lastmsg + "\n")
                record.close
            except:
                record = open("winrecord.txt", "xt")
                record.close
                record = open("winrecord.txt", "at")
                record.write(lastmsg + "\n")
                record.close

        # Set high score
        high = open("highscore.txt", "rt")
        highscore = high.read()
        high.close()
        highint = int(highscore)
        if highint < payout:
            high = open("highscore.txt", "wt")
            highmsg = str(payout)
            high.write(highmsg)
            high.close()
            user = open("highuser.txt", "wt")
            user.write(username)
            user.close

        # Clear Display for next user
        nonsense = input("Press c to continue... ")
        clear()
