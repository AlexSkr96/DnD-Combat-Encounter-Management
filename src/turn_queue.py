from character.character import Character


class TurnQueue:
    def __init__(self, characters: list[Character] = []):
        # All chracters are stored here in their turn order (int: initiative => Charachter: character)
        self.__queue = []
        for character in characters:
            self.add_character(character)


    def add_character(self, character: Character, team: int | None = None):
        self.__queue.append((character.roll_initiative(), character, team))
        self.__queue = sorted(self.__queue)


    # Get a list of all remaining teams
    def get_teams(self):
        teams = []
        for character in self.__queue:
            if character[2] and character[2] not in teams:
                teams.append(character[2])

        return sorted(teams)


    def get_teams_count(self, include_teamless = True):
        teams_cnt = len(self.get_teams())
        for character in self.__queue:
            if not character[2]:
                teams_cnt += 1

        return teams_cnt


    def add_team(self, characters: list[Character]):
        new_team = self.get_teams()[-1] + 1
        for character in characters:
            self.add_character(character, new_team)



    def new_round(self):
        for character in self.__queue:
            enemies = []
            for c2 in self.__queue:
                if character[2] != c2[2] or c2[2] is None:
                    enemies.append(c2[1])

            character.start_turn(enemies)
