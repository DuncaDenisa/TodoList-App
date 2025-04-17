from enemy import *
from zombie import *
from ogre import *
from hero import *

zombie = Zombie(15, 3)

ogre = Ogre(35, 3)

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        e1.special_atack()
        e2.special_atack()
        e1.attack()
        e2.health_points -= e1.attack_damage
        e2.attack()
        e1.health_points -= e2.attack_damage

        if e1.health_points > 0 :
            print(f'{e1.get_type_of_enemy()} wins!')
        else:
            print(f'{e2.get_type_of_enemy()} wins!')

#battle(zombie, ogre)


def hero_battle(hero: Hero, enemy: Enemy):

    while hero.health_points > 0 and enemy.health_points > 0:
        enemy.special_atack()
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.hero_attack()
        enemy.health_points -= hero.attack_damage

        if hero.health_points > 0 :
            print('Hero wins!')
        else:
            print(f'{enemy.get_type_of_enemy()} wins!')

hero = Hero(20, 5)
weapon = Weapon('sWORD', 1)
hero.weapon = weapon
hero.equip_weapon()
hero_battle(hero, zombie)