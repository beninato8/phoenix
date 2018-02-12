"""
compare = ['purple', 'yellow', 'blue green',
           'orange', 'yellow-green']

abc = "red blue green"
a = abc.split()
print(a)

b = ' '.join(a[1:])
print(b)

c = b in compare
print(c)

for i in range(10):
    print(i, i % 3)
"""

fruits = ['Apple', 
'Apricot', 
'Avocado', 
'Banana', 
'Berries', 
'Breadfruit', 
'Carob', 
'Cherry', 
'Citron', 
'Coconut', 
'Date', 
'Dragon Fruit', 
'Durian', 
'Fig', 
'Ginger', 
'Grapes', 
'Currant', 
'Raisin', 
'Grapefruit', 
'Guava', 
'Jackfruit', 
'Jujube', 
'Kiwifruit', 
'Kumquat', 
'Lemon', 
'Lime', 
'Longan', 
'Loquat', 
'Lucuma', 
'Lychee', 
'Mamey Sapote', 
'Mango', 
'Mangosteen', 
'Melons', 
'Nance', 
'Nectarine', 
'Noni', 
'Oranges', 
'Blood Orange', 
'Mandarin', 
'Navel', 
'Seville', 
'Valencia', 
'Papaya', 
'Passion Fruit', 
'Peach', 
'Pear', 
'Asian Pear', 
'Persimmon', 
'Pineapple', 
'Plantain', 
'Plum', 
'Damson', 
'Prunes', 
'Pomegranate', 
'Pomelo', 
'Prickly Pear', 
'Quince', 
'Rambutan', 
'Rhubarb', 
'Starfruit', 
'Tamarillo', 
'Tamarind', 
'Tangerine', 
'Tangelo', 
'Tomato']

res = []
search = 'x,y,z'
for x in fruits:
    for y in search:
        if y.lower() in x.lower() and x not in res:
            res.append(x)

print(res)

print(list(x for x in fruits for y in search.split(',') if y.lower() in x.lower()))

print("hello".split(','))
