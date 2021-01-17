import random

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","[","}","]","|",":",";","<",">",".","?","/","]"]

while True:
    length = input("Length of password wanted: ")
    try:
        bruh = int(length)
        break
    except:
        print("Please enter a NUMBER")
        continue

def letter_picker():
    index = random.randrange(0,len(alphabet)-1)
    letter = alphabet[index]
    decider = random.randrange(1,3)
    if decider == 2:
        return letter.upper()
    return letter

def number_picker():
    index = random.randrange(0,len(numbers)-1)
    number = numbers[index]
    return number

def symbol_picker():
    index = random.randrange(0,len(symbols)-1)
    symbol = symbols[index]
    return symbol

def generate():
    password = ""
    while len(password) < int(length):
        decider = random.randrange(1,101)
        if decider % 2 == 0:
            letter = letter_picker()
            password += letter
        if decider % 2 == 1:
            number = number_picker()
            password += number
        if decider % 3 == 0:
            symbol = symbol_picker()
            password += symbol
    print()
    print(password)
    print()

generate()
