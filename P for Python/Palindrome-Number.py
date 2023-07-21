# Palindrome Number 
#!/usr/bin/env python

""" Palindrome number - Check whether a number is palindrome or not. """

__author__      = "Kaushik-Chhappaniya"
__copyright__   = "Copyright 2023, Coding_Resources"


def isPalindrome(num):
    n = num #Making a copy of number
    newNum = 0
    while n!=0:
        reminder = n%10
        newNum = newNum*10 + reminder
        n = n//10
    return newNum == num

if __name__ == "__main__":
    print(isPalindrome(int(input())))
