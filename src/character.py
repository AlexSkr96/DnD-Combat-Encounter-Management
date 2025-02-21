class Character():
    def __init__(self):
        self.__hp = None
        self.__ac
        self.__speed
        self.__initiative

        #### Abilities ####
        self.__strength
        self.__intelligence
        self.__dexterity
        self.__wisdom
        self.__constitution
        self.__charisma
        #### #### #### ####

        self.__gear = [] # List of ?weapon? class objects
        self.__spells = [] # List of spell class objects
        self.__traits = [] # List of trait class objects
        self.__multiattack = 1 # Number of attacks per main action
