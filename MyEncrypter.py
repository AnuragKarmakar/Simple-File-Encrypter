from os import system
from time import sleep
from alive_progress import alive_bar


def clearTerminal():

    system('cls')


def encrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        print(f"index: {index} value: {value}", end="\r")
        data[index] = value ^ key
        sleep(0.005)

    print(f"index: {index} value: {value}")

    file = open("CC-" + filename, "wb")
    file.write(data)
    file.close()


def decrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        print(f"index: {index} value: {value}", end="\r")
        data[index] = value ^ key
        # sleep(0.05)

    print(f"index: {index} value: {value}")

    file = open(filename, "wb")
    file.write(data)
    file.close()


clearTerminal()

filename = input("Please enter a filename >> ")
print("What do you want to do ? [Press the numbers accordingly to choose]")
choice = int(input("1.Encrypt\n2.Decrypt\n3.Exit \n >> "))

while choice != 3:
    if (choice == 1):
        key = int(input("Ask for a key [between 1 - 255] >> "))
        if (0 < key < 256):
            encrypt(filename, key)
            print("Encryption Complete!")
            print('\n\x1b[1;31;40m' +
                  "ALWAYS REMEMBER THE KEY YOU PROVIDED!" + '\x1b[0m')
            print('\x1b[1;32;40m' + 'Encryption Complete' + '\x1b[0m')
            break
        else:
            print("Key Should be between 1 to 255")

    elif (choice == 2):
        key = int(input("Ask for a key between 1 - 255 >> "))
        decrypt(filename, key)
        print('\x1b[1;32;40m' + 'Decryption Complete' + '\x1b[0m')
        break

    elif (choice == 3):
        print("GoodBye!")
        exit
    else:
        print("invalid Input")


# decrypt(filename, key)


# print("______________________________________________")
