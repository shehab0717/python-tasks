
import random
import math


def rangeNums(start, lenght):
    numbers = []
    for num in range(start, start+lenght):
        numbers.append(num)
    return numbers

# print(rangeNums(5,5))


def divisibility(num: int):
    ret = ''
    if num % 3 == 0:
        ret = 'Fizz'
    if num % 5 == 0:
        ret = ret+'Buzz'
    return ret


# print(divisibility(3))

def reverseString():
    str = input("Enter a string: ")
    result = ''
    for char in str:
        result = char + result
    return result


# print(reverseString())

def getUserName():
    name = input("Enter your name: ")
    if name.isdigit():
        print("Name can't be a number!!")
        name = getUserName()
    return name


def userInfo():
    name = getUserName()
    email = input("Enter your email: ")
    print("------- Your info ----------")
    print(f"Name: {name} \nEmail: {email}")


# userInfo()

def isSorted(str):
    i = 1
    while i < len(str):
        if str[i] < str[i-1]:
            return False
        i += 1
    return True


def LAO(str):
    start = 0
    res = str[0]
    while start < len(str):
        end = start
        while end < len(str):
            if end - start + 1 > len(res) and isSorted(str[start: end+1]):
                res = str[start: end+1]
            end += 1
        start += 1
    return res

# print(LAO('abdulrahman'))


def inputNumbers():
    numbers = []
    print("Enter your numbers: ")
    num = input("> ")
    while num != 'done':
        if num.isdigit() == False:
            print('The input is not valid!!')
        else:
            numbers.append(int(num))
        num = input("> ")
    return numbers


def sum(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum


def calc():
    numbers = inputNumbers()
    print(f"""
        Count = {len(numbers)}
        Total = {sum(numbers)}
        Average = {sum(numbers)/len(numbers)}
    """)

# calc()


words = ["illusion", "marker", "elephant", "transaction", "whale"]


def guessChar():
    char = input('Guess one character> ')
    if len(char) == 1:
        return char
    print('You must enter only one character!!')
    return guessChar()


def hangman():
    userName = input('Enter your name: ')
    # print(f'Words: {words}\n----------------------------------')
    index = math.floor(random.random()*13453) % len(words)
    word = words[index]
    print(f'---------------{word}---------------')
    wordTemp = ''
    for i in range(len(word)):
        wordTemp = wordTemp + '-'
    tries = 10
    while tries:
        print(f'Guess the word [{wordTemp}], lenght = {len(word)}\nYou have {tries} tries')
        char = guessChar()
        if char in word:
            newTemp = ''
            for i in range(len(word)):
                if word[i] == char:
                    newTemp = newTemp + word[i]
                else:
                    newTemp = newTemp + wordTemp[i]
            wordTemp = newTemp
        if word == wordTemp:
            break;
        tries -= 1
    if word == wordTemp:
        print(f'Congratulations {userName}, you guessed it right :)')
    else:
        print(f'Sorry {userName}, you failed :(')

hangman()
