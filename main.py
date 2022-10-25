from random import randint
import os
on = 1
while on == 1:

    # Try to display scores
    try:
        high = open("highscore.txt", "rt")
        last = open("lastwin.txt", "rt")
        user = open("highuser.txt", "rt")
        print("Last big win was: ", last.read())
        last.close()
        print("High score is:    ", high.read(), "by", user.read())
        high.close()
    except:
        high = open("highscore.txt", "wt")
        last = open("lastwin.txt", "wt")
        user = open("highuser.txt", "wt")
        print("This machine is fresh!")
        high.write("0")
        last.write("0")
        user.write("0")
        high.close()
        last.close()
        user.close()

    # Print potential wins
    print("Cost to play:      10")
    print("x x y = 10    6 6 6 = 700")
    print("x x x = 400   6 9 6 = 1000")
    print("3 4 3 = 500   7 7 7 = 2000")
    print()

    # Set username and display current funds
    username = input("Enter your username to play! ")
    os.system('cls')
    if username == "Exit":
        on = 0
        quit()
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
    print(balancetxt)
    userscore.close()
    print("You currently have", balancetxt)
    balance = int(balancetxt)

    # Verify that user has funds
    if balance < 10:
        x = 1
        while x == 1:
            print("Please pay dealer 10 token")
            pinput = int(input("Please enter dealer PIN "))
            if pinput == 8898:
                balance = 10
                x = 0
            else:
                print("Try again")
    else:
        nonsense = input("Enter 'c' to continue... ")
    os.system('cls')

    # Roll the "dice"
    print()
    var1 = randint(1, 9)
    var2 = randint(1, 9)
    var3 = randint(1, 9)
    print("You roll:", var1, var2, var3)
    payout = 0

    # Assign payouts
    if var1 == 3 and var2 == 4 and var3 == 3:
        payout = 400
    elif var1 == 6 and var2 == 6 and var3 == 6:
        payout = 600
    elif var1 == 6 and var2 == 9 and var3 == 6:
        payout = 1000
    elif var1 == 7 and var2 == 7 and var3 == 7:
        payout = 2000
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

    # Set balance to user
    print("Balance is:", balance)
    newbal = balance + payout - 10
    print("New balance is:", newbal)
    userscore = open(username+".txt", "wt")
    userscoremsg = str(newbal)
    userscore.write(userscoremsg)
    userscore.close()

    # Set last win
    if payout > 5:
        last = open("lastwin.txt", "wt")
        lastmsg = str(payout) + " by " + username
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
    os.system('cls')
