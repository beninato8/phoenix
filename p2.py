import pandas as pd
import sys

args = sys.argv
df = pd.read_csv('phoenix2.csv')
categories = ['advantage', 'weapon', 'aura', 'zen', 'rarity']
specials = ['Shield', 'No Armor', 'Armor']
weapons = ['Focused', 'Spread', 'Beam', 'Blast', 'Homing', 'Tracking']
auras =  ['Bullet EMP', 'Stun EMP', 'Point Defense', 'Laser Storm', 'Barrier',
          'Missile Swarm', 'Stun Emp', 'Vorpal Lance', 'Chrono Field', 'Phalanx',
          'Ion Cannon', 'Blade Storm']
zens =  ['Kappa Drive', 'Personal Shield', 'Mega Bomb', 'Mega Laster', 'Mega Laser',
         'Teleport', 'Reflex EMP', 'Tracking Minigun', 'Trinity Teleport']
rarities =  ['Common', 'Rare', 'Super Rare']

print('Each category should not have any spaces in it, use only commas to seperate options. ' +
      'For options like \'Missile Swarm\', ' + 
      'replace the space with a dash. Capitalization isn\'t necessary.')
print('Arguments example:\nrarity:rare advantage:armor,no-armor, aura:phalanx,missile-swarm')
print('Use \'options\' as the only argument to display options\n')
if len(args) == 2 and type(args[1]) is str and args[1] == 'options':
    print('Categories:\n%s\n' % categories)
    print('Advantage Options:\n%s\n' % (list(x.lower().replace(' ', '-') for x in specials)))
    print('Weapon Options:\n%s\n' % (list(x.lower().replace(' ', '-') for x in weapons)))
    print('Aura Options:\n%s\n' % (list(x.lower().replace(' ', '-') for x in auras)))
    print('Zen Options:\n%s\n' % (list(x.lower().replace(' ', '-') for x in zens)))
    print('Rarity Options:\n%s\n' % (list(x.lower().replace(' ', '-') for x in rarities)))
    exit()

argsl = [x.split(':') for x in args if x not in [args[0]]]
argsl = [x for x in argsl if len(x) > 1 and x[0].lower() in categories]
print(list(x[0].title()+': '+x[1].replace(',', ', ').replace('-', ' ').title() for x in argsl))

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
    print(test)
