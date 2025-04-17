class Enemy:
    type_of_enemy: str
    health_points: int 
    attack_damage: int 

    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy  #private
        self.health_points = health_points  
        self.attack_damage = attack_damage
        

    def talk(self):
        print(f'{self.__type_of_enemy} says: I will attack you!')

    def walk_forward(self):
        print(f'{self.__type_of_enemy} is walking forward!')
    
    def attack(self):
        print(f'{self.__type_of_enemy} is attacking for {self.attack_damage} damage!')

    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    def set_type_of_enemy(self, type_of_enemy):
        self.__type_of_enemy = type_of_enemy

    def special_atack(self):
        print(f'Enemy has no special attack!')