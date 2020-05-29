import random
import string


def randomPassword(length):
    temparr = [i for i in range(0, length)]
    tempstr = [None]*length
    count = 0
    while(temparr != []):
        ch = random.choice(temparr)
        if count == 0 or count == 4:
            tempstr[ch] = random.choice(string.printable[0:10])
            count += 1
        elif(count == 1 or count == 5):
            tempstr[ch] = random.choice(string.printable[10:36])
            count += 1
        elif(count == 2 or count == 6):
            tempstr[ch] = random.choice(string.printable[36:62])
            count += 1
        elif(count == 3 or count == 7):
            tempstr[ch] = random.choice(string.printable[62:94])
            count += 1
        elif(count == 8):
            while(temparr != []):
                ch = random.choice(temparr)
                tempstr[ch] = random.choice(string.printable[0:94])
                temparr.remove(ch)
        else:
            continue

        if(count < 8):
            temparr.remove(ch)

    return ''.join(tempstr)


def check_length(length):
    if length < 8:
        return False
    else:
        return True


if __name__ == "__main__":
    length = int(input("Enter length of password: "))
    while not check_length(length):
        print("\nMinimim 8 characters are necessary")
        length = int(input("Enter length of password: "))
        print()
    print(randomPassword(length))
