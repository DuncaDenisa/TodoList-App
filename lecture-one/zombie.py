from enemy import Enemy
import random

class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        
        super().__init__(type_of_enemy= "Zombie", health_points=health_points, attack_damage=attack_damage)
    
    
    def talk(self):
        print("Brains...")

    def spread_infection(self):
        print("Zombie is spreading infection!")
    
    def special_attack(self):
        did_special_attack_random = random.random() < 0.50
        if did_special_attack_random:
            self.health_points += 5
            print("Zombie is healing for 5 HP!")
        