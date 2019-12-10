#!/usr/local/bin/python3.8
# -*-coding:Utf-8 -*

# Table function to print multiplication table of n until max
def table(n, max = 10):
    print(f"%%%%%%%%%%%% Table de {n} %%%%%%%%%%%%")
    i = 0

    # Prints multiplication table of the entered number
    while i < max: # While i lower than max
        print(f"{n} * {i + 1} = {n * (i + 1)}")
        i += 1