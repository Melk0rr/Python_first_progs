#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*

in_table = input("Saisissez un nombre: ") # The user inputs a number
n_table = int(in_table) # Conversion from string to integer
i = 1

print(f"%%%%%%%%%%%% Table de {n_table} %%%%%%%%%%%%")

# Prints multiplication table of the entered number
while i <= 10:
    print(f"{n_table} * {i} = {n_table * i}")
    i += 1