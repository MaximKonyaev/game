from random import randint

# this is a simple 1vs1 combat game

# dictionary that stores the player and enemy's information
player = {'name' : 'Hero',
        'level' : 1,
        'exp' : 0,
        'nextRank' : 20,
        'atributes' : {'strength' : 1,
                'agility' : 1,
                'wisdom' : 1,
                'hearts' : 50,
                'attack' : [6, 15]}}

enemy = {'name' : 'Enemy',
      'level' : 1,
      'exp' : 0,
      'prize' : 20,
      'nextRank': 20,
      'atributes' : {'strength' : 1,
                  'agility' : 1,
                  'wisdom' : 1,
                  'hearts' : 50,
                  'attack' : [6, 15]}}

# variable that stores the fighting scenes 
form = (
'''              xxxxx
              xxx    xxx                              xxx
             xx  xxxxx x                   x        xx  xxx
             x   xx  x x         x         x        x     xx
             xxx xxxxxxx       xxx         x        xx   xx
               xxxxxxx      xxx            xx        xxxxx
                 xx    x  xxx               xx         x
                 xxxxxxxxx                    xx  x    x
                 x       x                      xxxxxxxx
             xxxxxxxx                           xx   xxx
            xx      xx                             xxx  xx
            x        x                            xx     xx
───────────────────────────────────────────────────────────────────────''',
'''                              xxxxx
                              xxx    xxx              xxx
                             xx  xxxxx x   x        xx  xxx
                             x   xx  x x   x     x  x     xx
                             xxx xxxxxxx   x   xxx  xx   xx
                               xxxxxxx     xxxx      xxxxx
                                 xx    x  xxxx         x
                                 xxxxxxxxx    xx  x    x
                                 x       x      xxxxxxxx
                             xxxxxxxx           xx   xxx
                            xx      xx             xxx  xx
                            x        x            xx     xx
───────────────────────────────────────────────────────────────────────''',
'''              xxxxx
              xxx    xxx              xxx
             xx  xxxxx x   x        xx  xxx
             x   xx  x x   x     x  x     xx
             xxx xxxxxxx   x   xxx  xx   xx
               xxxxxxx     xxxx      xxxxx
                 xx    x  xxxx         x
                 xxxxxxxxx    xx  x    x
                 x       x      xxxxxxxx
             xxxxxxxx           xx   xxx
            xx      xx             xxx  xx
            x        x            xx     xx
───────────────────────────────────────────────────────────────────────''')

print(form[0])

#function that uses a while loop to determins if the player has enough exp to rank up to the next level. the loop also increases all three traits (strength, agility, and wisdom) by 1 point 
def rank(user):
  str, ag, wis = 0, 0, 0
  while user['exp'] >= user['nextRank']:
    user['level'] += 1
    user['exp'] = user['exp'] - user['nextRank']
    user["nextRank"] = round(user['nextRank'] * 2)
    str += 1
    ag += 1
    wis += 1
  # prints out the information calculated in the while loop
  print('level:', user['level'])
  print('Strength {} +{} Agility {} +{} Wisdom {} +{}'.format(user['atributes']['strength'], str,
                                                  user['atributes']['agility'], ag,
                                                  user['atributes']['wisdom'], wis))
  user['atributes']['strength'] += str
  user['atributes']['agility'] += ag
  user['atributes']['wisdom'] += wis

#function that randomly generates how much damage the attacker will do to the defender using the "randint" method from the random Library
def damage_calculator(attacker, defender):
  damage = randint(defender['atributes']['attack'][0], defender['atributes']['attack'][1])
  attacker['atributes']['hearts'] = attacker['atributes']['hearts'] - damage 
  if attacker['atributes']['hearts'] <= 0:
    print('{} has been slain'.format(attacker['name']))
    player['exp'] += enemy['prize']
    rank(player)
    input('Type any key to quit')
    exit(0)
  else:
     print('{} takes {} damage!'.format(defender['name'], damage))

# gives the dialogue options for the player on wether or not to atack the enemy 
def fight(hero, opponent):
  while True:
    ask = input('Do you wish to attack? y/n').lower()
    if 'n' in ask:
      print(form[2])
      print('{} swings their sword and attacks!'.format(enemy['name']))
      damage_calculator(opponent, hero)
    elif 'y' in ask:
      print(form[1])
      print('{} swings their sword and attacks!'.format(hero['name']))
      damage_calculator(hero, opponent)
    else:
        pass

fight(player, enemy)

