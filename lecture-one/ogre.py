from enemy import Enemy
import random

class Ogre(Enemy):
    def __init__(self, health_points, attack_damage):
        
        super().__init__(type_of_enemy= "Ogre", health_points=health_points, attack_damage=attack_damage)
    
    
    def talk(self):
        print("Uga uga!")

    def special_attack(self):
        did_special_attack_random = random.random() < 0.70
        if did_special_attack_random:
            self.health_points += 3
            print("Ogre is healing for 3 HP!")