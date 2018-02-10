import pandas as pd
import sys

args = sys.argv
df = pd.read_csv('phoenix2.csv')
shipslist = ['Shinova', 'NC-150', 'Tar\'cah', 
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
categories = ['advantage', 'weapon', 'aura', 'zen', 'rarity']
specials = ['Shield', 'No Armor', 'Armor']
weapons = ['Focused', 'Spread', 'Beam', 'Blast', 'Homing', 'Tracking']
auras =  ['Bullet EMP', 'Stun EMP', 'Point Defense', 'Laser Storm', 'Barrier',
          'Missile Swarm', 'Stun Emp', 'Vorpal Lance', 'Chrono Field', 'Phalanx',
          'Ion Cannon', 'Blade Storm']
zens =  ['Kappa Drive', 'Personal Shield', 'Mega Bomb', 'Mega Laster', 'Mega Laser',
         'Teleport', 'Reflex EMP', 'Tracking Minigun', 'Trinity Teleport']
rarities =  ['Common', 'Rare', 'Super Rare']

print('Use \'options\' as the only argument to display options\n')

if len(args) == 2 or len(args) == 3 and type(args[1]) is str:
    if len(args) == 2 and args[1] == 'options':
        print('Each category should not have any spaces in it, use only commas to seperate options. ' +
        'For options like \'Missile Swarm\', ' + 
        'replace the space with a dash. Capitalization isn\'t necessary.')
        print('Arguments example:\nrarity:rare advantage:armor,no-armor, aura:phalanx,missile-swarm')
        print('To see a list of ships, use \'ships\' as the only argument\n')
        print('To see the stats for all ships, use \'all\' as the only argument\n')
        print('You can also see the stats for individual ships. For exmaple, ' +
              'using \'tri\' as your argument will show the stats for Trinity and Trireme')
        print('You may need to make your terminal window a little wider to see the results')
        print('Categories:\n%s\n' % categories)
        print('Advantage Options:\n%s\n' % (list(x.lower().replace(' ', '-') for x in specials)))
        print('Weapon Options:\n%s\n' % (list(x.lower().replace(' ', '-') for x in weapons)))
        print('Aura Options:\n%s\n' % (list(x.lower().replace(' ', '-') for x in auras)))
        print('Zen Options:\n%s\n' % (list(x.lower().replace(' ', '-') for x in zens)))
        print('Rarity Options:\n%s\n' % (list(x.lower().replace(' ', '-') for x in rarities)))
        exit()
    if len(args) == 2 and args[1] == 'ships':
        tmplist = []
        tmp = ''
        for i, x in enumerate(shipslist):
            tmp += x + '      \t'
            if i % 3 == 2:
                tmplist.append(tmp.rstrip())
                tmp = ''
        for x in tmplist:
            print(x)
        exit()
    if len(args) == 2 and args[1] == 'all':
        with pd.option_context('display.max_rows', len(df)):
            print(df.to_string())
    if len(args) == 2 and any(args[1] in x.lower() for x in shipslist):
        test = df[df['Ship'].isin([x for x in shipslist if args[1] in x.lower()])]
        with pd.option_context('display.max_rows', len(test)):
            print(test.to_string())
        print()
        exit()
    if len(args) == 3 and any(' '.join([x for x in args[1:3]]) in x.lower() for x in shipslist):
        test = df[df['Ship'].isin([x for x in shipslist if ' '.join([x for x in args[1:3]]) in x.lower()])]
        with pd.option_context('display.max_rows', len(test)):
            print(test.to_string())
        exit()

argsl = [x.split(':') for x in args if x not in [args[0]]]
argsl = [x for x in argsl if len(x) > 1 and x[0].lower() in categories]
argsclean = list(x[0].title()+': '+x[1].replace(',', ', ').replace('-', ' ').title() for x in argsl)
if argsclean != []:
    print('Args: ', args)

special = []
weapon = []
aura = []
zen = []
rarity = []

for i, x in enumerate(argsl):
    if x[0] == 'advantage':
        special = list([y.title() for y in [z.replace('-', ' ') for z in x[1].split(',')]])
    if x[0] == 'weapon':
        weapon = list([y.title() for y in [z.replace('-', ' ') for z in x[1].split(',')]])
    if x[0] == 'aura':
        aura = list([y.title() for y in [z.replace('-', ' ') for z in x[1].split(',')]])
    if x[0] == 'zen':
        zen = list([y.title() for y in [z.replace('-', ' ') for z in x[1].split(',')]])
    if x[0] == 'rarity':
        rarity = list([y.title() for y in [z.replace('-', ' ') for z in x[1].split(',')]])

special = specials if special == [] else special
weapon = weapons if weapon == [] else weapon
aura = auras if aura == [] else aura
zen = zens if zen == [] else zen
rarity = rarities if rarity == [] else rarity

dfspecial = df['Best Against'].isin(special)
dfweapon = df['Main Weapon'].isin(weapon)
dfaura = df['Aura Ability'].isin(aura)
dfzen = df['Zen Ability'].isin(zen)
dfrarity = df['Rarity'].isin(rarity)

test = df[dfspecial & dfweapon & dfaura & dfzen & dfrarity]
if len(test) < len(df):
    with pd.option_context('display.max_rows', len(test)):
            print(test.to_string())
