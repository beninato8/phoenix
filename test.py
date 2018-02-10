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

