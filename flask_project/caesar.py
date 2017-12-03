from sys import argv, exit
import string

def encrypt(plaintext, rot):

    output = ''
    
    for char in plaintext:
        output += rotate_character(char, int(rot))
    
    return output

def alphabet_position(char):
    '''Returns the index of the alpha character within the alphabet. Case-insensitve.'''
    if char.islower():
        return string.ascii_lowercase.index(char)
    else:
        return string.ascii_uppercase.index(char)

def rotate_character(char, rot):
    '''Returns the letter (rot) number of letters after (char)'''
    if char.isalpha():
        if char.islower():
            return string.ascii_lowercase[(alphabet_position(char)+rot)%26]
        else:
            return string.ascii_uppercase[(alphabet_position(char)+rot)%26]
    else:
        return char # Pass through non-alpha characters


def main():
    if len(argv) != 2:
        print("usage: python caesar.py n")
        exit()
    
    if argv[1].isdigit() == False:
        print("usage: python caesar.py n")
        exit()

    print("Type a message:")
    plaintext = input()
    print(encrypt(plaintext, int(argv[1])))

if __name__ == "__main__":
    main()

