#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*

chaine = input("Saisissez une chaîne de caractères: ") # The user enters a string

# For every char|letter in the string
for lettre in chaine:
    if lettre in "AEIOUYaeiouy": # If the current char is a vowel
        print(f"{lettre}: voyelle")
    elif lettre in "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz": # If the current char is a consonant
        print(f"{lettre}: consonne")
    else:
        print(lettre)