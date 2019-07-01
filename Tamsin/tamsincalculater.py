import time

sleep_time =120

while True:
    print ("enter to numbers")
    c =int( input() )
    a =int( input() )
    while True:
        print ("do you want to +, *, -, /, or quit?")
        b =input()
        if b == "quit":
            exit()
        if b == "+" or b == "plus":
            print ("loading... (doing really hard maffs)")
            time.sleep(sleep_time)
            print (c+a)
            break
        elif b == "*" or b == "times":
            print ("loading... (doing really hard maffs)")
            time.sleep(sleep_time)
            print (c*a)
            break
        elif b == "-" or b == "minus":
            print ("loading... (doing really hard maffs)")
            time.sleep(sleep_time)
            print (c-a)
            break
        elif b == "/" or b == "divide":
            print ("loading... (doing really hard maffs)")
            time.sleep(sleep_time)
            print (c/a)
            break
        else:
            print ("that is not an operation")
