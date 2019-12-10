#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*

in_table = input("Saisissez un nombre: ")
n_table = int(in_table)
i = 1

print(f"%%%%%%%%%%%% Table de {n_table} %%%%%%%%%%%%")
while i <= 10:
    print(f"{n_table} * {i} = {n_table * i}")
    i += 1