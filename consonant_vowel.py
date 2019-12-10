#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*

chaine = input("Saisissez une chaîne de caractères: ")

for lettre in chaine:
    if lettre in "AEIOUYaeiouy":
        print(f"{lettre}: voyelle")
    elif lettre in "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz":
        print(f"{lettre}: consonne")
    else:
        print(lettre)