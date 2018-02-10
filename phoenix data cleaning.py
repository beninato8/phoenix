import pandas as pd
import numpy as np

df = pd.read_csv('phoenix.csv')
mylist = ['Shinova', 'NC-150', 'Tar\'cah',
          'Veil', 'Krillou', 'Jericho',
          'Fujin', 'Jn\'dur', 'Tempest',
          'Yoth-Hola', 'Razor VI', 'Mist Star',
          'Proxymar', 'Oran', 'Kada Veni',
          'Wrackr', 'Trireme', 'Cinnri',
          'Phoenix', 'Buhloo', 'Czar',
          'Havoc', 'Geist', 'Juggernaut',
          'Tillat\'or', 'Elyon', 'Ogon',
          'Vuxine', 'Photurius', 'Xaniea',
          'Arietis', 'Atlas', 'Essin',
          'EX04239', 'Aurora', 'Von Braun',
          'Gorthaur', 'Heechi', 'Prime X',
          'Sakura', 'Vani-Vith', 'Zephyr',
          'Baqlor', '502-Q8', 'Dragonfly',
          'Hime', 'Hunter', 'Gladius',
          'Lokie', 'Barret', 'Saber',
          'Valkyrie', 'Proteus', 'Yigothu',
          'Torrent', 'Orion', 'Exarch', 
          'Njorun', 'Boxer', 'Sonah', 
          'Corsair', 'Antioch', 'UHB',
          'Trinity', 'Wraith', 'X-81', 
          'Scuuxun', 'Shogun', 'NC-271', 
          'Predator', 'Lorilou', 'AB8/KLYN', 
          ]
# print(df)
df['Ship'] = df['Ship'].astype("category")
df['Ship'].cat.set_categories(mylist, inplace=True)
df = df.sort_values(["Ship"])
df = df.reset_index(drop=True)
print(df)
df.to_csv('phoenix2.csv', index=False)
template = {'Ship':'', 
            'Best Against':'', 
            'Main Weapon':'',  
            'Aura Ability':'', 
            'Zen Ability':'', 
            'Rarity':''}
# df2 = pd.DataFrame(input_rows)
# df = pd.concat([df, df2])
