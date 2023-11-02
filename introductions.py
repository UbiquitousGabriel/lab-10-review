## Write a function that takes 2 pieces of input and introduces them to one another

def introduction(name1, name2):
    print(name1, " meet ", name2)

name1 = input("Person 1, What is your name?")
name2 = input("Person 2, What is your name?")

introduction(name1,name2)