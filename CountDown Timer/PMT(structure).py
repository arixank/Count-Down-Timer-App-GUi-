import time

blast = int(input("Enter Countdown Time ?? \n"))


def Countdown(blast):
    if blast <= 0:
        print("Die Countdown")
    
    else:
        while blast > 0:
            time.sleep(1)
            print(blast)
            blast -= 1


Countdown(blast)
print("Done For Now !!")
