#   _____                                       _____               _             
#  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
#  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
#  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
#  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
#             |_|                                                                 

#
# Uzdevums:
# Uzrakstīt programmu, kas ļauj
# - ievadīt izdevumus: nosaukumu, summu un kategoriju
# - atspoguļot uz ekrāna visus izdevumus
# - iespēja atlasīt 10 lielākus izdevumus
# - iespēja atlasīt 10 mazākus izdevumus
# - iespēja apskatīt vidējo izdevumu summu
# [!] Programmai jaglabā izdevumu stāvokli kad programma ir izslēgta palaista no jauna
#

expenses = []

# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)

import json
f = open('expenses.json',) 
data = json.load(f)


pass

while True:
    command = input("\nChoose command:")
    if command == "1":
        dictionary_expenses = {}
        
        name = input('enter name of expenses: ')
        dictionary_expenses["name"] = name

        summa = input('enter summa of expenses: ')
        dictionary_expenses["summa"] = summa
                    
        category = input('enter category of expenses: ')
        dictionary_expenses["category"] = category

        expenses.append(dictionary_expenses)
    
    if command == "2":
        print(expenses)
        pass
    
    if command == "3":
        def my_func(expense):
            return int(expense["summa"])
        
        expenses.sort(key = my_func, reverse = True)
        print(expenses[0:10])
        pass
    
    if command == "4":
        def my_func(expense):
            return int(expense["summa"])
        
        expenses.sort(key = my_func)
        print(expenses[0:10])
        pass
    
    if command == "5":
            la = 0
            lenght = len(expenses)
            for x in expenses:
                la += int(x["summa"])
        
            middle = int(la) / int(lenght)
            print(middle)



            pass
    
    
    
    
    
    
    if command == "e":
        print("Exiting...")
        break

# save expenses to expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Writing JSON to a file in Python)
pass

