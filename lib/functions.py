#!/usr/bin/env python3
def greet_programmer():
    print("Hello, programmer!")



greet_programmer()    

def greet(name):
    print(f'Hello, {name}!')


greet('Bett')

def greet_with_default(name="programmer"):
    print(f'Hello, {name}!')


greet_with_default('programmer')    

def add(num1, num2):
    return num1 + num2


add(45,55) == 100    

def halve(number):
    result = (int(number)/2)
    print(result)
    return result


halve(100)    
