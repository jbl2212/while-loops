doExit = False
while not doExit:
    print ("put in a letter")
    choice = input()
    if choice == 'q':
        doExit = True
        print ("bye")
    print ("You pressed,",choice)
