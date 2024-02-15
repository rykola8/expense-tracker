fruit = [{"name": 'school', "cena":'30', "category": 'needs'},{"name": "food", "cena": '40', "category": 'foods'}]


la = 0
lenght = len(fruit)
for x in fruit:
    la += int(x["cena"])
    
middle = int(la) / int(lenght)
print(middle)