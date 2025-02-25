class Character:
    def __init__(
        self,
        name: str,
        hp: int,
        ac: int,
        speed: int,
        strength: int,
        intelligence: int,
        dexterity: int,
        wisdow: int,
        constitution: int,
        charisma: int,
    ):
        self.__name = None

        self.__max_hp = None
        self.hp = None
        self.__ac = None
        self.__speed = None
        self.__initiative = None

        #### Abilities ####
        self.__strength = None
        self.__intelligence = None
        self.__dexterity = None
        self.__wisdom = None
        self.__constitution = None
        self.__charisma = None
        #### #### #### ####

        self.__gear = [] # List of ?weapon? class objects
        self.__spells = [] # List of spell class objects
        self.__traits = [] # List of trait class objects
        self.__multiattack = 1 # Number of attacks per main action

    def attack(self, target: Character):
