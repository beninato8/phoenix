import pandas as pd
import sys
import collections

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
             'Predator', 'Lorilou', 'AB8/KLYN']

categories = ['advantage', 'weapon', 'aura', 'zen', 'rarity']
specials   = ['Shield', 'No Armor', 'Armor']
weapons    = ['Focused', 'Spread', 'Beam', 'Blast', 'Homing', 'Tracking']

auras      = ['Bullet Emp', 'Stun Emp', 'Point Defense', 'Laser Storm', 'Barrier',
              'Missile Swarm', 'Vorpal Lance', 'Chrono Field', 'Phalanx',
              'Ion Cannon', 'Blade Storm']
aurad      = ['Bullet Emp', 'Stun Emp', 'Point Defense', 'Barrier',
              'Chrono Field', 'Phalanx', 'Ion Cannon']
aurao      = ['Laser Storm', 'Missile Swarm', 'Blade Storm', 'Vorpal Lance', 'Ion Cannon']
auratype = {'offense':aurao, 'defense':aurad}

zens       = ['Kappa Drive', 'Personal Shield', 'Mega Bomb', 'Mega Laser',
              'Teleport', 'Reflex Emp', 'Tracking Minigun', 'Trinity Teleport']
zend       = ['Kappa Drive', 'Personal Shield', 'Teleport', 'Reflex Emp', 'Trinity Teleport']
zeno       = ['Mega Bomb', 'Mega Laser', 'Tracking Minigun', 'Kappa Drive', 'Trinity Teleport']
zentype = {'offense':zeno, 'defense':zend}

rarities   = ['Common', 'Rare', 'Super Rare']

print('Use \'help\' as your only argument to display options')

if len(args) == 2 or len(args) == 3 and type(args[1]) is str:
    if len(args) == 2 and args[1] == 'help':
        print('\nYou may need to make your terminal window a little wider to see the results.')
        print('Each category should not have any spaces in it, use only commas to seperate options.')
        print('For options with spaces, replace the space with a dash.')
        print('Capitalization isn\'t necessary.\n')
        print('Arguments example:\nrarity:rare advantage:armor,no-armor, aura:phalanx,missile-swarm')
        print('\nTo see a list of all options for categories, use \'options\' as your only argument.')
        print('To see a list of ships, use \'ships\' as your only argument.')
        print('To see the stats for all ships, use \'all\' as your only argument.')
        print('\nYou can also see the stats for individual ships that have your argument in their name.')
        print('Example: \'tri\' as your argument will show the stats for Trinity and Trireme.')
        exit()
    elif len(args) == 2 and args[1] == 'options':
        print('\nCategories:\n%s\n' % categories)
        print('Advantage Options:\n%s\n' % (list(x.lower().replace(' ', '-') for x in specials)))
        print('Weapon Options:\n%s\n' % (list(x.lower().replace(' ', '-') for x in weapons)))
        print('Aura Options:\n%s\n' % (list(x.lower().replace(' ', '-') for x in auras)))
        print('Zen Options:\n%s\n' % (list(x.lower().replace(' ', '-') for x in zens)))
        print('Rarity Options:\n%s\n' % (list(x.lower().replace(' ', '-') for x in rarities)))
        print('You can also use aura/zen:defense/offense for only defensive/offensive abilities ')
        exit()
    elif len(args) == 2 and args[1] == 'ships':
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
    elif len(args) == 2 and args[1] == 'all':
        with pd.option_context('display.max_rows', len(df)):
            print(df.to_string())
    elif len(args) == 2 and any(args[1] in x.lower() for x in shipslist):
        test = df[df['Ship'].isin([x for x in shipslist if args[1] in x.lower()])]
        with pd.option_context('display.max_rows', len(test)):
            print(test.to_string())
        exit()
    elif len(args) == 3 and any(' '.join([x for x in args[1:3]]) in x.lower() for x in shipslist):
        test = df[df['Ship'].isin([x for x in shipslist if ' '.join([x for x in args[1:3]]) in x.lower()])]
        with pd.option_context('display.max_rows', len(test)):
            print(test.to_string())
        exit()

argsl = [x.split(':') for x in args if x not in [args[0]]]
argsl = [x for x in argsl if len(x) > 1 and x[0].lower() in categories]
argsclean = list(x[0].title()+': '+x[1].replace(',', ', ').replace('-', ' ').title() for x in argsl)
if argsclean != []:
    print('Args: ', argsclean)

special = []
weapon = []
aura = []
zen = []
rarity = []

for i, x in enumerate(argsl):
    if x[0] == 'advantage':
        special = list([y.title() for y in [z.replace('-', ' ') for z in x[1].split(',')]])
    elif x[0] == 'weapon':
        weapon = list([y.title() for y in [z.replace('-', ' ') for z in x[1].split(',')]])
    elif x[0] == 'aura':
        if x[1] in ('offense', 'defense'):
            aura = auratype[x[1]]
        else:
            aura = list([y.title() for y in [z.replace('-', ' ') for z in x[1].split(',')]])
    elif x[0] == 'zen':
        if x[1] in ('offense', 'defense'):
            zen = zentype[x[1]]
        else:
            zen = list([y.title() for y in [z.replace('-', ' ') for z in x[1].split(',')]])
    elif x[0] == 'rarity':
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

