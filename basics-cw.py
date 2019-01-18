def main():
    problem1()
    problem2()
    problem3()
    problem4()



#Create a function with two variables.
# One should equal “My name is: “
# and the other should equal your actual name.
# Print the two variables in one print message.


def problem1():
    myName = ("My name is: ")
    realName = ("Chelsea")
    print(myName + realName)





#Create a function to ask the user to enter the extra credit they earned.
# If they entered less than 5 print “That’s not enough extra credit.”
# If they entered more than 20 print “That’s too much extra credit”.


def problem2():
    extraCred = int(input("Enter your extra credt:"))
    if(extraCred < 5):
        print("That's not enough extra credt.")
    elif(extraCred > 20):
        print("That's too much extra credit.")
    else:
        print("Great Job!")





#Create a function to ask a user to enter a password.
# Enter a password. Ask user to reenter password.
# Check to see if they are correct.


def problem3():
    passWord = input("Enter a password:")
    passWord2 = input("Reenter password:")
    if (passWord == passWord2):
        print("Password is set")
    else:
        print("Passwords do not match")






#Create a function to ask for two card numbers.
# If it equals 21 print BLACKJACK!,
# if it’s greater than 21 print BUST!,
# if it’s less than 21 print “The total is [THE TOTAL]”


def problem4():
    card1 = int(input("Enter a card number:"))
    card2 = int(input("Enter another card number:"))
    total = (card1 + card2)

    if (total == 21):
        print("BLACKJACK!")
    elif(total > 21):
        print("BUST!")
    elif(total < 21):
        print("The total is " + str(total))





if __name__ == '__main__':
        main()