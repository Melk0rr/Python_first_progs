#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*

str_year = input("Saisissez une année: ") # The user enters a year
year = int(str_year) # Converts from String to int

# Leap year condition
if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0): print(f"L'annee {year} est bissextile.")
else: print(f"L'annee {year} n'est pas bissextile.")