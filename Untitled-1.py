fruit = [{"name": 'school', "cena":'30', "category": 'needs'},{"name": "food", "cena": '40', "category": 'foods'}]

def my_func(expenses):
    return expenses["cena"] 
fruit.sort(key = my_func)
print(fruit)